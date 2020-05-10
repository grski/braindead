import functools
import http.server
import socketserver

from cleo import Application, Command

from braindead.constants import DIST_DIR
from braindead.rendering import render_blog


class RunCommand(Command):
    """
    This runs the engine and builds all the static pages, outputting the to DIST_DIR then serving them with server.
    run {--p|port=1644 : Port that content should be served on}
    """

    def handle(self) -> None:
        BuildCommand.handle(self)
        ServeCommand.handle(self)


class BuildCommand(Command):
    """
    Build the site without serving it.
    build
    """

    def handle(self: Command):
        render_blog()


class ServeCommand(Command):
    """
    Serve the files located in DIST_DIR directory at a given port
    serve {--p|port=1644 : Port that content should be served on}
    """

    def handle(self: Command) -> None:
        serve_port = int(self.option("p"))
        Handler: functools.partial = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIST_DIR)
        with socketserver.TCPServer(("", serve_port), Handler) as httpd:
            try:
                self.line(f"\n Serving content at localhost:{serve_port}...")
                httpd.serve_forever()
            except KeyboardInterrupt:
                httpd.server_close()
                self.line("Keyboard interrupt detected, shutting down the server gracefully.")


def cli() -> int:
    cleo_application: Application = Application()
    cleo_application.add(RunCommand())
    cleo_application.add(BuildCommand())
    cleo_application.add(ServeCommand())
    return cleo_application.run()
