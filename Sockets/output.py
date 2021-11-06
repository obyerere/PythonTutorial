with open('file.txt') as file:
    content = file.read()
    print(content)

print('\n---\n')

with open('file.txt', 'a') as file: # the 'a' in the  argument means to add not overite like w
    file.write("\nHello, I'm some text inside a file.")

with open('file.txt') as file:
    content = file.read()
    print(content)

"""
# creting file with python methode write, 2 arguments w means overwrite
with open('created.txt', 'w') as file:
    file.write("Hello, I'm some text inside a file.")

# python opening file with read method
with open('file.txt') as file:
    content = file.read()
    print(content)
"""