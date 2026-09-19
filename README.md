**English** | [Deutsch](README_de.md)

![law-checker banner](assets/banner.png)

# law-checker (Legal Department)

[![Version: 0.2.7](https://img.shields.io/badge/Version-0.2.7-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-28%20passed-brightgreen.svg)](tests/)
[![CI Matrix](https://img.shields.io/badge/CI-Multi--OS%20%7C%20Ubuntu%20%7C%20Windows%20%7C%20macOS-blue.svg)](.github/workflows/ci.yml)
[![Local-First](https://img.shields.io/badge/Architecture-Local--First-green.svg)](#data-privacy--confidentiality)
[![Zero-Egress](https://img.shields.io/badge/Privacy-100%25%20Offline%20%2F%20Zero--Egress-success.svg)](#data-privacy--confidentiality)
[![SBOM](https://img.shields.io/badge/SBOM-Level%201%20Compliant-blue.svg)](THIRD_PARTY_LICENSES.md)
[![Security SLA](https://img.shields.io/badge/Security-48h%20SLA-blue.svg)](SECURITY.md)
[![RDG](https://img.shields.io/badge/RDG-%C2%A7%202%20Abs.%201%20Compliant-brightgreen.svg)](#legal-framework--rdg-classification)
[![Claude Code Skill](https://img.shields.io/badge/Skill-Claude%20Code-purple.svg)](SKILL.md)
[![Ecosystem: ellmos-ai](https://img.shields.io/badge/Ecosystem-ellmos--ai-blue.svg)](https://github.com/ellmos-ai)
[![Umbrella: open-bricks](https://img.shields.io/badge/Umbrella-open--bricks-indigo.svg)](https://github.com/open-bricks)
[![llms.txt](https://img.shields.io/badge/AI--Friendly-llms.txt-brightgreen.svg)](llms.txt)
[![Language](https://img.shields.io/badge/Language-English-blue.svg)](#)

**Open-source AI workflow for source-grounded legal first-look orientation under German law.**

> [!NOTE]
> **AI / LLM Agent Discovery:** A machine-readable summary is available in [`llms.txt`](llms.txt) (last checked: 2026-09-19).

> [!IMPORTANT]
> **Important Notice / Wichtig: AI-assisted first-look legal orientation, no legal advice.** This tool is not a law firm, not a hosted legal service, and not a replacement for an individual legal assessment by an admitted attorney-at-law. Whether a specific deployment constitutes a regulated legal service under the German Legal Services Act (*Rechtsdienstleistungsgesetz*, RDG) depends on operational model, operator role, and the individual case. There is no automated deadline monitoring and no guarantee of completeness or currency. If official, administrative, or judicial legal correspondence and running deadlines are involved, consult qualified legal counsel immediately.

---

## Quick Navigation

1. [Overview](#overview)
2. [Target Personas & High-Intent Use Cases](#target-personas--high-intent-use-cases)
3. [Comparative Architecture Matrix](#comparative-architecture-matrix)
4. [System Architecture](#system-architecture)
5. [Workflow Lifecycle](#workflow-lifecycle)
6. [Governance & Runtime Invariants](#governance--runtime-invariants)
7. [Legal Framework & RDG Classification](#legal-framework--rdg-classification)
8. [Sibling Tools & Ecosystem](#sibling-tools--ecosystem)
9. [Installation & Quickstart](#installation--quickstart)
10. [Adding New Statutes](#adding-new-statutes)
11. [Data Privacy & Confidentiality](#data-privacy--confidentiality)
12. [Statute Registry Inventory](#statute-registry-inventory)
13. [Report Architecture & Visual Walkthrough](#report-architecture--visual-walkthrough)
14. [Third-Party Licenses & SBOM](#third-party-licenses--sbom)
15. [Repository Layout](#repository-layout)
16. [Security Policy](#security-policy)
17. [Provenance & Authorship](#provenance--authorship)
18. [Statutory Disclaimer (§ 521 BGB) & License](#statutory-disclaimer--521-bgb--license)

---

## Overview

`law-checker` (*Rechtsabteilung*) is a modular skill and agent collective for local LLM developer environments such as Claude Code. It produces structured, documented first-look legal assessments grounded in German federal and European Union law.

The system enforces strict evidentiary discipline:
- **Zero Hallucinated Citations:** Every statutory assertion must be drawn directly from locally stored, official statute texts and cited down to the exact article or section, paragraph, and sentence (`§ 823 Abs. 1 BGB` + verbatim excerpt + source file/retrieval timestamp). Memory-based norm citations are rejected.
- **Embodiment Principle:** A specialized generic agent ("You ARE the statute book") reads only the authentic statutory text — applying strict scope discipline (assessing applicability prior to application) and candidly flagging: *"My statutory wording does not decide this; here judicial interpretation begins."*
- **Separate Jurisprudence Layer:** Court decisions are never recalled from training memory. Case law is gathered strictly via live web verification (court, date, docket number, ECLI, and verified citation). Negative lookups are explicitly marked as "not identified".
- **Risk Traffic Light & Escalation Matrix:** Objective risk classification across Low, Medium, High, and Critical tiers, complemented by a legal specialization routing matrix and strict deadline discipline for incoming legal mail.

---

<a id="target-personas--use-cases"></a><a id="target-personas--high-intent-use-cases"></a>
## Target Personas & High-Intent Use Cases

`law-checker` is engineered for technical practitioners, developers, and compliance stakeholders operating under European and German legal jurisdictions who require fast, deterministic legal first-looks without risking hallucinated norms or data leakage:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TARGET PERSONA MAPPING & USE CASES                    │
├────────────────────────────────┬────────────────────────────────────────────┤
│ [PERSONA-01] Legal Tech / Ops  │ Automated statutory first-looks for in-    │
│                                │ house counsel without proprietary lock-in. │
├────────────────────────────────┼────────────────────────────────────────────┤
│ [PERSONA-02] OSS Maintainers   │ Rapid clarity on German Impressumspflicht, │
│                                │ GDPR privacy notices & license attribution.│
├────────────────────────────────┼────────────────────────────────────────────┤
│ [PERSONA-03] AI Architects     │ Zero-hallucination statutory embodiment &  │
│                                │ clean norm-vs-doctrine boundary design.    │
├────────────────────────────────┼────────────────────────────────────────────┤
│ [PERSONA-04] DPOs & Compliance │ Auditable assessment trails for GDPR, EHDS │
│                                │ (EU 2025/327) & SGB V digital health norms.│
└────────────────────────────────┴────────────────────────────────────────────┘
```

- **`[PERSONA-01]` Legal Tech Engineers & In-House Legal Operations:**
  - *Core Problem:* Commercial legal databases (Beck-Online, Juris) lack native agentic LLM integration and charge thousands of euros per seat license; naive LLM chats hallucinate statutes.
  - *Solution:* Fully scriptable, source-grounded CLI and skill pipeline for Claude Code grounded in official BMJ/BfJ XML repositories.
  - *High-Intent Queries:* `German legal tech AI first look`, `automated statute checker API`, `in-house legal workflow LLM`.
- **`[PERSONA-02]` Open-Source Maintainers & Indie Developers:**
  - *Core Problem:* Unclear German regulatory obligations (e.g. *Impressumspflicht* under TDDDG / TMG, DSGVO compliance on GitHub, MIT/AGPL copyright notices under UrhG).
  - *Solution:* Fast, reproducible check showing verbatim whether a personal developer repo requires a German imprint or falls under non-commercial exceptions.
  - *High-Intent Queries:* `Is an Impressum required for personal GitHub repo Germany`, `TDDDG Impressum open source`, `German copyright UrhG software license`.
- **`[PERSONA-03]` AI Agent Developers & Solution Architects:**
  - *Core Problem:* Vector-based RAG truncates statutory text across chunk boundaries, separating general provisions from lex-specialis exceptions and producing false claims.
  - *Solution:* The Embodiment Agent pattern (`agents/gesetzbuch.md`) where the LLM embodies the enacted statutory text with strict lexical discipline ("My wording does not decide this").
  - *High-Intent Queries:* `Statute embodiment AI agent architecture`, `zero hallucination legal prompt pattern`, `Claude Code legal skill`.
- **`[PERSONA-04]` Compliance Officers & Data Protection Officers (DPOs):**
  - *Core Problem:* Digital health apps, AI products, and research software require verifiable GDPR, EHDS (Regulation (EU) 2025/327), and SGB V compliance assessments with an audit trail.
  - *Solution:* 6-section Gutachten format with explicit risk scoring (Low, Medium, High, Critical), statutory citation timestamps, and professional legal referral escalation.
  - *High-Intent Queries:* `EHDS Regulation EU 2025/327 legal compliance check`, `SGB V health data AI assessment`, `DSGVO privacy risk triage`.

---

<a id="comparative-architecture-matrix"></a>
## Comparative Architecture Matrix

How `law-checker` compares across 10 mission-critical architectural criteria against common alternatives:

| Architectural Dimension | Naive LLM Chat (ChatGPT/Claude Raw) | Traditional Legal DBs (Beck/Juris) | Generic Legal RAG / Vectors | Unassisted Web Search / Forums | `law-checker` (Rechtsabteilung) |
|---|---|---|---|---|---|
| **1. Norm-Level Grounding** | ❌ None (param memory) | ⚠️ Manual lookup only | ⚠️ Partial (chunk splits) | ❌ Secondary sources only | ✅ **Strict Verbatim (§, Abs., S.)** |
| **2. Hallucination Immunity** | ❌ Frequent invented §§ | ✅ High (authentic text) | ❌ Hallucinates context | ❌ High (outdated posts) | ✅ **100% Enacted XML Caches** |
| **3. Embodiment Discipline** | ❌ Mixes opinion & law | ❌ N/A (human reader) | ❌ Blurs commentary & norm | ❌ Speculation rampant | ✅ **"You ARE the Statute Book"** |
| **4. Case Law Verification** | ❌ Confabulated Az./ECLI | ✅ Comprehensive (paywalled)| ⚠️ Unverified citations | ⚠️ Mixed accuracy | ✅ **Live Web-Verified Only** |
| **5. Zero-Egress Privacy** | ❌ Full prompt egress | ⚠️ Search queries logged | ⚠️ Embeddings sent to cloud | ❌ Trackers & search logs | ✅ **100% Local-First / Gitignored** |
| **6. Regulatory Demarcation** | ❌ Disclaimers often weak | ⚠️ Enterprise terms | ❌ Unclear liability | ❌ Unregulated advice risk | ✅ **Strict § 2 RDG Self-Use Notice** |
| **7. Deadline Triage** | ❌ Ignored | ❌ Manual calendar | ❌ Ignored | ❌ Easily missed | ✅ **Step 2 Priority Deadline Gate** |
| **8. Versioned Registry** | ❌ Black-box training cutoff | ⚠️ Silent updates | ❌ Unversioned indexes | ❌ Search engine flux | ✅ **Auditable `config.json` (v5)** |
| **9. Multi-OS CI Testing** | ❌ N/A | ❌ Closed proprietary | ⚠️ Ad-hoc unit tests | ❌ N/A | ✅ **Ubuntu / Windows / macOS CI** |
| **10. Cost & License** | ⚠️ $20–$200/month/seat | ❌ €1,500–€5,000+/year | ⚠️ Infrastructure compute | ✅ Free (but time-sink) | ✅ **100% Free & Open Source (MIT)** |

---

## System Architecture

The architecture separates orchestration, authentic statutory sources, judicial interpretation, and report generation into clean modular layers:

```mermaid
flowchart TD
    User["User Legal Query"] --> Skill["SKILL.md Orchestrator"]
    Skill --> Config["config.json Statute Registry"]
    Config --> Fetcher["_tools/gesetze_fetch.py"]
    Fetcher --> OfficialSources["Official Sources (gesetze-im-internet.de / EUR-Lex)"]
    OfficialSources --> LocalData["Local Statute Data Files (_data/gesetze/)"]
    LocalData --> Embodiment["agents/gesetzbuch.md (Statute Agent)"]
    Skill --> WebCaseLaw["Web-Verified Case Law Layer"]
    Embodiment --> ReportFormat["references/berichtsformat.md"]
    WebCaseLaw --> ReportFormat
    ReportFormat --> Assessment["First-Look Assessment & Risk Matrix (_gutachten/)"]
    Assessment --> Escalation["references/eskalation_risiko.md (Lawyer Referral)"]
```

---

## Workflow Lifecycle

The 10-step assessment lifecycle defined in `SKILL.md` ensures every legal orientation is reproducible, disciplined, and transparent:

```mermaid
sequenceDiagram
    autonumber
    actor User as "User / Practitioner"
    participant Skill as "SKILL.md (Orchestrator)"
    participant Config as "config.json (Registry)"
    participant Fetcher as "_tools/gesetze_fetch.py"
    participant Agent as "agents/gesetzbuch.md"
    participant Web as "Case Law Layer (Web)"
    participant Reporter as "references/berichtsformat.md"
    participant Reviewer as "Review Model (Optional)"

    User->>Skill: Legal Query / Case Facts (Step 2: auftrag_klaeren)
    Note over Skill: Step 2: Immediate Deadline Check on Incoming Mail
    Skill->>Config: Step 0 & 4: Load Active Statutes & Settings
    Config-->>Skill: Enabled Statutes & Source Files
    opt Missing or Outdated Statute Text
        Skill->>Fetcher: Fetch Official Law XML (gesetze-im-internet.de)
        Fetcher-->>Skill: Local Text File (_data/gesetze/)
    end
    loop For Each Relevant Statute (Step 5: verkoerperungs_runde)
        Skill->>Agent: Embody Statute (Strict Wording Bound)
        Agent-->>Skill: Structured Raw Findings (Norm, Para, Sentence)
    end
    Skill->>Web: Step 6: Query Web-Verified Rulings (Court, Date, Az, ECLI)
    Web-->>Skill: Verified Case Law (or explicitly "not found")
    Skill->>Skill: Step 7 & 8: Subsumption & Risk Score (Green/Yellow/Orange/Red)
    opt Substantial Assessment (Step 10: review_optional)
        Skill->>Reviewer: Adversarial Second-Opinion Review
        Reviewer-->>Skill: Objections / Validation Findings
    end
    Skill->>Reporter: Step 9: Render 6-Section Assessment
    Reporter-->>User: Structured Gutachten (_gutachten/YYYY-MM-DD_<slug>.md)
```

---

## Governance & Runtime Invariants

The tool guarantees 10 immutable architectural and runtime invariants:

| # | Invariant | Description | Enforcement Mechanism |
|---|---|---|---|
| 1 | **100% Local-First & Zero-Egress** | Statute retrieval and report generation execute locally; zero telemetry, tracking, or automated data egress. | `.gitignore` strictly ignores `_gutachten/`, `_data/gesetze/`, and `config.local.json`. |
| 2 | **Strict Source Grounding** | Statutory statements must cite exact norm articles/sections, paragraphs, sentences, and quotes from local texts. | `agents/gesetzbuch.md` and `references/berichtsformat.md` reject memory-recalled statutes. |
| 3 | **Web-Verified Jurisprudence** | Court decisions require court, date, docket number, and ECLI; unverified rulings are recorded as "not found". | `SKILL.md` Step 6 disallows citing case law from LLM parameters. |
| 4 | **Non-Advisory Self-Use Boundary** | Strict legal demarcation under § 2 Abs. 1 RDG; orientation only, creating no attorney-client relationship. | Prominent notices in `README.md`, `SKILL.md`, and Section 5 of every generated report. |
| 5 | **Strict Deadline Discipline** | Incoming legal notices or administrative mail mandate an immediate deadline check prior to substantive analysis. | `references/eskalation_risiko.md` prioritizes statutory and court deadlines. |
| 6 | **Statute Registry Versioning** | Statute additions and state modifications are deliberate, versioned configuration events. | Schema version counter in `config.json` with corresponding changelog entries. |
| 7 | **Non-Elevation & User-Mode Safety** | Runs under standard unprivileged user accounts with no administrative elevation (`RunAsInvoker`). | Pure Python 3 standard library and CLI invocation without system-level hooks. |
| 8 | **Deterministic Risk Scoring** | Maps legal findings to an objective 4-level traffic light (Low, Medium, High, Critical) with specialty routing. | Fixed evaluation matrix in `references/eskalation_risiko.md`. |
| 9 | **Multi-OS CI Matrix & Concurrency** | Tested across Ubuntu, Windows, and macOS with concurrent run cancellation (`cancel-in-progress: true`). | GitHub Actions workflow (`.github/workflows/ci.yml`) on Python 3.10 through 3.13. |
| 10 | **Bilingual Documentation Parity** | Full structural, conceptual, and navigation parity across English and German documentation. | Automated contract verification in `tests/test_metadata.py`. |

---

## Legal Framework & RDG Classification

This tool is designed exclusively for **locally operated self-use**: You apply it within your own LLM environment to **your own** questions and factual matters. There is no hosted platform, no client intake, no legal advisory support, and no deadline management by the authors.

Assessment under the German Legal Services Act (*Rechtsdienstleistungsgesetz*, RDG — project self-evaluation, as of 2026-07-11):

| Deployment Mode | Legal Classification |
|---|---|
| Use for **own** factual matters | Not a legal service (no "matter of another party", § 2 Abs. 1 RDG). |
| Publication / distribution of software | Not a legal service (generic instrument, not handling an individual case; cf. BGH, 09.09.2021 — I ZR 113/20 "Smartlaw" — applicable by analogy depending on design). |
| Deployment to evaluate cases **for third parties** | May constitute a regulated legal service (§ 2 Abs. 1 RDG is tool-neutral) — commercial provision requires an official license (§ 3 RDG); gratuitous service imposes statutory requirements (§ 6 Abs. 2 RDG). **This is expressly outside the intended purpose of this project.** |

Any entity modifying the operational structure (hosting, providing services, or handling matters for third parties) must re-evaluate legal compliance independently.
EU AI Act self-classification: see [`docs/ai-act-note.md`](docs/ai-act-note.md).

---

## Sibling Tools & Ecosystem

`law-checker` operates in harmony with sibling tools across the `ellmos-ai` developer ecosystem and umbrella organization `open-bricks`:

| Project | Role / Integration | Repository |
|---|---|---|
| **`ellmos-ai`** | Core AI infrastructure organization and MCP server collective | [ellmos-ai](https://github.com/ellmos-ai) |
| **`open-bricks`** | Umbrella open-source developer tooling and desktop ecosystem | [open-bricks](https://github.com/open-bricks) |
| **`policy-registry`** | Cross-agent governance policy management and signed delegation authority | [policy-registry](https://github.com/ellmos-ai/policy-registry) |
| **`anonymizer`** | Fail-closed document pseudonymization library for privacy-first pre-processing | [anonymizer](https://github.com/ellmos-ai/anonymizer) |
| **`lock-master`** | Multi-agent concurrency coordination and project locking system | [lock-master](https://github.com/ellmos-ai/lock-master) |
| **`automation-master`** | Event-sourced credit and reservation management for autonomous background agents | [automation-master](https://github.com/dev-bricks/automation-master) |
| **`system-gap-master`** | Multi-agent gap detection, policy enforcement, and repository hygiene auditing | [system-gap-master](https://github.com/ellmos-ai/system-gap-master) |
| **`companion-for-agy`** | Headless CLI runner, PTY lifecycle supervision, and diagnostic session recording | [companion-for-agy](https://github.com/ellmos-ai/companion-for-agy) |
| **`gardener`** | Ephemeral, sandboxed tool runner and local SQLite knowledgebase repository | [gardener](https://github.com/ellmos-ai/gardener) |
| **`marblerun`** | Multi-agent turn-based tactical orchestration and worker handoff engine | [marblerun](https://github.com/ellmos-ai/marblerun) |
| **`report-forge`** | Domain-neutral core engine for formatted report generation pipelines | [report-forge](https://github.com/ellmos-ai/report-forge) |
| **`steuer-assistent`** | Standalone tool for self-application tax expense documentation and orientation | [steuer-assistent](https://github.com/ellmos-ai/steuer-assistent) |

---

## Installation & Quickstart

### 1. Clone Repository and Install Dependencies

```bash
git clone https://github.com/ellmos-ai/law-checker.git
cd law-checker

# Install editable package (requires Python >=3.10)
pip install -e .
```

### 2. Fetch Official Statute Texts

Statute texts are retrieved directly from official repositories and stored locally:

```bash
# List all registered and active statutes
PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py --list

# Download and parse all enabled federal statutes
PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py
```

### 3. Deploy Skill & Agent to Claude Code

```bash
# Copy skill orchestrator and embodiment agent into your Claude environment
cp SKILL.md ~/.claude/skills/rechtsabteilung/SKILL.md
cp agents/gesetzbuch.md ~/.claude/agents/gesetzbuch.md
```

In `~/.claude/skills/rechtsabteilung/SKILL.md`, set `<MODUL>` to the absolute path of your local clone.

Invoke in Claude Code:
```text
/rechtsabteilung Is an imprint (Impressum) legally mandatory for purely personal open-source repositories on GitHub?
```

---

## Adding New Statutes

Expanding the statute catalog does not require modifying agent code:

1. **Add Entry to `config.json`:** Define a new key under `gesetzbuecher` (specifying `name`, `kurz`, `zitierweise`, `quelle`, and `xml_zip` for federal law).
2. **Fetch Official Text:**
   ```bash
   PYTHONIOENCODING=utf-8 python _tools/gesetze_fetch.py <key>
   ```
3. **Increment Version:** Bump the `version` field in `config.json` and record the change in the changelog.

*Note on EU and State Laws:* For legislation without XML endpoints on `gesetze-im-internet.de` (e.g., GDPR or Interstate Media Treaty), save the official text as a UTF-8 file in `_data/gesetze/` with source URL and retrieval timestamp in the file header.

---

## Data Privacy & Confidentiality

Legal inquiries frequently involve sensitive personal data, business secrets, or privileged correspondence. Adhere to these principles:

- **Data Minimization First:** Redact or pseudonymize names, addresses, docket numbers, and identifiable business details before prompting. Consider using [`anonymizer`](https://github.com/ellmos-ai/anonymizer) for automated pre-processing.
- **Cloud LLM Exposure:** Prompts sent to cloud models are processed by the respective provider. Never enter unredacted confidential legal mail, trade secrets, or medical data into third-party LLMs without appropriate data processing agreements.
- **Zero Data Egress in Local Tooling:** The tool operates entirely offline on your workstation. Statute downloads and generated assessments stay in `_data/gesetze/` and `_gutachten/`; nothing is transmitted to the authors.
- **Never Post Case Facts to Public Issues:** For GitHub issues or bug reports, use purely hypothetical, fabricated factual examples.

For further information, review [`SECURITY.md`](SECURITY.md).

---

## Statute Registry Inventory

The default statute registry (`config.json`, version 5) configures 13 statutes across German federal and EU law:

| Key | Statute Name | Jurisdiction | Status | Primary Source |
|---|---|---|---|---|
| `gg` | Grundgesetz für die Bundesrepublik Deutschland (Basic Law) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `bgb` | Bürgerliches Gesetzbuch (Civil Code) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `sgb5` | Sozialgesetzbuch V (Social Code Book V — Statutory Health Insurance) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `urhg` | Urheberrechtsgesetz (Copyright Act) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `rdg` | Rechtsdienstleistungsgesetz (Legal Services Act) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `markeng` | Markengesetz (Trade Mark Act) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `stberg` | Steuerberatungsgesetz (Tax Advisory Act) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `uwg` | Gesetz gegen den unlauteren Wettbewerb (Unfair Competition Act) | Federal (DE) | **Active** | gesetze-im-internet.de |
| `dsgvo` | General Data Protection Regulation (Regulation (EU) 2016/679) | European Union | **Active** | EUR-Lex |
| `ehds` | European Health Data Space (Regulation (EU) 2025/327) | European Union | **Active** | EUR-Lex |
| `grch` | Charter of Fundamental Rights of the European Union | European Union | **Active** | EUR-Lex |
| `stgb` | Strafgesetzbuch (Criminal Code) | Federal (DE) | *Inactive* | gesetze-im-internet.de |
| `mstv` | Medienstaatsvertrag (Interstate Media Treaty) | State Laws (DE)| *Inactive* | die-medienanstalten.de |

---

<a id="report-architecture--visual-walkthrough"></a>
## Report Architecture & Visual Walkthrough

Every legal assessment generated by `law-checker` adheres strictly to the standardized 6-section *Gutachten* structure defined in [`references/berichtsformat.md`](references/berichtsformat.md), guaranteeing rigorous legal methodology (*Gutachtenstil*):

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 STRUCTURED LEGAL FIRST-LOOK ASSESSMENT ARCHITECTURE         │
│ File: _gutachten/YYYY-MM-DD_<themen-slug>.md                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Sachverhalt & Fragestellung (Factual Inquest & Scope)                    │
│    ├─ Fragesteller, Kontext & Sachverhaltselemente                          │
│    └─ MANDATORY PRIORITY CHECK: Fristenprüfung bei behördlicher/Rechtspost  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. Norm-Ebene: Authentischer Gesetzeswortlaut (Embodiment Extracts)         │
│    ├─ Identifizierter relevanter Paragraphenbestand (z. B. § 5 TDDDG, BGB)   │
│    └─ Absatz- und satzgenaue Verbatim-Zitate aus lokalem XML-Bestand        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. Rechtsprechung & Auslegung (Web-Verified Jurisprudence)                  │
│    ├─ Relevante Leitentscheidungen (BGH, BAG, BVerfG, EuGH)                 │
│    └─ Strenges Format: Gericht, Datum, Aktenzeichen, Fundstelle, ECLI       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. Synthese & Subsumtion (Legal Methodology / Gutachtenstil)                │
│    ├─ Tatbestandsmerkmale vs. vorliegender Sachverhalt                      │
│    └─ Klare Kennzeichnung: Was ist zwingend, was vertretbare Auslegung?     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. Risikoeinstufung & Anwaltsempfehlung (Risk Traffic Light & Referral)     │
│    ├─ Ampel-Score: [GERING / GRÜN] | [MITTEL / GELB] | [HOCH] | [KRITISCH]   │
│    ├─ Begründung & konkrete Schadens-/Abmahnpotenziale                      │
│    └─ Fachanwalts-Empfehlung mit relevanter Fachgebietsbezeichnung          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. Quellenverzeichnis & Prüfprotokoll (Provenance & Audit Log)              │
│    ├─ Verwendete Gesetzestexte mit amtlichem Abruf- und Standstempel        │
│    └─ Revisions- und Modelldaten des ausführenden LLM-Laufs                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<a id="third-party-licenses--sbom"></a>
## Third-Party Licenses & SBOM

`law-checker` is certified open source under the [MIT License](LICENSE). The project maintains a complete software bill of materials (SBOM) and licensing audit in [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md):

- **Zero-Copyleft Guarantee:** No GPL, AGPL, or SSPL-licensed dependencies; completely free for commercial and non-commercial local engineering.
- **Unprivileged Execution (`RunAsInvoker`):** Requires no root or administrative elevation on any operating system.
- **Official Public Domain Texts:** Statutory texts obtained from `gesetze-im-internet.de` constitute official government works (*Amtliche Werke*) under § 5 Abs. 1 UrhG (German Copyright Act) and are free of copyright. European Union legislative acts are reused under Commission Decision 2011/833/EU.

---

## Repository Layout

```text
law-checker/
├── .github/workflows/ci.yml    ← Multi-OS CI matrix (Ubuntu, Windows, macOS)
├── .github/workflows/stale.yml ← Stale issue and pull request automation
├── SKILL.md                    ← Orchestrating skill workflow (10-step process)
├── config.json                 ← Statute registry and pipeline definition (v5)
├── agents/
│   └── gesetzbuch.md           ← Generic statute embodiment agent prompt
├── references/
│   ├── berichtsformat.md       ← 6-section legal report schema & citation rules
│   └── eskalation_risiko.md    ← Risk traffic light, deadline check, lawyer matrix
├── _tools/
│   ├── __init__.py             ← Python package marker
│   └── gesetze_fetch.py        ← Statute fetcher and XML parser
├── docs/
│   └── ai-act-note.md          ← EU AI Act self-classification note
├── tests/
│   ├── test_gesetze_fetch.py   ← Unit tests for statute fetching & extraction
│   └── test_metadata.py        ← Automated contract and metadata parity tests
├── CHANGELOG.md                ← Version and release history
├── SECURITY.md                 ← Security policy with 48h response SLA
├── THIRD_PARTY_LICENSES.md     ← Third-party license audit, SBOM & § 5 UrhG classification
├── MARKETING-LOG.txt           ← Local marketing & discoverability backlog
├── llms.txt                    ← Machine-readable context for AI coding agents
├── ellmos-module.v2.json       ← Standardized module manifest (rechtsabteilung)
├── pyproject.toml              ← PEP 621 package metadata & test configuration
├── _data/gesetze/              ← Downloaded statute files (ignored via .gitignore)
└── _gutachten/                 ← Generated legal assessments (ignored via .gitignore)
```

---

## Security Policy

Security, confidentiality, and data safety are foundational. Vulnerabilities may be reported privately through:
- [GitHub Security Advisories](https://github.com/ellmos-ai/law-checker/security/advisories)
- Direct Security Contacts: `security@ellmos.ai` | `security@open-bricks.org` | `support@lukasgeiger.com` | `lukas@open-bricks.org`

**Commitments:** Acknowledgment within 48 hours; initial triage and impact assessment within 5 business days. Full details are documented in [`SECURITY.md`](SECURITY.md).

---

## Provenance & Authorship

This project synthesizes three proven operational building blocks:
1. **Editorial Legal Policy:** Standardized report templates, 4-tier objective risk scoring, specialty attorney matching, and uncompromising deadline discipline.
2. **Living Constitution Research Prototype:** The statute embodiment paradigm (`Du BIST das Gesetzbuch`) enforcing strict fidelity to enacted legal text and distinct judicial interpretation layers.
3. **Jurisprudential Knowledge Base:** Structured taxonomy of German law domains and traditional legal methodology (*Gutachtenstil*).

The first complete evaluation executed by this workflow was its own public release audit — including an adversarial review by an independent secondary LLM.

---

<a id="license--disclaimers"></a><a id="statutory-disclaimer--521-bgb--license"></a>
## Statutory Disclaimer (§ 521 BGB) & License

### Gesetzlicher Haftungshinweis gem. § 521 BGB (Gefälligkeitsrecht) / Gratuitous Open-Source Provision

> [!IMPORTANT]
> **Haftungsbeschränkung gem. § 521 BGB:** Die Bereitstellung dieser Software, der Dokumentation, der Prompts und der Prüfungsabläufe erfolgt unentgeltlich und als Gefälligkeit im Sinne des deutschen Zivilrechts (§ 521 BGB). Die Haftung der Urheber, Maintainer und Mitwirkenden ist auf Vorsatz und grobe Fahrlässigkeit beschränkt. Die Software stellt keine Rechtsdienstleistung im Sinne des § 2 Abs. 1 RDG dar und ersetzt keine individuelle Prüfung durch eine zugelassene Rechtsanwältin oder einen zugelassenen Rechtsanwalt. Es erfolgt keine Fristenkontrolle und keine Gewähr für Vollständigkeit, Fehlerfreiheit oder Aktualität.

- **License:** Released under the permissive [MIT License](LICENSE) covering source code, agent prompts, and documentation.
- **Third-Party SBOM:** Comprehensive audit of third-party libraries and public domain status under § 5 Abs. 1 UrhG is documented in [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).
- **Warranty Disclaimer:** Provided "as is" without warranty of any kind regarding accuracy, completeness, or timeliness. Legal texts change over time; always verify against the official federal gazette (*Bundesgesetzblatt*) before relying on them.
- **No Legal Advice:** This software facilitates initial orientation and research only. It does not provide legal advice or create an attorney-client relationship.
