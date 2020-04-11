from jinja2 import Environment, FileSystemLoader, Template, Undefined

from braindead.constants import CONFIG, TEMPLATE_DIR


class SilentUndefined(Undefined):
    def _fail_with_undefined_error(self, *args, **kwargs) -> None:
        """ We do not want to fail on not known variables hence this thing."""
        return None


def render_jinja_template(template: Template, context: dict) -> str:
    """ Rendering jinja template with a context and global config. """
    context_with_globals = {**context, **CONFIG}
    return template.render(context_with_globals)


jinja_environment: Environment = Environment(  # nosec
    loader=FileSystemLoader(TEMPLATE_DIR), undefined=SilentUndefined, autoescape=False
)
