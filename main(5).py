print("------- Time 1 -----------")
print("Digite o nome do time: ", end="")
time1 = str(input())
print("Quantos pontos foram feitos: ", end="")
pontos1 = int(input())
print("Saldo de gols: ", end="")
saldo1 = int(input())
print("Quantidade de gols feitos: ", end="")
gols1 = int(input())

print("\n------- Time 2 -----------")
print("Digite o nome do time: ", end="")
time2 = str(input())
print("Quantos pontos foram feitos: ", end="")
pontos2 = int(input())
print("Saldo de gols: ", end="")
saldo2 = int(input())
print("Quantidade de gols feitos: ", end="")
gols2 = int(input())

if pontos1 < pontos2 or (pontos1 == pontos2 and saldo1 < saldo2) or (pontos1 == pontos2 and saldo1 == saldo2 and gols1 < gols2):
    print("\nTime vencedor: " + time2.lower())
elif pontos1 > pontos2 or (pontos1 == pontos2 and saldo1 > saldo2) or (pontos1 == pontos2 and saldo1 == saldo2 and gols1 > gols2):
    print("\nTime vencedor: " + time1.lower())
else:
    print("\nEMPATE")
