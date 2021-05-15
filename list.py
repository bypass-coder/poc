# var = ['Chirag','Aakarsh','Tejas',30,20,20,True,'Chirag']


# for var_ele in var:
#     print(str(var_ele) + " " + str(type(var_ele)))


# for i in range(1,len(var)):
#     print(var[i])
# var[0] = "Rahul"

# var = list(('Chirag','Aakarsh','Tejas',30,20,20,True,'Chirag'))

# var.append('test')

# var.insert(5,"test1")

# var1 = "chirag"

# var.extend(var1)

# var.remove("Chirag")

# del var

# var.clear()

# print(var)


var = list(('Chirag','Aakarsh','Tejas'))

# var1 = []

# for var_ele in var:
#     if var_ele not in var1:
#         var1.append(var_ele)

# [var1.append(var_ele) for var_ele in var if var_ele not in var1]
# data = var1.sort()
# print(var1)

# data = var
data = var.copy()
var.pop()

print(hex(id(var)))
print(hex(id(data)))

print(data)
print(var)

