import pandas as pd
import sys
import numpy as np

def calcular_repeticoes_necessarias(nome_arquivo_csv):
    """
    Analisa um arquivo CSV com dados de execução e sugere o número mínimo
    de repetições necessárias com base no coeficiente de variação do tempo
    de execução para cada tamanho de dados.

    Args:
        nome_arquivo_csv (str): O nome do arquivo CSV de entrada.
    """
    try:
        df = pd.read_csv(nome_arquivo_csv, header=None, names=['matricula', 'tamanho_dados', 'tempo_execucao'])
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_csv}' não foi encontrado.")
        return

    tamanhos_unicos = df['tamanho_dados'].unique()
    resultados = {}

    print("Análise da variabilidade do tempo de execução por tamanho de dados:")

    for tamanho in tamanhos_unicos:
        dados_tamanho = df[df['tamanho_dados'] == tamanho]['tempo_execucao']
        if len(dados_tamanho) > 1:
            media = np.mean(dados_tamanho)
            desvio_padrao = np.std(dados_tamanho)
            cv = desvio_padrao / media if media != 0 else 0
            print(f"Tamanho dos dados: {tamanho}, Média: {media:.4f}, Desvio Padrão: {desvio_padrao:.4f}, Coeficiente de Variação: {cv:.4f}")

            # Sugestão baseada no coeficiente de variação
            if cv < 0.05:
                sugestao = 10  # Baixa variabilidade, poucas repetições podem ser suficientes
            elif cv < 0.15:
                sugestao = 30  # Variabilidade moderada
            else:
                sugestao = 50  # Alta variabilidade, mais repetições são recomendadas

            resultados[tamanho] = sugestao
        else:
            print(f"Tamanho dos dados: {tamanho}, Insuficientes dados para calcular a variabilidade (apenas {len(dados_tamanho)} amostra).")
            resultados[tamanho] = "Insuficientes dados"

    print("\nSugestão do número mínimo de repetições por tamanho de dados:")
    for tamanho, sugestao in resultados.items():
        print(f"Tamanho: {tamanho}, Sugestão de repetições: {sugestao}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python calcular_repeticoes.py <nome_arquivo.csv>")
        sys.exit(1)
    nome_arquivo = sys.argv[1]
    calcular_repeticoes_necessarias(nome_arquivo)
