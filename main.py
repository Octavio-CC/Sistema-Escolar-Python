# Nome: Octavio Coelho Chaves
# Curso: Análise e Desenvolvimento de Sistemas	

import json

def mostrar_menu_principal():
    print('----- MENU PRINCIPAL -----')
    print('(1) - Estudantes.')
    print('(2) - Disciplinas.')
    print('(3) - Professores.')
    print('(4) - Turmas.')
    print('(5) - Matrículas.')
    print('(0) - Sair.')

    return input('Informe a opção desejada: ')


def processar_sub_menu(opcao):
    if opcao == '0':
        print('Saindo do programa...')
        return False

    if opcao == '1':
        while True:
            sub_opcao = mostrar_sub_menu_estudantes()
            print(f'Você escolheu a opção {sub_opcao}')

            if sub_opcao == '0':
                print('Voltando ao Menu Principal...')
                break
            elif sub_opcao == '1':
                incluir_estudante_ou_professor(estudantes, 'estudante')
            elif sub_opcao == '2':
                listar_cadastros(estudantes, 'estudantes')
            elif sub_opcao == '3':
                atualizar_cadastro(estudantes, 'estudante')
            elif sub_opcao == '4':
                excluir_cadastro(estudantes, 'estudante')
            else:
                print('Opção inválida! Tente novamente.')

    elif opcao == '2':
        while True:
            sub_opcao = mostrar_sub_menu_disciplinas()
            print(f'Você escolheu a opção {sub_opcao}')

            if sub_opcao == '0':
                print('Voltando ao Menu Principal...')
                break
            elif sub_opcao == '1':
                incluir_disciplina_ou_turmas(disciplinas, 'disciplina')
            elif sub_opcao == '2':
                listar_cadastros(disciplinas, 'disciplinas')
            elif sub_opcao == '3':
                atualizar_cadastro(disciplinas, 'disciplina')
            elif sub_opcao == '4':
                excluir_cadastro(disciplinas, 'disciplina')
            else:
                print('Opção inválida! Tente novamente.')

    elif opcao == '3':
        while True:
            sub_opcao = mostrar_sub_menu_professores()
            print(f'Você escolheu a opção {sub_opcao}')

            if sub_opcao == '0':
                print('Voltando ao Menu Principal...')
                break
            elif sub_opcao == '1':
                incluir_estudante_ou_professor(professores, 'professor')
            elif sub_opcao == '2':
                listar_cadastros(professores, 'professores')
            elif sub_opcao == '3':
                atualizar_cadastro(professores, 'professor')
            elif sub_opcao == '4':
                excluir_cadastro(professores, 'professor')
            else:
                print('Opção inválida! Tente novamente.')

    elif opcao == '4':
        while True:
            sub_opcao = mostrar_sub_menu_turmas()
            print(f'Você escolheu a opção {sub_opcao}')

            if sub_opcao == '0':
                print('Voltando ao Menu Principal...')
                break
            elif sub_opcao == '1':
                incluir_disciplina_ou_turmas(turmas, 'turmas')
            elif sub_opcao == '2':
                listar_cadastros(turmas, 'turma')
            elif sub_opcao == '3':
                atualizar_cadastro(turmas, 'turma')
            elif sub_opcao == '4':
                excluir_cadastro(turmas, 'turma')
            else:
                print('Opção inválida! Tente novamente.')

    elif opcao == '5':
        while True:
            sub_opcao = mostrar_sub_menu_matriculas()
            print(f'Você escolheu a opção {sub_opcao}')

            if sub_opcao == '0':
                print('Voltando ao Menu Principal...')
                break
            elif sub_opcao == '1':
                incluir_matricula(matriculas, 'matricula')
            elif sub_opcao == '2':
                listar_cadastros(matriculas, 'matriculas')
            elif sub_opcao == '3':
                atualizar_cadastro(matriculas, 'matricula')
            elif sub_opcao == '4':
                excluir_cadastro(matriculas, 'matricula')
            else:
                print('Opção inválida! Tente novamente.')

    return True


