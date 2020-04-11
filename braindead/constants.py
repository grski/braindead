import os

import toml

PACKAGE_LOCATION: str = os.path.split(os.path.realpath(__file__))[0]

# todo: add defualts/overwriting of site.toml
DEFAULT_CONFIG: dict = toml.load(os.path.join(PACKAGE_LOCATION, "site.toml"))
# todo: add validation of the toml?
NEW_CONFIG: dict = {} if not os.path.exists("site.toml") else toml.load("site.toml")
CONFIG: dict = {**DEFAULT_CONFIG, **NEW_CONFIG}
BASE_URL: str = CONFIG["BASE_URL"]
DIST_DIR: str = CONFIG.get("DIST_DIR", "dist")
TEMPLATE_DIR: str = CONFIG.get("TEMPLATE_DIR")

# todo other template flow (git clone?)
TEMPLATE_DIR = TEMPLATE_DIR if TEMPLATE_DIR else os.path.join(PACKAGE_LOCATION, "default_template")
