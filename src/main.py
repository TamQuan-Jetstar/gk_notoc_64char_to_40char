import sys

from create_config import create_config
from create_modules import create_modules
from start import start_notoc_conversion


def main(argv):
    # Default to running this code in production
    if len(argv) < 2:
        env = 'prd'
    elif argv[1] in ['dev', 'prd', 'test']:
        env = argv[1]
    else:
        env = 'prd'

    config = create_config(env)
    modules = create_modules(config)

    # get the logger module
    logger = modules['logger']

    logger.info("Started Notoc Integration")

    start_notoc_conversion(config, logger,
                           file_handling=modules['file_handling'],
                           text_handling=modules['text_handling'],
                           notoc_parser=modules['notoc_parser'],
                           notoc_builder=modules['notoc_builder'])

    logger.info("Completed Notoc Integration")

if __name__ == "__main__":
    main(sys.argv)
