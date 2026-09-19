# Changelog

All notable changes to this project are documented here.
The statute registry carries its own `version` counter in `config.json`;
registry changes are listed under the release that shipped them.

## 0.2.7 — 2026-09-19

### Added

- **Target Personas & High-Intent SEO Queries:** Formal persona mapping ([PERSONA-01] Legal Tech Engineers & In-House Legal Ops, [PERSONA-02] Open-Source Maintainers & Indie Developers, [PERSONA-03] AI Agent Developers & Solution Architects, [PERSONA-04] Compliance Officers & DPOs) with high-intent search queries in `README.md` and `README_de.md`.
- **10-Dimension Comparative Matrix vs. 4 Alternatives:** In-depth comparative analysis evaluating `law-checker` against Naive General LLMs, Traditional Legal Databases (Beck/Juris), RAG/Vector Embedding Retrieval, and Web Search across 10 architectural invariants.
- **18-Point Bilingual Navigation Parity:** Expanded quick navigation across `README.md` and `README_de.md` with reciprocal HTML anchor aliases (`<a id="..."></a>`) guaranteeing backward compatibility and bookmark stability.
- **Statutory Open-Source Notice (§ 521 BGB Gefälligkeitsrecht):** Explicit statutory disclaimer for gratuitous open-source provision under German civil law in both English and German documentation.
- **Third-Party License Audit & SBOM:** New canonical `THIRD_PARTY_LICENSES.md` documenting runtime dependencies, build tooling, and official public domain status (§ 5 Abs. 1 UrhG / Decision 2011/833/EU) with Zero-Copyleft isolation.
- **Visual Terminal & Report Architecture Walkthrough:** Structured ASCII and visual workflow representation detailing the 6-section legal orientation format and interactive execution model.
- **PEP 621 Metadata & Contract Test Expansion:** Updated `pyproject.toml` with `THIRD_PARTY_LICENSES.md` in `license-files`, enriched SEO keywords, and extended ecosystem URLs (`Third-Party Licenses`, `Marketing Log`, `LLM Ready`). Expanded `tests/test_metadata.py` with 6 new contract tests covering 18-point navigation, target personas, comparative matrix, third-party SBOM, § 521 BGB statutory notice, and version parity.

### Changed

- Synchronized `llms.txt` with version `0.2.7`, updated Last-checked date `2026-09-19`, expanded 18-point navigation references, and test suite counts.
- Updated Shields.io badges in `README.md` and `README_de.md` to version `0.2.7`, tests badge to passing, and enriched metadata.

## 0.2.6 — 2026-09-10

### Added

- Dedicated Stale Issues & Pull Requests workflow (`.github/workflows/stale.yml`) for automated lifecycle management and inactivity triage.
- Standardized OS classifiers in `pyproject.toml` for Microsoft Windows, POSIX Linux, and macOS.
- PEP 621 optional dependencies (`dev`, `test`) in `pyproject.toml` for standardized testing and linting environments.
- Pytest standard invocation configuration (`addopts = "-ra -v"`) and Ruff target configuration (`line-length = 100`, `target-version = "py310"`) in `pyproject.toml`.
- Expanded automated contract test suite in `tests/test_metadata.py` with 5 additional contract tests covering CI permissions and bytecode gates, stale workflow existence, .gitignore multi-host synchronization patterns, Pytest options and OS classifiers, and CHANGELOG release synchronization (24/24 tests passing).

### Changed

- Hardened CI workflow (`.github/workflows/ci.yml`) with explicit `permissions: { contents: read }`, standardized `pytest -ra -v` runner, and repository-wide bytecode compilation check (`python -m compileall -q .`).
- Hardened `.gitignore` with multi-host synchronization conflict patterns (`*-conflict-*`, `*.sync-temp-*`, `*-ASUS-GEI.*`, `*-WORKSTATION-LG.*`), multi-agent lock patterns (`LOCK`, `LOCK.*`, `LOCK.permissions.json`), and packaging caches (`wheelhouse/`, `coverage/`, `*.swp`, `*.log`).
- Bumped project version to `0.2.6` in `pyproject.toml` and synchronized `llms.txt` (version 0.2.6, Last-checked: 2026-09-10).
- Updated Shields.io badges in `README.md` and `README_de.md` to reflect version `0.2.6`, 24 passing tests, and updated discovery date.

