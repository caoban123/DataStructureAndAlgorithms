height = list(map(int,input().split()))
MaxHeight = max(height)
Area = MaxHeight * len(height)
cnt = 0
rows = [["WHITE"] * len(height) for _ in range(MaxHeight)]
for row in rows:
    for j in range(len(row)):
        if height[j] > 0:
            height[j] -= 1
            row[j] = "BLACK"
            x = j
            break
    for i in range(x+1,len(row)):
        if height[i] > 0:
            height[i] -= 1
            row[i] = "BLACK"
        else:
            row[i] = "BLUE"
            cnt += 1
    for j in range(len(row) - 1, -1 , -1):
        if row[j] != "BLACK":
            row[j] = "WHITE"
            cnt -= 1
        else:
            break
print(cnt)

