import unittest
import linked_list

"""Tests for linked_list.py"""


class TestLinky(unittest.TestCase):

    def testChunk():
        linky = Linkedlist()
        linky.linked_list.insert(1)
        linky.linked_list.insert(2)
        linky.linked_list.insert(3)
        linky.linked_list.insert(4)
        self.assertEqual([4, 3, 2, 1], linky.linked_list.print_me())
        print(linky.size())
        linky.pop()
        print(linky.print_me())
        print(linky.size())
        print(linky.search(3))
        print(linky.search(4))
        linky.remove(2)
        print(linky.print_me())

    def testPop():
        pass

    def testSize():
        pass

    def testSearch():
        pass

    def testRemove():
        pass

    def testPrint_me():
        pass

    # def testMessageShort(self):
    #     test_s = "a3th8go"
    #     self.assertEqual(test_s, myclient.start_client(test_s))

    # def testMessageLong(self):
    #     test_L = "asdfghjklasdfghjklsdfghjklsdfg32lsdfghjkldfghjk"
    #     self.assertEqual(test_L, myclient.start_client(test_L))

    # def testMessageExact(self):
    #     test_e = "12345678909876543212345678909876"
    #     self.assertEqual(test_e, myclient.start_client(test_e))

if __name__ == "__main__":
    unittest.main()