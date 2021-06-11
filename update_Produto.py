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
    codprod = input("Código (000-fim):")
    if codprod == "000":
        break

    
    cursor.execute ("Select dsprod, prvenda from produto where codprod = ?", (codprod,))
    
    consult = cursor.fetchone()

    if consult != None:
        
        print ("Descrição do produto: ", consult[0])
        print ("Preço de venda: ", consult[1])


        print("Digite o novo valor de venda para atualizar o cadastro")


        prvenda = input("Preço de venda:")
        if is_num(prvenda):
            break
        else:
            print("Preço de venda incorreto")
                    
    cursor.execute("update produto set prvenda = ? where codprod = ?" (prvenda, codprod))
    conn.commit()
    print("Produto atualizado com sucesso!")
    input("Pressione enter para continuar")


        
conn.close
quit()


