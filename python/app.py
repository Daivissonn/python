import tkinter as tk
from tkinter import messagebox

# --- LÓGICA DO CARRINHO (Modelos) ---
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_produto(self, produto):
        if produto.nome in self.itens:
            self.itens[produto.nome]['quantidade'] += 1
        else:
            self.itens[produto.nome] = {'produto': produto, 'quantidade': 1}

    def remover_produto(self, nome_produto):
        if nome_produto in self.itens:
            del self.itens[nome_produto]

    def calcular_total(self):
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens.values())

# --- INTERFACE GRÁFICA (Tkinter) ---
class AppCarrinho:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Meu E-Commerce Simples")
        self.root.geometry("500x400")
        
        # Inicializando dados
        self.carrinho = CarrinhoDeCompras()
        self.produtos_disponiveis = [
            Produto("Notebook", 3500.00),
            Produto("Mouse Gamer", 150.00),
            Produto("Teclado Mecânico", 250.00),
            Produto("Fone de Ouvido", 199.90)
        ]

        # --- Painel Esquerdo: Produtos da Loja ---
        self.frame_produtos = tk.LabelFrame(root, text=" Produtos Disponíveis ", padx=10, pady=10)
        self.frame_produtos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        for prod in self.produtos_disponiveis:
            btn = tk.Button(
                self.frame_produtos, 
                text=f"{prod.nome}\n(R$ {prod.preco:.2f})", 
                command=lambda p=prod: self.adicionar(p),
                bg="#e1f5fe", height=2
            )
            btn.pack(fill=tk.X, pady=5)

        # --- Painel Direito: Carrinho e Total ---
        self.frame_carrinho = tk.LabelFrame(root, text=" Seu Carrinho ", padx=10, pady=10)
        self.frame_carrinho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Lista visual do carrinho
        self.lista_visual = tk.Listbox(self.frame_carrinho, height=12)
        self.lista_visual.pack(fill=tk.BOTH, expand=True, pady=5)

        # Label de Total
        self.label_total = tk.Label(self.frame_carrinho, text="Total: R$ 0.00", font=("Arial", 12, "bold"))
        self.label_total.pack(pady=5)

        # Botões de Ação
        self.btn_remover = tk.Button(self.frame_carrinho, text="❌ Remover Selecionado", command=self.remover, bg="#ffcdd2")
        self.btn_remover.pack(fill=tk.X, pady=2)

        self.btn_finalizar = tk.Button(self.frame_carrinho, text="✅ Finalizar Compra", command=self.finalizar, bg="#c8e6c9")
        self.btn_finalizar.pack(fill=tk.X, pady=2)

    # --- Funções de Atualização da Tela ---
    def atualizar_tela(self):
        # Limpa a lista visual
        self.lista_visual.delete(0, tk.END)
        
        # Preenche com os itens atualizados
        for item in self.carrinho.itens.values():
            p = item['produto']
            q = item['quantidade']
            self.lista_visual.insert(tk.END, f"{q}x {p.nome} - R$ {p.preco * q:.2f}")
        
        # Atualiza o preço total
        self.label_total.config(text=f"Total: R$ {self.carrinho.calcular_total():.2f}")

    def adicionar(self, produto):
        self.carrinho.adicionar_produto(produto)
        self.atualizar_tela()

    def remover(self):
        try:
            # Pega o texto da linha selecionada na lista
            selecionado = self.lista_visual.get(self.lista_visual.curselection())
            # Descobre o nome do produto limpando o texto da linha (ex: "2x Notebook - R$ ...")
            nome_produto = selecionado.split("x ")[1].split(" -")[0]
            
            self.carrinho.remover_produto(nome_produto)
            self.atualizar_tela()
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um item no carrinho para remover.")

    def finalizar(self):
        if not self.carrinho.itens:
            messagebox.showwarning("Carrinho Vazio", "Adicione produtos antes de finalizar!")
            return
        
        total = self.carrinho.calcular_total()
        messagebox.showinfo("Sucesso!", f"Compra finalizada com sucesso!\nTotal: R$ {total:.2f}\nObrigado!")
        # Limpa o carrinho após finalizar
        self.carrinho = CarrinhoDeCompras()
        self.atualizar_tela()

# --- Execução do Programa ---
if __name__ == "__main__":
    janela = tk.Tk()
    app = AppCarrinho(janela)
    janela.mainloop()
