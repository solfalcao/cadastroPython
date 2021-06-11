import sqlite3

def is_num(num):
    try:
        float(num)
        return True

    except:
        pass
    return False

conn = sqlite3.connect("dbProduto.db")
cursor = conn.cursor()

while True:
    while True:
        codprod = input("Código (000-fim):")
        if codprod.isdigit():
            break
        else:
            print("Código inválido")
            continue

    if codprod == "000":
        break
       
    cursor.execute("Select count(*) from produto where codprod = ?", (codprod,))
    rs = cursor.fetchone()
    if rs[0] > 0:
        print ("Este código já está cadastrado")
        input("Pressione enter para continuar")
        continue
        
    while True:
        dsprod = input("Descrição:")
        if len(dsprod.strip()) > 0:
            break
        else:
            print("Preencha o campo com a descrição correta")

    while True:
        saldo  = input("Saldo:")
        if saldo.isdigit():
            break
        else:
            print("Digite o saldo correto")

    while True:
        sldmin = input("Saldo mínimo:")
        if sldmin.isdigit():
            break
        else:
            print("Digite o saldo mínimo correto")

    while True:        
        prvenda = input("Preço de venda:")
        if is_num(prvenda):
            break
        else:
            print("Preço de venda incorreto")
                    
    while True:   
        prcusto = input("Preço de custo:")
        if is_num(prcusto):
            break
        else:
            print("Preço de custo incorreto")
                
  
    cursor.execute("insert into produto values (?,?,?,?,?,?)",
                   (codprod, dsprod, saldo, sldmin, prvenda, prcusto))
    conn.commit()
    print("Produto cadastrado com sucesso!")
    input("Pressione enter para continuar")


conn.close
quit()


