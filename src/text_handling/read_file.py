from pathlib import Path


def read_file(logger, file: Path):
    logger.info("Reading Notoc")

    try:
        if not file.exists():
            raise FileNotFoundError()
        if file.is_dir():
            raise IsADirectoryError()

        with file.open(mode='r') as file_object:
            file_contents = file_object.readlines()
            return file_contents

    except FileNotFoundError:
        logger.exception(f"The file '{file.name}' does not exist")
    except IsADirectoryError:
        logger.exception(f"The specified path '{file}' is a directory")
    except PermissionError:
        logger.exception('Application does not have enough permissions to \
                         read the file names')
    except IOError:
        logger.exception('Failed to search for files in source folder.')

    return []
