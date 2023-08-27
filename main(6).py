print("Tipo de aparelho: ",end="")
tipo = str(input()).lower()
print("Modelo de aparelho: ", end="")
modelo = str(input()).lower()
print("Quantidade desejada: ", end="")
qtde = int(input())

if modelo=='samsung' and tipo=='celular':
  r = float(qtde*921.40)
elif modelo=='multilaser' and tipo=='tablet':
  r = float(qtde*339.50)
elif modelo=='motorola' and tipo=='celular':
  r = float(qtde*879.18)
else: #tipo = tablet e modelo = samsung
  r = float(qtde*417.72)

print("\n\tResultado = R${:.2f}".format(r))