#PART 1
input = open("input_1.txt", "rt", -1)

lines = input.readlines()

list_1 = []
list_2 = []

for line in lines:
    a, b = line.split()
    a = int(a)
    b = int(b)
    list_1.append(a)
    list_2.append(b)

n = len(list_1)

for i in range(n):
    swapped = False
    for k in range(0, n-i-1):
        if list_1[k] > list_1[k+1]:
                list_1[k], list_1[k+1] = list_1[k+1], list_1[k]
                swapped = True
    if (swapped == False):
         break

l = len(list_2)

for i in range(l):
    swapped = False
    for k in range(0, l-i-1):
        if list_2[k] > list_2[k+1]:
                list_2[k], list_2[k+1] = list_2[k+1], list_2[k]
                swapped = True
    if (swapped == False):
         break
    
distances = []

for i in range(len(list_1)):
     diff = abs(list_1[i] - list_2[i])
     distances.append(diff)

total_sum = sum(distances)
print("Total sum of distances is ", total_sum)
#PART 2

all_scores = []

for i in range(n):
    el = list_1[i]
    number = list_2.count(el)
    similarity_score = el * number
    all_scores.append(similarity_score)

total_score = sum(all_scores)

print("Total similarity score is ", total_score)
    