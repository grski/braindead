from typing import Iterable

from jinja2 import Template
from markdown import Markdown

from braindead.context import add_url_to_context, build_article_context
from braindead.files import find_all_pages, find_all_posts, gather_statics, save_output
from braindead.jinja_utils import jinja_environment, render_jinja_template
from braindead.markdown_utils import md


def render_blog() -> None:
    """ Renders both pages and posts for the blog and moves them to dist folder."""
    posts: Iterable[dict] = reversed(sorted(render_posts(), key=lambda x: x["date"]))
    render_all_pages()
    render_index(posts=posts)
    gather_statics()


def render_all_pages() -> None:
    """ Rendering of all the pages for the blog. markdown -> html with jinja -> html"""
    template: Template = jinja_environment.get_template("index.html")
    for filename in find_all_pages():
        render_page(filename=filename, md=md, template=template)


def render_page(filename: str, md: Markdown, template: Template, additional_context: dict = None):
    additional_context = additional_context if additional_context else {}
    page_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = {"page": {"content": page_html}, **additional_context}
    output: str = render_jinja_template(template=template, context=jinja_context)
    save_output(original_file_name=jinja_context.get("slug", filename), output=output)


def render_posts() -> Iterable[dict]:
    template: Template = jinja_environment.get_template("detail.html",)
    return [render_and_save_post(md=md, filename=filename, template=template) for filename in find_all_posts()]


def render_and_save_post(md, filename, template) -> dict:
    """ Renders blog posts and saves the output as html. md -> html with jinja -> html"""
    article_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = build_article_context(article_html=article_html, md=md)
    output: str = render_jinja_template(template=template, context=jinja_context)
    new_filename: str = save_output(original_file_name=jinja_context.get("slug", filename), output=output)
    return add_url_to_context(jinja_context=jinja_context, new_filename=new_filename)


def render_markdown_to_html(md: Markdown, filename: str) -> str:
    """ Markdown to html. Important here is to keep the reset() method. """
    return md.reset().convert(open(filename).read())


def render_index(posts: Iterable[dict]) -> None:
    md: Markdown = Markdown(extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"])
    template: Template = jinja_environment.get_template("index.html")
    filename = "index.md"
    additonal_context: dict = {"articles": posts}
    render_page(filename=filename, md=md, template=template, additional_context=additonal_context)
