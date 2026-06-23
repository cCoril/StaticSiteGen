from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def  __eq__(textnode2):
        if TextNode.text == textnode2.text and TextNode.text_type == textnode2.text_type and TextNode.url == textnode2.url:
            return True
    def  __repr__(TextNode):
        return f" TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url})"



