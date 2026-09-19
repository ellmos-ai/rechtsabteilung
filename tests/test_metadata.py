# -*- coding: utf-8 -*-
"""Automated metadata, CI matrix, manifest, and hygiene contract tests."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

ROOT = Path(__file__).resolve().parent.parent


def test_version_consistency():
    """Verify package version is consistent across pyproject, changelog, and llms.txt."""
    pyproject_data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = pyproject_data["project"]["version"]

    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert f"## {version}" in changelog_text, f"CHANGELOG.md missing release section for {version}"

    llms_text = (ROOT / "llms.txt").read_text(encoding="utf-8")
    assert version in llms_text, f"llms.txt missing version reference {version}"


def test_module_v2_manifest_contract():
    """Verify ellmos-module.v2.json conforms to standard contract."""
    manifest_path = ROOT / "ellmos-module.v2.json"
    assert manifest_path.is_file(), "ellmos-module.v2.json must exist"

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert data["schema"] == "ellmos.module.v2"
    assert data["id"] == "rechtsabteilung"
    assert data["status"] == "active"
    assert data["visibility"] == "public"
    assert data["source_of_truth"]["repository"] in [
        "https://github.com/ellmos-ai/rechtsabteilung",
        "https://github.com/ellmos-ai/law-checker",
    ]
    assert set(data["boundaries"]["platforms"]) == {"windows", "macos", "linux"}


def test_ci_workflow_matrix_and_concurrency():
    """Verify CI workflow tests multi-OS, Python versions, and enforces concurrency cancellation."""
    ci_file = ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_file.is_file(), ".github/workflows/ci.yml must exist"

    content = ci_file.read_text(encoding="utf-8")
    for os_target in ["ubuntu-latest", "windows-latest", "macos-latest"]:
        assert os_target in content, f"CI workflow missing OS: {os_target}"

    for py_ver in ["3.10", "3.11", "3.12", "3.13"]:
        assert py_ver in content, f"CI workflow missing Python version: {py_ver}"

    assert "actions/checkout@v4" in content, "CI workflow should use actions/checkout@v4"
    assert "actions/setup-python@v5" in content, "CI workflow should use actions/setup-python@v5"
    assert "cancel-in-progress: true" in content, "CI workflow must have cancel-in-progress: true"


def test_pyproject_pep621_metadata():
    """Verify pyproject.toml PEP 621 compliance and PEP 639 SPDX license."""
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = data.get("project", {})

    assert project.get("name") == "law-checker"
    assert project.get("license") == "MIT"
    assert "LICENSE" in project.get("license-files", [])
    assert project.get("requires-python") == ">=3.10"

    classifiers = project.get("classifiers", [])
    for expected in [
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ]:
        assert expected in classifiers, f"pyproject.toml missing classifier: {expected}"


def test_pyproject_ecosystem_urls():
    """Verify PEP 621 [project.urls] include parent org, umbrella, security, licenses, and repository."""
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    urls = data.get("project", {}).get("urls", {})

    expected_urls = {
        "Homepage": "https://github.com/ellmos-ai/law-checker",
        "Repository": "https://github.com/ellmos-ai/law-checker",
        "Documentation": "https://github.com/ellmos-ai/law-checker#readme",
        "Changelog": "https://github.com/ellmos-ai/law-checker/blob/main/CHANGELOG.md",
        "Issues": "https://github.com/ellmos-ai/law-checker/issues",
        "Security": "https://github.com/ellmos-ai/law-checker/blob/main/SECURITY.md",
        "Third-Party Licenses": "https://github.com/ellmos-ai/law-checker/blob/main/THIRD_PARTY_LICENSES.md",
        "Marketing Log": "https://github.com/ellmos-ai/law-checker/blob/main/MARKETING-LOG.txt",
        "LLM Ready": "https://raw.githubusercontent.com/ellmos-ai/law-checker/main/llms.txt",
        "Parent Organization": "https://github.com/ellmos-ai",
        "Umbrella Ecosystem": "https://github.com/open-bricks",
    }

    for key, expected_val in expected_urls.items():
        assert urls.get(key) == expected_val, f"URL mismatch for {key}: expected {expected_val}"


def test_security_policy_contract():
    """Verify SECURITY.md is bilingual and declares supported versions matrix, 48h SLA, and contacts."""
    sec_path = ROOT / "SECURITY.md"
    assert sec_path.is_file(), "SECURITY.md must exist in root"

    content = sec_path.read_text(encoding="utf-8")
    assert "## Supported Versions" in content
    assert "## Unterstützte Versionen" in content
    assert "0.2.x" in content
    assert "48 hours" in content or "48-hour" in content
    assert "48 Stunden" in content
    assert "security@ellmos.ai" in content
    assert "support@lukasgeiger.com" in content
    assert "lukas@open-bricks.org" in content
    assert "https://github.com/ellmos-ai/law-checker/security/advisories" in content


def test_gitignore_hygiene_patterns():
    """Verify .gitignore includes sync conflict, caches, test artifacts, and locks."""
    gi_path = ROOT / ".gitignore"
    assert gi_path.is_file(), ".gitignore must exist"

    content = gi_path.read_text(encoding="utf-8")
    for pattern in [
        "*.sync-conflict-*",
        "*.conflict",
        "*-CONFLIT-*",
        ".pytest_cache/",
        ".ruff_cache/",
        ".coverage",
        "htmlcov/",
        "LOCK*.txt",
        "*.lock",
    ]:
        assert pattern in content, f".gitignore missing pattern: {pattern}"


def test_llms_txt_structure_and_date():
    """Verify llms.txt contains synchronized Last-checked header and core file references."""
    llms_path = ROOT / "llms.txt"
    assert llms_path.is_file(), "llms.txt must exist"

    content = llms_path.read_text(encoding="utf-8")
    assert "## Last-checked: 2026-09-19" in content, "llms.txt Last-checked date must be 2026-09-19"
    assert "README.md" in content
    assert "README_de.md" in content
    assert "SKILL.md" in content
    assert "config.json" in content
    assert "SECURITY.md" in content
    assert "CHANGELOG.md" in content
    assert "THIRD_PARTY_LICENSES.md" in content


def test_readme_bilingual_and_badges():
    """Verify README.md contains bilingual sections, mermaid diagram, and essential badges."""
    readme_path = ROOT / "README.md"
    assert readme_path.is_file(), "README.md must exist"

    content = readme_path.read_text(encoding="utf-8")
    assert "```mermaid" in content, "README.md must contain architecture mermaid diagram"
    assert "Deutsch: Wichtiger Hinweis" in content or "Wichtig:" in content
    assert "Ecosystem-ellmos--ai" in content
    assert "Umbrella-open--bricks" in content
    assert "License-MIT" in content
    assert "llms.txt" in content
    assert "THIRD_PARTY_LICENSES.md" in content


def test_readme_bilingual_parity_and_navigation():
    """Verify 18-point quick navigation parity and language switchers across README.md and README_de.md."""
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    assert readme_en.is_file(), "README.md must exist"
    assert readme_de.is_file(), "README_de.md must exist"

    text_en = readme_en.read_text(encoding="utf-8")
    text_de = readme_de.read_text(encoding="utf-8")

    # Language switcher checks
    assert "**English** | [Deutsch](README_de.md)" in text_en, "README.md missing language switcher"
    assert "[English](README.md) | **Deutsch**" in text_de, "README_de.md missing language switcher"

    # 18 English anchors
    en_expected_anchors = [
        "#overview",
        "#target-personas--high-intent-use-cases",
        "#comparative-architecture-matrix",
        "#system-architecture",
        "#workflow-lifecycle",
        "#governance--runtime-invariants",
        "#legal-framework--rdg-classification",
        "#sibling-tools--ecosystem",
        "#installation--quickstart",
        "#adding-new-statutes",
        "#data-privacy--confidentiality",
        "#statute-registry-inventory",
        "#report-architecture--visual-walkthrough",
        "#third-party-licenses--sbom",
        "#repository-layout",
        "#security-policy",
        "#provenance--authorship",
        "#statutory-disclaimer--521-bgb--license",
    ]
    for anchor in en_expected_anchors:
        assert f"]({anchor})" in text_en, f"README.md missing navigation anchor: {anchor}"

    # 18 German anchors
    de_expected_anchors = [
        "#übersicht",
        "#zielgruppen--anwendungsfälle",
        "#vergleichsmatrix--alternativen",
        "#systemarchitektur",
        "#ablauf--und-prüfungslebenszyklus",
        "#governance--und-laufzeit-invarianten",
        "#rechtlicher-rahmen-und-rdg-einordnung",
        "#geschwisterwerkzeuge-und-ökosystem",
        "#installation-und-schnelleinstieg",
        "#neue-gesetze-hinzufügen",
        "#datenschutz-und-vertraulichkeit",
        "#gesetzes-registry-bestand",
        "#gutachten-architektur--visueller-walkthrough",
        "#drittanbieter-lizenzen--sbom",
        "#repository-struktur",
        "#sicherheitsrichtlinie",
        "#herkunft-und-autorenschaft",
        "#haftung-lizenz-und-grenzen",
    ]
    for anchor in de_expected_anchors:
        assert f"]({anchor})" in text_de, f"README_de.md missing navigation anchor: {anchor}"


def test_dual_mermaid_diagrams_in_readmes():
    """Verify both READMEs include flowchart and sequence diagram without unquoted parenthetical labels."""
    for readme_name in ["README.md", "README_de.md"]:
        text = (ROOT / readme_name).read_text(encoding="utf-8")
        assert "flowchart TD" in text, f"{readme_name} missing flowchart TD"
        assert "sequenceDiagram" in text, f"{readme_name} missing sequenceDiagram"
        assert "autonumber" in text, f"{readme_name} sequenceDiagram missing autonumber"


def test_governance_invariants_table_contract():
    """Verify both READMEs document the 10 Governance & Runtime Invariants."""
    for readme_name in ["README.md", "README_de.md"]:
        text = (ROOT / readme_name).read_text(encoding="utf-8")
        for inv_num in range(1, 11):
            assert f"| {inv_num} |" in text, f"{readme_name} missing Governance Invariant #{inv_num}"


def test_marketing_log_contract():
    """Verify local MARKETING-LOG.txt exists and contains structured Pfad B backlog."""
    log_path = ROOT / "MARKETING-LOG.txt"
    assert log_path.is_file(), "MARKETING-LOG.txt must exist in repository root"
    content = log_path.read_text(encoding="utf-8")
    assert "MARKETING-LOG.txt" in content
    assert "Pfad B" in content
    assert "2026-09-09" in content


def test_sibling_ecosystem_matrix():
    """Verify both READMEs contain ecosystem links to sibling tools."""
    for readme_name in ["README.md", "README_de.md"]:
        text = (ROOT / readme_name).read_text(encoding="utf-8")
        assert "https://github.com/ellmos-ai" in text
        assert "https://github.com/open-bricks" in text
        assert "https://github.com/ellmos-ai/anonymizer" in text
        assert "https://github.com/ellmos-ai/policy-registry" in text
        assert "https://github.com/ellmos-ai/lock-master" in text
        assert "https://github.com/dev-bricks/automation-master" in text


def test_no_forbidden_tracked_leaks():
    """Verify no local credentials, private keys, or host user path leaks exist in tracked files."""
    tracked = subprocess.check_output(
        ["git", "ls-files"], cwd=ROOT, text=True, encoding="utf-8"
    ).splitlines()

    for path_str in tracked:
        assert not path_str.endswith((".env", ".db", ".sqlite", ".sqlite3")), f"Leaked file tracked: {path_str}"

    forbidden_markers = (
        "C:\\" + "Users\\" + "lukas",
        "C:/" + "Users/" + "lukas",
        "/home/" + "lukas",
        "/c/Users/" + "lukas",
    )

    for rel_path in tracked:
        file_path = ROOT / rel_path
        if file_path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico", ".bin"}:
            continue
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for marker in forbidden_markers:
            assert marker.lower() not in text.lower(), f"Potential path leak '{marker}' in {rel_path}"


def test_pytest_ini_options_and_os_classifiers():
    """Verify pyproject.toml defines addopts with -ra -v and detailed OS classifiers."""
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    ini_opts = data.get("tool", {}).get("pytest", {}).get("ini_options", {})
    assert "-ra -v" in ini_opts.get("addopts", "")

    classifiers = data.get("project", {}).get("classifiers", [])
    for expected_os in [
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ]:
        assert expected_os in classifiers, f"Missing OS classifier: {expected_os}"

    opt_deps = data.get("project", {}).get("optional-dependencies", {})
    assert "dev" in opt_deps, "pyproject missing dev optional dependencies"
    assert "test" in opt_deps, "pyproject missing test optional dependencies"


def test_ci_workflow_hardening():
    """Verify CI workflow has permissions read, compilation step, and ruff gate."""
    ci_path = ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_path.is_file(), "ci.yml must exist"
    content = ci_path.read_text(encoding="utf-8")
    assert "permissions:" in content
    assert "contents: read" in content
    assert "python -m compileall -q ." in content
    assert "ruff check ." in content
    assert "python -m pytest -ra -v" in content


def test_stale_workflow_present():
    """Verify standard Stale Issues & PRs workflow exists and is configured."""
    stale_path = ROOT / ".github" / "workflows" / "stale.yml"
    assert stale_path.is_file(), ".github/workflows/stale.yml must exist"
    content = stale_path.read_text(encoding="utf-8")
    assert "actions/stale@v9" in content
    assert "issues: write" in content
    assert "pull-requests: write" in content


def test_multihost_conflict_and_lock_patterns():
    """Verify .gitignore contains full multi-host conflict, multi-agent lock, and packaging patterns."""
    gi_path = ROOT / ".gitignore"
    assert gi_path.is_file(), ".gitignore must exist"
    content = gi_path.read_text(encoding="utf-8")
    for pattern in [
        "*-conflict-*",
        "*.sync-temp-*",
        "*-ASUS-GEI.*",
        "*-WORKSTATION-LG.*",
        "LOCK",
        "LOCK.*",
        "LOCK.permissions.json",
        "wheelhouse/",
        "coverage/",
    ]:
        assert pattern in content, f".gitignore missing pattern: {pattern}"


def test_changelog_release_entry():
    """Verify CHANGELOG.md contains release entry for current version with date."""
    pyproject_data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = pyproject_data["project"]["version"]
    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert f"## {version} — 2026-09-19" in changelog_text, f"Missing release entry for {version} — 2026-09-19"


def test_target_personas_and_comparative_matrix():
    """Verify both READMEs feature target personas [PERSONA-01] to [PERSONA-04] and comparative matrix."""
    for readme_name in ["README.md", "README_de.md"]:
        content = (ROOT / readme_name).read_text(encoding="utf-8")
        for persona_tag in ["[PERSONA-01]", "[PERSONA-02]", "[PERSONA-03]", "[PERSONA-04]"]:
            assert persona_tag in content, f"{readme_name} missing persona: {persona_tag}"
        assert "Comparative Architecture Matrix" in content or "Vergleichsmatrix & Alternativen" in content
        assert "Beck/Juris" in content


def test_statutory_bgb_521_disclaimer():
    """Verify statutory § 521 BGB disclaimer is declared in both READMEs."""
    for readme_name in ["README.md", "README_de.md"]:
        content = (ROOT / readme_name).read_text(encoding="utf-8")
        assert "§ 521 BGB" in content, f"{readme_name} missing § 521 BGB statutory disclaimer"
        assert "Gefälligkeit" in content, f"{readme_name} missing Gefälligkeit mention"


def test_third_party_licenses_file():
    """Verify THIRD_PARTY_LICENSES.md exists, contains runtime dependencies and UrhG notice."""
    tpl_path = ROOT / "THIRD_PARTY_LICENSES.md"
    assert tpl_path.is_file(), "THIRD_PARTY_LICENSES.md must exist in root"
    content = tpl_path.read_text(encoding="utf-8")
    assert "requests" in content
    assert "urllib3" in content
    assert "§ 5 Abs. 1 UrhG" in content
    assert "Amtliche Werke" in content
    assert "INV-LOCAL-01" in content


def test_pyproject_license_files():
    """Verify pyproject.toml includes LICENSE and THIRD_PARTY_LICENSES.md in license-files."""
    pyproject_data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    license_files = pyproject_data.get("project", {}).get("license-files", [])
    assert "LICENSE" in license_files
    assert "THIRD_PARTY_LICENSES.md" in license_files

