from pathlib import Path
import re
from notoc_parser.constants import ITEM_BREAK


def build_notoc(logger, destination: Path, file, wrapped_output):
    logger.info("Building notoc")
    if len(wrapped_output) <= 0:
        return

    # TODO: heavily test the below
    filename = re.sub(r"\.txt$", "_40Char.txt", file, flags=re.IGNORECASE)

    target = destination.joinpath(filename)

    with open(target, 'w', encoding='UTF-8') as notoc:
        flag_dangerous_goods = False
        flag_other_special_load = False

        flag_section_break = 0

        for line in wrapped_output:
            if "SI EMERGENCY CONTACT" in line:
                flag_other_special_load = False
            if "OTHER SPECIAL LOAD" in line:
                flag_dangerous_goods = False
                flag_other_special_load = True
                flag_section_break = 0
            if "DANGEROUS GOODS" in line:
                flag_dangerous_goods = True
                flag_section_break = 0
            if (flag_dangerous_goods or flag_other_special_load) \
                    and (line[0].isdigit() and line[2] == ".") \
                    and ((flag_dangerous_goods and flag_section_break != 7) or (
                    flag_other_special_load and flag_section_break != 5)):
                notoc.write(ITEM_BREAK + "\n")
            notoc.write(line)
            notoc.write("\n")
            flag_section_break += 1
        notoc.write("\n")

    return target
