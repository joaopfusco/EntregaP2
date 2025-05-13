import pika

def publish(postagem_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='minha_fila')

    channel.basic_publish(exchange='',
                        routing_key='minha_fila',
                        body=str(postagem_id))

    print(" [x] Mensagem enviada!")

    connection.close()
