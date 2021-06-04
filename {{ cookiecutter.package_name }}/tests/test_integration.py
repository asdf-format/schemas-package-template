"""
Test that the asdf library integration is working properly.
"""
from pathlib import Path

import asdf
import pytest
import yaml


RESOURCES_ROOT = Path(__file__).absolute().parent.parent / "resources"


@pytest.mark.parametrize("manifest_path", (RESOURCES_ROOT / "manifests").glob("**/*.yaml"))
def test_manifest_integration(manifest_path):
    content = manifest_path.read_bytes()
    manifest = yaml.safe_load(content)
    asdf_content = asdf.get_config().resource_manager[manifest["id"]]
    assert asdf_content == content


@pytest.mark.parametrize("schema_path", (RESOURCES_ROOT / "schemas").glob("**/*.yaml"))
def test_schema_integration(schema_path):
    content = schema_path.read_bytes()
    schema = yaml.safe_load(content)
    asdf_content = asdf.get_config().resource_manager[schema["id"]]
    assert asdf_content == content
