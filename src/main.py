# from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    test_props = {
        "href": "example.com",
        "target": "_blank",
        "fake_attr": "fake_value"
    }

    html_node = HTMLNode("a", "testing text", None, test_props)
    print(html_node.props_to_html())



if __name__ == "__main__":
    main()
