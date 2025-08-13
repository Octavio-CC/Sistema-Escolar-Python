import tkinter as tk
from tkinter import ttk, messagebox
import json

# --- Funções de Arquivo ---
def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

# --- Serviços por Tabela ---
SERVICOS = {
    'Estudantes': {
        'arquivo': 'estudantes.json',
        'campos': ['codigo_estudante', 'nome_estudante', 'cpf_estudante']
    },
    'Disciplinas': {
        'arquivo': 'disciplinas.json',
        'campos': ['codigo_disciplina', 'nome_disciplina']
    },
    'Professores': {
        'arquivo': 'professores.json',
        'campos': ['codigo_professor', 'nome_professor', 'cpf_professor']
    },
    'Turmas': {
        'arquivo': 'turmas.json',
        'campos': ['codigo_turma', 'nome_turma']
    },
    'Matriculas': {
        'arquivo': 'matriculas.json',
        'campos': ['codigo_matricula', 'codigo_estudante', 'nome_estudante']
    },
}

# --- Classe Principal ---
class SistemaAcademico(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sistema Acadêmico')
        self.geometry('750x500')

        self.quadro_menu = tk.Frame(self, width=200, bg='#e0e0e0')
        self.quadro_menu.pack(side='left', fill='y')

        self.quadro_conteudo = tk.Frame(self)
        self.quadro_conteudo.pack(side='right', expand=True, fill='both')

        for nome in SERVICOS:
            botao = ttk.Button(
                self.quadro_menu,
                text=nome,
                command=lambda n=nome: self.mostrar_lista(n)
            )
            botao.pack(fill='x', pady=4, padx=10)

        self.tabela = None
        self.servico_atual = None

    def mostrar_lista(self, nome_servico):
        self.servico_atual = nome_servico
        config = SERVICOS[nome_servico]
        dados = carregar_arquivo(config['arquivo'])

        for widget in self.quadro_conteudo.winfo_children():
            widget.destroy()

        cabecalho = ttk.Label(self.quadro_conteudo, text=nome_servico, font=('Arial', 16))
        cabecalho.pack(pady=10)

        colunas = config['campos']
        self.tabela = ttk.Treeview(self.quadro_conteudo, columns=colunas, show='headings')
        for coluna in colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=120)
        self.tabela.pack(expand=True, fill='both', padx=10, pady=10)

        for item in dados:
            valores = [item.get(campo, '') for campo in colunas]
            self.tabela.insert('', 'end', values=valores)

        quadro_botoes = tk.Frame(self.quadro_conteudo)
        quadro_botoes.pack(pady=10)
        ttk.Button(quadro_botoes, text='Adicionar', command=self.abrir_adicionar).pack(side='left', padx=5)
        ttk.Button(quadro_botoes, text='Editar', command=self.abrir_editar).pack(side='left', padx=5)
        ttk.Button(quadro_botoes, text='Excluir', command=self.excluir_item).pack(side='left', padx=5)

    def abrir_adicionar(self):
        self.abrir_formulario('Adicionar')

    def abrir_editar(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning('Atenção', 'Selecione um registro para editar.')
            return
        self.abrir_formulario('Editar', selecionado[0])

    def abrir_formulario(self, acao, id_item=None):
        janela_formulario = tk.Toplevel(self)
        janela_formulario.title(f'{acao} - {self.servico_atual}')
        config = SERVICOS[self.servico_atual]
        entradas = {}
        valores = []

        if acao == 'Editar':
            valores = self.tabela.item(id_item)['values']

        for i, campo in enumerate(config['campos']):
            ttk.Label(janela_formulario, text=campo).grid(row=i, column=0, pady=5, padx=5, sticky='e')
            entrada = ttk.Entry(janela_formulario)
            entrada.grid(row=i, column=1, pady=5, padx=5)
            if acao == 'Editar':
                entrada.insert(0, valores[i])
            entradas[campo] = entrada

        def salvar():
            registro = {campo: entrada.get() for campo, entrada in entradas.items()}
            arquivo_servico = config['arquivo']
            lista = carregar_arquivo(arquivo_servico)
            chave = config['campos'][0]

            if acao == 'Editar':
                original = valores[0]
                for i, reg in enumerate(lista):
                    if reg.get(chave) == original:
                        lista[i] = registro
                        break
            else:
                if any(r.get(chave) == registro[chave] for r in lista):
                    messagebox.showerror('Erro', 'Código já cadastrado.')
                    return
                lista.append(registro)

            salvar_arquivo(lista, arquivo_servico)
            janela_formulario.destroy()
            self.mostrar_lista(self.servico_atual)

        ttk.Button(janela_formulario, text='Salvar', command=salvar).grid(row=len(config['campos']), column=0, columnspan=2, pady=10)

    def excluir_item(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning('Atenção', 'Selecione um registro para excluir.')
            return

        config = SERVICOS[self.servico_atual]
        arquivo_servico = config['arquivo']
        lista = carregar_arquivo(arquivo_servico)
        chave = config['campos'][0]
        valores = self.tabela.item(selecionado[0])['values']
        codigo = valores[0]

        if messagebox.askyesno('Confirmar', 'Deseja realmente excluir esse registro?'):
            lista = [r for r in lista if r.get(chave) != codigo]
            salvar_arquivo(lista, arquivo_servico)
            self.mostrar_lista(self.servico_atual)

if __name__ == '__main__':
    app = SistemaAcademico()
    app.mainloop()
