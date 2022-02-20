#intersection of 2 arrays
def intersect(x1,x2):
    point=[]
    for i in range(len(x1)):
        for j in range(len(x2)):
            if x1[i]==x2[j]:
                if x1[i] not in point:
                    point.append(x1[i])
                    print(point)
    return (point)
#drive
X1=[1,3,5,7]
X2=[4,7,9,12,5]
print("intersection points are:",intersect(X1,X2))
