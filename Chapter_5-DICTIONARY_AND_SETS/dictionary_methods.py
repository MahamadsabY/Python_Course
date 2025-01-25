marks = {
    "mahamad" : 56,
    "Mubbu" : 88,
    "Shaju" : 100
}

print(marks, type(marks))

print(marks["Mubbu"])

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"mahamad" : 100})

marks.update({"mahamadsab" : 99})

print(marks)

print(marks.get("mahamadsab5"))  # Prints None

print(marks("mahamad2"))     # Gives an error

