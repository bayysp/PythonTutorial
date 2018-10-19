listData = [1,2,3] #this is an array , but it can be a list, lets we test in example below

listData.append(5) #put a data into listData
print (listData) # it will show 1,2,3,5

#list can also have a value with different data type, fox example
listData.append("hello") #put a string hello into dataList
print (listData) # it will show 1,2,3,5,hello

#you can input list into list, , fox example
listData.append([6,7,"world"])
print (listData) #it will show 1,2,3,5,hello,[6,7,world] <- this is an antoher list inside dataList

#if you output an index with that array which is you apped before, it will be like this
print (listData[5]) #the output is 6,7,world

#if you want to delete a data in list, you can us e function pop() after listData, example
listData.pop() # this will delete the last index on list
print (listData) # it will show 1,2,3,5,hello

#if you want to choose the index that you want to delete, put an index into brackets
listData.pop(2) # this will delete index number 2 -> value 3
print (listData) # it will show 1,2,5,hello

#if you want to change the position the index of list, its very simple, you can do it like this
listData[0] , listData[2] = listData[2] , listData[0] #change posisition of value 1 with 5 (index 0 with index 2)
print (listData) #it will show 5,2,1,hello