print("Tipo de participante: ",end="")
tipo = str(input()).lower()
if tipo!='ex-aluno':
  print("Idade do participante: ", end="")
  idade = int(input())

if tipo=='ex-aluno':
  r = float(60)
else:
  if idade>=12:
    r = float(50)
  else:
    if idade>3 and idade<=11:
      r = float(25)
    else:
      r = 0
      
print("\nTotal a ser pago = R$ {:.2f}".format(r))