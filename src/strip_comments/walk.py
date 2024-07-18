from strip_comments.models import Options

__all__ = [
    'walk',
]


def _recur(node, keep_protected: bool, first_seen: bool, first: bool, preserve_newlines: bool) -> str:
    output: str = ''

    for child in node.nodes:
        match child.type:
            case 'block':
                if first and first_seen is True:
                    output += _recur(child, keep_protected, first_seen, first, preserve_newlines)
                    continue

                if preserve_newlines is True:
                    inner = _recur(child, keep_protected, first_seen, first, preserve_newlines)
                    lines = inner.split('\n')
                    output += '\n' * (len(lines) - 1)
                    continue

                if keep_protected is True and child.is_protected is True:
                    output += _recur(child, keep_protected, first_seen, first, preserve_newlines)
                    continue

                first_seen = True
                continue

            case 'line':
                if first and first_seen is True:
                    output += child.value
                    continue

                if keep_protected is True and child.is_protected is True:
                    output += child.value

                first_seen = True
                continue

            case 'open' | 'close' | 'text' | 'newline':
                output += child.value or ''
                continue

            case _:
                output += child.value or ''
                continue

    return output


def walk(cst, options: Options):
    return _recur(
        cst,
        keep_protected=options.keep_protected,
        first_seen=False,
        first=options.first,
        preserve_newlines=options.preserve_newlines
    )
