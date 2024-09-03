# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

# Dados do exercício#

# import json


# with open("dados_ex_3.json") as dados:
#     faturamento_diario = json.load(dados)
    
# faturamento_diario_final = [dia['valor'] for dia in faturamento_diario]    
    
# # menor_faturamento_final = min(faturamento_diario_final)
# # maior_faturamento_final = max(faturamento_diario_final)
# # soma = 0

# # for item  in faturamento_diario_final:
# #     int(item)
# # if item < menor_faturamento_final:
# #         menor_faturamento_final = item
        
# # if item > maior_faturamento_final:
# #     maior_faturamento_final = item
    
# # soma = sum(faturamento_diario_final) + item
# # print(soma)
# # media_faturamento = (soma/len(faturamento_diario_final))


# # print(f"Maior faturamento diário: R$ {maior_faturamento_final:.2f}")
# # print(f"Menor faturamento diário: R$ {menor_faturamento_final:.2f}")
# # print(f"Média de faturamento diário: R$ {media_faturamento:.2f}")


import json

# Função para carregar dados da JSON

def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    return dados['faturamento_diario']
        
        


# Função para calcular as estatísticas de faturamento
def calcular_estatisticas(faturamento_diario):
    valores = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

    # Verificando se há dias com faturamento_diario
    if not valores:
        return None, None, 0

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_da_media = len([dia for dia in faturamento_diario if dia['valor'] > media_mensal])

    return menor_valor, maior_valor, dias_acima_da_media

# Função principal
def main():
    # Carregar dados do faturamento
    faturamento_diario = carregar_dados('dados_ex_3.json')
    
    # Calcular as estatísticas
    menor, maior, num_dias_acima_media = calcular_estatisticas(faturamento_diario)
    
    # Resultado
    print(f'Menor valor de faturamento: R${menor:.2f}')
    print(f'Maior valor de faturamento: R${maior:.2f}')
    print(f'Números de dias que tiveram faturamento acima da média: {num_dias_acima_media}')

if __name__ == '__main__':
    main()
