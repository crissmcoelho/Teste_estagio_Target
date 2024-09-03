# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
out = float(19849.53)
total = float(sp + rj + mg + es + out)
print(total)
porcentagem_sp = ((sp/total)*100)
porcentagem_rj = ((rj/total)*100)
porcentagem_mg = ((mg/total)*100)
porcentagem_es = ((es/total)*100)
porcentagem_outros = ((out/total)*100)

print(f"Porcentagem de SP: {porcentagem_sp:.2f}%")
print(f"Porcentagem de RJ: {porcentagem_rj:.2f}%")
print(f"Porcentagem de MG: {porcentagem_mg:.2f}%")
print(f"Porcentagem de ES: {porcentagem_es:.2f}%")
print(f"Porcentagem de outros: {porcentagem_outros:.2f}%")