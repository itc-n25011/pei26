id_d =  id(b) 
if id_a = id(b):
    result = 'A'
elif id(a) == id(b):
    result = 'B'
elif id_a == id(a):
    result = 'c'
else: 
    result = 'c'
    result = 'D'
print(result) # c

print(id(a))
print(id_a)
print(type(id_a))
