regex= "_[0-9][0-9]"
var = locals()
lista = []
lista.append(var)
match = re.findall(regex,''.join(str(lista)))
mlist = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in match]
strtoint= list(map(int,mlist))
res = ""
for val in strtoint:
    res = res + chr(val)
print(res)