'''

#1)Find the largest number (using max())
#input:[12,78,32,54,69,100]
#output:100
li = [12,78,32,54,69,100]
max_num = li[0]
for num in li:
    if num > max_num:
        max_num = num
print(max_num) 
print(max(li))
print(min(li))
'''
'''

#2)check palindrome (using reversed() & join())
s=input()
print("palindrome" if s==s[::-1] else "not palindrome")

print("".join(reversed(s)))

print(list(reversed([1,2,3,4,5])))
'''
'''
#remove duplicates (using set())
# li=[1,2,3,4,5,1,2,3]
li=[1,2,3,4,5,1,2,3]
print(list(set(li)))
'''
#sum of numbers (using sum())
# input:123
# output:6
num = input()
total = 0
for digit in num:
    total += int(digit)
print(total)
print(sum(int(digit) for digit in num))

#Sort Words  Alphabetically (using sorted())
li = ['preeti','mujeeb','kalyai','dinesh','suresh']
print(sorted(li))

'''
#index with Value (using enumerate())
li = ['preeti','mujeeb','kalyai','dinesh','suresh']
for index, value in enumerate(li):
    print(index,"==>", value)

'''

li1 = [1,2,3,4,5]
li2 = [10,20,30,40,50]
#res = [11,22,33,44,55]
res = [li1[i]+li2[i] for i in range(len(li1))]
print(res)

res1 = [x+y for x,y in zip(li1,li2)]
print(res1)

#Find Second Largest Number (using sorted())
list = [10,20,30,40,50,100,50,60,70,100]
sort_