from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Javascript",
        "descricao": "Estudar para a prova de matemática",
        "status": "Em andamento",
        "prioridade": "Alta",
        "data_criacao": "2025-02-25",
        "responsavel": "Mariana"
    },
    {
        "id": 2,
        "titulo": "Estudar",
        "descricao": "Fazer a janta, lavar os uniformes, pintar unhas",
        "status": "Não iniciado",
        "prioridade": "Média",
        "data_criacao": "2025-02-25",
        "responsavel": "Mariana"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tarefas)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/task', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1 if tarefas else 1
    task['id'] = ultimo_id
    task.setdefault('prioridade', "Baixa")
    task.setdefault('data_criacao', "2025-02-25")
    task.setdefault('responsavel', "Desconhecido")

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id
            task_body = request.json({
                "titulo": task_body.get("titulo", tarefa["titulo"]),
                "descricao": task_body.get("descricao", tarefa["descricao"]),
                "status": task_body.get("status", tarefa["status"]),
                "prioridade": task_body.get("prioridade", tarefa["prioridade"]),
                "data_criacao": task_body.get("data_criacao", tarefa["data_criacao"]),
                "responsavel": task_body.get("responsavel", tarefa["responsavel"])
            })
            return.json(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
