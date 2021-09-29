d={'07/09/1945':'albert','02/09/1930':'benjamin','21/05/1785':'ada'}
print(type(d))
print(d)
print(d["07/09/1945"])
d1={'albert11':'02/08/1985','benjamin':'05/08/1958','ada':'08/05/1954'}
print(d1["ada"])
print(d1.keys())
print(d1.values())
name=input("enter the name")
for name in d1:
    print(d1[name])
