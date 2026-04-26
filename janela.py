import tkinter as tk
from tkinter import messagebox, filedialog
import math

def calcular_tudo():
    try:
        # Dados de entrada
        c = float(ent_comp.get())
        h = float(ent_alt.get())
        l = float(ent_esp.get())
        qc = float(ent_qc.get())
        qan = float(ent_qan.get())
        
        # Preço (Kwanza)
        preco_saco = float(ent_preco.get()) if ent_preco.get() else 0

        # --- LÓGICA DE REBOCO (Conforme teu caderno) ---
        traco_total = qc + qan
        sacos_exatos = (35.64 * c * h * l) / traco_total
        sacos_final = math.ceil(sacos_exatos)
        areia_m3 = 1.485 * (1 / traco_total) * c * h * l * qan
        agua_l = 0.67 * (1 / traco_total) * c * h * l * 1000
        custo_total = sacos_final * preco_saco

        # --- LÓGICA DE TIJOLOS (Padrão 20x20x10) ---
        area = c * h
        # Estimativa de 25 tijolos por m2 (ajustável conforme o tijolo)
        total_tijolos = math.ceil(area * 25)

        res = (f"--- RELATÓRIO SIDNEY TECH ---\n"
               f"Área Total: {area:.2f} m²\n"
               f"-----------------------------\n"
               f"CIMENTO: {sacos_final} Sacos\n"
               f"AREIA: {areia_m3:.2f} m³\n"
               f"ÁGUA: {agua_l:.1f} Litros\n"
               f"TIJOLOS: {total_tijolos} Unidades\n"
               f"-----------------------------\n"
               f"INVESTIMENTO CIMENTO: {custo_total:,.2f} Kz\n"
               f"-----------------------------\n"
               f"Traço: {int(qc)}:{qan} | Espessura: {l}m")
        
        messagebox.showinfo("RESULTADOS", res)
        # Guardar para exportação
        global ultimo_resultado
        ultimo_resultado = res

    except ValueError:
        messagebox.showerror("Erro", "Verifica se usaste ponto (.) e preencheste os campos!")

def exportar_txt():
    if 'ultimo_resultado' in globals():
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", 
                                     initialfile="Orcamento_SidneyTech.txt")
        if f:
            f.write(ultimo_resultado)
            f.close()
            messagebox.showinfo("Sucesso", "Orçamento guardado com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Primeiro faz um cálculo!")

def limpar():
    for e in [ent_comp, ent_alt, ent_esp, ent_preco]: e.delete(0, tk.END)

# --- Interface ---
app = tk.Tk()
app.title("SIDNEY TECH V5 - GESTÃO DE OBRAS")
app.geometry("450x750")
app.configure(bg="#0f172a")

tk.Label(app, text="SISTEMA DE MATERIAIS - SIDNEY", font=("Arial", 14, "bold"), 
         bg="#1e40af", fg="white", pady=15).pack(fill="x")

def campo(txt, padrao=""):
    tk.Label(app, text=txt, bg="#0f172a", fg="#94a3b8", font=("Arial", 9, "bold")).pack(pady=(10,0))
    e = tk.Entry(app, justify="center", font=("Arial", 11))
    if padrao: e.insert(0, padrao)
    e.pack(ipady=3)
    return e

ent_comp = campo("COMPRIMENTO (m)")
ent_alt = campo("ALTURA (m)")
ent_esp = campo("ESPESSURA REBOCO (m)", "0.025")
ent_preco = campo("PREÇO DO SACO (Kz)")

# Traço
f_t = tk.Frame(app, bg="#0f172a")
f_t.pack(pady=15)
ent_qc = tk.Entry(f_t, width=4, justify="center"); ent_qc.insert(0, "1"); ent_qc.pack(side="left", padx=2)
tk.Label(f_t, text=":", bg="#0f172a", fg="white").pack(side="left")
ent_qan = tk.Entry(f_t, width=4, justify="center"); ent_qan.insert(0, "4"); ent_qan.pack(side="left", padx=2)

# Botões
tk.Button(app, text="CALCULAR TUDO", command=calcular_tudo, bg="#22c55e", fg="white", 
          font=("Arial", 11, "bold"), width=25, pady=10).pack(pady=10)
tk.Button(app, text="EXPORTAR PARA TXT", command=exportar_txt, bg="#3b82f6", fg="white", 
          width=25).pack(pady=5)
tk.Button(app, text="LIMPAR", command=limpar, bg="#475569", fg="white", width=25).pack(pady=5)

app.mainloop()