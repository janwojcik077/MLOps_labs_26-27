from settings import Settings


def test_settings_load_correctly():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "Lab1-Test"
    assert settings.API_KEY == "test_api_key_12345"
