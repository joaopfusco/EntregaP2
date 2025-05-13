import pika

class Subscriber:
    def __init__(self, queue, callback, dlq_enabled=False) -> None:
        self.__host = "localhost"
        self.__exchange = "meu_exchange_fanout"
        self.__queue = queue
        self.__callback = callback
        self.__dlq_enabled = dlq_enabled
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.__host))
        channel = connection.channel()
        
        channel.exchange_declare(exchange=self.__exchange, exchange_type="fanout")

        if self.__dlq_enabled:
            dlx_exchange = "dlx_exchange"
            dlq_name = "minha-dlq"

            channel.exchange_declare(exchange=dlx_exchange, exchange_type='fanout')
            
            channel.queue_declare(queue=dlq_name, durable=True)
            channel.queue_bind(exchange=dlx_exchange, queue=dlq_name)

            args = {
                'x-message-ttl': 10000,
                'x-dead-letter-exchange': dlx_exchange
            }
        else:
            args = {}

        channel.queue_declare(queue=self.__queue, durable=True, arguments=args)
        channel.queue_bind(exchange=self.__exchange, queue=self.__queue)

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=False,
            on_message_callback=self.__callback
        )
        
        return channel
        
    def start(self):
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()
