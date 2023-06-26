# Python Project

# Variáveis
menu = 0
listaPessoas = []

# Funções 

# Cadastrar pessoas
def cadastrar():

    # Inserir dados nas variáveis
    while True:
        nome = str(input("Nome: "))
        if any(char.isdigit() for char in nome):
            entreLinhas("ERRO: Nome inválido, não pode conter números.")
            continue
        elif nome.strip() == "":
            entreLinhas("ERRO: Nome inválido, digite novamente.")
        else:
            break
    
    while True:
        
        idade_str = input("Idade: ")
        if idade_str.strip() == "":
            entreLinhas("ERRO: Idade não fornecida, tente novamente.")
            continue
        elif not idade_str.isdigit():
            entreLinhas("Idade inválida! Tente novamente.")
            continue
        
        idade = int(idade_str)
        if idade <= 0:
            entreLinhas("ERRO: Idade inválida, a idade deve ser maior que zero.")
            continue
        else:
            break
        
    # Objeto 
    pessoa = {
            "Nome": nome,
            "Idade": idade
        }
        
    # Insere o objeto em um lista
    listaPessoas.append(pessoa);
        
    entreLinhas("Pessoa cadastrada com sucesso!")
  
#  Função para listar as pessoas cadastradas  
def listar():
    if len(listaPessoas) < 1:
        entreLinhas("Não há pessoas cadastradas!")
    else:
        entreLinhas("PESSOAS CADASTRADAS")
        print("NOME".ljust(30) + "| IDADE")
        linha()
        for pessoa in listaPessoas:
            nome = pessoa["Nome"]
            idade = pessoa["Idade"]
            print(f"{nome.ljust(30)}| {idade}")
        linha()
    

# Colocar uma mensagem entre uma linha separadora
def entreLinhas(msg):
    print("-"*50)
    print(msg.center(50))
    print("-"*50)

# Inserir linhas 
def linha():
    print("-"*50)
    
    

# Laço de repetição
while menu != 3:
    {entreLinhas("MENU PRINCIPAL")}
    entreLinhas("""
    1 - Ver pessoas cadastradas
    2 - Cadastrar nova pessoa
    3 - Sair do Sistema
    """)
    
    try:
        menu = int(input("Sua opção: "))
        
        
        if menu == 1:
            listar()
        elif menu == 2:
            cadastrar()
        elif menu == 3:
            entreLinhas(f"Programa finalizado, volte sempre!")
        else: 
            entreLinhas("Opção inválida! Por favor, escolha uma opção válida.")
    except ValueError:
        entreLinhas("ERRO: Por favor, digite um número inteiro.")
