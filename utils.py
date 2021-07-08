import subprocess
import typer


def run(cmd):
    typer.secho(typer.style(cmd, fg='blue'))
    return subprocess.call(cmd.split())
