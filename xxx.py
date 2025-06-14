def greet(name=None):
    if name == None:
        return "hello Stranger"

    return f"hello {name}"

print("Hey")
print(greet('Evaan'))