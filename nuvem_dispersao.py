import pandas as pd
import matplotlib.pyplot as plt
import sys

def gerar_grafico_dispersao_execucoes_por_arquivo(lista_arquivos):
    """
    Gera e exibe um gráfico de dispersão onde o eixo x representa o número da execução
    (reiniciando em 1 para cada arquivo) e o eixo y representa o tempo de execução,
    combinando dados de múltiplos arquivos CSV.

    Args:
        lista_arquivos (list): Uma lista de strings, onde cada string é o caminho
                               de um arquivo CSV. Espera-se que cada arquivo CSV
                               tenha três colunas: matrícula, tamanho_dados, tempo_execucao.
    """
    if not lista_arquivos:
        print("Erro: Nenhum arquivo CSV foi fornecido como parâmetro.")
        return

    plt.figure(figsize=(14, 8))

    for nome_arquivo in lista_arquivos:
        try:
            df = pd.read_csv(nome_arquivo, header=None, names=['matricula', 'tamanho_dados', 'tempo_execucao'])
            print(f"Dados do arquivo '{nome_arquivo}' carregados com sucesso.")

            # O eixo x agora será um range de 1 até o número de linhas no DataFrame
            num_execucoes_arquivo = len(df)
            plt.scatter(range(1, num_execucoes_arquivo + 1), df['tempo_execucao'],
                        label=f'Arquivo: {nome_arquivo}')

        except FileNotFoundError:
            print(f"Aviso: Arquivo '{nome_arquivo}' não encontrado e será ignorado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")

    plt.xlabel('Número da Execução (por arquivo)')
    plt.ylabel('Tempo de Execução')
    plt.title('Nuvem de Dispersão do Tempo de Execução')
    plt.grid(True)
    plt.legend()
    plt.savefig('nuvem_dispersao_por_arquivo.png')
    plt.show()
    plt.close()

    print("Nuvem de dispersão das execuções gerada com sucesso e salva como 'nuvem_dispersao_por_arquivo.png' e exibida na tela.")

if __name__ == "__main__":
    arquivos_csv = sys.argv[1:]
    gerar_grafico_dispersao_execucoes_por_arquivo(arquivos_csv)
