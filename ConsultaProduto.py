import sqlite3

conn = sqlite3.connect("dbProduto.db")
cursor = conn.cursor()

while True:
    codprod = input("Código (000-fim):")
    if codprod == "000":
        break
    
    cursor.execute ("Select * from produto where codprod = ?", (codprod,))

    consult = cursor.fetchone()

    if consult != None:
        
        print ("Descrição do produto: ", consult[1])
        print ("Saldo atual: ", consult[2])
        print ("Saldo mínimo: ", consult[3])
        print ("Preço de venda: ", consult[4])
        print ("Preço de custo: ", consult[5])
    else:
        print("Produto não cadastrado!")
        input("Pressione enter para continuar")
        
conn.close
quit()


