import customtkinter as ctk 
from tkinter import messagebox

ctk.set_appearance_mode("red")
ctk.set_default_color_theme("dark-blue")

janelinha = ctk.CTk()
''
janelinha.title("será que vc pode dirigir?") 

janelinha.geometry("200x300")

def verificar_habilitacao():
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if not nome or not idade:
        messagebox.showarring("campos vazios", "preencha todos os campos!")
        return

    try:
        idade = int(idade)
    except ValueError:
          messagebox.showarring("erro", "A idade precisa ser um número inteiro.")
          return

    if idade >= 18:
        resultado.configure(f"{nome}, você está apto(a) a dirigir!")
    else:
        resultado.configure(f"{nome}, você nao está apto(a) a dirigir.")

label_nome = ctk.CTkLabel(janelinha, text="Digite seu nome:")
label_nome.pack(pady=10)

entrada_nome = ctk.CTkEntry(janelinha, width=250)
entrada_nome.pack()    

label_idade = ctk.CTkLabel(janelinha, text="Digite sua idade:")
label_idade.pack(pady=10)

entrada_idade = ctk.CTkEntry(janelinha, width=250)
entrada_idade.pack() 

botao = ctk.CTkButton(janelinha, text="Verificar Habilitação", command=verificar_habilitacao)
botao.pack(pady=10)

resultado_label = ctk.CTkLabel(janelinha, text="")
resultado_label.pack(pady=10)


janelinha.mainloop()
