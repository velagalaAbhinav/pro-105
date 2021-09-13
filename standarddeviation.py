import csv 
import math
with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]
#finding mean
def mean(data):
    m = len(data)
    total = 0 
    for x in data:
        total += int(x)
    mean = total/m
    return mean

squaredlist = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredlist.append(a)

sum = 0 
for i in squaredlist:
    sum =  sum + i

result = sum/(len(data)-1)

standarddeviation = math.sqrt(result)
print(standarddeviation) 