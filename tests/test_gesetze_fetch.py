# -*- coding: utf-8 -*-
"""Unit tests for _tools/gesetze_fetch.py."""
import xml.etree.ElementTree as ET

from _tools.gesetze_fetch import load_registry, norm_text, extract, process


def test_load_registry():
    registry = load_registry()
    assert isinstance(registry, dict)
    assert "gg" in registry
    assert "bgb" in registry
    assert registry["gg"]["enabled"] is True


def test_norm_text():
    xml_str = """
    <norm>
        <metadaten>
            <enbez>§ 1</enbez>
            <titel>Test Title</titel>
        </metadaten>
        <textdaten>
            <text>
                <Content>Sample content text.</Content>
            </text>
        </textdaten>
    </norm>
    """
    elem = ET.fromstring(xml_str)
    enbez, titel, text = norm_text(elem)
    assert enbez == "§ 1"
    assert titel == "Test Title"
    assert "Sample content text." in text


def test_extract():
    xml_str = """<?xml version="1.0" encoding="UTF-8"?>
    <dokumente>
        <norm>
            <metadaten>
                <enbez>§ 1</enbez>
                <titel>Geltungsbereich</titel>
            </metadaten>
            <textdaten>
                <text>
                    <Content>Dies ist der Gesetzestext.</Content>
                </text>
            </textdaten>
        </norm>
    </dokumente>
    """
    full, idx = extract(xml_str.encode("utf-8"), "Test Law", "https://example.com")
    assert "# Test Law" in full
    assert "Geltungsbereich" in full
    assert "Dies ist der Gesetzestext." in full
    assert "§ 1 Geltungsbereich" in idx


def test_process_skip_no_xml(capsys):
    entry = {"kurz": "TEST", "hinweis": "Manuell beschaffen"}
    result = process("test_no_xml", entry)
    assert result is True
    captured = capsys.readouterr()
    assert "ÜBERSPRUNGEN" in captured.out
