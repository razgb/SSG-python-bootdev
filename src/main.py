from leafnode import LeafNode
from parentnode import ParentNode

def main():
    parent = ParentNode("p", [
        LeafNode("i", "Once"),
        LeafNode(None, "upon a"),
        LeafNode("b", "time"),
        LeafNode(None, ".")
    ])

    print(parent.to_html())


if __name__ == "__main__":
    main()
