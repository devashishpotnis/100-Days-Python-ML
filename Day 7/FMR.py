from functools import reduce

Data=[7,10,15,12,4,6,9,8,12,16]
print("Inpur Data :",Data)

FData= list(filter(lambda no:(no%2==0),Data))
print("Filter Output :",FData)

MData=list(map(lambda no : no+1,FData))
print("Map Output :",MData)

RData=reduce(lambda a,b :a+b,MData)
print("Reduced Outpu :",RData)