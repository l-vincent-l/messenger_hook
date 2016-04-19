from distutils.core import setup

def is_pkg(line):
    return line and not line.startswith(('--', 'git', '#'))

with open('requirements.txt', encoding='utf-8') as reqs:
    install_requires = [l for l in reqs.read().split('\n') if is_pkg(l)]

setup(
  name = 'messenger_hook',
  packages = ['messenger_hook'], # this must be the same as the name above
  version = '0.1.4',
  description = 'A library to create hooks for facebook messenger',
  author = 'Vincent Lara',
  author_email = 'lara.vincent@gmail.com',
  url = 'https://github.com/l-vincent-l/messenger_hook', # use the URL to the github repo
  download_url = 'https://github.com/l-vincent-l/messenger_hook/tarball/0.1', # I'll explain this in a second
  keywords = ['facebook', 'messenger'], # arbitrary keywords
  classifiers = [],
  extras_require = {
      'falcon': ['falcon']
  },
  install_requires=install_requires
)
