#!/usr/bin/env python3

from pandocfilters import toJSONFilter, Para, Image, get_filename4code, get_caption, get_extension
from subprocess import call, Popen, PIPE, STDOUT

def dotpdf(key, value, format, meta):
  if not format=='latex':
    # rise ValueError('This filter works only with latex/pdf output format')
    pass
  if key == 'CodeBlock':
    [[ident, classes, keyvals], code] = value
    if 'dotpdf' in classes:
      caption, typef, keyvals = get_caption(keyvals)

      code = value[1]
      dst = get_filename4code('graphviz', code, 'pdf')
      p = Popen(['dot', '-Tpdf', '-o', dst],
                stdout=PIPE, stdin=PIPE, stderr=PIPE)
      p.communicate(bytes(code, 'utf-8'))[0]
      return Para([Image([ident, [], keyvals], caption, [dst, typef])])

if __name__ == '__main__':
  toJSONFilter(dotpdf)
