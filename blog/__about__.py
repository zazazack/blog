import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'blog', 'VERSION'), encoding='utf-8') as f:
    __version__ = f.read().strip()
