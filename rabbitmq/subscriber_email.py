import pika
import time
from app.db.database import get_db
from app.services.postagem_service import PostagemService

def send_email(postagem_id):
    db = next(get_db())

    postagem_service = PostagemService()
    postagem = postagem_service.get_one(postagem_id, db)

    for participante in postagem.evento.participantes:
        texto = f"Nova postagem de {postagem.autor.nome} no evento {postagem.evento.nome}. Conteudo: {postagem.conteudo}"
        email = participante.usuario.email
        print(f"Enviando email para {email} com o texto: {texto}")
        time.sleep(1)
        print(f"Email enviado para {email} com sucesso!")

def subscribe():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    exchange_name = 'meu_exchange_fanout'
    channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

    queue_name = 'minha-fila-email'
    channel.queue_declare(queue=queue_name, durable=False, exclusive=False, auto_delete=False)
    channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key='')

    print("Aguardando mensagens.")

    def callback(ch, method, properties, body):
        postagem_id = body.decode('utf-8')
        try:
            send_email(int(postagem_id))
            print("Mensagem processada com sucesso!")
        except Exception as e:
            print(f"Erro ao processar a mensagem: {str(e)}")
        ch.stop_consuming()

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
