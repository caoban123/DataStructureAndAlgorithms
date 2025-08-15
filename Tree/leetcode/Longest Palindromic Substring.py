s = input()
Max = 1
MaxStr = s[0]
for l in range(0,len(s)):
    for r in range(l,len(s)):
        if r - l + 1 > Max and s[l:r+1] == s[l:r+1][::-1]:
            MaxStr = s[l:r+1]
            Max = r - l + 1
print(len(MaxStr))
