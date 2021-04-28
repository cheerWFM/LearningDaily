#!/usr/bin/env python 
# coding:utf-8
import unittest
from name import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """name.py"""
    def test_first_last_name(self):
        """能够处理向Janis Joplin这样到姓名吗？"""
        formatted_name = get_formatted_name("janis",'joplin')
        self.assertEqual(formatted_name,"Janis Joplin")
    def test_first_last_middle_name(self):
        """测试名字包含中间名"""
        formatted_name = get_formatted_name("hello", "wfm","hu")
        self.assertEqual(formatted_name,"Hello Hu Wfm")

unittest.main()