#!/usr/bin/env python

from pandocfilters import toJSONFilter, RawInline


def extract_keyval(keyvals, key, default=None):
  val = default
  rest = []
  for k, v in keyvals:
    if k == key:
      val = v
    else:
      rest.append([k, v]) # pandocfilters uses lists instead of tuples.
  return val, rest


def shadowedimages(key, value, pandoctarget, _):
  if not key == 'Image':
    return

  [[ident, classes, keyvals], alt, [src, typef]] = value
  if not 'shadow' in classes:
    return

  caption, keyvals = extract_keyval(keyvals, 'caption', [])

  result = '''
    \\begin{figure}[H]
      \\centering
      \\tikz\\node[blur shadow={shadow blur steps=5}]{
        \\fcolorbox{black}{white}{
          \\includegraphics[width=\\textwidth]{%s}
        }
      };
      \\caption{%s}
      \\label{%s}
    \\end{figure}
  ''' % (src, caption, ident)
  return RawInline('latex', result)


if __name__ == '__main__':
  toJSONFilter(shadowedimages)
