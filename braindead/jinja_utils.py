from jinja2 import Environment, FileSystemLoader, Template

from braindead import jinja_filters
from braindead.constants import CONFIG, TEMPLATE_DIR


def render_jinja_template(template: Template, context: dict) -> str:
    """ Rendering jinja template with a context and global config. """
    context_with_globals = {**context, "config": CONFIG}
    return template.render(context_with_globals)


def add_additional_filters_to_environment(environment: Environment) -> Environment:
    """ Adding additional filters that begin with jinja_ prefix and are defined in jinja_filters.py file"""
    filters = {
        jinja_filter: getattr(jinja_filters, jinja_filter)
        for jinja_filter in dir(jinja_filters)
        if jinja_filter.startswith("jinja_")
    }
    for filter_name, filter_function in filters.items():
        environment.filters[filter_name.replace("jinja_", "")] = filter_function
    return environment


jinja_environment: Environment = add_additional_filters_to_environment(
    Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=False)  # nosec
)
