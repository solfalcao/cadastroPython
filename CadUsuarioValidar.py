import sqlite3

conn = sqlite3.connect("dbProduto.db")
cursor = conn.cursor()

while True:
    while True:
        cpf = input("CPF (000-fim):")
        if cpf.isdigit():
            break
        else:
            print("CPF inválido")
            continue

    if cpf == "000":
        break
       
        cursor.execute("Select count(*) from usuario where cpf = ?", (cpf))
        rs = cursor.fetchone()
        if rs[0] > 0:
            print ("Este usuário já está cadastrado")
            input("Pressione enter para continuar")
            continue
        
    while True:
        nome  = input("Nome:")
        if len(nome.strip()) > 0:
            break
        else:
            print("Preencha o campo com o nome correto")


    while True:
        login = input("Digite seu login:")
        if len(login.strip()) > 0:
            break
        else:
            print("Digite um login válido")

        cursor.execute("Select count(*) from produto where login = ?", (login))
        consult = cursor.fetchone()
        if consult[0] > 0:
            print ("Este login já está cadastrado")
            input("Pressione enter para continuar")
            continue


    while True:
        senha  = input("Digite sua senha:")
        if len(senha.strip()) > 0:
            break
        else:
            print("Preencha o campo com uma senha válida")

                
  
    cursor.execute("insert into usuario values (?,?,?,?)",
                   (cpf, nome, login, senha))
    conn.commit()
    print("Usuário cadastrado com sucesso!")
    input("Pressione enter para continuar")


conn.close
quit()


