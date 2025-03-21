class TextNode:
    def __init__(self,text = None,text_type = None,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(node1,node2):
        if node1.text == node2.text and node1.text_type == node2.text_type and node1.url == node2.url:
            return True
        return False
    
    def __repr__(node):
        return f"TextNode({node.text},{node.text_type},{node.url})"
    
