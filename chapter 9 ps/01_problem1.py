f = open("p oem.txt")
content = f.read()
if("Twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word Twinkle is not present in the content")
f.close()