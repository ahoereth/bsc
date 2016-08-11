#!/usr/bin/env python3

from pandocfilters import toJSONFilter, Str, RawBlock
from subprocess import Popen, PIPE, STDOUT

def dot2tex(key, value, format, meta):
  if not format == 'latex':
    pass
  if key == 'CodeBlock':
    [[ident, classes, keyvals], graph] = value
    if 'dot' in classes:
      caption = ''
      label = ''
      width = '\\columnwidth'
      for k, v in keyvals:
        if k == 'caption': caption = v
        if k == 'label': label = v
        if k == 'width': width = v

      p = Popen(['dot2tex', '--codeonly'],
                stdout=PIPE, stdin=PIPE, stderr=PIPE)
      code, err = p.communicate(bytes(graph, 'utf-8'))
      # p = Popen(['fdp'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
      # dot, err = p.communicate(bytes(graph, 'utf-8'))

      # p2 = Popen(['dot2tex', '-ftikz', '--codeonly'],
      #           stdout=PIPE, stdin=PIPE, stderr=PIPE)
      # code, err = p.communicate(dot)

      if len(err) != 0:
          raise ValueError(err.decode('utf-8'))

      result = '''
        \\begin{figure}
          \\centering
          \\adjustbox{max width=%s}{
            \\begin{tikzpicture}
              %s
            \\end{tikzpicture}
          }
          \\caption{%s}
          \\label{%s}
        \\end{figure}
      ''' % (width, code.decode('utf-8'), caption, label)
      return { 'c': ['latex', result], 't': 'RawBlock' }

if __name__ == '__main__':
    toJSONFilter(dot2tex)