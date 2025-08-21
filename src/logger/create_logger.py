from pathlib import Path
import logging
import os


class LoggerSingleton:
    _instance = None
    _logger = None

    def __new__(cls, log_folder: Path, log_filename: str) -> logging.Logger:
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            cls._logger = cls._instance._configure_logger(log_folder,
                                                          log_filename)

        return cls._logger

    def _configure_logger(self, log_folder: Path, log_filename: str) -> logging.Logger:
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)

        datefmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s ||> %(message)s', datefmt)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Create the folder if it doesn't exist
        os.makedirs(log_folder, exist_ok=True)
        file_handler = logging.FileHandler(
            os.path.join(log_folder, log_filename))
        file_handler.setFormatter(formatter)

        self._logger.addHandler(console_handler)
        self._logger.addHandler(file_handler)

        return self._logger
