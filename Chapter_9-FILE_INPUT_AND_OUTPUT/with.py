f = open("file.txt")
print(f.read())
f.close()

# the same statement you can write using with statement
with open("file.txt") as f:
    print(f.read())

    # you dont have to explicitly close the file