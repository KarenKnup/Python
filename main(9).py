print("Tempo de serviço: ", end="")
tempo = int(input())
print("Salário atual: ", end="")
salario = float(input())

if tempo<55:
  r=0
else:
  if tempo==55:
    r=0.6*salario
  else:
    r=(0.6*salario)+((tempo-55)*0.15*salario)

if r!=0:
  print("\nTotal de benefício = R$ {:.2f}".format(r))
else:
  print("\nNão tem direito ao benefício")