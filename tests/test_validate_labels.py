from pathlib import Path

from lib.validate_labels import NO_WIKIPEDIA_STATUS, validate_rows


def agency_row(**overrides):
    row = {
        "canonical_id": "cip",
        "label": "org.ent.pressagency.cip",
        "trainable": True,
        "wikipedia_url": None,
        "status": NO_WIKIPEDIA_STATUS,
        "metadata_sources": [{"type": "history", "url": "https://example.org/cip"}],
        "description": "Belgian Catholic news agency.",
        "active_period": {"start": "1944", "end": "2001"},
        "aliases_by_language": {"fr": ["CIP"]},
    }
    row.update(overrides)
    return row


def run(row):
    return [
        e for e in validate_rows([row], expected_prefix="org.ent.pressagency.", source=Path("seeds.json"))
        if "wikipedia_url" in e or "metadata_sources" in e
    ]


def test_no_wikipedia_status_with_sources_may_omit_wikipedia_url():
    assert run(agency_row()) == []


def test_no_wikipedia_status_requires_metadata_sources():
    assert any("metadata_sources" in e for e in run(agency_row(metadata_sources=[])))


def test_other_status_still_requires_wikipedia_url():
    assert any("wikipedia_url" in e for e in run(agency_row(status="metadata_enriched")))
