You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.
def pk(lst):
        lst.sort(key=lambda x: (x[-2]))
        return lst
lst=['abc','bcd','hjai']
i=pk(lst)
print(i)
