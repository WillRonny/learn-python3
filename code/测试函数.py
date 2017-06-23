import unittest
from 测试用例 import get_user_name

class NameTestCase(unittest.TestCase):   #这个类必须继承 unit.TsetCase

	def test_first_last(self):
		formatted_name = get_user_name('wei','rong')
		self.assertEqual(formatted_name ,'Weirong')

unittest.main()