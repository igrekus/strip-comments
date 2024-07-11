from strip_comments.models import Options

__all__ = [
  'walk',
]


def walk(cst, options: Options):
    keep_protected = options.safe is True or options.keep_protected is True
    first_seen = False

    def _walk(node) -> str:
        output: str = ''
        nonlocal first_seen

        for child in node.nodes:
            match child.type:
                case 'block':
                    if options.first and first_seen is True:
                        output += _walk(child)
                        continue

                    if options.preserve_newlines is True:
                        inner = _walk(child)
                        lines = inner.split('\n')
                        output += '\n' * (len(lines) - 1)
                        continue

                    if keep_protected is True and child.is_protected is True:
                        output += _walk(child)
                        continue

                    first_seen = True
                    continue

                case 'line':
                    if options.first and first_seen is True:
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

    return _walk(cst)
