from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text)
        self.url = url

    def  __eq__(textnode1, textnode2):
        if textnode1.text == textnode2.text and textnode1.text_type == textnode2.text_type and textnode1.ur == textnode2.url:
            return True
    def  __repr__(TextNode):
        return f" TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url})"



