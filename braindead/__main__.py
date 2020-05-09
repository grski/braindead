from cleo import Application

from braindead.commands import BuildCommand, RunCommand, ServeCommand

PORT = 8000

application = Application()
application.add(RunCommand())
application.add(BuildCommand())
application.add(ServeCommand())

if __name__ == "__main__":
    application.run()
