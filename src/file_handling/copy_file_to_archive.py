from pathlib import Path
import shutil
import datetime
import os
import math

def copy_file_to_archive(logger, archive: Path, file: Path):
    logger.info(f"Copying {file.name} to {archive} folder")

    try:
        
        timestamp = datetime.datetime.now()
        year = timestamp.year
        month = timestamp.month
        day = timestamp.day
        
        archiveExtStr = f"{str(archive)}\\{str(year)}\\{str(month)}\\{day}"
        targetPath = Path(archiveExtStr)
        # Ensure the archive folder exists, create it if necessary
        targetPath.mkdir(parents=True, exist_ok=True)

        # Deals with the rare scenario that there is a matching filename already in archive
        counter = 1
        if os.path.exists(Path(archiveExtStr + f"\\{file.name}")):
            counter += 1
            while os.path.exists(Path(archiveExtStr + f"\\{file.stem}_{counter}.txt")):
                counter += 1
            targetPath = Path(archiveExtStr + f"\\{file.stem}_{counter}.txt")
        else:
            # there is no duplicate and attach the base file name
            targetPath = Path(archiveExtStr + f"\\{file.name}")
        
        # shutil.copy to copy the file to the archive folder
        shutil.copy(str(file), str(targetPath))

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
