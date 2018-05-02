"""
Bubble Sort Algorithm
"""
def bubbleSort(List):
	Flag=True
	while Flag:
		Flag=False
		i=0;
		while i<len(List)-1:
			if(List[i]>List[i+1]):
				temp=List[i]
				List[i]=List[i+1]
				List[i+1]=temp
				Flag=True
			i=i+1
List=[12,5,7,18,11,6,12,4,17,1]
bubbleSort(List)
print List