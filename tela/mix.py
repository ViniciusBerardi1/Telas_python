from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vinic\Desktop\tela\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fazer_login():
    usuario = entry_1.get()
    senha = entry_2.get()

    # Verificar as credenciais
    if usuario == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Esconde a janela de login após o login bem-sucedido
        window.withdraw()
        
        # Cria a próxima tela após o login bem-sucedido
        window_principal = Tk()
        window_principal.geometry("700x500")
        window_principal.configure(bg="#FFFFFF")

        canvas = Canvas(
            window_principal,
            bg="#FFFFFF",
            height=500,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            250.0,
            500.0,
            fill="#3058A8",
            outline=""
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png")
        )
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=66.0,
            y=24.0,
            width=119.0,
            height=119.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png")
        )
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=66.0,
            y=191.0,
            width=119.0,
            height=119.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png")
        )
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=66.0,
            y=358.0,
            width=119.0,
            height=119.0
        )

        canvas.create_rectangle(
            262.0,
            191.0,
            690.0,
            310.0,
            fill="#3093A8",
            outline=""
        )

        canvas.create_rectangle(
            269.0,
            358.0,
            697.0,
            477.0,
            fill="#3093A8",
            outline=""
        )

        canvas.create_rectangle(
            262.0,
            24.0,
            690.0,
            143.0,
            fill="#3093A8",
            outline=""
        )

        canvas.create_text(
            276.0,
            33.0,
            anchor="nw",
            text="PLANTAÇÃO DE ALFACE",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        canvas.create_text(
            276.0,
            56.0,
            anchor="nw",
            text="Evite áreas sujeitas a encharcamento para prevenir doenças nas raízes. \nPara cultivares comuns, o espaçamento entre as plantas e linhas deve ser\n de 30 centímetros. \nRealize irrigações diárias de manhã ou no final da tarde, \ndependendo do clima e tipo de solo.\n",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        canvas.create_rectangle(
            66.0,
            24.0,
            185.0,
            143.0,
            fill="#FFFFFF",
            outline=""
        )

        window_principal.resizable(False, False)
        window_principal.mainloop()
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

window = Tk()
window.geometry("700x500")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 350.0, 500.0, fill="#2F93A7", outline="")
canvas.create_text(67.0, 68.0, anchor="nw", text="HYDROEASY", fill="#FFFFFF", font=("Inter", 30 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(519.0, 186.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=406.0, y=166.0, width=226.0, height=38.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(519.0, 289.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_2.place(x=406.0, y=269.0, width=226.0, height=38.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=fazer_login,  # Chama a função fazer_login ao clicar
    relief="flat"
)
button_1.place(x=390.0, y=372.0, width=258.0, height=40.0)

canvas.create_text(390.0, 372.0, anchor="nw", text="OK", fill="#000000", font=("Inter Medium", 20 * -1))
canvas.create_text(372.0, 242.0, anchor="nw", text="Senha", fill="#2F58A7", font=("Inter Medium", 20 * -1))
canvas.create_text(380.0, 143.0, anchor="nw", text="Usuário", fill="#2F58A7", font=("Inter Medium", 20 * -1))
canvas.create_text(57.0, 138.0, anchor="nw", text="Aplicativo \ndesenvolvido para \nprogramação de \nirrigação e \nmonitoramento\n", fill="#FFFFFF", font=("Inter Thin", 30 * -1))
canvas.create_text(361.0, 68.0, anchor="nw", text="Faça o login", fill="#2F58A7", font=("Inter", 30 * -1))

window.resizable(False, False)
window.mainloop()
