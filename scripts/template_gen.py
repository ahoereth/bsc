import jinja2
env = jinja2.Environment()
env.loader = jinja2.FileSystemLoader('.')
template = env.get_template('ClassicThesis.tex')

# TODO: Use config.yaml here
config = {
  'fontsize': '11pt',
  'paper': 'a4', #'b5',
  'BCOR': '5mm',
  'language': 'english',
  'crop': False, #'a4',
  'table_of_contents': {
    'contents': True,
    'figures': True,
    'tables': False,
    'listings': True
  },
}

with open('./thesis_skeleton.latex', 'w') as f:
  f.write(template.render(**config))
