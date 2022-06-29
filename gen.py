#!/usr/bin/env python3
from page.gen import generate_site

ROOT = '/Users/f/SITES/'
SOURCE = f'{ROOT}unilex-altmed'
TARGET = f'{ROOT}unilex/static/altmed'
TPL = f'{ROOT}unilex-altmed/_tpl'
EXT = ''  # can be '.htm'/'.html'
CTX = dict(
    site_name='Alt med',
    site_url='https://unilexicon.com/altmed',
    repo_url='https://github.com/fmalina/unilex-sip/blob/main/',  # for edit links
    site_root='/altmed',
    dev=True  # show/hide editing links
)

if __name__ == '__main__':
    generate_site(SOURCE, TARGET, TPL, EXT, CTX)
