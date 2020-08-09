# IMPORTANT: every registered filter must start with the phrase 'jinja_'
from jinja2 import contextfilter

from braindead.constants import CONFIG
from braindead.i18n import TRANSLATIONS


@contextfilter
def jinja_i18n(context: dict, slug: str, *args) -> str:
    """
    Tries to find proper translation for a given slug for a given language.
    If it's not found, replaces it with the default value for the default language.
    If the string is not found it raises and error. Hence it's important to have translations for all strings
    in default language.
    """
    for obj in [context, *args]:
        if language := obj.get("language"):  # NOQA
            return TRANSLATIONS[slug][language]
    return TRANSLATIONS[slug][CONFIG["language"]]
