from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def  __eq__(self, textnode2) -> bool:
        if self.text == textnode2.text and self.text_type == textnode2.text_type and self.url == textnode2.url:
            return True
        
    def  __repr__(TextNode) -> str:
        return f" TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url})"

    def text_node_to_html_node(text_node: any) -> LeafNode:
        match text_node.text_type:
            case text_node.text_type.TEXT:
                return LeafNode(None, text_node.text)
            case text_node.text_type.BOLD:
                return LeafNode("b", text_node.text)
            case text_node.text_type.ITALIC:
                return LeafNode("i", text_node.text)
            case text_node.text_type.CODE:
                return LeafNode("code", text_node.text)
            case text_node.text_type.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case text_node.text_type.IMAGE:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception("Conversion error")