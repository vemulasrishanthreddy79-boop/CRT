s= "python"
print(s[2])
print(s[1:])
''''''
#Reverse a string without using built-in functions and slice operator
st = input()
#Solution 1
res =""
stop = -1 * (len(st)+1)
for i in range(-1, stop, -1):
    res += st[i]
print(res)
#Solution 2
res1 = ""
for ch in st:
    res1 = ch + res1
print(res1)

def frequency_count(s):
    pass
print(frequency_count("abcabc"))#{'a':2, 'b':2, 'c':2}
def frequency_count(s):
    d={}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d
print(frequency_count("abcabc"))#{'a':2, 'b':2, 'c':2}

def is_Anagrams(st1,st2):
    pass

print(is_Anagrams("space","paces"))
print(is_Anagrams)