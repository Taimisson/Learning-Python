username = str(input("Digite o seu nome: "));

print("DIGITE O SEU ENDEREÇO ABAIXO !");

nomeRua = str(input("Digite o nome da rua: "));
numCasa = input("Número da casa: ");
CEP = str(input("Digite o CEP: "));
bairro = str(input("Digite o bairro: "));


print("="*20)
print("NOME:", username);
print("RUA:", nomeRua + ", " + numCasa)
print("CEP:", CEP);
print("BAIRRO:", bairro);
print("="*20)
