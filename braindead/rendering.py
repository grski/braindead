from time import time
from typing import Iterable, List

from jinja2 import Template
from markdown import Markdown

from braindead.context import add_url_to_context, build_article_context
from braindead.files import find_all_pages, find_all_posts, gather_statics, save_output
from braindead.jinja_utils import jinja_environment, render_jinja_template
from braindead.markdown_utils import md


def render_blog() -> None:
    """ Renders both pages and posts for the blog and moves them to dist folder."""
    started_at: float = time()
    posts: List[dict] = list(reversed(sorted(render_posts(), key=lambda x: x["date"])))
    pages: List[str] = render_all_pages()
    render_index(posts=posts)
    gather_statics()
    print(
        f"Rendered {len(posts+pages)+1} files! Pages: {len(pages)+1} and posts: {len(posts)}\n"
        f"Took: {time()-started_at:.3f} seconds.\n"
    )


def render_all_pages() -> List[str]:
    """ Rendering of all the pages for the blog. markdown -> html with jinja -> html"""
    return [render_page(filename=filename, md=md) for filename in find_all_pages()]


def render_page(filename: str, md: Markdown, additional_context: dict = None):
    additional_context = additional_context if additional_context else {}
    page_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = {"page": {"content": page_html}, **additional_context}
    template: Template = jinja_environment.get_template(md.Meta.get("template", ["index.html"])[0])
    output: str = render_jinja_template(template=template, context=jinja_context)
    return save_output(original_file_name=jinja_context.get("slug", filename), output=output)


def render_posts() -> List[dict]:
    return [render_and_save_post(md=md, filename=filename) for filename in find_all_posts()]


def render_and_save_post(md: Markdown, filename: str) -> dict:
    """ Renders blog posts and saves the output as html. md -> html with jinja -> html"""
    article_html: str = render_markdown_to_html(md=md, filename=filename)
    template: Template = jinja_environment.get_template(md.Meta.get("template", "detail.html"))
    jinja_context: dict = build_article_context(article_html=article_html, md=md)
    output: str = render_jinja_template(template=template, context=jinja_context)
    new_filename: str = save_output(original_file_name=jinja_context.get("slug", filename), output=output)
    return add_url_to_context(jinja_context=jinja_context, new_filename=new_filename)


def render_markdown_to_html(md: Markdown, filename: str) -> str:
    """ Markdown to html. Important here is to keep the reset() method. """
    return md.reset().convert(open(filename).read())


def render_index(posts: Iterable[dict]) -> str:
    md: Markdown = Markdown(extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"])
    filename = "index.md"
    additonal_context: dict = {"articles": posts}
    return render_page(filename=filename, md=md, additional_context=additonal_context)