def mostrar_sub_menu_estudantes():
    print('----- MENU ESTUDANTES -----')
    print('(1) - Incluir.')
    print('(2) - Listar.')
    print('(3) - Atualizar.')
    print('(4) - Excluir.')
    print('(0) - Voltar ao Menu Principal.')

    return input('Informe a opção desejada: ')


def mostrar_sub_menu_professores():
    print('----- MENU PROFESSORES -----')
    print('(1) - Incluir.')
    print('(2) - Listar.')
    print('(3) - Atualizar.')
    print('(4) - Excluir.')
    print('(0) - Voltar ao Menu Principal.')

    return input('Informe a opção desejada: ')


def mostrar_sub_menu_disciplinas():
    print('----- MENU DISCIPLINAS -----')
    print('(1) - Incluir.')
    print('(2) - Listar.')
    print('(3) - Atualizar.')
    print('(4) - Excluir.')
    print('(0) - Voltar ao Menu Principal.')

    return input('Informe a opção desejada: ')


def mostrar_sub_menu_turmas():
    print('----- MENU TURMAS -----')
    print('(1) - Incluir.')
    print('(2) - Listar.')
    print('(3) - Atualizar.')
    print('(4) - Excluir.')
    print('(0) - Voltar ao Menu Principal.')

    return input('Informe a opção desejada: ')


def mostrar_sub_menu_matriculas():
    print('----- MENU MATRÍCULAS -----')
    print('(1) - Incluir.')
    print('(2) - Listar.')
    print('(3) - Atualizar.')
    print('(4) - Excluir.')
    print('(0) - Voltar ao Menu Principal.')

    return input('Informe a opção desejada: ')


def incluir_estudante_ou_professor(lista, tipo):
    print(f'----- INCLUIR {tipo.upper()} -----\n')
    codigo = input(f'Informe o código do {tipo}: ')

    for item in lista:
        if item[f'codigo_{tipo}'] == codigo:
            print('Código já cadastrado. Tente novamente.')
            return

    nome = input(f'Informe o nome do {tipo}: ')
    cpf = input(f'Informe o CPF do {tipo}: ')

    novo_item = {
        f'codigo_{tipo}': codigo,
        f'nome_{tipo}': nome,
        f'cpf_{tipo}': cpf
    }

    lista.append(novo_item)
    salvar_arquivo(lista, f'{tipo}s.json')
    print(f'Cadastro do {tipo} {nome} realizado com sucesso!')


def incluir_disciplina_ou_turmas(lista, tipo):
    print(f'----- INCLUIR {tipo.upper()} -----\n')
    tipo_chave = 'turma' if tipo == 'turmas' else tipo
    codigo = input(f'Informe o código da {tipo}: ')

    for item in lista:
        if item[f'codigo_{tipo_chave}'] == codigo:
            print('Código já cadastrado. Tente novamente.')
            return

    nome = input(f'Informe o nome da {tipo}: ')

    novo_item = {
        f'codigo_{tipo_chave}': codigo,
        f'nome_{tipo_chave}': nome
    }

    lista.append(novo_item)
    salvar_arquivo(lista, f'{tipo}s.json')
    print(f'Cadastro da {tipo} {nome} realizado com sucesso!')


