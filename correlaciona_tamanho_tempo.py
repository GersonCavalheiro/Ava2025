import pandas as pd
import sys
import matplotlib.pyplot as plt

def correlacionar_tamanho_tempo_ordenado_multiplos_arquivos(lista_arquivos):
    """
    Lê múltiplos arquivos CSV, combina os dados, ordena pelo tempo de execução
    e calcula a correlação de Pearson entre o tamanho dos dados e o tempo
    de execução para todos os dados combinados. Gera um gráfico de
    dispersão dos tamanhos dos dados ordenados pelo tempo de execução
    e exibe uma mensagem sobre a força da correlação.

    Args:
        lista_arquivos (list): Uma lista de strings, onde cada string é o
                               caminho de um arquivo CSV.
    """
    todos_dataframes = []
    for nome_arquivo in lista_arquivos:
        try:
            df = pd.read_csv(nome_arquivo, header=None, names=['matricula', 'tamanho_dados', 'tempo_execucao'])
            todos_dataframes.append(df)
            print(f"Arquivo '{nome_arquivo}' lido com sucesso.")
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado e será ignorado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")

    if not todos_dataframes:
        print("Erro: Nenhum dado válido foi encontrado nos arquivos fornecidos.")
        return

    # Combinar todos os DataFrames em um único DataFrame
    df_combinado = pd.concat(todos_dataframes, ignore_index=True)

    # Ordenar o DataFrame combinado pelo tempo de execução
    df_ordenado = df_combinado.sort_values(by='tempo_execucao')

    # Calcular a correlação de Pearson entre 'tamanho_dados' e 'tempo_execucao'
    correlacao = df_ordenado['tamanho_dados'].corr(df_ordenado['tempo_execucao'], method='pearson')

    print("\nAnálise para todos os arquivos combinados:")
    print(f"Correlação de Pearson entre tamanho dos dados e tempo de execução (após ordenação pelo tempo): {correlacao:.4f}")

    # Mensagem sobre a força da correlação
    if abs(correlacao) >= 0.7:
        print("A correlação entre o tamanho dos dados e o tempo de execução (após ordenação) é alta.")
    elif 0.3 <= abs(correlacao) < 0.7:
        print("A correlação entre o tamanho dos dados e o tempo de execução (após ordenação) é moderada.")
    else:
        print("A correlação entre o tamanho dos dados e o tempo de execução (após ordenação) é baixa.")

    # Gerar gráfico de dispersão dos tamanhos dos dados ordenados
    plt.figure(figsize=(12, 7))
    plt.scatter(df_ordenado.index, df_ordenado['tamanho_dados'], label='Tamanho dos Dados (ordenado por tempo)', s=10)
    plt.xlabel('Índice (após ordenação por tempo de execução de todos os dados)')
    plt.ylabel('Tamanho dos Dados')
    plt.title('Tamanho dos Dados Ordenado pelo Tempo de Execução (Todos os Arquivos)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python correlacao_ordenada_combinada.py <arquivo1.csv> [arquivo2.csv ...]")
        sys.exit(1)

    lista_arquivos = sys.argv[1:]
    correlacionar_tamanho_tempo_ordenado_multiplos_arquivos(lista_arquivos)
