from lib.compile import compile_
from lib.parse import parse


def strip(input_, **kwargs):
    opts = {
        **kwargs,
        'block': True,
        'line': True,
    }
    return compile_(parse(input_, **opts), **opts)


def block(input_, **kwargs):
    opts = {
        **kwargs,
        'block': True,
    }
    return compile_(parse(input_, **opts), **opts)


def line(input_, **kwargs):
    opts = {
        **kwargs,
        'line': True,
    }
    return compile_(parse(input_, **opts), **opts)


def first(input_, **kwargs):
    opts = {
        **kwargs,
        'block': True,
        'line': True,
        'first': True,
    }
    return compile_(parse(input_, **opts), **opts)
