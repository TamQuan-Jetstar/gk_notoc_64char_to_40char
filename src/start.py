def start_notoc_conversion(config, logger, file_handling, text_handling, notoc_parser, notoc_builder):
    notoc_list = file_handling.fetch_files_from_source(logger,
                                                       source=config['notoc']['source'])
    
    if len(notoc_list) == 0: # if there are no NOTOCS 
        logger.info("No NOTOC files found in source directory.")
    else:
        logger.info(f"{len(notoc_list)} NOTOC files were found")
        
    # run the notoc conversion process for every file in the source directory
    if notoc_list is not None:
        for notoc in notoc_list:
            contents = text_handling.read_file(logger,
                                            file=notoc)
            wrapped_output = notoc_parser.parse_notoc(logger,
                                                    text_handling,
                                                    file=notoc,
                                                    notoc=contents)
            target = notoc_builder.build_notoc(logger,
                                            destination=config['notoc']['destination'],
                                            file=notoc.name,
                                            wrapped_output=wrapped_output)
            file_handling.copy_file_to_archive(logger,
                                            archive=config['notoc']['archive'],
                                            file=target)
            file_handling.move_file_to_archive(logger,
                                            archive=config['notoc']['archive'],
                                            file=notoc)
