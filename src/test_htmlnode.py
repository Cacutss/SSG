import unittest

from htmlnode import HTMLNODE

from htmlnode import LeafNode

from htmlnode import ParentNode

from textnode import TextNode

from text_node_to_html import text_node_to_html_node

from md_to_textnode import split_nodes_delimiter,extract_markdown_images,extract_markdown_links

class TestHTMLNODE(unittest.TestCase):
    def test_props(self):
        node1 = HTMLNODE("h1","hello wolrd","patrick",href = "facebook.com",b = "l")
        node2 = HTMLNODE("a")
        print ("\n TEST PROPS")
        print(node1.props_to_html(),node2.props_to_html())

    def test_tohtml(self):
        node1 = LeafNode(value = "")
        node2 = LeafNode(tag = "title",value = "no",href= "youtube.com", letras= "23")
        node3 = LeafNode(value = "value")
        print("\n TEST TOHTML LEAFNODE")
        print(node1.to_html())
        print(node2.to_html())
        print(node3.to_html())

    def test_tohtmlparent(self):
        node2 = LeafNode(tag = "2",value= "3")
        node3 = ParentNode(tag= "p",children= [LeafNode(tag = "h1",value= "None")])
        node1 = ParentNode(tag = "h2",children = [node2,node3],a= "fart",b ="schizo")
        node4 = ParentNode(tag = "furry",children=[LeafNode(tag= "hello kitty",value="fire")], value= "nothing", a= "mondongo")
        print("\n TEST TOHTMLPARENT")
        print(node1.to_html())
        print(node4.to_html())

class TestTextNode(unittest.TestCase):
    def test_textnode(self):
        textnode1 = TextNode(text = "krill *yousef* joder *now*", text_type= "text")
        textnode2 = TextNode(text = "`hola`", text_type= "text")
        textnode3 = TextNode(text = "*ufa*", url="fuera" ,text_type="text")
        print("\n TEST TEXTNODE TO HTML")
        print(text_node_to_html_node(textnode1).to_html())
        print(text_node_to_html_node(textnode2).to_html())
        print(text_node_to_html_node(textnode3).to_html())
        print(split_nodes_delimiter([textnode1,textnode3],"*","bold"))
        print(split_nodes_delimiter([textnode2],"`","italic"))    

class TestRegex(unittest.TestCase):
    def test_regex(self):
        string = "![a picture of a ghost](ghostadventures.gif) and [fortnite](battlepass)"
        string2 = "![black people only](idk.com)"
        print("\n TESTING REGEX")
        print(extract_markdown_images(string))
        print(extract_markdown_links(string2))

if __name__ == "__main__":
    unittest.main()
