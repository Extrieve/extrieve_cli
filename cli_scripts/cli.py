import typer, os, shutil
from typing import Optional

from cli_scripts import __appname__, __version__

app = typer.Typer()

# let's define a function that access every file within a directory
# recursively and if it matchnes the pattern remove it.
def _access_and_delete_files(directory: str, pattern: str) -> None:
    for file in os.listdir(directory):
        if os.path.isdir(file):
            _access_and_delete_files(file)
        else:
            if pattern in file:
                os.remove(file)
                typer.echo(f"File {file} removed")


@app.command(help = "Clean a directory", name = "clean", no_args_is_help = True)
def clean_directory(
        directory: str = typer.Argument(
            ...,
            help="Directory to clean"
        ),
        folder_to_remove: Optional[str] = typer.Option(
            None,
            "--folder",
            "-f",
            help="I will remove any folder in this directory with this name or name containing this string"
        ),
        file_to_remove: Optional[str] = typer.Option(
            None,
            "--file",
            "-F",
            help="I will remove any file in this directory with this name"
        )
    ) -> None:
    # Access the directory
    if not os.path.isdir(directory):
        typer.echo(f"Directory {directory} does not exist")
        raise typer.Exit(1)

    # Access the directory
    os.chdir(directory)

    # if not folder remove all folders in directory
    if not folder_to_remove and file_to_remove:
        # remove all files within each folder in directory
        _access_and_delete_files(directory)
    
    elif folder_to_remove and not file_to_remove:
        # remove all files within each folder in directory that matches folder_to_remove
        for folder in os.listdir(directory):
            if os.path.isdir(folder) and folder_to_remove in folder:
                shutil.rmtree(folder)

    elif folder_to_remove and file_to_remove:
        # remove all files within each folder in directory that matches folder_to_remove
        for folder in os.listdir(directory):
            if os.path.isdir(folder) and folder_to_remove in folder:
                _access_and_delete_files(folder, file_to_remove)

    else:
        typer.echo("You need to specify at least one option")
        raise typer.Exit(1)

def _version_callback(value: bool):
    if value:
        typer.echo(f"{__appname__} version {__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=_version_callback,
        is_eager=True,
        help="Show version and exit",
    )
) -> None: return