# Function containing both args and kwargs
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any, {}, ?".format(kind))

    for arg in arguments:
        print(arg)

    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

# Driver program to test above function
cheeseshop("Burger", "It's very funny, sir.",
           "It's really very, VERY funny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")