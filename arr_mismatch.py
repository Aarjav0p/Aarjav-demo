arr = ["bana", "apple", "banaba", "bananza"]
s = "banana"
mis = 0
for item in arr:
    if len(item) != len(s):
        continue
    else:
        for i in range(len(s)):
            if item[i] == s[i]:
                continue
            else:
                mis += 1
    if mis == 1:
        print(f"Item with one char mismatch : {item}")
