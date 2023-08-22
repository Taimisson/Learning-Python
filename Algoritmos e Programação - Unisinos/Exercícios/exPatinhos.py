# Ajude a Xuxa

quantidadePatinhos = int(input("Digite a quantidade de patinhos: "))

while quantidadePatinhos < 2:
    print("A quantidade de patinhos deve ser maior que 2!")
    quantidadePatinhos = int(input("Digite a quantidade de patinhos: "))
 
# SALVANDO A QUATNIDADE DE PATOS EM OUTRA VARIÁVEL 
patinhos = quantidadePatinhos
 
# INÍCIO DO LAÇO    
while quantidadePatinhos != 0:
    
    if quantidadePatinhos == 2:
        print(f"""
        {quantidadePatinhos} patinhos
        foram passear
        Além das montanhas
        Para brincar
        A mamãe gritou
        Quack quack quack
        Mas {quantidadePatinhos-1} patinho
        Voltou de lá
        """)        
    elif quantidadePatinhos == 1:
        print(f"""
        {quantidadePatinhos} patinho foi passear
        Além das montanhas
        Para brincar
        A mamãe gritou
        Quack quack quack
        Mas nenhum patinho
        Voltou de lá
        """)
    else:
        print(f"""
        {quantidadePatinhos} patinhos
        Foram passear
        Além das montanhas
        Para brincar
        A mamãe gritou
        Quack quack quack
        Mas só {quantidadePatinhos-1} patinhos
        Voltaram de lá
            """)
        
    quantidadePatinhos -= 1
        
        # FIM DO WHILE

print(f"""
        A mamãe patinha
        Foi procurar
        Além das montanhas
        Na beira do mar
        A mamãe gritou
        Quack quack quack
        E os {patinhos} patinhos
        Voltaram de lá
      """)