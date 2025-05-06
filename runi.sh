#!/bin/bash

# Verifica se o número mínimo de argumentos foi fornecido
if [ "$#" -lt 2 ]; then
  echo "Uso: $0 <numero_de_repeticoes> <tamanho1> [tamanho2 ...]"
  echo "Exemplo: $0 5 100 500 1000"
  exit 1
fi

# Atribui o primeiro argumento ao número de repetições
N="$1"
shift # Remove o primeiro argumento da lista

# A lista restante de argumentos é a lista de tamanhos
TAMANHOS=("$@")

# Verifica se o programa 'ord' existe no diretório local e é executável
if [ ! -f "./ord" ]; then
  echo "Erro: O programa './ord' não foi encontrado no diretório local."
  exit 1
fi

if [ ! -x "./ord" ]; then
  echo "Erro: O programa './ord' não tem permissão de execução."
  exit 1
fi

echo "Executando './ord' $N vezes para cada tamanho e gravando em arquivos 'ord_TAM.csv'..."

# Loop para realizar as repetições de forma intercalada
for ((i=1; i<=N; i++)); do
  for TAM in "${TAMANHOS[@]}"; do
    ARQUIVO_SAIDA="ord_${TAM}.csv"
    echo "Executando './ord $TAM', repetição $i, e anexando a '$ARQUIVO_SAIDA'..."
    ./ord "$TAM" >> "$ARQUIVO_SAIDA"
  done
done

echo "Processo concluído. Os resultados foram gravados em arquivos 'ord_TAM.csv'."

exit 0
