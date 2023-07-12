#Question 2
lst1 = ["Tom", "", "Dick", "Harry", "", "Here", "", "There", "", "Everywhere"]
def clean_list(lst1):
    i = 0
    newlist = []
    while i < len(lst1):
        if lst1[i] != "":
            newlist.append(lst1[i])
        i += 1
    return print(newlist)
print(lst1)
clean_list(lst1)