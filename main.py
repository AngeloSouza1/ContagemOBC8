import tkinter as tk
from PIL import Image, ImageTk
from modulo_niveis import calcular_niveis_exclusivos


class AdventureLevelApp:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.carregar_widgets()
        self.campos_visiveis = False

    def configurar_janela(self):
        self.root.title("Contagem de Níveis de Aventura 🎮✨")
        largura_janela = 819
        altura_janela = 819
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x_central = int((largura_tela - largura_janela) / 2)
        y_central = int((altura_janela - largura_janela) / 2)
        self.root.geometry(f"{largura_janela}x{largura_janela}+{x_central}+{y_central}")
        self.root.resizable(False, False)

        # Adicionando o background
        self.background_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

    def carregar_widgets(self):
        # Botão principal
        self.botao_imagem = ImageTk.PhotoImage(Image.open("assets/start_button.png").resize((50, 50)))
        self.botao_iniciar = tk.Button(
            self.root,
            image=self.botao_imagem,
            command=self.mostrar_campos,
            bg="#2b2b2b",
            bd=0,
            activebackground="#1E1E1E",
        )
        self.botao_iniciar.place(relx=0.95, rely=0.95, anchor="se")

    def mostrar_campos(self):
        if not self.campos_visiveis:
            # Campo para inserir a experiência
            self.experiencia_label = tk.Label(
                self.root,
                text="Digite as experiências ganhas (separadas por espaço):",
                bg="#2b2b2b",
                fg="#FFD700",
                font=("Helvetica", 12),
            )
            self.experiencia_label.place(relx=0.1, rely=0.3, anchor="w")

            self.experiencia_entry = tk.Entry(
                self.root, font=("Helvetica", 12), width=50, bg="#1E1E1E", fg="#FFD700", insertbackground="#FFD700"
            )
            self.experiencia_entry.place(relx=0.1, rely=0.35, anchor="w")

            # Botão para calcular os níveis
            self.botao_calcular = tk.Button(
                self.root,
                text="Calcular Níveis",
                command=self.calcular_niveis,
                bg="#FFD700",
                fg="#2b2b2b",
                font=("Helvetica", 12, "bold"),
            )
            self.botao_calcular.place(relx=0.1, rely=0.5, anchor="w")

            self.campos_visiveis = True

    def calcular_niveis(self):
        try:
            experiencias = list(map(int, self.experiencia_entry.get().split()))
            if not experiencias:
                self.exibir_erro("❌ Entrada vazia! Insira os valores de experiência.")
                return
        except ValueError:
            self.exibir_erro("❌ Entrada inválida! Certifique-se de inserir números inteiros separados por espaço.")
            return

        niveis_conquistados = calcular_niveis_exclusivos(experiencias)
        self.exibir_saida(experiencias, niveis_conquistados)

    def exibir_saida(self, experiencias, niveis_conquistados):
        if hasattr(self, "output_frame"):
            self.output_frame.destroy()

        self.output_frame = tk.Frame(
            self.root, bg="#333333", highlightthickness=2, highlightbackground="#FFD700", relief="raised"
        )
        self.output_frame.place(relx=0.5, rely=0.6, anchor="center", width=600, height=300)

        self.close_icon = ImageTk.PhotoImage(Image.open("assets/close_icon.png").resize((20, 20)))
        self.close_button = tk.Button(
            self.output_frame,
            image=self.close_icon,
            bg="#333333",
            bd=0,
            activebackground="#444444",
            command=self.resetar_tela,
        )
        self.close_button.place(x=570, y=5)

        experiencias_label = tk.Label(
            self.output_frame,
            text=f"Experiências: {', '.join(map(str, experiencias))}",
            bg="#333333",
            fg="#FFD700",
            font=("Courier", 12),
        )
        experiencias_label.place(x=10, y=30)

        niveis_label = tk.Label(
            self.output_frame,
            text=f"Níveis Conquistados: {niveis_conquistados}",
            bg="#333333",
            fg="#00FF00",
            font=("Courier", 14, "bold"),
        )
        niveis_label.place(x=10, y=70)

    def exibir_erro(self, mensagem):
        # Centralizando o popup com base na posição da janela principal
        largura_janela = self.root.winfo_width()
        altura_janela = self.root.winfo_height()
        x_janela = self.root.winfo_x()
        y_janela = self.root.winfo_y()

        largura_popup = 350
        altura_popup = 150
        x_centralizado = x_janela + (largura_janela - largura_popup) // 2
        y_centralizado = y_janela + (altura_janela - altura_popup) // 2

        popup = tk.Toplevel(self.root)
        popup.geometry(f"{largura_popup}x{altura_popup}+{x_centralizado}+{y_centralizado}")
        popup.configure(bg="#2b2b2b")
        popup.title("Aviso ⚠️")

        erro_label = tk.Label(
            popup,
            text=mensagem,
            fg="#FFD700",
            bg="#2b2b2b",
            font=("Helvetica", 12, "bold"),
            wraplength=300,
            justify="center",
        )
        erro_label.pack(pady=20)

        tk.Button(
            popup,
            text="Entendido",
            command=popup.destroy,
            bg="#FFD700",
            fg="#2b2b2b",
            font=("Helvetica", 10, "bold"),
            activebackground="#444444",
            activeforeground="#FFD700",
        ).pack()

    def resetar_tela(self):
        if hasattr(self, "output_frame"):
            self.output_frame.destroy()
            del self.output_frame
        self.resetar_campos()

    def resetar_campos(self):
        if hasattr(self, "experiencia_entry"):
            self.experiencia_entry.place_forget()
            self.botao_calcular.place_forget()
            self.experiencia_label.place_forget()
            self.campos_visiveis = False


if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureLevelApp(root)
    root.mainloop()
