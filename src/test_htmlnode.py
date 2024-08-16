import unittest

from htmlnode import HTMLNODE

from htmlnode import LeafNode

from htmlnode import ParentNode

class TestHTMLNODE(unittest.TestCase):
    def test_props(self):
        node1 = HTMLNODE("h1","hello wolrd","patrick",a= "fart",b = "l")
        node2 = HTMLNODE("a")
        print(node1.props_to_html(),node2.props_to_html())

    def test_tohtml(self):
        node1 = LeafNode(value = "")
        node2 = LeafNode(tag = "farting",value = "a",a = "n")
        node3 = LeafNode(value = "value")
        print(node1.to_html())
        print(node2.to_html())
        print(node3.to_html())

    def test_tohtmlparent(self):
        node2 = LeafNode("2","3")
        node1 = ParentNode(tag = "h2",a= "fart",b ="schizo")
        print(node1)

if __name__ == "__main__":
    unittest.main()
