import pika

def publish(postagem_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    exchange_name = 'meu_exchange_fanout'
    channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

    channel.basic_publish(
        exchange=exchange_name,
        routing_key='',
        body=str(postagem_id)
    )

    print(" [x] Mensagem enviada!")

    connection.close()
