#!/bin/bash

# Verifica se o número correto de argumentos foi fornecido
if [ "$#" -ne 2 ]; then
  echo "Uso: $0 <numero_de_repeticoes> <tamanho_da_area>"
  exit 1
fi

# Atribui os argumentos às variáveis
N="$1"
TAM="$2"
ARQUIVO_SAIDA="ord_${TAM}.csv"

# Verifica se o programa 'ord' existe no diretório local e é executável
if [ ! -f "./ord" ]; then
  echo "Erro: O programa './ord' não foi encontrado no diretório local."
  exit 1
fi

if [ ! -x "./ord" ]; then
  echo "Erro: O programa './ord' não tem permissão de execução."
  exit 1
fi

# Executa o programa 'ord' N vezes e redireciona a saída para o arquivo
echo "Executando './ord $TAM' $N vezes e gravando em '$ARQUIVO_SAIDA'..."
for i in $(seq 1 "$N"); do
  ./ord "$TAM" >> "$ARQUIVO_SAIDA"
done

echo "Processo concluído. Os resultados foram gravados em '$ARQUIVO_SAIDA'."

exit 0
