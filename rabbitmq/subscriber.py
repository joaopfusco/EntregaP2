import pika

class Subscriber:
    def __init__(self, queue, callback) -> None:
        self.__host = "localhost"
        self.__exchange = "meu_exchange_fanout"
        self.__queue = queue
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.__host))

        channel = connection.channel()
        channel.exchange_declare(exchange=self.__exchange, exchange_type="fanout")

        channel.queue_declare(queue=self.__queue, durable=True)
        channel.queue_bind(exchange=self.__exchange, queue=self.__queue)

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )
        
        return channel
        
    def start(self):
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()

# def minha_callback(ch, method, properties, body):
#     print(body)

# subscriber = Subscriber("queue_teste", minha_callback)
# subscriber.start()