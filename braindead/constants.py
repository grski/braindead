import os

import toml

USER_CONFIG_FILE = "pyproject.toml"


def get_user_config():
    if not os.path.exists(USER_CONFIG_FILE):
        return {}
    return toml.load(USER_CONFIG_FILE).get("tool", {}).get("braindead", {})


PACKAGE_LOCATION: str = os.path.split(os.path.realpath(__file__))[0]
DEFAULT_CONFIG: dict = toml.load(os.path.join(PACKAGE_LOCATION, "default_config.toml"))
USER_CONFIG: dict = get_user_config()
CONFIG: dict = {**DEFAULT_CONFIG, **USER_CONFIG}
BASE_URL: str = CONFIG["site"]["base_url"]
DIST_DIR: str = CONFIG["site"].get("dist_dir", "dist")
# todo: add git cloning of templates
TEMPLATE_DIR: str = CONFIG.get("template_dir", os.path.join(PACKAGE_LOCATION, "default_template"))
