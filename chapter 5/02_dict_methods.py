marks = {
    "Kanna" : 100,
    "Shubham" : 56,
    "Rohan" : 25,
    0: "Kanna"
 }

# print(marks.keys())
# print(marks.items())
# print(marks.values())
# marks.update({"Kanna": 99, "john": 25})
# print(marks)


print(marks.get("Kanna2")) # prints None
print(marks["Kanna2"]) # returns an error