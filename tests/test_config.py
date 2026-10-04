import os

from config import Config


def test_default_environment():
    original_environment = os.environ.pop("ENVIRONMENT", None)

    try:
        assert Config.ENVIRONMENT == "development"
    finally:
        if original_environment is not None:
            os.environ["ENVIRONMENT"] = original_environment
