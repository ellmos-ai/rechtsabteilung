# Third-Party Licenses & Software Bill of Materials (SBOM)

**Project:** `law-checker` (`ellmos-ai/rechtsabteilung`)  
**Status:** Certified Open Source (MIT)  
**Audit Date:** 2026-09-19  
**Specification Level:** Level 1 Compliant (Strict Invariant Tracking)

---

## 1. Overview & Licensing Policy

`law-checker` is published under the permissive **MIT License**. The project adheres to strict licensing and data governance hygiene:
- **Zero-Copyleft Contagion Guarantee:** The core application and runtime toolchain do not link against, bundle, or dynamically depend on any GPL, AGPL, or SSPL-licensed libraries.
- **Unprivileged Execution (`RunAsInvoker`):** Operates entirely within standard user privileges; no root/administrator elevation required.
- **100% Local Data Boundaries:** Statute retrieval and report rendering occur strictly on local developer environments; zero telemetry or telemetry egress.
- **Public Domain Official Texts:** German federal statutory texts retrieved via `gesetze-im-internet.de` constitute official government works (*Amtliche Werke*) under § 5 Abs. 1 UrhG (German Copyright Act) and are in the public domain.

---

## 2. Direct Runtime Dependencies

| Package | Version Range | License (SPDX) | Primary Use Case | Project Home / Repository |
|---|---|---|---|---|
| **`requests`** | `>=2.28.0` | `Apache-2.0` | HTTP retrieval of official statute XML zip archives | https://requests.readthedocs.io/ |
| **`urllib3`** | `>=1.26.0` | `MIT` | Low-level HTTP transport and connection management | https://urllib3.readthedocs.io/ |

---

## 3. Development, Build & Test Toolchain

These dependencies are used exclusively for development, automated contract testing, code formatting, and packaging. They are **not** shipped as runtime requirements for end users.

| Package | Version Range | License (SPDX) | Purpose |
|---|---|---|---|
| **`setuptools`** | `>=77.0` | `MIT` | PEP 517 / PEP 621 build backend |
| **`pytest`** | `>=7.0` | `MIT` | Automated unit, metadata, and contract test runner |
| **`ruff`** | `>=0.4.0` | `MIT` / `Apache-2.0` | Extremely fast Python linter and code quality validator |

---

## 4. Official Primary Statutory Sources

| Source Identifier | Publisher / Authority | Legal Status / Term |
|---|---|---|
| **`gesetze-im-internet.de`** | Bundesministerium der Justiz (BMJ) & Bundesamt für Justiz (BfJ) | **Amtliche Werke gem. § 5 Abs. 1 UrhG** (gemeinfrei / public domain). Gesetzestexte und Rechtsverordnungen des Bundes genießen keinen Urheberschutz. |
| **EUR-Lex** | Publications Office of the European Union | **Commission Decision 2011/833/EU** on the reuse of Commission documents. Free commercial and non-commercial reuse with attribution (equivalent to CC-BY-4.0). |

---

## 5. Governance & Invariant Compliance Matrix

| Invariant ID | Requirement | Compliance Status | Technical Verification |
|---|---|---|---|
| **`INV-LOCAL-01`** | Zero-Copyleft Contagion | **VERIFIED** | 100% MIT / Apache-2.0 / Public Domain dependencies. |
| **`INV-LOCAL-02`** | Non-Elevation (`RunAsInvoker`) | **VERIFIED** | Pure user-space Python CLI and file operations. |
| **`INV-LOCAL-03`** | Zero-Egress / Local-First | **VERIFIED** | Statute caches stored in `.gitignore`'d `_data/gesetze/`; reports in `_gutachten/`. |
| **`INV-LOCAL-04`** | Evidentiary Grounding | **VERIFIED** | Strict norm verification against local XML extracts. |
| **`INV-LOCAL-05`** | Statutory Disclaimer | **VERIFIED** | § 521 BGB gratuitous open-source notice in documentation and reports. |

---

## 6. License Texts Summary

### MIT License
All internal project code and documentation are released under the MIT License (see [`LICENSE`](LICENSE)).

### Apache License 2.0 (`requests`, `ruff`)
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
