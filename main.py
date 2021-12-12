# importing list in different file for usability
from list1 import plates_list

# importing counter for unique elements
from collections import Counter

# checking input
search = str(input("Search for your plate: "))

if search.upper() in plates_list:
    print("Yup, your plate is here :)")
else:
    print("Nah, it's not here ):")

# get num of unique elements
list1 = Counter(plates_list).keys()
print("Unique plates counter:", len(list1))

# sum of numbers in input
res_str = search[2:-2]
res = sum(map(int, (str(res_str))))
print("Sum of numbers equals to " + str(res))
