#!/usr/bin/env python3

from pandocfilters import toJSONFilter, Str, RawBlock, get_filename4code
from subprocess import call, Popen, PIPE, STDOUT

def dotpng(key, value, format, meta):
  if not format=='latex':
    # rise ValueError('This filter works only with latex/pdf output format')
    pass

  if key == 'CodeBlock':
    [[ident, classes, keyvals], code] = value
    if 'dotpng' in classes:
      caption = ''
      label = ''
      sizing = 'width=\\textwidth'
      for k, v in keyvals:
        if k == 'caption': caption = v
        if k == 'label':   label   = v
        if k == 'width':   sizing  = 'width='+v
        if k == 'height':  sizing  = 'height='+v
        if k == 'scale':   ssizing = 'scale='+v

      dst = get_filename4code('graphviz', code, 'png')
      p = Popen(['dot', '-Tpng', '-o', dst], stdout=PIPE, stdin=PIPE, stderr=PIPE)
      p.communicate(bytes(code, 'utf-8'))

      result = '''
        \\begin{figure}
          \\centering
          \\includegraphics[%s]{%s}
          \\caption{%s}
          \\label{%s}
        \\end{figure}
      ''' % (sizing, dst, caption, label)
      return { 'c': ['latex', result], 't': 'RawBlock' }

if __name__ == '__main__':
  toJSONFilter(dotpng)
