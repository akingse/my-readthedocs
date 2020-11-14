### 配置文件



```python
import recommonmark
from recommonmark.transform import AutoStructify

project = 'sp_test'
copyright = '2020, akingse'
author = 'akingse'
release = '1.0'

extensions = [
'recommonmark'
]
templates_path = ['_templates']
language = 'zh_CN'
html_search_language = 'zh_CN'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
```

