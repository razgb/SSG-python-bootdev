from leafnode import LeafNode

def main():
    node = LeafNode("p", "This is a paragraph of text.")
    print(node.to_html())

    anchor = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(anchor.to_html())


if __name__ == "__main__":
    main()
