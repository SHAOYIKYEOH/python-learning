# initailize hashmap manually 1 by 1
Hashmap = {}

Hashmap["apple"]=10
Hashmap["banana"]=20

# Dict comprehension
import math
Hashmap2 = {i : int(math.pow(i,2)) for i in range(5)} # key doesnt always has to be strings 
print(Hashmap2)