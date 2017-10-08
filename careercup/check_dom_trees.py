'''
Created on 7 de out de 2017

@author: fernando
'''


'''
Check if two DOM Trees have the same text.
e.g. <html><p>hello</p></html>, 
<html><p><b>h</b>ello</p></html> should be the same text

DOMNode class definition (string tag, string text, bool isText, vector<DOMNode*> children)


* Fernando’s comments: I have a question here: is “text” only the text or the whole inner HTML?
Because if it’s just the text (aka. “ello” in the second tree sample), then we don’t know whether the node’s or children’s text comes first. For instance, the two trees below are different, but an algorithm that compares them may think they’re the same.

<html>
    <p>
        <b>h</b>
        ello
    </p>
</html>

<html>
    <p>        
        ello
        <b>h</b>
    </p>
</html>

Even worse, we may not be able to detect the following trees have the same text:

<html>
    <p>
        <b>h</b>
        ello
    </p>
</html>

<html>
    <p>        
        h
        <b>ello</b>
    </p>
</html>

If DOMNode’s text attribute contains the HTML, then we can try to parse it and figure out if we start with the text or with children (but I don’t think it does...).  




Otherwise we can only have an algorithm that return true if the trees MAY be similar by building a graph of 
characters perhaps, then comparing the graphs from the two DOMTrees. However, this solution is a bit too complex...
Below is a part of a solution (NOT TESTED SO FAR!!):
'''

class CharNode:
    def __init__(self, char):
        self.char = char
        self.next_nodes = []

    

def getCharListFromString(string):
    first_node =  last_node = None
    for i in len(string):
        curr_node = CharNode(string[i])
        if first_node is None:
            first_node = curr_node
        if last_node != None:
            last_node.next_nodes.append(curr_node)

        last_node = curr_node
        
    return first_node, last_node


def getDomTreeText(node):
    result = result_last = text_char_list = None
    if node.isText:
        text_char_list, text_char_last_node = getCharListFromString (node.text)

    children_char_list = last_node = None
    for child in node.children:
        curr_node, curr_last_node = getDomTreeText(child)
        if children_char_list is None:
            children_char_list = curr_node
        if last_node != None:
            last_node.next_nodes.append(curr_node)
        
        if curr_node != None:
            last_node = curr_last_node
    
    if text_char_list != None:
        result = text_char_list
        if children_char_list != None:
            text_char_last_node.next_nodes.append(children_char_list)
            result_last = last_node
        else:
            result_last = text_char_last_node
        
    
    if last_node != None:
        if text_char_list != None:
            last_node.next_nodes.append(text_char_list)
        else:
            result = children_char_list
            result_last = last_node

    return result, result_last
