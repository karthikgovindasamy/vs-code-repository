"""
Insertion Sort Algorithm
"""
def InsertionSort(List):
    Flagposition=0
    while Flagposition<len(List)-1:
        if(List[Flagposition]>List[Flagposition+1]):
            i=Flagposition;
            while i>=0:
                if(List[i]>List[i+1]):
                    temp=List[i+1]
                    List[i+1]=List[i]
                    List[i]=temp
                    i=i-1
                else:
                    i=-1
            
        Flagposition=Flagposition+1
List=[12,5,7,18,11,6,4,17,1]
InsertionSort(List)
print List