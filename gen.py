#!/usr/bin/env python3
from page.gen import generate_site

ROOT = '/Users/f/SITES/'
SOURCE = f'{ROOT}unilex-sip'
TARGET = f'{ROOT}unilex/static/sip'
TPL = f'{ROOT}unilex-sip/_tpl'
EXT = ''  # can be '.htm'/'.html'
CTX = dict(
    site_name='Sipsip',
    site_url='https://unilexicon.com/sip',
    repo_url='https://github.com/fmalina/unilex-sip/blob/main/',  # for edit links
    site_root='/sip',
    dev=True  # show/hide editing links
)

if __name__ == '__main__':
    generate_site(SOURCE, TARGET, TPL, EXT, CTX)
