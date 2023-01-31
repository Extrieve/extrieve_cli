import typer, os, shutil
from typing import Optional

from cli_scripts import __appname__, __version__

app = typer.Typer()

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
    if not folder_to_remove:
        for folder in os.listdir():
            if os.path.isdir(folder) and not file_to_remove:
                shutil.rmtree(folder)
                # log to user
                typer.echo(f"Removed {folder}")
            elif os.path.isdir(folder) and file_to_remove:
                for file in os.listdir(folder):
                    if file == file_to_remove:
                        os.remove(os.path.join(folder, file))
            else:
                continue

    if folder_to_remove:
        for folder in os.listdir():
            if folder_to_remove in folder:
                shutil.rmtree(folder)
            else:
                continue
    
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