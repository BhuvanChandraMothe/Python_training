# Question-2: 
# Given:D1 = {'ok': 1, 'nok': 2}
# D2 = {'ok': 2, 'new':3 }
# Create below:
# # union of keys, #value does not matter
# D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
# # intersection of keys, #value does not matter
# D_INTERSECTION = {'ok': 1}
# D1- D2 = {'nok': 2 }
# #values are added for same keys
# D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }

D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
D_UNION = D1 | D2
print(f"{D_UNION=}")

D_INTERSECTION={}
for key in D1:
    if key in D2:
        D_INTERSECTION[key] = D1[key] 
print(f"{D_INTERSECTION=}")

D1D2 ={}
for key in D1:
    if key not in D2:
        D1D2[key] = D1[key] 
print(f"D1-D2={D1D2}")

D_MERGE ={}
for key in D1:
    if key in D2:
        D_MERGE[key] = D1[key] + D2[key]
    else:
        D_MERGE[key] = D1[key]
for key in D2:
        if key not in D_MERGE:
             D_MERGE[key] = D2[key]
print(F"{D_MERGE=}")