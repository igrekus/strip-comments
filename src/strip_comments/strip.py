from strip_comments.models import Options
from strip_comments.parse import parse
from strip_comments.walk import walk
import strip_comments.languages as languages


__all__ = [
    'block',
    'first',
    'line',
    'strip',
]


def strip(
        source: str,
        block=True,
        line=True,
        first=False,
        language='javascript',
        keep_protected=False,
        safe=False,
        preserve_newlines=False
):
    if not isinstance(source, str):
        raise ValueError('Expected input to be a string')

    name = language.lower()
    lang = getattr(languages, name, None)

    if lang is None:
        raise ValueError(f'Language {name} is not supported by strip-comments')

    options = Options(
        block=block,
        line=line,
        first=first,
        language=lang,
        keep_protected=keep_protected,
        safe=safe,
        preserve_newlines=preserve_newlines,
    )
    return walk(parse(source, options), options)


def block(source, language='javascript', keep_protected=False, safe=False, preserve_newlines=False):
    return strip(
        source,
        block=True,
        line=False,
        first=False,
        language=language,
        keep_protected=keep_protected,
        safe=safe,
        preserve_newlines=preserve_newlines
    )


def line(source, language='javascript', keep_protected=False, safe=False, preserve_newlines=False):
    return strip(
        source,
        block=False,
        line=True,
        first=False,
        language=language,
        keep_protected=keep_protected,
        safe=safe,
        preserve_newlines=preserve_newlines
    )


def first(source, language='javascript', keep_protected=False, safe=False, preserve_newlines=False):
    return strip(
        source,
        block=True,
        line=True,
        first=True,
        language=language,
        keep_protected=keep_protected,
        safe=safe,
        preserve_newlines=preserve_newlines
    )
