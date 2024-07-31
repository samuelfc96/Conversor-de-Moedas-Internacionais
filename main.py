# janela - 500x500
# Titulo "Conversor de Moedas
# Campos de Selecionar Moeda de origem e destino (Campos de listas)com Labels "Selecione as moeda de Destino" "Selecione a moeda de Origem"
# Botão de "Converter"
# Lista de exibição com os nomes das moedas 

import customtkinter

# Criar e Configurar Janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#padroes = customtkinter.CTk(padx=10, pady=10)
janela = customtkinter.CTk()
janela.geometry("500x500")

# Criar os botoes,txtos e elementos
titulo = customtkinter.CTkLabel(janela, text= "Conversor de Moedas", font=("",30))
texto_moeda_origem = customtkinter.CTkLabel(janela, text= "Selecione a Moeda de Origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text= "Selecione a Moeda de Destino")

campo_moeda_origem =customtkinter.CTkOptionMenu(janela, values= ["USD","BRL","EUR","BTC"])
campo_moeda_destino =customtkinter.CTkOptionMenu(janela, values= ["USD","BRL","EUR","BTC"])

def converter_moeda():
    print("Funcionou")
    
botao_converter = customtkinter.CTkButton(janela, text= "Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dolar Americano", "BRL: Real Brasileiro","BTC: Bitcoin" ]
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

# Colocar elementos na tela(janela)
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# Rodar Janela
janela.mainloop()  