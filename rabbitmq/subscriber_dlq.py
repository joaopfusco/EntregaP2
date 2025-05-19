from subscriber import Subscriber

def callback(ch, method, properties, body):
    try:
        print(body.decode('utf-8'))
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Erro no processamento: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

subscriber_dlq = Subscriber("minha-dlq", callback)
subscriber_dlq.start()
