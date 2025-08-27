from notoc_parser.constants import TO, CL_DV_COMP, SUB_RSK, \
    PCS, QTY_TI, RRR_CAT, PCK_GRP, IMP_CODE, CAO, POS, \
    AWB_NR, UN_ID_NR, ULD_CODE


def parse_dangerous_good_information(logger, notoc_line, goods_info, pass_val):
    logger.info(f"Parsing dangerous good information in {notoc_line}")

    try:
        # if the notoc_line is the first line of the 64 char dangerous goods info
        if pass_val == 1:
            goods_info[TO] = notoc_line[0:13].strip().ljust(13)
            goods_info[CL_DV_COMP] = notoc_line[13:19].strip().ljust(6)
            goods_info[SUB_RSK] = notoc_line[25:29].strip().ljust(4)
            goods_info[PCS] = notoc_line[29:34].strip().ljust(5)
            goods_info[QTY_TI] = notoc_line[34:41].strip().rjust(6)
            goods_info[RRR_CAT] = notoc_line[41:45].strip().ljust(4)
            goods_info[PCK_GRP] = notoc_line[45:49].strip().ljust(4)
            goods_info[IMP_CODE] = notoc_line[49:54].strip().ljust(5)
            goods_info[CAO] = notoc_line[54:58].strip().ljust(12)
            goods_info[POS] = notoc_line[60:63].strip().ljust(5)
        # if the notoc_line is the second line of the 64 char dangerous goods info
        elif pass_val == 2:
            goods_info[AWB_NR] = notoc_line[4:19].strip().ljust(15)
            goods_info[UN_ID_NR] = notoc_line[19:53].strip().ljust(21)
            goods_info[ULD_CODE] = notoc_line[53:63].strip().rjust(10)

    except IndexError:
        logger.exception()
        return goods_info

    return goods_info
