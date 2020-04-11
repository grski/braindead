from typing import Dict

from markdown import Markdown

from braindead.constants import BASE_URL, DIST_DIR


def build_meta_context(md: Markdown) -> Dict[str, str]:
    """
    This builds context that we get from Meta items from markdown like
    post/page Title, Description and so on.
    """
    return {key: "\n".join(value) for key, value in md.Meta.items()}


def build_article_context(article_html: str, md: Markdown) -> Dict[str, str]:
    """ Contant that'll be used to render template with jinja. """
    return {"content": article_html, **build_meta_context(md=md)}


def add_url_to_context(jinja_context: dict, new_filename: str) -> dict:
    """ Builds and adds url for a given page/post to jinja context. """
    jinja_context["url"] = f"{BASE_URL}{new_filename.replace(f'{DIST_DIR}/', '')}"
    return jinja_context
