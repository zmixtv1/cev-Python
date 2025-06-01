import tkinter as tk
from tkinter import messagebox
import threading
import instaloader
import csv

def coletar_perfis():
    def run():
        usuario_alvo = entrada_usuario.get().strip()
        try:
            quantidade = int(entrada_quantidade.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido para a quantidade.")
            return

        usuario_logado = "rodrigo_alaor"

        if not usuario_alvo:
            messagebox.showerror("Erro", "Digite um nome de perfil.")
            return

        try:
            btn_coletar.config(state="disabled")
            status_label.config(text="⏳ Coletando perfis...")

            L = instaloader.Instaloader()
            L.load_session_from_file(usuario_logado)

            perfil = instaloader.Profile.from_username(L.context, usuario_alvo)
            seguidores = perfil.get_followers()

            coletados = []
            for seguidor in seguidores:
                if seguidor.is_private:
                    continue
                coletados.append((seguidor.username, seguidor.full_name, seguidor.biography))
                if len(coletados) >= quantidade:
                    break

            nome_arquivo = f"seguidores_{usuario_alvo}.csv"
            with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Username", "Nome", "Bio"])
                writer.writerows(coletados)

            status_label.config(text="")
            messagebox.showinfo("Sucesso", f"{len(coletados)} perfis salvos em {nome_arquivo}")

        except Exception as e:
            status_label.config(text="")
            messagebox.showerror("Erro", str(e))
        finally:
            btn_coletar.config(state="normal")

    # Executa em uma thread separada para não travar a janela
    threading.Thread(target=run).start()


# Interface Tkinter
janela = tk.Tk()
janela.title("Coletar Perfis do Instagram")
janela.geometry("400x220")

tk.Label(janela, text="Usuário base do Instagram:").pack(pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.insert(0, "cfoab")
entrada_usuario.pack()

tk.Label(janela, text="Quantidade de perfis públicos:").pack(pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.insert(0, "5")
entrada_quantidade.pack()

btn_coletar = tk.Button(janela, text="Coletar Perfis", command=coletar_perfis)
btn_coletar.pack(pady=15)

status_label = tk.Label(janela, text="", fg="blue")
status_label.pack()

janela.mainloop()
