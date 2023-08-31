# Petrônio está com uma rádio online. Ele acredita que sua rádio está crescendo de audiência, mas ele não tem certeza. Você, então, deve ajudar Petrônio, analisando se os valores de audiência de sua rádio são sempre crescentes ou não.

# Para isto, crie um programa que lê os valores de audiência de alguns meses e verifica se a audiência é sempre crescente ou não. Seu programa deve recebe um inteiro que corresponde a quantos valores de audiência serão digitados pelo usuário. Em seguida, o programa deve solicitar todos estes dados de audiência (que são valores com ponto flutuante) e imprimir na tela a mensagem "AUDIÊNCIA SEMPRE CRESCENTE" ou "AUDIÊNCIA NEM SEMPRE CRESCENTE". Também imprima a média de audiência dos meses informados (com apenas 1 casa depois da vírgula). Ao final de cada resultado, seu programa deve perguntar ao usuário se ele deseja continuar ou não, e se ele quiser continuar, faça uma nova análise. Caso ele não queira continuar, o programa termina. 



while True:
   
    try:
        qntdAudiencia = int(input("Digite quantos meses de audiência você deseja analisar: "))
        dadosAudiencia = []
        crescente = 0

        for i in range(qntdAudiencia):
            
            media = float(input(f"Digite a média do {i + 1}º mês: "))
            dadosAudiencia.append(media)

            somaLista = sum(dadosAudiencia)
            mediaAudiencia = somaLista / qntdAudiencia
            
        listaOrdenada = sorted(dadosAudiencia)
        
        if listaOrdenada == dadosAudiencia:
            print("AUDIÊNCIA SEMPRE CRESCENTE! ", end="")
        else:
            print("AUDIÊNCIA NEM SEMPRE CRESCENTE! ", end="")

        print(f"Média de audiência: {mediaAudiencia:.1f}")
        
        pergunta = str(input("Deseja continuar? [S/N] ")).lower()
        
        if pergunta == "n":
            print("Encerrando programa...")
            break
        
    except ValueError:
        print("Valor inválido!")
    
    
    # print("teste")
    