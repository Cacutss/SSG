class HTMLNODE:
    def __init__(self,tag = None,value = None,children:list = None,**kwargs):
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

     
    def props_to_html(self):
        if self.props == {}:
            return ""
        props = ""
        for key,value in self.props.items():
            props += f" {key}={value}"
        return props
    
    def to_html(self):
        if self.value == None:
            raise ValueError("No value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNODE):
    def __init__(self,tag = None,children:list = None,**kwargs):
        super().__init__(tag,children,**kwargs)

    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("NO CHILDREN, NO PARENT")
        string = ""
        string += self.children[0].to_html()
        
    def __repr__(self):
        return f"tag = {self.tag}, children = {self.children}, props = {self.props}"