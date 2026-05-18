import sys
import json
from datetime import datetime

def adicionar_tarefas():
    try:
        with open('bancoJSON.json', 'r',encoding='utf-8') as arquivo:
            tarefas = json.load(arquivo)
    except:
        tarefas = []
    id_tarefa = len(tarefas) + 1
    descricao_tarefa = (sys.argv[2])
    status = 'todo'
    create_date = datetime.now().isoformat()
    update_date = datetime.now().isoformat()
    nova_tarefa = {
        'id': id_tarefa,
        'descricao': descricao_tarefa,
        'status': 'todo',
        'data': create_date,
        'dataup': update_date
    }
    tarefas.append(nova_tarefa)
    with open('bancoJSON.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent= 4)
    print(f"Tarefa adicionada com sucesso (ID: {id_tarefa})")

def atualizar_tarefa():
    with open("bancoJSON.json", "r",encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    id_desejado = int(sys.argv[2])
    for tarefa in tarefas:
        if tarefa.get('id') == id_desejado:
            nova_descricao = (sys.argv[3])
            tarefa["descricao"] = nova_descricao
            tarefa["dataup"] = datetime.now().isoformat()
            break
    with open('bancoJSON.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def deletar_tarefa():
    with open("bancoJSON.json", "r",encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    id_desejado = int(sys.argv[2])
    for tarefa in tarefas:
        if tarefa.get('id') == id_desejado:
            tarefas.remove(tarefa)
            break
    with open('bancoJSON.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def listar_tarefas (filtro_status=None):
    with open('bancoJSON.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    for item in tarefas:
        status = item.get("status", "todo")
        if filtro_status is None or status == filtro_status:
            print(f"ID: {item['id']}")
            print(f"Nome da Atividade: {item['descricao']}")
            print(f"Status: {item['status']}")
            print(f"Data inclusão: {item['data']}")
            print(f"Data Alteração: {item['dataup']}\n------------------------")

def marcar_progresso():
    with open("bancoJSON.json", "r",encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    id_desejado = int(sys.argv[2])
    for tarefa in tarefas:
        if tarefa.get('id') == id_desejado:
            novo_status = "em-progresso"
            tarefa["status"] = novo_status
            tarefa["dataup"] = datetime.now().isoformat()
            break
    with open('bancoJSON.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def marcar_feita():
    with open("bancoJSON.json", "r",encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    id_desejado = int(sys.argv[2])
    for tarefa in tarefas:
        if tarefa.get('id') == id_desejado:
            novo_status = "feita"
            tarefa["status"] = novo_status
            tarefa["dataup"] = datetime.now().isoformat()
            break
    with open('bancoJSON.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

comando = sys.argv[1]
if comando == "add":
    descricao = sys.argv[2]
    print("Executando a ação de adicionar a tarefa")
    adicionar_tarefas()
elif comando == "list":
    status_desejado = sys.argv[2]
    print("Executando a ação de listar todas as tarefas: ")
    listar_tarefas(status_desejado)
elif comando == "update":
    id_desejado = sys.argv[2]
    nova_descricao = sys.argv[3]
    print("Executando a ação de atualizar as tarefas: ")
    atualizar_tarefa()
elif comando == "delete":
    id_desejado = sys.argv[2]
    print("Executando a ação de deletar")
    deletar_tarefa()
elif comando == "mark-in-progress":
    id_desejado = sys.argv[2]
    marcar_progresso()
    print("Tarefa marcada em-progresso.")
elif comando == "mark-done":
    id_desejado = sys.argv[2]
    marcar_feita()
    print("Tarefa feita.")