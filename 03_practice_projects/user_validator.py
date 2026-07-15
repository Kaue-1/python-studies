# Validador simples de usuário: 

name = input("Insira seu nome completo: ")
name = name.strip()

while name == "":
    print("Inválido, você precisa escrever alguma coisa")
    name = input("Insira novamente: ")
    name = name.strip()    

phone = input("Insira seu telefone: ")
phone = phone.replace("-", "")

while len(phone) < 8:
    print("Inválido! O número precisa ter no mínimo 8 caracteres.")
    phone = input("Insira novamente: ")
    phone = phone.replace("-", "")

email = input("Insira seu e-mail: ")
email = email.strip()

while "@" not in email: 
    print('O e-mail precisa ter o "@"!')
    email = input("insira novamente: ")
    email = email.strip()
    

name = name.title()

print(f"Seu nome é:  {name}, seu número de telefone é: {phone} e seu e-mail é: {email}")





