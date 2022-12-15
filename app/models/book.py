# ~~~~~~ Book Class ~~~~~~
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Lollipops in the Rain", "A kids book about eating lollipops in the rain"),
    Book(2, "Dragons at sunrise", "A fantasy book about a child with a dragon friend"),
    Book(3, "Mai Tai Anytime", "An adult fiction book about a man who loves drinking Mai Tai's")
    ]
