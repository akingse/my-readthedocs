我的 read the docs
================================
简介区
这些都是首页说明文字，不会显示在左侧目录栏；（采用类md的CRLF换行）

source目录下markdown文件和 index.rst；

其中，markdown为子目录文件可使用文件夹；

index.rst为目录索引文件，建议使用reStructuredText语法;

目录
==================
说明区
下面是toctree，加载指定md文件，目录专用；

.. toctree::
   :maxdepth: 2
   :caption: 我的目录（标题）

   hello.md
   other_folder/autumn.md

