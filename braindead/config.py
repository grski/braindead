import os

import toml

USER_CONFIG_FILE: str = "pyproject.toml"


class ConfigValidator:
    def __init__(self, config: dict) -> None:
        self.config: dict = config

    def check_if_language_in_i18n(self):
        try:
            self.config["language"] in self.config["i18n"]["languages"]
        except KeyError:  # TODO: handle this more gracefully/implement
            pass

    def validate(self):
        self.check_if_language_in_i18n()
        return self.config


def validate_config(config: dict) -> dict:
    validator: ConfigValidator = ConfigValidator(config)
    return validator.validate()


def get_user_config():
    if not os.path.exists(USER_CONFIG_FILE):
        return {}
    return toml.load(USER_CONFIG_FILE).get("tool", {}).get("braindead", {}).get("config", {})
