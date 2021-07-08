import typer

import bootstrap

cli = typer.Typer()
cli.add_typer(bootstrap.cli, name="bootstrap")

if __name__ == '__main__':
    cli()
