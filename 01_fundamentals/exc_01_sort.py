# Create a function that takes a dictionary of ANDi names and returns
# a list of their names in alphabetical order. 

names_dict = dict(andi1 = 'Yasir', andi2 = 'John', andi3 = 'Priya', andi4 = 'Zeid')
def sortAlphabetically(names_dic):
    namesListUnsorted = list(names_dic.values())
    namesListSorted = sorted(namesListUnsorted)
    return namesListSorted

result = sortAlphabetically(names_dict)
print('Sorted names list:')
for name in result:
    print(name)