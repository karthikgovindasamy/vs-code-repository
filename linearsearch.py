def linearSearch(List,item):
    found=False
    position=0
    
    while position<len(List) and not found:
        if List[position]==item:
            found=True
            return 'Data {} found at position {}'.format(item,position)
        else:
            position=position+1
    if(found==False):
        return 'Data {} is not found in the list'.format(item)

List=[75, 85, 119, 37, 149, 50, 37, 51, 103, 110, 107, 144, 153, 44, 167, 197, 18, 165, 25, 153, 100, 41, 73, 111, 48, 88, 101, 35, 95, 30, 26, 42, 97, 181, 192, 119, 19, 23, 78, 62, 51, 151, 88, 84, 120, 88, 180, 20, 80, 35, 99, 107, 162, 117, 87, 52, 28, 61, 6, 2, 82, 197, 67, 151, 118, 189, 167, 70, 7, 200, 143, 94, 134, 132, 188, 16, 5, 47, 61, 174, 1, 42, 177, 63, 154, 59, 181, 19, 197, 140, 179, 200, 42, 93, 36, 162, 78, 164, 104, 154]

print linearSearch(List,23)
print linearSearch(List,48)
print linearSearch(List,73)
print linearSearch(List,34)
print linearSearch(List,9)
print linearSearch(List,89)
print linearSearch(List,13)
print linearSearch(List,54)
print linearSearch(List,99)
