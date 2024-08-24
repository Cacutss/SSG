from textnode import TextNode
from htmlnode import LeafNode
def text_node_to_html_node(text_node:TextNode):
    match(text_node.text_type):
        case "bold":
            return LeafNode(tag = "b",value = text_node.text)
        case "text":
            return LeafNode(value = text_node.text)
        case "italic":
            return LeafNode(tag = "i",value = text_node.text)
        case "code":
            return LeafNode(tag= "code",value = text_node.text)
        case "link":
            return LeafNode(tag= "a",value = text_node.text,href = text_node.url)
        case "image":
            return LeafNode(tag = "img",value = "",src = text_node.url,alt = text_node.text)
        case _:
            raise Exception("Unsupported type")
