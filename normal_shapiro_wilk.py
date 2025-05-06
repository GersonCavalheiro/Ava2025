import pandas as pd
import sys
from scipy import stats

def verificar_normalidade_shapiro_wilk_alpha(nome_arquivo_csv, alpha):
    """
    Calcula o teste de Shapiro-Wilk para o tempo de execução em um arquivo CSV,
    recebendo o valor alpha como parâmetro.

    Args:
        nome_arquivo_csv (str): O nome do arquivo CSV de entrada.
        alpha (float): O nível de significância (alpha) para o teste.
    """
    try:
        df = pd.read_csv(nome_arquivo_csv, header=None, names=['matricula', 'tamanho_dados', 'tempo_execucao'])
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_csv}' não foi encontrado.")
        return

    try:
        alpha = float(alpha)
        if not 0 < alpha < 1:
            print("Erro: O valor de alpha deve estar entre 0 e 1.")
            return
    except ValueError:
        print("Erro: O valor de alpha fornecido não é um número válido.")
        return

    tempos_execucao = df['tempo_execucao']

    if len(tempos_execucao) < 3:
        print("A amostra precisa ter pelo menos 3 observações para o teste de Shapiro-Wilk.")
        return

    shapiro_test = stats.shapiro(tempos_execucao)
    statistic = shapiro_test.statistic
    p_value = shapiro_test.pvalue

    print(f"Teste de Shapiro-Wilk para o arquivo: '{nome_arquivo_csv}' com alpha = {alpha:.2f}")
    print(f"Estatística de Teste (W): {statistic:.4f}")
    print(f"Valor p: {p_value:.4f}")

    if p_value > alpha:
        print(f"O valor p ({p_value:.4f}) é maior que o nível de significância ({alpha:.2f}).")
        print("Conclusão: A amostra parece seguir uma distribuição normal (não há evidências suficientes para rejeitar a hipótese nula).")
    else:
        print(f"O valor p ({p_value:.4f}) é menor ou igual ao nível de significância ({alpha:.2f}).")
        print("Conclusão: A amostra não parece seguir uma distribuição normal (há evidências suficientes para rejeitar a hipótese nula).")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python verificar_shapiro_wilk_alpha.py <nome_arquivo.csv> <valor_alpha>")
        print("Exemplo: python verificar_shapiro_wilk_alpha.py dados.csv 0.01")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    valor_alpha = sys.argv[2]
    verificar_normalidade_shapiro_wilk_alpha(nome_arquivo, valor_alpha)
