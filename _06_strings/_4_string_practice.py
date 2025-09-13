# count 'o' in srt and its indexes

greeting = 'Hello, World!'

count_o = 0
indexes = []

for i in range(len(greeting)):
    if greeting[i] == 'o':
         count_o += 1
         indexes.append(i)

print(count_o)
print(indexes)
