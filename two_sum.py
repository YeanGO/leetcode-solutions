nums = list(map(int, input().split()))
target = 9
new_nums = sorted(nums)
pairs = []
for i in range(len(new_nums)):
    for j in range(i+1,len(new_nums)):
        current_sum = new_nums[i] + new_nums[j]
        if (current_sum == target):
            pairs.append(i)
            pairs.append(j)
            print(pairs)