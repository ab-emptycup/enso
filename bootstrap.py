from typer import Typer, secho

# import utils
from utils import run

cli = Typer()


@cli.command()
def git(username: str, email: str):
    secho(f"Setting {username} & {email} in config...")
    run('git config --global user.name "John Doe"')


@cli.command()
def command(name: str):
     secho(f"Bootstrapping new CLI tool: {name}")


@cli.command()
def repo(name: str):
    secho(f"Bootstrapping new repo directory: {name}")
