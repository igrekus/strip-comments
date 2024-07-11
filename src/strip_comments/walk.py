__all__ = [
  'walk',
]


def walk(cst, **kwargs):
    keep_protected = kwargs.get('safe', False) is True or kwargs.get('keep_protected', False) is True
    first_seen = False

    def _walk(node, parent=None) -> str:
        output: str = ''
        inner: str = ''
        lines: list[str] = []
        nonlocal first_seen

        for child in node.nodes:
            try:
                match child.type:
                    case 'block':
                        if kwargs.get('first', None) and first_seen is True:
                            output += _walk(child, node)
                            continue

                        if kwargs.get('preserve_newlines', None) is True:
                            inner = _walk(child, node)
                            lines = inner.split('\n')
                            output += '\n' * (len(lines) - 1)
                            continue

                        if keep_protected is True and child.is_protected is True:
                            output += _walk(child, node)
                            continue

                        first_seen = True
                        continue

                    case 'line':
                        if kwargs.get('first', None) and first_seen is True:
                            output += child.value
                            continue

                        if keep_protected is True and child.is_protected is True:
                            output += child.value

                        first_seen = True
                        continue

                    case 'open':
                        output += child.value or ''
                        continue

                    case 'close':
                        output += child.value or ''
                        continue

                    case 'text':
                        output += child.value or ''
                        continue

                    case 'newline':
                        output += child.value or ''
                        continue

                    case _:
                        output += child.value or ''
                        continue

            except RuntimeError:
                pass

        return output

    return _walk(cst)
