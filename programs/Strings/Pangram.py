# First Method
def checkPangram(string):
    li = []
    for i in range(26):
        li.append(False)

    for c in string.lower():
        if not c == " ":
            li[ord(c) - ord('a')] = True

    for ch in li:
        if ch == False:
            return False
    return True
