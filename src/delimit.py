from textnode import TextNode, TextType
from enum import Enum

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
            if node.text_type == TextType.TEXT:
                if delimiter not in node.text:
                    raise Exception("Markdown error: Delimiter not found in text")
                temp_list = node.text.split(delimiter)
                for i in range(0, len(temp_list)):
                    if i % 2 == 0:
                         new_list.append(TextNode(temp_list[i], TextType.TEXT))
                    else:
                        new_list.append(TextNode(temp_list[i], text_type))
            else:
                 new_list.append(node)
    return new_list
                    

                
