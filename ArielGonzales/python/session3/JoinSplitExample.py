# function replace(s, old, new) that replaces all occurrences of old with new in a string s
def replace(text, toChange, changed):
    words = text.split(toChange)
    return changed.join(words)


s = "I love spom! Spom is my favorite food.Spom, spom, yum!"
print(replace("Missisiippi", "i", "I"))
print(replace(s, "om", "am"))
print(replace(s, "o", "a"))
