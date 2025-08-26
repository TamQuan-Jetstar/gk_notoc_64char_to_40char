from textwrap import TextWrapper


def wrap_text(logger, line):
    logger.info(f"Wrapping Line {line}")
    try:
        wrapper = TextWrapper(width=40,
                              break_on_hyphens=True,
                              expand_tabs=False)

        wrapped_output = wrapper.wrap(line)

        # if the line is a section break, hence a line full of * or a line full of -, then return ""
        if len(wrapped_output) > 1:
            if wrapped_output[0] == '*' * 40 or \
                wrapped_output[0] == '-' * 40:
                return ""

        return wrapped_output
    except (TypeError, ValueError):
        logger.exception(f"Unsupported argument {line} \
                         supplied to wrapper.")
        return ""
    except MemoryError:
        logger.exception(f"Extremely long line of text - {line}")
        return ""