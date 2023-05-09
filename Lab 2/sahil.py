with open('report.txt', 'r') as file:
    x = file.read().split()
my_dict = {}
count_list = []
for word in x:
    num = x.count(word)
    if num not in my_dict:
        my_dict[num] = []

for word in x:
    count = x.count(word)
    if count not in count_list:
        count_list.append(count)
count_list.reverse()

for word in x:
    num = x.count(word)
    if word not in my_dict[num]:
        my_dict[num].append(word)

for num in count_list:
    print(num, ':', my_dict[num])
