print("Setores:\n\t(1) Arquibancada\n\t(2) Platéia VIP\n\t(3) Cadeira")
print("Setor desejado? ",end="")
setor = int(input())
print("\nTipos de ingresso:\n\t(1) Meia\n\t(2) Inteira")
print("Tipo de ingresso desejado? ",end="")
tipo = int(input())

if tipo==2: #inteira
  if setor==1: #Arquibancada
    r = float(100 + (0.05*100))
  else:
    if setor==3:#Cadeira
      r = float(200 + (0.05*200))
    else:
      if setor==2: #VIP
        r = float(350 + 17.50)
else: #meia
  if setor==1:
    r = float((100/2) + (0.05*100))
  else:
    if setor==3:
      r = float((200/2) + (0.05*200))
    else:
      if setor==2:
        r=0
      else:
        r=-1

if r>0:
  print("\nTotal = R$ {:.2f}".format(r))
else:
  if r==0:
    print("\nTipo de ingresso inválido")
  else:
    print("\nSetor inválido")