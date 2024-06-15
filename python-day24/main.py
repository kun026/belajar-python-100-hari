# file = open("./hello.txt")
#####
# file.close()

# Read file
"""
with open("./hello.txt") as file:
    content = file.read()
    print(content)
"""

# Write file
with open("./hello.txt", mode='a') as file:
    file.write("\nHandika ganteng banget pokoknya dah.")