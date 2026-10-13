#!/usr/bin/env python3
"""Beschafft Normtexte für das Modul law-checker — registry-getrieben.

Quelle: gesetze-im-internet.de (Bundesministerium der Justiz, amtliche
Arbeitsfassung). Liest die Gesetzes-Registry aus ../config.json, lädt die
XML-Gesamtausgaben der angeforderten Gesetze, extrahiert den Normtext und
schreibt UTF-8-Textdateien nach ``_data/gesetze/`` (Pfade laut Registry).

Herkunft: erweitert aus dem gesetze_fetch.py des Forschungsprojekts
"Lebende Verfassung LLM" (dort fest auf GG+BGB; hier beliebige Registry-Eintraege).

Aufruf (aus dem Modulordner):
    PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py            # alle mit enabled: true
    PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py bgb stgb   # gezielte Schlüssel (auch disabled)
    PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py --list     # Registry anzeigen

Gesetze ohne xml_zip (EU-/Länderrecht) werden übersprungen und gemeldet —
deren Texte manuell beschaffen (Hinweis-Feld des Registry-Eintrags beachten).
"""
from __future__ import annotations

import datetime as _dt
import io
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent.parent
CONFIG = MODULE_DIR / "config.json"

# Ab dieser Textgroesse wird zusaetzlich ein Strukturindex geschrieben,
# wenn die Registry einen index-Pfad nennt.
INDEX_THRESHOLD = 300_000


def load_registry() -> dict:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    return cfg.get("gesetzbuecher", {})


def fetch_zip(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research fetch)"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        return resp.read()


def norm_text(norm: ET.Element) -> tuple[str, str, str]:
    """Liefert (enbez, titel, text) einer <norm>."""
    enbez = (norm.findtext(".//enbez") or "").strip()
    titel = (norm.findtext(".//metadaten/titel") or "").strip()
    parts: list[str] = []
    for content in norm.iter("Content"):
        txt = " ".join(t.strip() for t in content.itertext() if t.strip())
        if txt:
            parts.append(txt)
    return enbez, titel, "\n".join(parts)


def extract(xml_bytes: bytes, label: str, source_url: str) -> tuple[str, str]:
    """Liefert (volltext, index) mit Provenienz-Kopf."""
    root = ET.fromstring(xml_bytes)
    stamp = _dt.date.today().isoformat()  # noqa: DTZ011 - lokales Abrufdatum
    head = (
        f"# {label} — amtliche Arbeitsfassung, Quelle: {source_url}\n"
        f"# Abgerufen: {stamp} | Extraktion: _tools/gesetze_fetch.py (Modul rechtsabteilung)\n"
        f"# Hinweis: Nicht amtliche Bekanntmachung; massgeblich ist das BGBl.\n\n"
    )
    body: list[str] = []
    index: list[str] = []
    for norm in root.iter("norm"):
        enbez, titel, text = norm_text(norm)
        if not (enbez or titel or text):
            continue
        header = " ".join(x for x in (enbez, titel) if x)
        if header:
            body.append(f"\n===== {header} =====")
            index.append(header)
        if text:
            body.append(text)
    return head + "\n".join(body) + "\n", head + "\n".join(index) + "\n"


def process(key: str, entry: dict) -> bool:
    label = entry.get("kurz") or key.upper()
    url = entry.get("xml_zip")
    if not url:
        print(f"[{label}] ÜBERSPRUNGEN: kein xml_zip (EU-/Länderrecht?) — "
              f"manuell beschaffen. Hinweis: {entry.get('hinweis', '—')}")
        return True
    quelle = entry.get("quelle")
    if not quelle:
        print(f"[{label}] FEHLER: Registry-Eintrag ohne 'quelle'-Pfad", file=sys.stderr)
        return False
    out = MODULE_DIR / quelle
    out.parent.mkdir(parents=True, exist_ok=True)

    print(f"[{label}] lade {url} ...")
    blob = fetch_zip(url)
    with zipfile.ZipFile(io.BytesIO(blob)) as zf:
        xml_names = [n for n in zf.namelist() if n.lower().endswith(".xml")]
        if not xml_names:
            print(f"[{label}] FEHLER: kein XML im Zip", file=sys.stderr)
            return False
        xml_bytes = zf.read(xml_names[0])
    full, idx = extract(xml_bytes, entry.get("name", label), url)
    out.write_text(full, encoding="utf-8")
    print(f"[{label}] geschrieben: {out} ({len(full):,} Zeichen)")

    index_path = entry.get("index")
    if index_path and len(full) >= INDEX_THRESHOLD:
        ipath = MODULE_DIR / index_path
        ipath.write_text(idx, encoding="utf-8")
        print(f"[{label}] Index geschrieben: {ipath} ({len(idx):,} Zeichen)")
    elif index_path:
        # Klein genug fuer Volltextzugriff — Index trotzdem schreiben, wenn konfiguriert.
        ipath = MODULE_DIR / index_path
        ipath.write_text(idx, encoding="utf-8")
        print(f"[{label}] Index geschrieben: {ipath}")
    return True


def main(argv: list[str]) -> int:
    registry = load_registry()
    if "--list" in argv:
        for key, entry in registry.items():
            state = "AKTIV  " if entry.get("enabled") else "inaktiv"
            src = entry.get("xml_zip") or "(manuelle Quelle)"
            print(f"{state}  {key:10s} {entry.get('kurz', ''):8s} {src}")
        return 0

    keys = [a for a in argv if not a.startswith("-")]
    if keys:
        unknown = [k for k in keys if k not in registry]
        if unknown:
            print(f"FEHLER: unbekannte Registry-Schlüssel: {', '.join(unknown)}", file=sys.stderr)
            print(f"Bekannt: {', '.join(registry)}", file=sys.stderr)
            return 1
        selected = {k: registry[k] for k in keys}
    else:
        selected = {k: v for k, v in registry.items() if v.get("enabled")}
        if not selected:
            print("Keine aktiven Gesetze in der Registry (und keine Schlüssel angegeben).")
            return 0

    ok = True
    for key, entry in selected.items():
        try:
            ok = process(key, entry) and ok
        except Exception as exc:  # noqa: BLE001 - Netzwerk-/Parsefehler pro Gesetz isolieren
            print(f"[{key}] FEHLER: {exc}", file=sys.stderr)
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
