from notoc_parser.constants import TO, PCS, IMP_CODE, POS, \
    AWB_NR, ULD_CODE, CONTENTS, QTY


def parse_other_special_load(logger, notoc_line, goods_info, pass_val):
    logger.info("Parsing other special load information.")

    try:
        if pass_val == 0:
            goods_info[CONTENTS] = notoc_line[0:38].strip()
            goods_info[PCS] = notoc_line[38:43].strip().ljust(12)
            goods_info[QTY] = notoc_line[43:49].strip().ljust(6)
            goods_info[IMP_CODE] = notoc_line[49:54].strip().ljust(17)
            goods_info[POS] = notoc_line[54:63].strip().ljust(4)
        elif pass_val == 1:
            goods_info[TO] = notoc_line[0:4].strip().ljust(4)
            goods_info[AWB_NR] = notoc_line[4:53].strip().ljust(18)
            goods_info[ULD_CODE] = notoc_line[53:63].strip().rjust(10)
    except IndexError:
        logger.exception()
        return goods_info

    return goods_info
