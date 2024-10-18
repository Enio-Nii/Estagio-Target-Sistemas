import json
from datetime import datetime

timestamp_atual = datetime.now()

nome_mes = timestamp_atual.strftime("%B")


def calcular_faturamento(arquivo):

    # CARREGAR ARQUIVO JSON:
    with open('SRC/dados.json') as f:
        dados = json.load(f)

    faturamento_diario = dados
    
    valores = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    
    if not valores:
        print("Não há dias com faturamento.")
        return
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])
    
    print(f'Média mensal: R${media_mensal:.2f}')
    print(f'Menor faturamento: R${menor_faturamento:.2f}')
    print(f'Maior faturamento: R${maior_faturamento:.2f}')
    print(f'Nº de dias com faturamento acima da média: {dias_acima_da_media}')

# Chamada da função com o arquivo JSON
calcular_faturamento('faturamento.json')
