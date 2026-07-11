import re
from textnode import TextNode, TextType

def extract_markdown_images(text: str) -> list[tuple]:
     results = re.findall(r"!\[([^\[\]]+)\]\(([^\(\)]+)\)", text)
     return results
     

def extract_markdown_links(text: str) -> list[tuple]:
     results = re.findall(r"\[([^\[\]]+)\]\(([^\(\)]+)\)", text)
     return results

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
     pass

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
     new_list = []
     for old_node in old_nodes:
          link_list = extract_markdown_links(old_node.text)
          split_nodes = re.split(r"\[[^\[\]]+\]\([^\(\)]+\)", old_node.text)
          if split_nodes[len(split_nodes) - 1] == "":
               split_nodes.pop()
          i = 0
          while i < len(link_list):
               new_list.append(TextNode(split_nodes[i], TextType.TEXT))
               new_list.append(TextNode(link_list[i][0], TextType.LINK, link_list[i][1]))
               i += 1
          while i < len(split_nodes):
               new_list.append(TextNode(split_nodes[i], TextType.TEXT))
               i += 1  
     return new_list
                    