def match_word(words):
    ctr= 0
    list = []
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            ctr += 1
            list.append(i)
    print("List of words with first and last letter the same:")
    return ctr
count = match_word(["aba", "ghg", "wrgfh"])
print(count)

