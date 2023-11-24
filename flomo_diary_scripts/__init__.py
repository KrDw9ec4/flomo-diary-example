#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
此模块用于保存一些类，包含了用于正则表达式和文件路径类。

- Patterns: 保存编译好的正则表达式对象。
- Path: 保存文件路径。
"""

__author__ = "krdw"

import re


class Patterns:
    """
    Patterns 类来保存要用到的正则表达式（已编译好的 RE 对象）
    """

    parse_date = re.compile(r'(\d{4})[年/.-]?(\d{2})[月/.-]?(\d{2})[日号]?')

    """
    解析不同格式的日期，用于 input_date 模块。

    `.group(0)`: 整个日期字符串(tuple)
    """


class Path:
    """
    Path 类用来保存要用到的文件路径。
    """

    json = "./flomo_diary_scripts/output.json"

    """
    用于保存 output.json 的路径。
    """
