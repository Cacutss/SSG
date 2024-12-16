from textnode import *

from htmlnode import *

from text_node_to_html import text_node_to_html_node

import re

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    resulting_nodes = []
    old_nodes_copy = old_nodes[:]
    for i in range(0,len(old_nodes_copy)):
        #if the old is of type text, do the whole operation, otherwise just append
        if old_nodes_copy[i].text_type == "text":
            #if the delimiters aren't matched by an end of a delimiter, then raise exception
            if old_nodes_copy[i].text.count(delimiter)%2 > 0:
                raise Exception("Invalid markdown syntax")
            #separate string based on delimiter
            delimited = old_nodes_copy[i].text.split(delimiter)
            for j in range(0,len(delimited)):
                #for white space, skip
                if delimited[j] == "":
                    continue
                #for even index append as text, else append as specified type
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

def split_nodes_images(old_nodes : list[TextNode]):
    old_nodes_copy = old_nodes[:]
    resulting_nodes = []
    if old_nodes_copy == []:
        return resulting_nodes
    elif old_nodes_copy[0].text_type == "text":
        last_call = old_nodes_copy[0].text
        lst = extract_markdown_images(old_nodes_copy[0].text)
        if not lst == []:
            for i in range(0,len(lst)):
                splitted = last_call.split(f"![{lst[i][0]}]({lst[i][1]})",1)
                if splitted == old_nodes_copy[0].text:
                    resulting_nodes.append(old_nodes_copy[0])
                    return resulting_nodes
                if not splitted[0] == "":
                    resulting_nodes.append(TextNode(text=splitted[0],text_type="text"))
                resulting_nodes.append(TextNode(text=lst[i][0],text_type="image",url=lst[i][1]))
                if i == len(lst)-1 and not splitted[1] == "":
                    resulting_nodes.append(TextNode(text=splitted[1],text_type="text"))
                else:
                    last_call = splitted[1]
        else:
            resulting_nodes.append(old_nodes_copy[0])
    else:
        resulting_nodes.append(old_nodes_copy[0])
    resulting_nodes.extend(split_nodes_images(old_nodes_copy[1:]))
    return resulting_nodes

def split_nodes_links(old_nodes : list[TextNode]):
    old_nodes_copy = old_nodes[:]
    resulting_nodes = []
    if old_nodes_copy == []:
        return resulting_nodes
    elif old_nodes_copy[0].text_type == "text":
        last_call = old_nodes_copy[0].text
        lst = extract_markdown_links(old_nodes_copy[0].text)
        if not lst == []:
            for i in range(0,len(lst)):
                splitted = last_call.split(f"[{lst[i][0]}]({lst[i][1]})",1)
    
                if splitted[0] == last_call:
                    resulting_nodes.append(old_nodes_copy[0])
                    return resulting_nodes
                if not splitted[0] == "":
                    resulting_nodes.append(TextNode(text=splitted[0],text_type="text"))
                resulting_nodes.append(TextNode(text=lst[i][0],text_type="link",url=lst[i][1]))
                if i == len(lst)-1 and not splitted[1] == "":
                    resulting_nodes.append(TextNode(text=splitted[1],text_type="text"))
                else:
                    last_call = splitted[1]
        else:
            resulting_nodes.append(old_nodes_copy[0])
    else:
        resulting_nodes.append(old_nodes_copy[0])
    resulting_nodes.extend(split_nodes_links(old_nodes_copy[1:]))
    return resulting_nodes

def text_to_textnodes(text):
    result = split_nodes_delimiter([TextNode(text,text_type="text")],"**","bold")
    result1 = split_nodes_delimiter(result,"*","italic")
    result2 = split_nodes_delimiter(result1,"`","code")
    result3 = split_nodes_images(result2)
    result4 = split_nodes_links(result3)
    return result4

def markdown_to_blocks(markdown : list):
    result = []
    current = ""
    for line in markdown:
        if line == "\n":
            result.append(current)
            current = ""
            continue
        current += line.strip()
    result.append(current)
    return result

def blocks_to_type_blocks(block : str):
    types = {">" : "blockquote",
            "#" : "h",
            "```" : "code",
            "* " : "ul",
            "- " : "ul",
            "1." : "ol"}
    string = ''
    count = 0
    for i in range(0,len(block)):
        string += block[i]
        if count > 0 and block[i] == " ":
            return f"h{count}"
        elif "#" == string[i]:
            count += 1
        elif string in types.keys():
            return types[string]
        elif i > 3:
            return "p"

def split_block_type(block : str,type : str) -> str:
    result = block
    if type == "ul":
        result = block.split("* ")
        if len(result) == 1:
            result = block.split("- ")
        return result
    elif type == "ol":
        i = 1
        while i >= 1:
            if f"{i}." in result:
                result = result.replace(f"{i}. ","* ")
                i += 1
            else:
                i = 0
        return result.split("* ")
    elif type == "blockquote":
        result = block.split("> ")
        return result[1]
    elif type == "code":
        result = block.split("```")
        return result[1]
    return result
   

def block_to_html_node(block):
    node = ParentNode()
    type = blocks_to_type_blocks(block)
    node.tag = type
    if type == "ul" or type == "ol":
        ulist = split_block_type(block,type)
        for i in range(0,len(ulist)):
            if ulist[i] == "":
                continue
            nodes = text_to_textnodes(ulist[i])
            res = ParentNode(tag="li")
            for j in range(0,len(nodes)):
                res.children.append(text_node_to_html_node(nodes[j]))
            node.children.append(res)
    else:
        if "h" in type:
            textnodes = text_to_textnodes(block[(int(type[1])+1):])
        else:
            split = split_block_type(block,type)
            textnodes = text_to_textnodes(split)
        for textnode in textnodes:
            node.children.append(text_node_to_html_node(textnode))
    return node

def markdown_to_html_node(markdown):
    string = open(markdown,"r")
    blocks = markdown_to_blocks(string)
    result = ParentNode(tag="div")
    for i in range(0,len(blocks)):
        result.children.append(block_to_html_node(blocks[i]))
    string.close()
    return result