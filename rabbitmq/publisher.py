import pika

class Publisher:
    def __init__(self):
        self.__host = "localhost"
        self.__exchange = "meu_exchange_fanout"
        self.__routing_key = ""
        self.__channel = self.__create_channel()
    
    def __create_channel(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.__host))
        channel = connection.channel()
        channel.exchange_declare(exchange=self.__exchange, exchange_type='fanout')
        return channel

    def send_message(self, body):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=str(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        print("Mensagem enviada!")

# publisher = Publisher()
# publisher.send_message("ola mundo!")
