# memberships
text1 = "hello"
text2 = "ball"

list = ["plane", "paper", "ball", "dish", "apple", "hello"]
# Using membership "in"
if (text1 in list):
    print(text1, "exist in the list")
else:
    print(text1, "does not exist in the list")

# Using membership "not in"
if (text2 not in list):
    print(text2, "does not exist in the list")
else:
    print(text2, "exist in the list")
