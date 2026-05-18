import sys
import json
from datetime import datetime

def adicionar_tarefas():
    try:
        with open('bancoJSON.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
    except:
        tarefas = []
    id_tarefa = len(tarefas) + 1
    descricao_tarefa = input("Escreva a descrição da tarefa: ")
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

def listar_tarefas ():
    with open('bancoJSON.json', 'r') as arquivo:
        tarefas = json.load(arquivo)
    for item in tarefas:
        print(f"ID: {item['id']}")
        print(f"Nome da Atividade: {item['descricao']}")
        print(f"Status: {item['status']}")
        print(f"Data inclusão: {item['data']}\n------------------------")

comando = sys.argv[1]
if comando == "add":
    descricao = sys.argv[2]
    print("Executando a ação de adicionar a tarefa")
    adicionar_tarefas()
elif comando == "list":
    print("Executando a ação de listar todas as tarefas: ")
    listar_tarefas()
