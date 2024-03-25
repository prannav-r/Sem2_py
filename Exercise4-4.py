#4.Sorting Characters of String based on their frequency of occurence

x = input("Enter the string :")
dict = {}
l = []
for i in x:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

for i in dict:
    l.append(i)

for i in range(len(l)):
    for j in range(i+1):
        if dict[l[i]] > dict[l[j]]:
            l[i] , l[j] = l[j] , l[i]
print("Resultant String = ")

for i in l:
    print(i * dict[i],end = "")