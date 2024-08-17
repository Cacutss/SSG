from textnode import TextNode
class HTMLNODE:
    def __init__(self,tag = None,value = None,children = None,**kwargs):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = kwargs

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == {}:
            return ""
        props = ""
        for key,value in self.props.items():
            props += f" {key}={value}"
        return props
    
    def __repr__(self):
        return f"tag = {self.tag},value = {self.value},children = {self.children}, props = {self.props}\n"

    
class LeafNode(HTMLNODE):
    def __init__(self,tag = None,value = None,**kwargs):
        super().__init__(tag,value,**kwargs)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        
        
class ParentNode(HTMLNODE):
    def __init__(self,tag = None,value= None,children:list[LeafNode] = None,**kwargs):
        super().__init__(tag,value,children,**kwargs)

    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("NO CHILDREN, NO PARENT")
        string = ""
        for child in self.children:
            string += child.to_html()
        return f"<{self.tag}{super().props_to_html()}>{string}</{self.tag}>"


    
    def __repr__(self):
        return f"tag = {self.tag},value = {self.value}, children = {self.children}, props = {self.props}"
    
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
        