## 0.2.5 — 2026-09-09

### Added

- Canonical German documentation (`README_de.md`) with 100% bilingual parity to `README.md`, including bidirectional language switchers (`**English** | [Deutsch](README_de.md)` / `[English](README.md) | **Deutsch**`).
- 14-point standardized quick navigation with matching anchor parity across English and German documentation.
- Dual bilingual Mermaid diagrams:
  - System architecture flowchart (`flowchart TD`) mapping orchestrator, statute registry, XML fetcher, embodiment agent, case law layer, report format, and escalation matrix.
  - 10-step legal orientation lifecycle sequence diagram (`sequenceDiagram` with `autonumber`) illustrating the step-by-step execution path, incoming mail deadline triage, parallel statute embodiment, web-verified jurisprudence, and adversarial review.
- Comprehensive table of 10 immutable Governance & Runtime Invariants (100% local-first isolation, strict source grounding, web-verified jurisprudence, RDG self-use boundaries, strict deadline discipline, statute registry versioning, non-elevation safety, deterministic risk scoring, multi-OS CI matrix, and bilingual documentation parity).
- Sibling Tools & Ecosystem integration matrix cross-linking 12 partner repositories across `ellmos-ai` and `open-bricks` (including `anonymizer`, `policy-registry`, `lock-master`, `automation-master`, `companion-for-agy`, etc.).
- Local marketing and discoverability log (`MARKETING-LOG.txt`) tracking completed visibility enhancements, homepage URL fixes, and open external recommendations (screencast walkthrough, legal tech publications, MCP server directory listings, D-A-CH statute expansion, local UI demo).
- Expanded automated contract test suite in `tests/test_metadata.py` verifying navigation anchor parity, bilingual language switchers, mermaid diagram syntax validity, governance invariants, and marketing log presence.

### Changed

- Overhauled `README.md` to full English documentation with modernized Shields.io badges, comprehensive operational guidelines, and legal classification under § 2 Abs. 1 RDG.
- Corrected live GitHub repository homepage URL from outdated hash link to canonical `https://github.com/ellmos-ai/rechtsabteilung#readme`.
- Bumped project version to `0.2.5` in `pyproject.toml` and synchronized `llms.txt` (version 0.2.5, Last-checked: 2026-09-09).

## 0.2.4 — 2026-09-06

### Added

- Multi-OS GitHub Actions CI workflow (`.github/workflows/ci.yml`) testing matrix across Ubuntu, Windows, and macOS on Python 3.10, 3.11, 3.12, and 3.13 with concurrency cancellation (`cancel-in-progress: true`).
- Comprehensive automated contract test suite (`tests/test_metadata.py`) verifying PEP 621 metadata, PEP 639 SPDX license, CI matrix integrity, bilingual security policy, .gitignore patterns, llms.txt parity, and zero path leaks (14/14 Pytest tests passing | 100% pass).
- Full PEP 621 `[project.urls]` in `pyproject.toml` including Parent Organization (`ellmos-ai`), Umbrella Ecosystem (`open-bricks`), and Security policy links.
- `_tools/__init__.py` and explicit `[tool.setuptools.packages.find]` packaging configuration in `pyproject.toml` resolving flat-layout packaging build error.
- Bilingual security policy (`SECURITY.md`) with structured Supported Versions table (`0.2.x`), 48-hour response SLA, and official security contacts (`security@ellmos.ai`, `support@lukasgeiger.com`, `lukas@open-bricks.org`, `security@open-bricks.org`).
- Repository hygiene and `.gitignore` hardening with sync conflict patterns, test caches, coverage artifacts, and lock file rules.
- Shields.io badges in `README.md` synchronized to 14 passed Pytest tests, multi-OS CI matrix, ecosystem, umbrella, and AI-friendly discovery.
- Synchronized `llms.txt` with version `0.2.4` and Last-checked date `2026-09-06`.

## 0.2.3 — 2026-07-28

### Added

- Synchronized `llms.txt` and `README.md` AI/LLM discovery verification timestamp (`2026-07-28`).
- Verified 4/4 Pytest unit test suite passing (0.48s).

### Fixed

- Synchronized the PEP 621 project version with the documented `0.2.3`
  release. The later PEP 639 license-metadata migration had left
  `pyproject.toml` at `0.2.2`; this correction does not change the separate
  statute-registry version (`config.json` v5).

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
