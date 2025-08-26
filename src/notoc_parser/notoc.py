from pathlib import Path

from notoc_parser.constants import NIL, ULD_CODE, POS, \
    SECTION_BREAK, \
    SI_EMERGENCY_CONTACT, \
    NO_EVIDENCE, \
    LOADING_SUPERVISOR, \
    SIGNATURE, \
    EMERGENCY_RESPONSE_CODE, \
    DANGEROUS_GOODS_SECTION_NAME, \
    DANGEROUS_GOOD_COLUMN_HEADERS, \
    OTHER_SPECIAL_LOAD_SECTION_NAME, \
    OTHER_SPECIAL_LOAD_COLUMN_HEADERS

from notoc_parser.dangerous_good_info import parse_dangerous_good_information
from notoc_parser.other_special_load import parse_other_special_load

import notoc_builder


def parse_notoc(logger, text_handling, file: Path, notoc):
    logger.info(f"Parsing Notoc - {file.name}")

    wrapped_output = list[str]()

    # flags for if in the middle of a multiline parse
    flag_dangerous_goods = False
    flag_dangerous_goods_list = False
    flag_other_special_load = False
    flag_other_special_load_list = False
    index = 0
    notoc_document_index = 0

    try:
        for notoc_line in notoc:
            output = text_handling.wrap_text(logger,
                                             line=notoc_line)
            goods_info = dict()
            for line in output:
                # if currently in a multiline parse
                if flag_dangerous_goods or flag_other_special_load:
                    index += 1
                    # line 4 means into the list of dangerous goods or special load
                    if index == 4:
                        if flag_dangerous_goods:
                            flag_dangerous_goods_list = True
                        if flag_other_special_load:
                            flag_other_special_load_list = True
                        flag_dangerous_goods = False
                        flag_other_special_load = False
                        index = 0
                    continue

                if DANGEROUS_GOODS_SECTION_NAME in line:
                    flag_dangerous_goods = True
                    wrapped_output.append(SECTION_BREAK)
                    wrapped_output.append(line)
                    for header_line in DANGEROUS_GOOD_COLUMN_HEADERS:
                        wrapped_output.append(header_line)
                    wrapped_output.append(SECTION_BREAK)
                    continue

                if NIL in line:
                    wrapped_output.append(NIL)

                if flag_dangerous_goods_list and EMERGENCY_RESPONSE_CODE in line:
                    for i in range(1, 3):
                        parse_dangerous_good_information(logger,
                                                         notoc_line=notoc[notoc_document_index + i],
                                                         goods_info=goods_info,
                                                         pass_val=i)

                    if not notoc[notoc_document_index - 1][0:2].isdigit():
                        temp_var_name = notoc[notoc_document_index - 1].strip()
                        wrapped_output.append(f"    {temp_var_name}".ljust(40))
                        goods_info[ULD_CODE] = (
                            goods_info[POS].strip()).rjust(13)
                        goods_info[POS] = ""

                    wrapped_output.append(line)

                    for i in range(1, 4):
                        output = notoc_builder.build_dangerous_goods(logger, goods_info,
                                                                     pass_val=i)
                        wrapped_output.append(output)

                if OTHER_SPECIAL_LOAD_SECTION_NAME in line:
                    flag_dangerous_goods_list = False
                    flag_other_special_load = True
                    wrapped_output.append(SECTION_BREAK)
                    wrapped_output.append(line)
                    for header_line in OTHER_SPECIAL_LOAD_COLUMN_HEADERS:
                        wrapped_output.append(header_line)
                    wrapped_output.append(SECTION_BREAK)
                    continue

                if flag_other_special_load_list and \
                        line[0:2].isdigit() and \
                        line[2] == ".":
                    for i in range(0, 2):
                        parse_other_special_load(logger,
                                                 notoc_line=notoc[notoc_document_index + i],
                                                 goods_info=goods_info,
                                                 pass_val=i)

                    for i in range(0, 3):
                        output = notoc_builder.build_special_goods(logger, goods_info,
                                                                   pass_val=i)
                        wrapped_output.append(output)

                if SI_EMERGENCY_CONTACT in line:
                    flag_other_special_load_list = False
                    wrapped_output.append(SECTION_BREAK)

                if NO_EVIDENCE in line:
                    wrapped_output.append(SECTION_BREAK)

                if LOADING_SUPERVISOR in line:
                    # Earlier there was a "`" in this append statement.
                    wrapped_output.append(" ")

                # Catches all the other lines, such as the first 4 lines with the FROM, FLIGHT, DATE, A/C REG, the name of the dangerous goods, name of special load, special instructions
                if not flag_dangerous_goods_list or \
                        (notoc_line[0:2].isdigit() and notoc_line[2] == "."):
                    if not flag_other_special_load_list and SIGNATURE not in line:
                        wrapped_output.append(line)
                    
            notoc_document_index += 1
    except IOError:
        logger.exception()
        return []
    
    return wrapped_output

