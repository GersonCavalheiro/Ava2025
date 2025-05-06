import pandas as pd
import sys
import matplotlib.pyplot as plt

def gerar_grafico_media_por_tamanho_com_reta(lista_arquivos):
    """
    Lê múltiplos arquivos CSV, calcula a média do tempo de execução para cada
    tamanho de dados encontrado em todos os arquivos e apresenta um gráfico
    de linha com a média do tempo de execução por tamanho. Adiciona uma reta
    unindo o primeiro e o último ponto do gráfico.

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

    # Calcular a média do tempo de execução para cada tamanho de dados
    media_por_tamanho = df_combinado.groupby('tamanho_dados')['tempo_execucao'].mean().reset_index()

    # Ordenar por tamanho dos dados para o gráfico
    media_por_tamanho = media_por_tamanho.sort_values(by='tamanho_dados')

    # Gerar o gráfico de linha
    plt.figure(figsize=(10, 6))
    plt.plot(media_por_tamanho['tamanho_dados'], media_por_tamanho['tempo_execucao'], marker='o', linestyle='-', label='Média por Tamanho')

    # Adicionar a reta unindo o primeiro e o último ponto
    if not media_por_tamanho.empty:
        primeiro_tamanho = media_por_tamanho['tamanho_dados'].iloc[0]
        primeiro_tempo = media_por_tamanho['tempo_execucao'].iloc[0]
        ultimo_tamanho = media_por_tamanho['tamanho_dados'].iloc[-1]
        ultimo_tempo = media_por_tamanho['tempo_execucao'].iloc[-1]
        plt.plot([primeiro_tamanho, ultimo_tamanho], [primeiro_tempo, ultimo_tempo], linestyle='--', color='red', label='Tendência (Início-Fim)')

    plt.xlabel('Tamanho dos Dados')
    plt.ylabel('Média do Tempo de Execução')
    plt.title('Média do Tempo de Execução por Tamanho dos Dados com Reta de Tendência')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python grafico_media_tamanho_reta.py <arquivo1.csv> [arquivo2.csv ...]")
        sys.exit(1)

    lista_arquivos = sys.argv[1:]
    gerar_grafico_media_por_tamanho_com_reta(lista_arquivos)
