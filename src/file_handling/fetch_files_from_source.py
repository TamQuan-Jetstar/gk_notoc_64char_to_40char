import fnmatch
from pathlib import Path

def fetch_files_from_source(logger, source: Path):
    logger.info(f"Fetching files from '{source}'")
    
    try:
        if not source.exists() or not source.is_dir():
            raise FileNotFoundError()

        # Get all the txt files in the source directory.
        file_list = [file for file in source.iterdir() 
                     if file.is_file() and fnmatch.fnmatch(file.name.lower(), '*.txt')]
        
        return file_list
    except FileNotFoundError:
        logger.exception(f"The specified folder '{source}' does not exist \
                         or is not a directory.")
    except PermissionError:
        logger.exception('Application does not have enough permissions to \
                         read the file names')
    except IOError:
        logger.exception('Failed to search for files in source folder.')
