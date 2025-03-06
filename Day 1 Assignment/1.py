# input_str = "Hello world and Hello Earth" 
# print frequency of each words 

input_str = "Hello world and Hello Earth"
c = {}
for word in input_str.split():
    if word not in c:
        c[word] = 1
    else:
        c[word] += 1
print(c)
