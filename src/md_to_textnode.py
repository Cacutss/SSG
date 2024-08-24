from textnode import TextNode

import re

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    resulting_nodes = []
    old_nodes_copy = old_nodes[:]
    for i in range(0,len(old_nodes_copy)):
        if old_nodes_copy[i].text_type == "text":
            if old_nodes_copy[i].text.count(delimiter)%2 > 0:
                raise Exception("Invalid markdown syntax")
            delimited = old_nodes_copy[i].text.split(delimiter)
            for j in range(0,len(delimited)):
                if delimited[j] == "":
                    continue
                if j %2 == 0:
                    resulting_nodes.append(TextNode(delimited[j],"text"))
                else:
                    resulting_nodes.append(TextNode(delimited[j],text_type))
        else:  
            resulting_nodes.append(old_nodes_copy[i])
    return resulting_nodes

def extract_markdown_images(text):
    return re.findall(r"(?<=!)\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)