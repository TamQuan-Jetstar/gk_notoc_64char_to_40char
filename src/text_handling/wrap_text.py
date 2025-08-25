from textwrap import TextWrapper


def wrap_text(logger, line):
    logger.info(f"Wrapping Line {line}")
    try:
        wrapper = TextWrapper(width=40,
                              break_on_hyphens=True,
                              expand_tabs=False)

        wrapped_output = wrapper.wrap(line)

        # if its a line of * or -, which hence starts with these characters then don't parse these and skip
        if len(wrapped_output) > 1:
            if wrapped_output[0].startswith("*") or \
                    wrapped_output[0].startswith("-") or \
                    wrapped_output[1].startswith("*") or \
                    wrapped_output[1].startswith("-"):
                return ""

        return wrapped_output
    except (TypeError, ValueError):
        logger.exception(f"Unsupported argument {line} \
                         supplied to wrapper.")
        return ""
    except MemoryError:
        logger.exception(f"Extremely long line of text - {line}")
        return ""
