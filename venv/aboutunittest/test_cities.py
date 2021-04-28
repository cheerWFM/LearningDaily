#!/usr/bin/env python 
# coding:utf-8
import unittest
from city_function import get_city

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_name = get_city("nanning","china")
        self.assertEqual(city_country_name,"nanning,china")
    def test_city_country_pupulation(self):
        city_country_name = get_city("nanjing","china","908978")
        self.assertEqual(city_country_name,"nanjing,china-population 908978")
unittest.main()
