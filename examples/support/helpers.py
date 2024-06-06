import lib.languages as langs


def strip(s: str) -> str:
    return '*/'.join(s.split('*\\/'))


# this is used by the readme template to generate the list of languages
def languages():
    omit = {'js', 'ts'}
    keys = set(item for item in dir(langs) if not item.startswith('__')) - omit
    k_str = '\n'.join(keys)
    return f'\n- {k_str}'
