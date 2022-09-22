import random
origin=[0,0,0]
for i in range(0,3):
    origin[i]=random.randint(1,9)
    for j in range(0,i):
        if origin[i] == origin[j]:
            origin[i]=random.randint(1,9)

    print(origin[i])