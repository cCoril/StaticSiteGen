class HTMLNode:

    def __init__(self, tag:str | None =None, value: str | None=None, children: list[any] | None=None, props: dict | None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        result = ""
        if self.props == None:
            return result
        for key in self.props.keys():
            result += f' {key}="{self.props[key]}"'
        return result

    def __repr__(self):
        print(f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}")


class LeafNode(HTMLNode):

    def __init__(self, tag: str | None, value: str, props: dict | None = None):
        super().__init__(tag, value, None, props)
        
    
    def __repr__(self):
        print(f"LeafNode: {self.tag}, {self.value}, {self.props}")


    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    
    def __init__(self, tag,  children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children == [] or self.children is None:
            raise ValueError("ParentNode must have children")
        result = ""
        for child in self.children:
            result += child.to_html()
        if self.props is None:
            return f'<{self.tag}>{result}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'
        
