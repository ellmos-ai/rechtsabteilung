# Changelog

All notable changes to this project are documented here.
The statute registry carries its own `version` counter in `config.json`;
registry changes are listed under the release that shipped them.

## Unreleased

### Fixed

- Synchronized the PEP 621 project version with the documented `0.2.3`
  release. The later PEP 639 license-metadata migration had left
  `pyproject.toml` at `0.2.2`; this correction does not change the separate
  statute-registry version (`config.json` v5).

## 0.2.3 — 2026-07-28

### Added

- Synchronized `llms.txt` and `README.md` AI/LLM discovery verification timestamp (`2026-07-28`).
- Verified 4/4 Pytest unit test suite passing (0.48s).

## 0.2.2 — 2026-07-26

### Added

- Added unit test suite (`tests/test_gesetze_fetch.py`) testing registry loading, norm text extraction, XML parsing, and skip logic in `_tools/gesetze_fetch.py`.
- Verified 4/4 Pytest unit tests passing (0.13s).
- Synchronized `llms.txt` verification timestamp (`2026-07-26`).

## 0.2.1 — 2026-07-25

### Added

- Added PEP 621 compliant `pyproject.toml` with project metadata, dependencies (`requests`, `urllib3`), keywords, project URLs, and `[tool.pytest.ini_options]`.
- Added GFM `> [!NOTE]` alert callout in `README.md` highlighting machine-readable `llms.txt` discovery for AI and LLM agents.
- Added Mermaid System Architecture diagram in `README.md` illustrating the multi-stage legal orientation workflow (Request -> SKILL.md -> config.json registry -> official statute fetcher -> statute embodiment agent -> case-law verification -> report format & risk matrix).
- Verified `llms.txt` verification timestamp (`2026-07-25`).

### Documentation

- Removed absolute local paths and author-specific tooling references from
  `SKILL.md`; the module path is now described generically, so a fresh clone
  works without knowing the author's directory layout.
- Corrected the installation section: `gesetze_fetch.py` without arguments
  fetches **all enabled** registry entries, not just GG and BGB. Added the
  current registry inventory (13 registered, 11 active) and `--list` as the
  first step.
- Completed the repository layout tree (`CHANGELOG.md`, `SECURITY.md`,
  `llms.txt` and `ellmos-module.v2.json` were missing from it).
- Added `SECURITY.md` covering confidential legal material, cloud-LLM exposure
  and the reporting path.

### Fixed

- Normalised German end-user strings in `config.json` and in the CLI output of
  `_tools/gesetze_fetch.py` to real umlauts (`für`, `über`, `Bürgerliches`,
  `außergerichtliche`, …). JSON keys, registry keys, workflow step identifiers
  and file paths were deliberately left untouched.
- Added `.gitattributes` (`* text=auto eol=lf`). Without it, Windows clones
  reported every tracked text file as modified right after checkout.
- `_tools/gesetze_fetch.py` still referred to the module by its former name
  (`rechtsabteilung`) in its docstring.
- Module manifest (`ellmos-module.v2.json`) still declared
  `status: development` and `visibility: public-candidate` although the
  repository has been public since the 0.1.0 release.

### Removed

- `TODO.md` is no longer tracked. It was an internal audit record (auditor,
  gate exit code, internal repository path) that was never meant for readers of
  the public repository. Its open follow-ups are tracked with the project
  rather than in the published tree.

## 0.1.0 — 2026-07-23

Initial public release under the MIT license.

### Added

- Skill and agent bundle for source-grounded first-look legal orientation on
  German law: orchestration workflow (`SKILL.md`), generic statute embodiment
  agent (`agents/gesetzbuch.md`), report format and risk/escalation references.
- Configurable statute registry (`config.json`) with `_tools/gesetze_fetch.py`
  for fetching official federal law texts from gesetze-im-internet.de.
- EU AI Act self-classification note (`docs/ai-act-note.md`) and an RDG scope
  table in the README.
- Public discovery metadata in `llms.txt`, README banner and Shields.io badges.

### Registry

- **config v5 (2026-07-23):** added and activated the German Tax Advisory Act
  (StBerG) on demand for the `steuer-assistent` publication review.
- **config v4 (2026-07-19):** activated SGB V and the GDPR; added and activated
  Regulation (EU) 2025/327 (EHDS) and the Charter of Fundamental Rights of the
  European Union from official federal and EUR-Lex source texts.
