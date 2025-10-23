from logger.create_logger import LoggerSingleton
import file_handling
import text_handling
import notoc_parser
import notoc_builder


def create_modules(config):
    
    logger = LoggerSingleton(log_folder=config['logger']['log_folder'],
                             log_filename=config['logger']['log_filename'],)

    modules = {}
    modules['logger'] = logger
    modules['file_handling'] = file_handling
    modules['text_handling'] = text_handling
    modules['notoc_parser'] = notoc_parser
    modules['notoc_builder'] = notoc_builder

    return modules
