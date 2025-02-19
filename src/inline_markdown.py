from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            node_list.append(node)
            continue
        
        sections = node.text.split(delimiter)
        
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        split_nodes = []
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        node_list.extend(split_nodes)

    return node_list