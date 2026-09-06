# Security Policy / Sicherheitsrichtlinie

This repository contains prompts, a statute registry and a fetch tool. It ships
no server, no hosted service and no AI model. The security surface that matters
here is therefore less about the code and more about **what users put into it**:
legal matters routinely carry personal data, business secrets and privileged
correspondence.

## Supported Versions

| Version | Supported | Notes |
| ------- | --------- | ----- |
| `0.2.x` | :white_check_mark: | Current active release branch (`main`) |
| `< 0.2` | :x: | Legacy development tags — please upgrade |

## Confidential Material — What Stays Local

The tool itself sends nothing to the authors. Two directories hold whatever you
feed in or generate, and both are excluded from version control:

| Path | Content | Tracked? |
|---|---|---|
| `_gutachten/` | your generated assessments, including the underlying facts | no (`.gitignore`) |
| `_data/gesetze/` | statute texts fetched from official sources | no (`.gitignore`) |
| `config.local.json` | local overrides, e.g. paths to your own knowledge base | no (`.gitignore`) |

Verify this before you commit: `git status --porcelain` should never list a file
from `_gutachten/`. If it does, do not commit — check `.gitignore` first.

## The Real Exposure: Your Model Provider

`law-checker` runs inside **your** LLM environment. Everything you paste into a
prompt goes wherever that environment sends it.

- Running against a cloud model means your facts reach that provider. Do not
  paste unredacted legal correspondence, health data, client matters or
  anything under a duty of confidentiality into a third-party model without
  checking its terms first.
- Minimise before you prompt: redact names, addresses, case numbers and
  identifiers wherever the legal question does not depend on them.
- Statute texts are public; your facts are not. Only the latter needs care.

## Never in a GitHub Issue

Do not put real case material — documents, letters, names, case numbers,
generated assessments — into issues, discussions or pull requests. Reduce the
problem to a minimal, invented example. Anything posted there is public and
permanent.

## Reporting a Vulnerability

Please report security issues responsibly:

1. **Do not open a public issue.**
2. Use [GitHub Security Advisories](https://github.com/ellmos-ai/law-checker/security/advisories) on this repository (private vulnerability report).
3. Alternatively, report directly to our official security team:
   - `security@ellmos.ai`
   - `support@lukasgeiger.com`
   - `lukas@open-bricks.org`
   - `security@open-bricks.org`

### Response SLA

- **Acknowledgment:** Within 48 hours.
- **Initial Assessment & Triage:** Within 5 business days.
- **Remediation & Advisory:** Coordinated release and advisory publication.

Relevant findings include: a path that writes assessment content outside the ignored directories, a registry entry pointing at a non-official source, or a change that causes local data to be committed or transmitted.

## Out of Scope

Legal accuracy is not a security matter. The tool produces a **first-look orientation and no legal advice**; incorrect, incomplete or outdated legal conclusions are a documented limitation (see `README.md`), not a vulnerability. Statute texts age — re-run `_tools/gesetze_fetch.py` before relying on them.

---

## Sicherheitsrichtlinie (Deutsch)

Dieses Repository enthält Prompts, eine Gesetzes-Registry und ein Abrufwerkzeug. Es betreibt keinen externen Server und kein Cloud-Backend. Das relevante Sicherheitsrisiko betrifft daher die Vertraulichkeit verarbeiteter Rechtsdaten und Fakten.

### Unterstützte Versionen

| Version | Unterstützt | Anmerkung |
| ------- | ----------- | --------- |
| `0.2.x` | :white_check_mark: | Aktueller Entwicklungs- und Release-Zweig (`main`) |
| `< 0.2` | :x: | Veraltet — bitte auf aktuelle Version aktualisieren |

### Vertrauliche Inhalte & Lokale Datenhaltung

Das Werkzeug selbst übermittelt keine Daten an die Autoren. Bewertungsdaten verbleiben lokal in unversionierten Verzeichnissen (`_gutachten/`, `_data/gesetze/`, `config.local.json`).

### Verantwortliche Schwachstellenmeldung

Bitte melden Sie Sicherheitslücken nicht über öffentliche GitHub-Issues, sondern über [GitHub Security Advisories](https://github.com/ellmos-ai/law-checker/security/advisories) oder direkt an:
- `security@ellmos.ai`
- `support@lukasgeiger.com`
- `lukas@open-bricks.org`
- `security@open-bricks.org`

**Reaktions-SLA:** Empfangsbestätigung innerhalb von 48 Stunden, qualifizierte Ersteinschätzung innerhalb von 5 Werktagen.
