from notoc_parser.constants import CONTENTS, TO, AWB_NR, \
    PCS, QTY, IMP_CODE, POS, ULD_CODE


def build_special_goods(logger, goods_info, pass_val):
    logger.info("Building special goods text for notoc")
    try:
        if pass_val == 0:
            val = goods_info[CONTENTS]
            return val.ljust(40)
        elif pass_val == 1:
            return (
                f"{goods_info[TO]}{goods_info[AWB_NR]}"
                f"{goods_info[PCS]}{goods_info[QTY]}"
            )
        else:
            return (
                f"        {goods_info[IMP_CODE]}"
                f"{goods_info[POS]}{goods_info[ULD_CODE]}"
            )
    except KeyError:
        logger.exception()
        return ""
    except ValueError:
        logger.exception()
        return ""
