from strip_comments.parse import parse
from strip_comments.walk import walk


def strip(input_, **kwargs):
    opts = {
        **kwargs,
        'block': True,
        'line': True,
    }
    return walk(parse(input_, **opts), **opts)


def block(input_, **kwargs):
    opts = {
        **kwargs,
        'block': True,
    }
    return walk(parse(input_, **opts), **opts)


def line(input_, **kwargs):
    opts = {
        **kwargs,
        'line': True,
    }
    return walk(parse(input_, **opts), **opts)


def first(input_, **kwargs):
    opts = {
        **kwargs,
        'block': True,
        'line': True,
        'first': True,
    }
    return walk(parse(input_, **opts), **opts)
