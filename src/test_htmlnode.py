import unittest

from textnode import TextNode

from htmlnode import HTMLNODE

from htmlnode import LeafNode

from htmlnode import ParentNode

from htmlnode import text_node_to_html_node

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
        node2 = LeafNode(tag = "2",value= "3")
        node3 = ParentNode(tag= "p",children= [LeafNode(tag = "h1",value= "None")])
        node1 = ParentNode(tag = "h2",children = [node2,node3],a= "fart",b ="schizo")
        node4 = ParentNode(tag = "furry",children=[LeafNode(tag= "hello kitty",value="fire")], value= "nothing", a= "mondongo")
        print(node1.to_html())
        print(node4.to_html())

    def test_textnode_tohtml(self):
        textnode1 = TextNode(text = "joder", text_type= "bold")
        textnode2 = TextNode(text = "", text_type= "italic", url="joder.com")
        textnode3 = TextNode(url="fuera" ,text_type="image")
        print(text_node_to_html_node(textnode1).to_html())
        print(text_node_to_html_node(textnode2).to_html())
        print(text_node_to_html_node(textnode3).to_html())

if __name__ == "__main__":
    unittest.main()
