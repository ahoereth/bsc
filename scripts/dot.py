#!/usr/bin/env python3

from subprocess import Popen, PIPE
from pandocfilters import toJSONFilter, get_extension, get_filename4code, RawBlock, Para, Image, RawInline


def extract_keyval(keyvals, key, default=None):
  val = default
  rest = []
  for k, v in keyvals:
    if k == key:
      val = v
    else:
      rest.append([k, v]) # pandocfilters uses lists instead of tuples.
  return val, rest


def dot(key, value, pandoctarget, _):
  if not key == 'CodeBlock':
    return

  [[ident, classes, keyvals], code] = value
  if not 'dot' in classes:
    return

  caption, keyvals = extract_keyval(keyvals, 'caption', [])

  # If src keyval is given, we read the val's file and ignore the block's body.
  # If src class is given, the file is specified in the block's body.
  src, keyvals = extract_keyval(keyvals, 'src')
  if src is not None or 'src' in classes:
    if src is None:
      src = code
    with open(src, 'r') as f:
      code = f.read()

  # Users may specify the format explicitly because sometimes dot2tex does not
  # result in the desired output.
  targetformat = get_extension(pandoctarget, 'png', html='png', latex='tex')
  targetformat, keyvals = extract_keyval(keyvals, 'format', targetformat)

  width, keyvals = extract_keyval(keyvals, 'width', '\\textwidth')

  if targetformat == 'tex':

    p = Popen(['dot2tex', '-ftikz', '--codeonly'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    tikz, err = p.communicate(bytes(code, 'utf-8'))
    if len(err) != 0:
      raise ValueError(err.decode('utf-8'))

    result = '''
      \\begin{figure}[H]
        \\centering
        \\resizebox{%s}{!}{
          \\begin{tikzpicture}
            %s
          \\end{tikzpicture}
        }
        \\caption{%s}
        \\label{%s}
      \\end{figure}
    ''' % (width, tikz.decode('utf-8'), caption, ident)
    return RawBlock('latex', result)

  elif targetformat in ['png', 'pdf']:
    dst = get_filename4code('dot', code, targetformat)
    scale, keyvals = extract_keyval(keyvals, 'scale')


    p = Popen(['dot', '-T' + targetformat, '-o', dst],
              stdout=PIPE, stdin=PIPE, stderr=PIPE)
    _, err = p.communicate(bytes(code, 'utf-8'))
    if len(err) != 0:
      raise ValueError(err.decode('utf-8'))

    graphic = '\\resizebox{%s}{!}{\\includegraphics{%s}}' % (width, dst)
    if scale is not None:
      graphic = '\\scalebox{%s}{\\includegraphics{%s}}' % (scale, dst)

    result = '''
      \\begin{figure}[htbp]
        \\centering
        %s
        \\caption{%s}
        \\label{%s}
      \\end{figure}
    ''' % (graphic, caption, ident)
    return RawBlock('latex', result);

if __name__ == '__main__':
    toJSONFilter(dot)
