class HTMLNode:

    def __init__(self, tag:str | None =None, value: str | None=None, children: list[any] | None=None, props: dict | None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str = ""
        count = 0
        for key in self.props.keys():
            count += 1
            str += f' {key}="{self.props[key]}"'
        return str

    def __repr__(self):
        print(f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}")


class LeafNode(HTMLNode):

    def __init__(self, tag: str | None, value: str, props: dict | None = None):
        super().__init__(tag, value, props)
        
    
    def __repr__(self):
        print(f"LeafNode: {self.tag}, {self.value}, {self.props}")


    def to_html(self):
        if self.value == None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}"