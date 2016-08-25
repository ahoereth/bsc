#!/usr/bin/env python3

from pandocfilters import toJSONFilter, RawInline, Str


def marginnotes(key, value, pandoctarget, _):
  if not key == 'Note':
    return

  para = value[0]
  start, *rest = para['c']
  if (start['c'][0] != '>'):
    return

  return [
    RawInline('latex', '\marginpar{'),
    Str(start['c'][1:]), *rest,
    RawInline('latex', '}')
  ]


if __name__ == '__main__':
    toJSONFilter(marginnotes)
