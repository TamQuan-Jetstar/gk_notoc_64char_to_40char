from pathlib import Path
import shutil


def move_file_to_archive(logger, archive: Path, file: Path):
    logger.info(f"Moving {file.name} to {archive} folder")

    try:
        # Ensure the archive folder exists, create it if necessary
        archive.mkdir(parents=True, exist_ok=True)
        # shutil.move to move the file to the archive folder
        shutil.move(str(file), str(archive.joinpath(file.name)))
    except TypeError:
        logger.exception('Invalid archive or file path.')
    except PermissionError:
        logger.exception('Application does not have enough \
                         permissions to move or create directories.')
    except FileNotFoundError:
        logger.exception(f"{file} does not exist at this location.")
    except IsADirectoryError:
        logger.exception(f"{file} is a directory and not a file \
                         and thus cannot be moved.")
    except OSError:
        logger.exception()
