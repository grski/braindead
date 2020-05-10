# IMPORTANT: every registered filter must start with the phrase 'jinja_'
from jinja2 import contextfilter

from braindead.constants import CONFIG
from braindead.i18n import TRANSLATIONS


@contextfilter
def jinja_i18n(context: dict, slug: str, *args) -> str:
    for obj in [context, *args]:
        if language := obj.get("language"):  # NOQA
            return TRANSLATIONS[slug][language]
    return TRANSLATIONS[slug][CONFIG["language"]]
