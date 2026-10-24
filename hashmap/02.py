# initailize hashmap manually 1 by 1
Hashmap = {}

Hashmap["apple"]=10
Hashmap["banana"]=20

# Dict comprehension
import math
Hashmap2 = {i : int(math.pow(i,2)) for i in range(5)} # key doesnt always has to be strings 
print(Hashmap2)

# we can also save lists into hashmap
Hashmap3 = {"apple":["japan","newzeland"], "banana":["taiwan","malaysia"]}
print(Hashmap3) # {'apple': ['japan', 'newzeland'], 'banana': ['taiwan', 'malaysia']}

# add elements_method_1
Hashmap3["mango"] = ["thailand","mango"]
print(Hashmap3) # {'apple': ['japan', 'newzeland'], 'banana': ['taiwan', 'malaysia'], 'mango': ['thailand', 'mango']}

# add elements_method_2 (when the key is ady exist)
Hashmap3["mango"].append("taiwan")
print(Hashmap3) # {'apple': ['japan', 'newzeland'], 'banana': ['taiwan', 'malaysia'], 'mango': ['thailand', 'mango', 'taiwan']}
print(Hashmap3.values()) # dict_values([['japan', 'newzeland'], ['taiwan', 'malaysia'], ['thailand', 'mango', 'taiwan']])
print (list(Hashmap3.values())) # [['japan', 'newzeland'], ['taiwan', 'malaysia'], ['thailand', 'mango', 'taiwan']]