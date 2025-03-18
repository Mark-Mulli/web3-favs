from script.deploy import deployed
import pytest


@pytest.fixture(scope = "session")
def fixture_deploy():
    contract = deployed()
    return contract