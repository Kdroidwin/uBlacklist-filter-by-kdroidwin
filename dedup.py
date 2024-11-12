f = open("uBlacklist.txt", "r", encoding='utf-8')
res = set()
for i in f.readlines():
    if len(i) > 1:
        res.add(i)
f.close()
print("loaded", len(res), "records")

f = open("uBlacklist.txt", "w", encoding='utf-8')
res = list(res)
res.sort()
for i in res:
    f.write(i)
f.close()
