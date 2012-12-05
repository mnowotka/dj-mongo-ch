# -*- coding: utf-8 -*-
# Author Karol Sikora <karol.sikora@laboratorium.ee>, (c) 2012

from django.utils import unittest
from django.core.cache import get_cache
import time
import random

class CacheTest(unittest.TestCase):

    def setUp(self):
        self.cache = get_cache('default')

    def test_add_get(self):
        self.cache.add('wfsafw', 'eavtrtWRXW')
        self.assertEqual(self.cache.get('wfsafw'), 'eavtrtWRXW')

    def test_has_key(self):
        self.cache.add('RTAVAREXAERCET43w', 'reaaaaaaexr')
        self.assertTrue(self.cache.has_key('RTAVAREXAERCET43w'))

    def test_clear(self):
        self.cache.add('adwadwad', 'turtxwewa')
        self.cache.clear()
        self.assertIsNone(self.cache.get('adwadwad'))

#    def test_timeout(self):
#        self.cache.add('sefgragrsaf', 'ryjtrsdwada')
#        time.sleep(2)#depends on 1s timeout in settings!
#        self.assertIsNone(self.cache.get('sefgragrsaf'))

    def test_get_many(self):
        self.cache.add('wfsafwa', 'eavtrtWRXWa')
        res = self.cache.get_many(['wfsafwa'])
        self.assertEqual('eavtrtWRXWa', res['wfsafwa'])


