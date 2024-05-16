import tkinter as tk
from tkinter import messagebox


def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        root_login.destroy()  # Fechar a tela de login após o login bem-sucedido
        criar_tela_menu()
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos")


def criar_tela_login():
    global root_login
    root_login = tk.Tk()
    root_login.title("Login")
    root_login.geometry("300x200")
    root_login.configure(bg="#3498db")

    frame_login = tk.Frame(root_login, bg="#3498db")
    frame_login.place(relx=0.5, rely=0.5, anchor="center")

    label_usuario = tk.Label(
        frame_login, text="Usuário:", bg="#3498db", fg="white")
    label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    label_senha = tk.Label(frame_login, text="Senha:",
                           bg="#3498db", fg="white")
    label_senha.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    global entry_usuario
    entry_usuario = tk.Entry(frame_login)
    entry_usuario.grid(row=0, column=1, padx=5, pady=5)

    global entry_senha
    entry_senha = tk.Entry(frame_login, show="*")
    entry_senha.grid(row=1, column=1, padx=5, pady=5)

    button_login = tk.Button(frame_login, text="Login", command=login)
    button_login.grid(row=2, columnspan=2, padx=5, pady=5)

    root_login.mainloop()


def criar_tela_menu():
    menu = tk.Tk()
    menu.title("Menu")
    menu.geometry("440x400")
    menu.configure(bg="#87ceeb")  # Cor de fundo azul claro

    label_welcome = tk.Label(
        menu, text="Bem-vindo ao Hydroeasy", font=("Arial", 14, "bold"), bg="#87ceeb")
    label_welcome.grid(row=0, column=0, columnspan=5, padx=20, pady=10)

    button1 = tk.Button(menu, text="Alface", width=10)
    button1.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    frame_plantacao1 = tk.Frame(menu, bg="white", bd=2, relief=tk.GROOVE)
    frame_plantacao1.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    label_info1 = tk.Label(
        frame_plantacao1, text="Plantação de alface \nRegado pela última vez: 13:30 \nPróximo agendamento: 18:15 \nHumidade 70%", bg="white")
    label_info1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    button_agendamento1 = tk.Button(menu, text="Agendamento", width=15)
    button_agendamento1.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    button2 = tk.Button(menu, text="Tomate", width=10)
    button2.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    frame_plantacao2 = tk.Frame(menu, bg="white", bd=2, relief=tk.GROOVE)
    frame_plantacao2.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    label_info2 = tk.Label(
        frame_plantacao2, text="Plantação de Tomate  \nRegado pela última vez: 15:20 \nSem agendamentos \nHumidade 90%", bg="white")
    label_info2.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    button_agendamento2 = tk.Button(menu, text="Agendamento", width=15)
    button_agendamento2.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    button3 = tk.Button(menu, text="Cebolinha", width=10)
    button3.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    frame_plantacao3 = tk.Frame(menu, bg="white", bd=2, relief=tk.GROOVE)
    frame_plantacao3.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    label_info3 = tk.Label(
        frame_plantacao3, text="Plantação de Cebolinha \nRegado pela última vez: 09:00 \nPróximo agendamento: 15:30 \nHumidade 20%", bg="white")
    label_info3.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    button_agendamento3 = tk.Button(menu, text="Agendamento", width=15)
    button_agendamento3.grid(row=3, column=2, padx=10, pady=10, sticky="w")

    menu.mainloop()


criar_tela_login()
