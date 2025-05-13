import pika
import requests
from app.db.database import get_db 
from app.services.postagem_service import PostagemService
from app.schemas.participante_schema import ParticipanteIn

def put_participantes(postagem_id):
    db = next(get_db())

    postagem_service = PostagemService()
    postagem = postagem_service.get_one(postagem_id, db)

    for participante in postagem.evento.participantes:
        texto = f"Nova postagem de {postagem.autor.nome} no evento {postagem.evento.nome}. Conteudo: {postagem.conteudo}"
        participante.ultima_notificacao = texto

        url = f'http://localhost:8000/participantes/{participante.id}'
        headers = {'Content-Type': 'application/json'}
        data = {
            "usuario_id": participante.usuario_id,
            "evento_id": participante.evento_id,
            "ultima_notificacao": participante.ultima_notificacao
        }
        response = requests.put(url, json=data, headers=headers)
        if response.status_code == 200:
            print(f"Participante {participante.id} atualizado com sucesso!")
        else:
            print(f"Erro ao adicionar participante: {response.status_code} - {response.text}")

def subscribe():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    exchange_name = 'meu_exchange_fanout'
    channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

    queue_name = 'minha-fila-db'
    channel.queue_declare(queue=queue_name, durable=False, exclusive=False, auto_delete=False)
    channel.queue_bind(queue=queue_name, exchange=exchange_name)

    print("Aguardando mensagens.")

    def callback(ch, method, properties, body):
        postagem_id = body.decode('utf-8')
        try:
            put_participantes(int(postagem_id))
            print("Mensagem processada com sucesso!")
        except Exception as e:
            print(f"Erro ao processar a mensagem: {str(e)}")
        ch.stop_consuming()

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
