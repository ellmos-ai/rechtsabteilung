[English](README.md) | **Deutsch**

![law-checker banner](assets/banner.png)

# law-checker (Rechtsabteilung)

[![Version: 0.2.7](https://img.shields.io/badge/Version-0.2.7-blue.svg)](CHANGELOG.md)
[![Lizenz: MIT](https://img.shields.io/badge/Lizenz-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-28%20passed-brightgreen.svg)](tests/)
[![CI-Matrix](https://img.shields.io/badge/CI-Multi--OS%20%7C%20Ubuntu%20%7C%20Windows%20%7C%20macOS-blue.svg)](.github/workflows/ci.yml)
[![Local-First](https://img.shields.io/badge/Architektur-Local--First-green.svg)](#datenschutz-und-vertraulichkeit)
[![Zero-Egress](https://img.shields.io/badge/Datenschutz-100%25%20Offline%20%2F%20Zero--Egress-success.svg)](#datenschutz-und-vertraulichkeit)
[![SBOM](https://img.shields.io/badge/SBOM-Level%201%20Konform-blue.svg)](THIRD_PARTY_LICENSES.md)
[![Sicherheits-SLA](https://img.shields.io/badge/Sicherheit-48h%20SLA-blue.svg)](SECURITY.md)
[![RDG](https://img.shields.io/badge/RDG-%C2%A7%202%20Abs.%201%20Konform-brightgreen.svg)](#rechtlicher-rahmen-und-rdg-einordnung)
[![Claude Code Skill](https://img.shields.io/badge/Skill-Claude%20Code-purple.svg)](SKILL.md)
[![Ökosystem: ellmos-ai](https://img.shields.io/badge/%C3%96kosystem-ellmos--ai-blue.svg)](https://github.com/ellmos-ai)
[![Dachorganisation: open-bricks](https://img.shields.io/badge/Dachorganisation-open--bricks-indigo.svg)](https://github.com/open-bricks)
[![llms.txt](https://img.shields.io/badge/KI--Freundlich-llms.txt-brightgreen.svg)](llms.txt)
[![Sprachauswahl](https://img.shields.io/badge/Sprache-Deutsch-yellow.svg)](#)

**Open-Source-KI-Workflow für quellbelegte rechtliche Ersteinschätzungen nach deutschem Recht.**

> [!NOTE]
> **KI- / LLM-Agenten-Erkennung:** Eine maschinenlesbare Zusammenfassung steht in [`llms.txt`](llms.txt) zur Verfügung (Stand: 2026-09-19).

> [!IMPORTANT]
> **Wichtig: KI-gestützte Erstorientierung, keine Rechtsberatung.** Dieses Werkzeug ersetzt weder die individuelle Prüfung noch die Beratung durch eine zugelassene Rechtsanwältin oder einen zugelassenen Rechtsanwalt. Ob ein konkreter Einsatz eine Rechtsdienstleistung darstellt und zulässig ist, hängt von Einsatzform, Betreiberrolle und Einzelfall ab. Es erfolgt keine Fristenüberwachung und keine automatische Vollständigkeits- oder Aktualitätsgarantie. Bei behördlicher oder gerichtlicher Rechtspost sowie laufenden Rechtsbehelfsfristen ist unverzüglich professioneller Rechtsrat einzuholen.

---

## Schnellnavigation

1. [Übersicht](#übersicht)
2. [Zielgruppen & Anwendungsfälle](#zielgruppen--anwendungsfälle)
3. [Vergleichsmatrix & Alternativen](#vergleichsmatrix--alternativen)
4. [Systemarchitektur](#systemarchitektur)
5. [Ablauf- und Prüfungslebenszyklus](#ablauf--und-prüfungslebenszyklus)
6. [Governance- und Laufzeit-Invarianten](#governance--und-laufzeit-invarianten)
7. [Rechtlicher Rahmen und RDG-Einordnung](#rechtlicher-rahmen-und-rdg-einordnung)
8. [Geschwisterwerkzeuge und Ökosystem](#geschwisterwerkzeuge-und-ökosystem)
9. [Installation und Schnelleinstieg](#installation-und-schnelleinstieg)
10. [Neue Gesetze hinzufügen](#neue-gesetze-hinzufügen)
11. [Datenschutz und Vertraulichkeit](#datenschutz-und-vertraulichkeit)
12. [Gesetzes-Registry-Bestand](#gesetzes-registry-bestand)
13. [Gutachten-Architektur & Visueller Walkthrough](#gutachten-architektur--visueller-walkthrough)
14. [Drittanbieter-Lizenzen & SBOM](#drittanbieter-lizenzen--sbom)
15. [Repository-Struktur](#repository-struktur)
16. [Sicherheitsrichtlinie](#sicherheitsrichtlinie)
17. [Herkunft und Autorenschaft](#herkunft-und-autorenschaft)
18. [Haftung, Lizenz und Grenzen](#haftung-lizenz-und-grenzen)

---

## Übersicht

`law-checker` (Rechtsabteilung) ist ein modularer Skill und Agentenverbund für lokale LLM-Entwicklungsumgebungen wie Claude Code. Er ermöglicht das methodisch saubere Erstellen dokumentierter rechtlicher Ersteinschätzungen für deutsches Bundes- und Europarecht.

Die Kernphilosophie beruht auf strikter Belegdisziplin:
- **Keine Paragraphen aus dem Modellgedächtnis:** Jede gesetzliche Aussage muss unmittelbar aus lokal gespeicherten, amtlichen Normtexten stammen und Absatz- sowie Satz-genau belegt werden (`§ 823 Abs. 1 BGB` + Wortlaut-Kurzzitat + Quelldatei/Abrufdatum).
- **Verkörperungs-Prinzip:** Ein generischer Spezialagent („Du BIST das Gesetzbuch") liest ausschließlich den authentischen Normtext – mit strenger Reichweiten-Disziplin (Anwendungsbereich vor Anwendung) und dem Eingeständnis: „Mein Wortlaut entscheidet das nicht; hier beginnt Auslegung."
- **Getrennte Rechtsprechungsschicht:** Gerichtsentscheidungen werden niemals halluziniert, sondern ausschließlich web-verifiziert mit Gericht, Datum, Aktenzeichen, ECLI und Fundstelle herangezogen; ein negatives Suchergebnis wird explizit als „nicht ermittelt" ausgewiesen.
- **Risiko-Ampel & Eskalation:** Objektive Einstufung in Gering, Mittel, Hoch oder Kritisch, inklusive Anwaltsmatrix mit Fachgebietszuordnung und harter Fristendisziplin bei eingehender Rechtspost.

---

<a id="zielgruppen--anwendungsfaelle"></a><a id="zielgruppen--anwendungsfälle"></a>
## Zielgruppen & Anwendungsfälle

`law-checker` wurde für Softwareingenieure, Open-Source-Maintainer und Compliance-Verantwortliche entwickelt, die im deutschen und europäischen Rechtsraum agieren und verlässliche, quellbelegte rechtliche Ersteinschätzungen ohne Halluzinationen oder Datenabfluss benötigen:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 ZIELGRUPPEN-MAPPING & ANWENDUNGSFÄLLE (PERSONAS)            │
├────────────────────────────────┬────────────────────────────────────────────┤
│ [PERSONA-01] Legal Tech & Ops  │ Automatisierte Norm-Ersteinschätzungen für │
│                                │ Inhouse-Counsel ohne proprietären Lock-in. │
├────────────────────────────────┼────────────────────────────────────────────┤
│ [PERSONA-02] OSS-Maintainer    │ Schnelle Klärung zu deutscher Impressums-  │
│                                │ pflicht, DSGVO-Hinweisen & Lizenz-UrhG.    │
├────────────────────────────────┼────────────────────────────────────────────┤
│ [PERSONA-03] KI-Architekten    │ Zero-Hallucination-Normverkörperung und    │
│                                │ methodisch saubere Auslegungsabgrenzung.   │
├────────────────────────────────┼────────────────────────────────────────────┤
│ [PERSONA-04] DPOs & Compliance │ Nachvollziehbare Audit-Trails für DSGVO,   │
│                                │ EHDS (EU 2025/327) und SGB-V-Gesundheits-KI│
└────────────────────────────────┴────────────────────────────────────────────┘
```

- **`[PERSONA-01]` Legal-Tech-Ingenieure & Inhouse-Legal-Operations:**
  - *Kernproblem:* Kommerzielle Fachdatenbanken (Beck-Online, Juris) bieten keine offene LLM-Agenten-Schnittstelle und kosten tausende Euro pro Arbeitsplatz; unkontrollierte Standard-LLMs erfinden Paragraphen.
  - *Lösung:* Skriptbare, quellbelegte CLI- und Skill-Pipeline für Claude Code, basierend auf amtlichen XML-Beständen von BMJ und BfJ.
  - *Suchintention:* `German legal tech AI first look`, `automatisierte Gesetzesprüfung LLM`, `Inhouse Legal Workflow Agent`.
- **`[PERSONA-02]` Open-Source-Maintainer & Indie-Entwickler:**
  - *Kernproblem:* Rechtsunsicherheit bezüglich deutscher Informationspflichten (z. B. *Impressumspflicht* nach TDDDG / TMG auf GitHub, DSGVO-Datenschutzerklärungen, MIT/GPL-Lizenzpflichten nach deutschem Urheberrecht).
  - *Lösung:* Deterministische Prüfung anhand des authentischen Gesetzeswortlauts, ob ein privates Entwickler-Repo unter geschäftsmäßige Telemedien fällt oder eine Ausnahme greift.
  - *Suchintention:* `Impressumspflicht privates GitHub Repo Deutschland`, `TDDDG Impressum Open Source`, `Urheberrecht UrhG Softwarelizenz BGB`.
- **`[PERSONA-03]` KI-Agenten-Entwickler & Solution Architects:**
  - *Kernproblem:* Vektor-RAG zerstückelt Gesetzestexte an semantischen Chunk-Grenzen, wodurch Tatbestände von Ausnahmetatbeständen (*lex specialis*) getrennt werden und Fehlurteile entstehen.
  - *Lösung:* Das Verkörperungs-Agentenmuster (`agents/gesetzbuch.md`): Das Modell schlüpft in die Rolle des verabschiedeten Gesetzestextes und beachtet strikte Wortlautdisziplin („Mein Wortlaut entscheidet das nicht").
  - *Suchintention:* `Gesetzbuch Verkörperung KI Agent Prompt`, `Zero Hallucination Legal AI Pattern`, `Claude Code Legal Skill`.
- **`[PERSONA-04]` Datenschutzbeauftragte (DPOs) & Compliance-Manager:**
  - *Kernproblem:* Digitale Gesundheitsanwendungen, KI-Systeme und Forschungssoftware verlangen belastbare Vorprüfungen zu DSGVO, EHDS (Verordnung (EU) 2025/327) und SGB V mit nachweisbarem Prüfungsprotokoll.
  - *Lösung:* Standardisiertes 6-Punkte-Gutachtenformat mit objektiver Risiko-Ampel (Gering, Mittel, Hoch, Kritisch), Abrufstempeln und Fachanwaltsempfehlung.
  - *Suchintention:* `EHDS Verordnung EU 2025/327 Compliance Check`, `SGB V Gesundheitsdaten KI Prüfung`, `DSGVO Risiko Ersteinschätzung`.

---

<a id="vergleichsmatrix--alternativen"></a>
## Vergleichsmatrix & Alternativen

10-dimensionaler Architekturvergleich von `law-checker` mit herkömmlichen Recherche- und LLM-Ansätzen:

| Dimension | Naive LLM-Prompts (ChatGPT/Claude roh) | Klassische Rechtsdatenbanken (Beck/Juris) | Generische Legal RAG / Vektoren | Manuelle Websuche & Foren | `law-checker` (Rechtsabteilung) |
|---|---|---|---|---|---|
| **1. Normtreue & Belege** | ❌ Keine (reines Gedächtnis) | ⚠️ Manuelles Suchen erforderlich | ⚠️ Fragmentiert (Chunk-Splits) | ❌ Nur Sekundärquellen | ✅ **Streng authentisch (§, Abs., S.)** |
| **2. Halluzinations-Immunität** | ❌ Häufig erfundene Normen | ✅ Hoch (amtliche Texte) | ❌ Kontextuelle Halluzination | ❌ Hoch (veraltete Forenbeiträge) | ✅ **100% amtliche XML-Caches** |
| **3. Verkörperungs-Disziplin** | ❌ Vermischt Meinung & Text | ❌ Nicht zutreffend (Mensch liest) | ❌ Vermengt Kommentar & Norm | ❌ Reine Spekulation | ✅ **„Du BIST das Gesetzbuch"** |
| **4. Rechtsprechungsschicht** | ❌ Erfundene Az. & ECLIs | ✅ Vollständig (hinter Paywall) | ⚠️ Unverifizierte Zitate | ⚠️ Durchwachsene Treffer | ✅ **Ausschließlich live verifiziert** |
| **5. Zero-Egress-Datenschutz** | ❌ Vollständiger Prompt-Egress | ⚠️ Suchanfragen protokolliert | ⚠️ Vektoren an Cloud gesendet | ❌ Tracker & Suchmaschinen-Logs | ✅ **100% lokal / gitignored** |
| **6. RDG-Rechtsabgrenzung** | ❌ Häufig schwache Hinweise | ⚠️ Enterprise-AGB | ❌ Haftungsfragen ungeklärt | ❌ Abmahnrisiko unbefugter Rat | ✅ **Strikte § 2 RDG Eigenprüfung** |
| **7. Fristen-Triage** | ❌ Völlig ignoriert | ❌ Nur manuelle Wiedervorlage | ❌ Ignoriert | ❌ Fristversäumnis-Risiko | ✅ **Schritt 2 Vorrang-Fristen-Gate** |
| **8. Versionierte Registry** | ❌ Unklare Trainings-Cutoffs | ⚠️ Unbemerkte Textänderungen | ❌ Nicht-versionierte Indizes | ❌ Ständige Web-Fluktuation | ✅ **Auditierbare `config.json` (v5)** |
| **9. Multi-OS CI-Tests** | ❌ Nicht zutreffend | ❌ Proprietär geschlossen | ⚠️ Gelegentliche Unittests | ❌ Nicht zutreffend | ✅ **Ubuntu / Windows / macOS CI** |
| **10. Kosten & Lizenz** | ⚠️ 20–200 €/Monat/Nutzer | ❌ 1.500–5.000+ €/Jahr/Sitz | ⚠️ Cloud-Infrastrukturkosten | ✅ Kostenlos (aber Zeitfresser) | ✅ **100% Frei & Open Source (MIT)** |

---

## Systemarchitektur

Das Gesamtsystem gliedert sich in modulare Schichten von der Aufgabenorchestrierung über die Gesetzestexte bis zur Auslegung und Berichtsabfassung:

```mermaid
flowchart TD
    User["Nutzer / Prüffrage"] --> Skill["SKILL.md Orchestrator"]
    Skill --> Config["config.json Gesetzes-Registry"]
    Config --> Fetcher["_tools/gesetze_fetch.py"]
    Fetcher --> OfficialSources["Amtliche Quellen (gesetze-im-internet.de / EUR-Lex)"]
    OfficialSources --> LocalData["Lokale Normtext-Dateien (_data/gesetze/)"]
    LocalData --> Embodiment["agents/gesetzbuch.md (Verkörperungs-Agent)"]
    Skill --> WebCaseLaw["Web-verifizierte Rechtsprechungsschicht"]
    Embodiment --> ReportFormat["references/berichtsformat.md"]
    WebCaseLaw --> ReportFormat
    ReportFormat --> Assessment["Gutachten & Risiko-Ampel (_gutachten/)"]
    Assessment --> Escalation["references/eskalation_risiko.md (Anwalts-Matrix)"]
```

---

## Ablauf- und Prüfungslebenszyklus

Der 10-stufige Prüfungsablauf gemäß `SKILL.md` stellt sicher, dass jeder Prüfungsschritt methodisch nachvollziehbar und reproduzierbar bleibt:

```mermaid
sequenceDiagram
    autonumber
    actor User as "Nutzer / Anwender"
    participant Skill as "SKILL.md (Orchestrator)"
    participant Config as "config.json (Registry)"
    participant Fetcher as "_tools/gesetze_fetch.py"
    participant Agent as "agents/gesetzbuch.md"
    participant Web as "Rechtsprechungsschicht (Web)"
    participant Reporter as "references/berichtsformat.md"
    participant Reviewer as "Review-Modell (Optional)"

    User->>Skill: Prüffrage / Sachverhalt (Schritt 2: auftrag_klaeren)
    Note over Skill: Schritt 2: Sofortiger Fristen-Check bei eingehender Rechtspost
    Skill->>Config: Schritt 0 & 4: Aktive Gesetzbücher & Einstellungen laden
    Config-->>Skill: Aktivierte Gesetze & Quelldateien
    opt Fehlender oder veralteter Normtext
        Skill->>Fetcher: Amtliches Norm-XML laden (gesetze-im-internet.de)
        Fetcher-->>Skill: Lokale Textdatei (_data/gesetze/)
    end
    loop Für jedes einschlägige Gesetzbuch (Schritt 5: verkoerperungs_runde)
        Skill->>Agent: Gesetzbuch verkörpern (strikte Wortlautbindung)
        Agent-->>Skill: Strukturierte Rohbefunde (Norm, Absatz, Satz)
    end
    Skill->>Web: Schritt 6: Web-verifizierte Urteile abfragen (Gericht, Az, Datum, ECLI)
    Web-->>Skill: Verifizierte Rechtsprechung (oder explizit "nicht ermittelt")
    Skill->>Skill: Schritt 7 & 8: Subsumtion & Risiko-Ampel (Grün/Gelb/Orange/Rot)
    opt Substanzielles Gutachten (Schritt 10: review_optional)
        Skill->>Reviewer: Adversarial Second-Opinion Zweitprüfung
        Reviewer-->>Skill: Einwände / Validierungsbefunde
    end
    Skill->>Reporter: Schritt 9: 6-teiligen Gutachtenbericht formatieren
    Reporter-->>User: Strukturiertes Gutachten (_gutachten/JJJJ-MM-TT_<slug>.md)
```

---

## Governance- und Laufzeit-Invarianten

Das System garantiert 10 unverletzliche Governance- und Laufzeit-Invarianten:

| # | Invariante | Beschreibung | Durchsetzungsmechanismus |
|---|---|---|---|
| 1 | **100% Local-First & Zero-Egress** | Gesetzesabruf und Berichterstellung arbeiten vollständig lokal; keine Telemetrie, kein Tracking, kein unerwünschter Datenabfluss. | `.gitignore` schließt `_gutachten/`, `_data/gesetze/` und `config.local.json` strikt aus. |
| 2 | **Strikte Quellenbindung** | Jede gesetzliche Aussage muss exakt mit Artikel/Paragraph, Absatz, Satz und amtlichem Wortlautzitat belegt werden. | `agents/gesetzbuch.md` und `references/berichtsformat.md` verwerfen Erinnerungszitate. |
| 3 | **Web-verifizierte Rechtsprechung** | Urteile dürfen nur mit Gericht, Datum, Aktenzeichen und ECLI zitiert werden; unbestätigte Urteile gelten als „nicht ermittelt". | `SKILL.md` Schritt 6 trennt die Auslegungsschicht strikt vom Modellwissen. |
| 4 | **Reine Selbstanwendung (RDG)** | Klare rechtliche Zweckbindung nach § 2 Abs. 1 RDG; Erstorientierung ohne Begründung eines Mandatsverhältnisses. | Verbindliche Warnhinweise in `README.md`, `SKILL.md` und Abschnitt 5 jedes Berichts. |
| 5 | **Harte Fristendisziplin** | Bei behördlicher oder gerichtlicher Rechtspost hat die Prüfung von Notfristen absoluten Vorrang vor jeder inhaltlichen Prüfung. | `references/eskalation_risiko.md` erzwingt die sofortige Anwaltsempfehlung bei Fristsachen. |
| 6 | **Versionierte Gesetzes-Registry** | Zuschaltungen und Änderungen an Gesetzbüchern sind bewusste, versionierte Architekturentscheidungen. | Schema-Versionierung in `config.json` mit Nachweispflicht im Changelog. |
| 7 | **Benutzermodus & Non-Elevation** | Sämtliche Skripte und Workflows laufen in regulären Benutzerrechten ohne administrative Elevation (`RunAsInvoker`). | Reiner Standard-Python-Interpreter ohne Systemtreiber oder Privilegieneskalation. |
| 8 | **Deterministische Risikomatrix** | Jedes Gutachten ordnet Feststellungen einer 4-stufigen Skala (Gering, Mittel, Hoch, Kritisch) und einer Fachanwaltsdisziplin zu. | Feste Prüfungsmatrix in `references/eskalation_risiko.md`. |
| 9 | **Multi-OS CI-Matrix & Concurrency** | Automatisierte Tests laufen auf Ubuntu, Windows und macOS mit strikter Concurrency-Stornierung (`cancel-in-progress`). | GitHub Actions Matrix (`.github/workflows/ci.yml`) über Python 3.10–3.13. |
| 10 | **Zweisprachige Dokumentationsparität** | Vollständige Parität zwischen deutscher und englischer Dokumentation, verifiziert durch automatisierte Vertragstests. | Pytest-Vertragstestsuite in `tests/test_metadata.py`. |

---

## Rechtlicher Rahmen und RDG-Einordnung

Dieses Werkzeug ist für die **lokal betriebene Selbstanwendung** bestimmt: Du wendest es in deiner eigenen LLM-Umgebung auf **deine eigenen** Fragestellungen an. Es gibt kein zentrales Hosting, keine Fallannahme, keinen Beratungs-Support und keine Fristüberwachung durch die Autoren.

Zur Einordnung nach deutschem Rechtsdienstleistungsrecht (Selbstprüfung des Projekts, Stand 2026-07-11 — Erstorientierung, keine Rechtsberatung):

| Einsatzform | Einordnung |
|---|---|
| Nutzung auf **eigene** Fragestellungen | Keine Rechtsdienstleistung (keine „fremde Angelegenheit", § 2 Abs. 1 RDG). |
| Veröffentlichung/Weitergabe des Werkzeugs | Keine Rechtsdienstleistung (generisches Instrument, kein Einzelfall; vgl. BGH, Urt. v. 09.09.2021 — I ZR 113/20 „Smartlaw" — analog übertragbar und designabhängig). |
| Einsatz, um **für Dritte** konkrete Einzelfälle zu prüfen | Kann Rechtsdienstleistung sein (§ 2 Abs. 1 RDG ist werkzeugneutral) — entgeltlich i. d. R. erlaubnispflichtig (§ 3 RDG); auch unentgeltlich gelten Anforderungen (§ 6 Abs. 2 RDG). **Nicht der vorgesehene Zweck dieses Projekts.** |

Wer die Betriebsform ändert (Hosting, Dienstleistung, Fallbearbeitung für Dritte), muss die Zulässigkeit eigenverantwortlich neu prüfen.
Projektbezogene EU-AI-Act-Selbsteinordnung: siehe [`docs/ai-act-note.md`](docs/ai-act-note.md).

---

## Geschwisterwerkzeuge und Ökosystem

`law-checker` ist in das modulare Open-Source-Ökosystem von `ellmos-ai` und die Dachorganisation `open-bricks` eingebunden:

| Projekt | Rolle / Integration | Repository |
|---|---|---|
| **`ellmos-ai`** | KI-Infrastruktur-Organisation & MCP-Server-Kollektiv | [ellmos-ai](https://github.com/ellmos-ai) |
| **`open-bricks`** | Dachorganisation für modulare Entwickler- und Desktopwerkzeuge | [open-bricks](https://github.com/open-bricks) |
| **`policy-registry`** | Multi-Agenten Governance- und Richtlinienverwaltung | [policy-registry](https://github.com/ellmos-ai/policy-registry) |
| **`anonymizer`** | Fail-Closed Dokumenten-Pseudonymisierung für sicheres Pre-Processing | [anonymizer](https://github.com/ellmos-ai/anonymizer) |
| **`lock-master`** | Multi-Agenten Dateisperr- und Koordinationssystem | [lock-master](https://github.com/ellmos-ai/lock-master) |
| **`automation-master`** | Event-Sourced Reservierungs- und Guthabenverwaltung für Hintergrundagenten | [automation-master](https://github.com/dev-bricks/automation-master) |
| **`system-gap-master`** | Automatisiertes Lücken- und Hygiene-Audit-System | [system-gap-master](https://github.com/ellmos-ai/system-gap-master) |
| **`companion-for-agy`** | Headless CLI-Runner, PTY-Lifecycle-Supervision und Session-Recording | [companion-for-agy](https://github.com/ellmos-ai/companion-for-agy) |
| **`gardener`** | Sandboxed Tool-Execution und lokale SQLite-Wissensdatenbank | [gardener](https://github.com/ellmos-ai/gardener) |
| **`marblerun`** | Multi-Agenten Rundenablauf- und Handoff-Steuerung | [marblerun](https://github.com/ellmos-ai/marblerun) |
| **`report-forge`** | Domänenneutraler Kern für formatierte Gutachten- und Berichts-Pipelines | [report-forge](https://github.com/ellmos-ai/report-forge) |
| **`steuer-assistent`** | Standalone-Werkzeug für Selbstanwendungs-Werbungskosten und Nachweiserfassung | [steuer-assistent](https://github.com/ellmos-ai/steuer-assistent) |

---

## Installation und Schnelleinstieg

### 1. Repository klonen und Abhängigkeiten einrichten

```bash
git clone https://github.com/ellmos-ai/law-checker.git
cd law-checker

# Abhängigkeiten installieren (erfordert Python >=3.10)
pip install -e .
```

### 2. Amtliche Normtexte abrufen

Die Normtexte werden direkt von den amtlichen Stellen bezogen und lokal abgelegt:

```bash
# Verfügbare und aktive Gesetzbücher anzeigen
PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py --list

# Alle aktivierten Gesetzbücher herunterladen und aufbereiten
PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py
```

### 3. Skill & Agent in Claude Code einbinden

```bash
# Skill und Verkörperungs-Agent in das Benutzerprofil kopieren
cp SKILL.md ~/.claude/skills/rechtsabteilung/SKILL.md
cp agents/gesetzbuch.md ~/.claude/agents/gesetzbuch.md
```

Passe in `~/.claude/skills/rechtsabteilung/SKILL.md` die Variable `<MODUL>` an den absoluten Pfad deines lokalen Klons an.

Aufruf in Claude Code:
```text
/rechtsabteilung Ist ein Impressum für rein private Open-Source-Repositories auf GitHub verpflichtend?
```

---

## Neue Gesetze hinzufügen

Das Hinzufügen weiterer Gesetze erfordert keine Code-Änderung an den Agenten:

1. **Eintrag in `config.json`:** Neuen Schlüssel unter `gesetzbuecher` definieren (inkl. `name`, `kurz`, `zitierweise`, `quelle` und ggf. `xml_zip` bei Bundesrecht).
2. **Normtext abrufen:**
   ```bash
   PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py <schluessel>
   ```
3. **Versionierung nachziehen:** Die `version` in `config.json` inkrementieren und die Erweiterung im Changelog festhalten.

*Hinweis zu EU- und Landesrecht:* Für Rechtsakte ohne XML-Schnittstelle auf `gesetze-im-internet.de` (z. B. DSGVO oder MStV) wird der Text als UTF-8-Datei in `_data/gesetze/` abgelegt, versehen mit amtlicher Fundstelle und Abrufdatum im Dateikopf.

---

## Datenschutz und Vertraulichkeit

Rechtliche Fragestellungen berühren regelmäßig sensible persönliche Daten, Geschäftsgeheimnisse oder vertrauliche Kommunikation. Bitte beachte:

- **Datenminimierung:** Schwärze oder anonymisiere Namen, Adressen, Aktenzeichen und finanzielle Details vor der Eingabe in ein LLM. Nutze hierfür ggf. das Partnerprojekt [`anonymizer`](https://github.com/ellmos-ai/anonymizer).
- **Cloud-LLM-Exposition:** Bei der Nutzung von Cloud-Modellen gelangen Eingabedaten an den jeweiligen Modellanbieter. Verwende keine vertraulichen Mandatsunterlagen ohne entsprechende Auftragsverarbeitungsvereinbarung (AVV).
- **Lokale Datenhaltung:** Normtexte und erzeugte Gutachten verbleiben lokal auf deinem System (`_data/gesetze/`, `_gutachten/`). Es erfolgt keinerlei Übermittlung an die Entwickler von `law-checker`.
- **Keine Realdaten in GitHub-Issues:** Verwende für Fehlerberichte oder Feature-Anfragen ausschließlich frei erfundene Mustersachverhalte.

Ausführliche Richtlinien findest du in [`SECURITY.md`](SECURITY.md).

---

## Gesetzes-Registry-Bestand

Die standardmäßige Gesetzes-Registry (`config.json`, v5) umfasst 13 vorkonfigurierte Rechtsmaterien:

| Schlüssel | Bezeichnung | Typ | Status | Quelle |
|---|---|---|---|---|
| `gg` | Grundgesetz für die Bundesrepublik Deutschland | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `bgb` | Bürgerliches Gesetzbuch | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `sgb5` | Sozialgesetzbuch (SGB) Fünftes Buch (V) — GKV | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `urhg` | Urheberrechtsgesetz | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `rdg` | Rechtsdienstleistungsgesetz | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `markeng` | Markengesetz | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `stberg` | Steuerberatungsgesetz | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `uwg` | Gesetz gegen den unlauteren Wettbewerb | Bundesrecht | **Aktiv** | gesetze-im-internet.de |
| `dsgvo` | Datenschutz-Grundverordnung (VO (EU) 2016/679) | EU-Recht | **Aktiv** | EUR-Lex |
| `ehds` | European Health Data Space (VO (EU) 2025/327) | EU-Recht | **Aktiv** | EUR-Lex |
| `grch` | Charta der Grundrechte der Europäischen Union | EU-Recht | **Aktiv** | EUR-Lex |
| `stgb` | Strafgesetzbuch | Bundesrecht | *Inaktiv* | gesetze-im-internet.de |
| `mstv` | Medienstaatsvertrag | Landesrecht | *Inaktiv* | die-medienanstalten.de |

---

<a id="gutachten-architektur--visueller-walkthrough"></a>
## Gutachten-Architektur & Visueller Walkthrough

Jedes von `law-checker` erstellte Rechtsgutachten folgt strikt der standardisierten 6-Punkte-Struktur aus [`references/berichtsformat.md`](references/berichtsformat.md) und wahrt die juristische Methodik (*Gutachtenstil*):

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 STRUKTURIERTE JURISTISCHE ERSTEINSCHÄTZUNG                  │
│ Datei: _gutachten/YYYY-MM-DD_<themen-slug>.md                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Sachverhalt & Fragestellung (Factual Inquest & Scope)                    │
│    ├─ Fragesteller, Kontext & Sachverhaltselemente                          │
│    └─ VORRANGIGER PFLICHTCHECK: Fristenprüfung bei behördlicher/Rechtspost  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. Norm-Ebene: Authentischer Gesetzeswortlaut (Embodiment-Auszüge)          │
│    ├─ Ermittelter relevanter Normbestand (z. B. § 5 TDDDG, BGB)             │
│    └─ Absatz- und satzgenaue Verbatim-Zitate aus lokalem XML-Bestand        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. Rechtsprechung & Auslegung (Web-verifizierte Leitentscheidungen)         │
│    ├─ Einschlägige obergerichtliche Urteile (BGH, BAG, BVerfG, EuGH)        │
│    └─ Strenges Zitierformat: Gericht, Datum, Az., Fundstelle, ECLI          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. Synthese & Subsumtion (Juristische Methodik / Gutachtenstil)             │
│    ├─ Tatbestandsmerkmale vs. vorliegender Lebenssachverhalt                │
│    └─ Eindeutige Kennzeichnung: Was ist zwingend, was vertretbare Auslegung?│
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. Risikoeinstufung & Anwaltsempfehlung (Risiko-Ampel & Eskalation)         │
│    ├─ Ampel-Score: [GERING / GRÜN] | [MITTEL / GELB] | [HOCH] | [KRITISCH]   │
│    ├─ Begründung & konkrete Schadens-/Abmahnpotenziale                      │
│    └─ Fachanwalts-Empfehlung mit zutreffender Fachanwaltsbezeichnung        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. Quellenverzeichnis & Prüfprotokoll (Provenance & Audit-Log)              │
│    ├─ Verwendete Gesetzestexte mit amtlichem Abruf- und Standstempel        │
│    └─ Revisions- und Modelldaten des ausführenden LLM-Laufs                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<a id="drittanbieter-lizenzen--sbom"></a>
## Drittanbieter-Lizenzen & SBOM

`law-checker` ist freie Open-Source-Software unter der [MIT-Lizenz](LICENSE). Eine vollständige Software-Stückliste (SBOM) und Lizenzprüfung ist in [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) hinterlegt:

- **Frei von Copyleft-Infektionen:** Keine GPL-, AGPL- oder SSPL-Abhängigkeiten; uneingeschränkt nutzbar für lokale Entwickler und Unternehmen.
- **Unprivilegierte Ausführung (`RunAsInvoker`):** Benötigt unter keinem Betriebssystem Administrator- oder Root-Rechte.
- **Amtliche Werke im Public Domain:** Die über `gesetze-im-internet.de` bezogenen Normtexte sind amtliche Werke im Sinne von § 5 Abs. 1 UrhG und gemeinfrei. Rechtsakte der Europäischen Union werden auf Grundlage des Beschlusses 2011/833/EU der Kommission weiterverwendet.

---

## Repository-Struktur

```text
law-checker/
├── .github/workflows/ci.yml    ← Multi-OS CI-Matrix (Ubuntu, Windows, macOS)
├── .github/workflows/stale.yml ← Automatisierte Bereinigung verwaister Issues & PRs
├── SKILL.md                    ← Orchestrierungs-Skill (10-Schritte-Workflow)
├── config.json                 ← Gesetzes-Registry und Ablaufdefinition (v5)
├── agents/
│   └── gesetzbuch.md           ← Generischer Normtext-Verkörperungsagent
├── references/
│   ├── berichtsformat.md       ← 6-teiliges Gutachten-Schema & Belegformate
│   └── eskalation_risiko.md    ← Risiko-Ampel, Fristen-Check, Anwaltsmatrix
├── _tools/
│   ├── __init__.py             ← Python-Paket-Initialisierung
│   └── gesetze_fetch.py        ← Normtext-Downloader & XML-Extraktor
├── docs/
│   └── ai-act-note.md          ← EU-AI-Act-Selbsteinordnung
├── tests/
│   ├── test_gesetze_fetch.py   ← Unit-Tests für Parser & XML-Extraktion
│   └── test_metadata.py        ← Automatisierte Metadaten- & Paritäts-Tests
├── CHANGELOG.md                ← Chronologischer Versionsverlauf
├── SECURITY.md                 ← Sicherheitsrichtlinie mit 48h-Reaktions-SLA
├── THIRD_PARTY_LICENSES.md     ← Drittanbieter-Lizenzaudit, SBOM & § 5 UrhG Nachweis
├── MARKETING-LOG.txt           ← Lokale Marketing- & Discoverability-Empfehlungen
├── llms.txt                    ← Maschinenlesbarer Kontext für KI-Agenten
├── ellmos-module.v2.json       ← Modulmanifest (rechtsabteilung)
├── pyproject.toml              ← PEP 621 Metadaten & Test-Konfiguration
├── _data/gesetze/              ← Lokale Normtexte (unversioniert via .gitignore)
└── _gutachten/                 ← Erstellte Prüfberichte (unversioniert via .gitignore)
```

---

## Sicherheitsrichtlinie

Sicherheit und Vertraulichkeit haben oberste Priorität. Schwachstellen können vertraulich gemeldet werden über:
- [GitHub Security Advisories](https://github.com/ellmos-ai/law-checker/security/advisories)
- E-Mail: `security@ellmos.ai` | `security@open-bricks.org` | `support@lukasgeiger.com` | `lukas@open-bricks.org`

**Verbindliche SLAs:** Eingangsbestätigung innerhalb von 48 Stunden; Triage und Bewertung innerhalb von 5 Werktagen. Weitere Details in [`SECURITY.md`](SECURITY.md).

---

## Herkunft und Autorenschaft

Das Projekt führt drei praxiserprobte Konzepte zusammen:
1. **Redaktions-Rechtspolicy:** Strukturierte Berichtsformate, objektive 4-Stufen-Risikomatrix, Fachanwaltszuordnung und kompromisslose Fristendisziplin.
2. **Forschungsprototyp „Lebende Verfassung":** Das Muster der Normverkörperung mit strenger Quellenbindung, getrennter Auslegungsschicht und Begrenzung auf den authentischen Wortlaut.
3. **Jura-Wissenssystematik:** Systematische Zuordnung nach Rechtsgebieten und Grundsätzen des deutschen Gutachtenstils.

Der erste Volllauf des systems war seine eigene Veröffentlichungsprüfung — inklusive eines adversarialen Reviews durch ein unabhängiges Zweitmodell.

---

<a id="haftung-lizenz-und-grenzen"></a><a id="gesetzlicher-haftungshinweis--521-bgb--lizenz"></a>
## Haftung, Lizenz und Grenzen

### Gesetzlicher Haftungshinweis gem. § 521 BGB (Gefälligkeitsrecht)

> [!IMPORTANT]
> **Haftungsbeschränkung gem. § 521 BGB:** Die Bereitstellung dieser Software, der Dokumentation, der Prompts und der Prüfungsabläufe erfolgt unentgeltlich und als Gefälligkeit im Sinne des deutschen Zivilrechts (§ 521 BGB). Die Haftung der Urheber, Maintainer und Mitwirkenden ist auf Vorsatz und grobe Fahrlässigkeit beschränkt. Die Software stellt keine Rechtsdienstleistung im Sinne des § 2 Abs. 1 RDG dar und ersetzt keine individuelle Prüfung durch eine zugelassene Rechtsanwältin oder einen zugelassenen Rechtsanwalt. Es erfolgt keine Fristenkontrolle und keine Gewähr für Vollständigkeit, Fehlerfreiheit oder Aktualität.

- **Lizenz:** Veröffentlicht unter der permissiven [MIT-Lizenz](LICENSE) — gültig für Quelltext, Prompts und Dokumentation.
- **Drittanbieter-SBOM:** Der Lizenzaudit zu Drittanbieter-Bibliotheken sowie die Gemeinfreiheit amtlicher Werke gem. § 5 Abs. 1 UrhG sind in [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) dokumentiert.
- **Haftungsausschluss:** Der Betrieb erfolgt ohne Gewährleistung für Aktualität, Richtigkeit oder Vollständigkeit der erzeugten Auswertungen. Gesetzestexte unterliegen dem Wandel; vor rechtserheblichen Entscheidungen sind die amtlichen Verkündungsblätter (Bundesgesetzblatt) heranzuziehen.
- **Keine Rechtsberatung:** Das Werkzeug dient ausschließlich der Vorbereitung und Erstorientierung.
