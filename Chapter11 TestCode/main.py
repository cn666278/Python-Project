import unittest
from name_function import get_formatted_name

# print("Enter 'q' at any time to quit. ")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("\nPlease give me a last name: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print("\n\tNearly formatted name: " + formatted_name + ".")

# -----------------------------------------------------------------
# 单元测试 和 测试用例
# <NameTestCase> inherit <unittest.TestCase>
class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够处理像 Monkey D Luffey 这样的名字吗？"""
        formatted_name = get_formatted_name('Monkey', 'Luffey')
        self.assertEqual(formatted_name, 'Monkey D Luffey')

unittest.main()