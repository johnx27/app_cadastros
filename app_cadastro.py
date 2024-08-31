import psycopg2
from tkinter import *

dbname   = 'python1'
user     = 'postgres'
password = '99695421'
host     = 'localhost'
port     = '5432' 

# Criar uma conexão
conn = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

cursor= conn.cursor()



def carga_de_dados():
    #convertendo Entry para um str psycopg2 conseguir ler
    user_name = text_user.get()
    user_number = text_number.get()

    cursor.execute(
    """INSERT INTO usuarios (nome_gerado,numero_celular)
    VALUES (%s,%s)""",(
        (user_name, user_number)
        )
        )
    
    texto= "usuario cadastrado"
    text_cadastro ["text"]=texto

    conn.commit()
    cursor.close()
    conn.close()


janela= Tk()
janela.geometry("300x250")
janela.resizable(False,False)
janela.title("CADASTROS DE USUARIOS")

name_user= Label(janela,text="USUARIO:")
name_user.grid(column=0,row=0)

text_user= Entry(janela,width=25)
text_user.grid(column=1,row=0,padx=10)

number_user= Label(janela,text="TELEFONE:")
number_user.grid(column=0,row=2,pady=10,)

text_number= Entry(janela,width=25)
text_number.grid(column=1,row=2,padx=10)

button= Button(janela,text="enviar",command=carga_de_dados)
button.grid(column=1,row=3,pady=20)

text_cadastro= Label(janela,text="")
text_cadastro.grid(column=1,row=4)



janela.mainloop()