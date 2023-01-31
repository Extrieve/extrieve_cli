"""Top-level package for RP To-Do."""

__appname__ = "extrieve_file_cleanup_cli"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(5)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    ID_ERROR: "id error",
}