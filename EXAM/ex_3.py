def cookbook(*info):
    book = {}
    for name, cuisine, ingredients in info:
        if cuisine not in book:
            book[cuisine] = []
        book[cuisine].append((name, ingredients))

    for cuisine in book:
        book[cuisine] = sorted(book[cuisine], key=lambda x: x[0])

    sorted_book = dict(sorted(book.items(), key=lambda x: (-len(x[1]), x[0])))

    msg = ''
    for k, v in sorted_book.items():
        msg += f"{k} cuisine contains {len(v)} recipes:\n"
        for el in v:
            msg += f"  * {el[0]} -> Ingredients: {', '.join(el[1])}\n"

    return msg


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))






