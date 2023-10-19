# Algoritmos Genéticos

- A Base do AG é dada pela evolução de amostras

- Algoritmos baseados na genética biológica

- Onde aplicamos AG? Exemplo: encontrar um funcionário
    * Trabalhamos com regiões de busca 
    * Soluções heurísticas e não determinísticas 

    * Navegação robótica 
    * Inteligência Artificial
    * Geração de novos dados
    * Jogos digitais

- Exemplo: 
    * Gerar combinações de resposta para o usuário 
    * Gerar combinações de perguntas
    * Deixar o sistema mais próximo de uma interação humana 

- Exemplo:
    * Planejamento de rotas em robôs móveis

# Métodos de otimização para algoritmos genéticos

- Como implementar um AG?
    * Passo 0: Gera população inicial
    - Gera população aleatória 
    - Define a população dentro de uma região de busca

    * Passo 1: Seleção dos melhores indivíduos iniciais
    - Método de seleção por roleta
    - Seleciona os melhores indivíduos dada sua probabilidade

    * Passo 2: Recombinação de indivíduos
    - A recombinação vai recombinaara os dois melhores indivíduos
    - AA meta é gerar um indivíduo melhor do que seus pais

    * Passo 3: Seleção dos melhores indivíduos iniciais
    - Selecionar um ponto de cromossomo e gerar mutação 
    - Evita a convergência prematura do AG
    // Antes da mutação: 11100
    // Depois: 11000

# Funcionamento na prática...

* Gerar soluções para o comportamento dos personagens em um game 
- Evitar comportamentos repetidos entre os agentes do game
- Gerar comportamentos novos para cada agente 
- Ensinar um agente em seu funcionamento desde o ponto "zero". 
    * Ensinar o comportamento do agente do "zero"
    * Aprendizado por tentativa e erro

#