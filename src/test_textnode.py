import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        node3 = TextNode("this is text","bold")
        node4 = TextNode("this is text","italic")
        self.assertNotEqual(node3,node4)

    def test_url(self):
        node1 = TextNode("n","n")
        node2 = TextNode("","","url")
        self.assertIsNone(node1.url)
        self.assertIsNotNone(node2.url)

if __name__ == "__main__":
    unittest.main()
