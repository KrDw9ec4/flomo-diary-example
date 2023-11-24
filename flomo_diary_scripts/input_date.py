#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
```python
from flomo_diary_scripts.input_date import main as input_date

input_date()
```

---

导入本模块的 main() 函数，直接调用后在控制台输入日期，程序会自动匹配并解析日期，最终将日期信息写入 JSON 文件。

支持的日期格式:

- YYYY年MM月DD日
- YYYY年MM月DD号
- YYYY/MM/DD
- YYYY.MM.DD
- YYYY-MM-DD
- YYYYMMDD
"""

__author__ = "krdw"

import unittest
from datetime import datetime
from __init__ import Patterns, Path
from rw_json import update_json


def date_reminder():
    """
    根据当前时间，如果在凌晨时段（6点以前），提醒用户注意汇总日期。

    Parameters: None

    Returns: None
    """

    now = datetime.now()
    if now.hour <= 6:
        print(f"现在是{now.year}年{now.month}月{now.day}日凌晨{now.hour}点{now.minute}分，注意汇总日期")
    else:
        print(f"现在是{now.year}年{now.month}月{now.day}日{now.hour}点{now.minute}分")


def date_parser(date):
    """
    根据用户输入的日期字符串，匹配并解析出年、月、日的元组。支持多种日期格式。

    Parameters:
        date (str): 用户输入的日期字符串

    Returns:
        date (tuple): 匹配到的日期元组，未匹配到则返回 None
    """

    matched_date = Patterns.parse_date.match(date)
    return matched_date.groups() if matched_date else None


def date_confirm(date):
    """
    在解析日期后，通过用户确认，确保日期解析正确。用户需回车确认，若确认错误，需重新输入。

    Parameters:
        date (tuple): 匹配到的日期元组

    Returns:
        bool: 用户确认正确返回 True，否则返回 False
    """

    confirm = input(f"匹配到：{date[0]}年{date[1]}月{date[2]}日，确认请输入回车：")
    return not confirm


def date_dump(date):
    """
    将解析得到的日期信息以 JSON 格式写入文件，以备后续使用。

    Parameters:
        date (tuple): 匹配到的日期元组

    Returns: None
    """

    output = {
        "IO_value": {
            "date": date
        },
        "yaml": {
            "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }
    }
    update_json(Path.json, output)


def main():
    """
    整合模块功能，提醒当前日期，循环接收用户输入的日期，解析并确认，最终将日期信息写入 JSON 文件。

    Parameters: None

    Returns: None
    """

    date_reminder()

    while True:
        date = input("请输入日期：")
        if parsed_date := date_parser(date):
            if date_confirm(parsed_date):
                break
        else:
            print("未匹配到日期，请重新输入")

    date_dump(parsed_date)


class TestDateParser(unittest.TestCase):
    """
    支持的日期格式:
    1. YYYY年MM月DD日
    2. YYYY年MM月DD号
    3. YYYY/MM/DD
    4. YYYY.MM.DD
    5. YYYY-MM-DD
    6. YYYYMMDD
    """

    def test_diff_formmat(self):
        self.assertEqual(date_parser("2023年11月23日"), ('2023', '11', '23'))
        self.assertEqual(date_parser("2023年11月23号"), ('2023', '11', '23'))
        self.assertEqual(date_parser("2023/11/23"), ('2023', '11', '23'))
        self.assertEqual(date_parser("2023.11.23"), ('2023', '11', '23'))
        self.assertEqual(date_parser("2023-11-23"), ('2023', '11', '23'))
        self.assertEqual(date_parser("20231123"), ('2023', '11', '23'))


if __name__ == "__main__":  # 进行单元测试
    unittest.main()
