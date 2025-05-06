#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Uso: " << argv[0] << " <numero_de_elementos>" << std::endl;
        return 1;
    }

    int numElementos = std::stoi(argv[1]);

    std::vector<int> dados(numElementos);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, 1000); // Distribuição entre 1 e 1000

    for (int i = 0; i < numElementos; ++i)
        dados[i] = distrib(gen);

    auto inicio = std::chrono::high_resolution_clock::now();
    std::sort(dados.begin(), dados.end());
    auto fim = std::chrono::high_resolution_clock::now();

    auto duracao = std::chrono::duration_cast<std::chrono::microseconds>(fim - inicio);

    std::cout << "1313, " << numElementos << ", " << duracao.count() << std::endl;

    return 0;
}
