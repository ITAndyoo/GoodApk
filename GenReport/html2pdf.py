#!/usr/bin/env.python
# -*- coding:utf-8 -*-

import pdfkit

#更换为html报告路径，当前文件夹下有测试文件
#path = 'http://60.205.214.66/upload/'
path = 'report.html'
pdfkit.from_url(path,'report.pdf')