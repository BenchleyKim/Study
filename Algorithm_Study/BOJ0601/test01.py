
str1 = "12234"
num_dict = {}
base_dict = num_dict
for n in str1 :
    base_dict[n] = {}
    print(base_dict)
    base_dict = base_dict[n]
print(num_dict)
