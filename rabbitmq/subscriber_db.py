import requests
from subscriber import Subscriber
from get_postagem import get_postagem

def put_participantes(ch, method, properties, body):
    postagem_id = int(body.decode('utf-8'))
    postagem = get_postagem(postagem_id)    

    for participante in postagem["evento"]["participantes"]:
        texto = f"Nova postagem de {postagem["autor"]["nome"]} no evento {postagem["evento"]["nome"]}. Conteudo: {postagem["conteudo"]}"
        url = f'http://localhost:8000/participantes/{participante["id"]}'
        headers = {'Content-Type': 'application/json'}
        data = {
            "usuario_id": participante["usuario_id"],
            "evento_id": participante["evento_id"],
            "ultima_notificacao": texto
        }
        response = requests.put(url, json=data, headers=headers)
        if response.status_code == 200:
            print(f"Participante {participante["id"]} atualizado com sucesso!")
        else:
            print(f"Erro ao adicionar participante: {response.status_code} - {response.text}")

subscriber_db = Subscriber("minha-fila-db", put_participantes)
subscriber_db.start()
