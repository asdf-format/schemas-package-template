"""
Test that the manifest file is correctly structured and refers
to schemas that exist.
"""
from pathlib import Path

import asdf
import pytest
import yaml


RESOURCES_ROOT = Path(__file__).absolute().parent.parent / "resources"


@pytest.mark.parametrize("manifest_path", (RESOURCES_ROOT / "manifests").glob("**/*.yaml"))
def test_manifest(manifest_path):
    content = manifest_path.read_bytes()
    manifest = yaml.safe_load(content)
    schema = asdf.schema.load_schema("asdf://asdf-format.org/core/schemas/extension_manifest-1.0.0")

    asdf.schema.validate(manifest, schema=schema)

    for tag in manifest.get("tags", []):
        # Check that the schema exists:
        if "schema_uri" in tag:
            assert tag["schema_uri"] in asdf.get_config().resource_manager
