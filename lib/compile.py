__all__ = [
  'compile_',
]


def compile_(cst, **kwargs):
    keep_protected = kwargs.get('safe', False) is True or kwargs.get('keep_protected', False) is True
    first_seen = False

    def _walk(node, parent = None) -> str:
        output: str = ''
        inner: str = ''
        lines: list[str] = []
        nonlocal first_seen

        for child in node.nodes:
            match child.type:
                case 'block':
                    if kwargs['first'] and first_seen is True:
                        output += _walk(child, node)

                    if kwargs['preserve_newlines'] is True:
                        inner = _walk(child, node)
                        lines = inner.split('\n')
                        output += '\n' * (len(lines) - 1)

                    if keep_protected is True and child.is_protected is True:
                        output += _walk(child, node)

                    first_seen = True

                case 'line':
                    if kwargs.get('first', None) and first_seen is True:
                        output += child.value

                    if keep_protected is True and child.is_protected is True:
                        output += child.value

                    first_seen = True

                case _:
                    # case 'open':
                    # case 'close':
                    # case 'text':
                    # case 'newline':
                    output += child.value or ''

        return output

    return _walk(cst)
