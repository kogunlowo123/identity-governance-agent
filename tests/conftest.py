"""Test configuration for Identity Governance Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "identity-governance-agent", "category": "Security AI"}
