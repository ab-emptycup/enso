from typer import Typer, secho

# import utils
from utils import run

cli = Typer()


@cli.command()
def git(username: str, email: str):
    secho(f"Setting {username} & {email} in config...")
    run(f'git config --global user.name "{username}"')
    run(f'git config --global user.email "{email}"')


@cli.command()
def command(name: str):
     secho(f"Bootstrapping new CLI tool: {name}")


@cli.command()
def repo(name: str):
    secho(f"Bootstrapping new repo directory: {name}")
