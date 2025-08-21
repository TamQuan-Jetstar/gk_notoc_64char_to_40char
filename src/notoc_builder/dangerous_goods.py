from notoc_parser.constants import TO, CL_DV_COMP, SUB_RSK, \
    PCS, QTY_TI, RRR_CAT, PCK_GRP, IMP_CODE, CAO, POS, \
    AWB_NR, UN_ID_NR, ULD_CODE


def build_dangerous_goods(logger, goods_info, pass_val):
    logger.info("Building dangerous goods text for notoc")
    try:
        if pass_val == 1:
            return (
                f"{goods_info[TO]}{goods_info[CL_DV_COMP]}"
                f"UN/   {goods_info[SUB_RSK]}{goods_info[PCS]}{goods_info[QTY_TI]}"
            )
        elif pass_val == 2:
            return f"    {goods_info[AWB_NR]}{goods_info[UN_ID_NR]}"
        else:
            return (
                f"{goods_info[RRR_CAT]}{goods_info[PCK_GRP]}"
                f"{goods_info[IMP_CODE]}{goods_info[CAO]}"
                f"{goods_info[POS]}{goods_info[ULD_CODE]}"
            )

    except KeyError:
        logger.exception()
        return ""
    except ValueError:
        logger.exception()
        return ""
