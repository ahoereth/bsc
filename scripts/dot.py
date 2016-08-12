#!/usr/bin/env python3

from subprocess import Popen, PIPE
from pandocfilters import toJSONFilter, get_extension, get_caption, get_filename4code, RawBlock, Para, Image


def extract_keyval(keyvals, key, default=None):
  val = default
  rest = []
  for k, v in keyvals:
    if k == key and val is not None:
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

  if targetformat == 'tex':
    width, keyvals = extract_keyval(keyvals, 'width', '\\columnwidth')
    caption, _ = extract_keyval(keyvals, 'caption')

    p = Popen(['dot2tex', '--codeonly'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    tikz, err = p.communicate(bytes(code, 'utf-8'))
    if len(err) != 0:
      raise ValueError(err.decode('utf-8'))

    result = '''
      \\begin{figure}[H]
        \\centering
        \\adjustbox{max width=%s}{
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
    caption, _, keyvals = get_caption(keyvals)
    dst = get_filename4code('dot', code, targetformat)

    p = Popen(['dot', '-T' + targetformat, '-o', dst],
              stdout=PIPE, stdin=PIPE, stderr=PIPE)
    _, err = p.communicate(bytes(code, 'utf-8'))
    if len(err) != 0:
      raise ValueError(err.decode('utf-8'))

    # This overwrites ident prefixes like lst to fig. Desired behavior?
    return Para([Image([ident, [], keyvals], caption, [dst, 'fig:'])])

if __name__ == '__main__':
    toJSONFilter(dot)
