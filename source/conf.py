import recommonmark
from recommonmark.transform import AutoStructify
import sphinx_rtd_theme

project = 'sp_test'
copyright = '2020, akingse'
author = 'akingse'
release = '1.0'
language = 'zh_CN'
html_search_language = 'zh_CN'
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = ['recommonmark','sphinx_markdown_tables']
templates_path = ['_templates']
html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]



github_doc_root = 'https://github.com/lbc-team/etherscan-docs/tree/master/source/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url[:-4],
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
