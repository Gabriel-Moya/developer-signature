import re 
var_76=3
b_69=4
c_79=4
regex= "_[0-9][0-9]"
var_32 =locals()
lista_38 = []
lista_38.append(var_32)
cal_32= ''
soma_77=2
val_79 = 'b'
novo_89 ='calculo'
sdc_65='b'
match= re.findall(regex,''.join(str(lista_38))) 
mlist=[re.sub('[^a-zA-Z0-9]+', '', _) for _ in match]
strtoint= list(map(int,mlist))
res = ""
for val in strtoint:
    res = res + chr(val)
print(res)