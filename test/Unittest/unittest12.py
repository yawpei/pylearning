import unittest


def my_func1(a):
    if a == 1:
        return 2
    elif a == -1:
        return 3
    else:
        return 1


def my_func2(b):
    if b != "yes":
        raise ValueError("you can only say yes!")
    else:
        return True


# class TestFunc(unittest.TestCase):
#     def test_func1(self):
#         self.assertEqual(my_func1(1), 2)
#         self.assertEqual(my_func1(-1), 3)
#         for i in range(-100, 100):
#             if i == 1 or i == -1:
#                 continue
#             self.assertEqual(my_func1(i), 1)
#
#     def test_func2(self):
#         self.assertTrue(my_func2("yes"))
#         with self.assertRaises(ValueError):
#             my_func2("nononono")
#
#
# unittest.main()


class TestFunc(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(my_func1(1), 2)
        self.assertEqual(my_func1(-1), 3)
        for i in range(-100, 100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(my_func1(i), 1)

    def test_func2(self):
        self.assertTrue(my_func2("yes"))
        with self.assertRaises(ValueError):
            my_func2("nononono")


# 定义一个 suite 替换 unittext.main()
suite = unittest.TestSuite()
suite.addTest(TestFunc('test_func1'))
unittest.TextTestRunner().run(suite)
