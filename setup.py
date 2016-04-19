from distutils.core import setup

def is_pkg(line):
    return line and not line.startswith(('--', 'git', '#'))

with open('requirements.txt', encoding='utf-8') as reqs:
    install_requires = [l for l in reqs.read().split('\n') if is_pkg(l)]

setup(
  name = 'messenger_hook',
  packages = ['messenger_hook'],
  version = '0.1.4',
  description = 'A library to create hooks for facebook messenger',
  author = 'Vincent Lara',
  author_email = 'lara.vincent@gmail.com',
  url = 'https://github.com/l-vincent-l/messenger_hook',
  download_url = 'https://github.com/l-vincent-l/messenger_hook/tarball/0.1',
  keywords = ['facebook', 'messenger'],
  classifiers = [],
  extras_require = {
      'falcon': ['falcon']
  },
  install_requires=install_requires
)