def incluir_matricula(lista, tipo):
    print(f'----- INCLUIR MATRÍCULAS -----\n')
    codigo = input(f'Informe o código da {tipo}: ')

    if not codigo:
        print("O código da turma não pode ser vazio. Tente novamente.")
        return

    chave_codigo = f'codigo_{tipo}'

    for item in lista:
        if item.get(chave_codigo) == codigo:
            print(f'Código já cadastrado. Tente novamente.')
            return

    codigo_estudante = input(f'Informe o código do estudante: ')

    if not codigo_estudante:
        print("O código do estudante não pode ser vazio. Tente novamente.")
        return

    nome_estudante = input(f'Informe o nome do estudante: ')

    if not nome_estudante:
        print("O nome do estudante não pode ser vazio. Tente novamente.")
        return
    novo_item = {
        chave_codigo: codigo,
        'codigo_estudante': codigo_estudante,
        'nome_estudante': nome_estudante,
    }
    lista.append(novo_item)
    salvar_arquivo(lista, 'matriculas.json')
    print('Matrícula incluída com sucesso!')


def listar_cadastros(lista, tipo):
    tipo_singular = {
        'estudantes': 'estudante',
        'disciplinas': 'disciplina',
        'professores': 'professor',
        'turmas': 'turma',
        'matriculas': 'matricula'
    }.get(tipo, tipo)

    if not lista:
        print(f'Não há {tipo} cadastrados.')
    else:
        print(f'\n----- LISTAR {tipo.upper()} -----')
        for item in lista:
            if tipo == 'matriculas':
                print(f'- Código Matrícula: {item.get("codigo_matricula", "N/A")}')
                print(f'- Código Estudante: {item.get("codigo_estudante", "N/A")}')
                print(f'- Nome Estudante: {item.get("nome_estudante", "N/A")}')
            else:
                print(f'- Código: {item.get(f"codigo_{tipo_singular}", "N/A")}')
                print(f'- Nome: {item.get(f"nome_{tipo_singular}", "N/A")}')
            print('------------------')



def atualizar_cadastro(lista, tipo):
    print(f'\n----- ATUALIZAR {tipo.upper()} -----')
    codigo = input(f'Informe o código do {tipo} que deseja atualizar: ')

    for item in lista:
        if item[f'codigo_{tipo}'] == codigo:
            novo_codigo = input(f'Novo código do {tipo} (pressione Enter para manter o mesmo): ')
            novo_nome = input(f'Novo nome do {tipo} (pressione Enter para manter o mesmo): ')

            if f'cpf_{tipo}' in item:
                novo_cpf = input(f'Novo CPF do {tipo} (pressione Enter para manter o mesmo): ')
                if novo_cpf:
                    item[f'cpf_{tipo}'] = novo_cpf

            if novo_codigo:
                item[f'codigo_{tipo}'] = novo_codigo
            if novo_nome:
                item[f'nome_{tipo}'] = novo_nome

            salvar_arquivo(lista, f'{tipo}s.json')
            print(f'{tipo.capitalize()} atualizado com sucesso!')
            return

    print(f'{tipo.capitalize()} com código {codigo} não encontrado.')



def excluir_cadastro(lista, tipo):
    print(f'\n----- EXCLUIR {tipo.upper()} -----')
    codigo = input(f'Informe o código do {tipo} que deseja excluir: ')

    encontrado = False
    for item in lista:
        if item[f'codigo_{tipo}'] == codigo:
            lista.remove(item)
            salvar_arquivo(lista, f'{tipo}s.json')
            print(f'Cadastro do {tipo} {codigo} excluído com sucesso!')
            encontrado = True
            break

    if not encontrado:
        print(f'{tipo.capitalize()} não encontrado.')


def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            if not conteudo.strip():
                return []
            f.seek(0)
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


estudantes = carregar_arquivo('estudantes.json')
disciplinas = carregar_arquivo('disciplinas.json')
professores = carregar_arquivo('professores.json')
turmas = carregar_arquivo('turmas.json')
matriculas = carregar_arquivo('matriculas.json')

while True:
    opcao = mostrar_menu_principal()
    print(f'Você escolheu a opção {opcao}')

    if opcao == '0':
        print('Saindo do programa...')
        break
    elif opcao in ['1', '2', '3', '4', '5']:
        processar_sub_menu(opcao)
    else:
        print('Opção inválida! Tente novamente.')