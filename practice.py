# # task 1
# num = int(input())
# for i in range(1, num+1):
#     if i % 3 == 0 or i % 5 == 0:
#         if not (i % 3 == 0 and i % 5 == 0):
#             print(i, end = ' ') 

# # task 2
# n = int(input())
# string = str(n)
# lens = len(string)
# total = 0

# for i in string:
#     total += int(i) ** lens
# print(total == n)

# task 3

nums = input()

total = ""
count = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        count+= 1
    else:
        total += nums[i-1] + str(count)
        count = 1
total += nums[-1] + str(count)
print(total)

# task 4

ns = input()
ns = ns.lower()
ns = ns.replace(" ", "")
if ns == ns[::-1]: 
    print(True)
else:
    print(False)
    
    
# task 5
text = input()
nm = int(input())
nm = nm % len(text)
print(text[-nm:] + text[:-nm])