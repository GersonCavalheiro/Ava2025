import pandas as pd
import matplotlib.pyplot as plt
import sys

def gerar_boxplot_multiplos_arquivos(lista_arquivos):
    """
    Gera e exibe um boxplot dos tempos de execução de múltiplos arquivos CSV.

    Args:
        lista_arquivos (list): Uma lista de strings, onde cada string é o caminho
                               de um arquivo CSV. Espera-se que cada arquivo CSV
                               tenha três colunas: matrícula, tamanho_dados, tempo_execucao.
    """
    if not lista_arquivos:
        print("Erro: Nenhum arquivo CSV foi fornecido como parâmetro.")
        return

    tempos_execucao_por_arquivo = []
    nomes_arquivos = []

    for nome_arquivo in lista_arquivos:
        try:
            df = pd.read_csv(nome_arquivo, header=None, names=['matricula', 'tamanho_dados', 'tempo_execucao'])
            tempos_execucao_por_arquivo.append(df['tempo_execucao'])
            nomes_arquivos.append(nome_arquivo)
            print(f"Dados do arquivo '{nome_arquivo}' carregados com sucesso.")
        except FileNotFoundError:
            print(f"Aviso: Arquivo '{nome_arquivo}' não encontrado e será ignorado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")

    if not tempos_execucao_por_arquivo:
        print("Erro: Nenhum dado válido foi encontrado nos arquivos fornecidos.")
        return

    plt.figure(figsize=(12, 8))
    plt.boxplot(tempos_execucao_por_arquivo, labels=nomes_arquivos)
    plt.xlabel('Arquivo')
    plt.ylabel('Tempo de Execução')
    plt.title('Boxplot dos Tempos de Execução por Arquivo')
    plt.grid(True)
    plt.savefig('boxplot_tempos_execucao.png')
    plt.show()
    plt.close()

    print("Boxplot dos tempos de execução gerado com sucesso e salvo como 'boxplot_tempos_execucao.png' e exibido na tela.")

if __name__ == "__main__":
    arquivos_csv = sys.argv[1:]
    gerar_boxplot_multiplos_arquivos(arquivos_csv)
