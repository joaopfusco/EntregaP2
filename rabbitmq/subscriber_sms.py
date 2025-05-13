import time
from subscriber import Subscriber
from get_postagem import get_postagem

def send_sms(ch, method, properties, body):
    try:
        postagem_id = int(body.decode('utf-8'))
        postagem = get_postagem(postagem_id) 

        for participante in postagem["evento"]["participantes"]:
            texto = f"Nova postagem de {postagem["autor"]["nome"]} no evento {postagem["evento"]["nome"]}. Conteudo: {postagem["conteudo"]}"
            telefone = participante["usuario"]["telefone"]
            print(f"Enviando sms para {telefone} com o texto: {texto}")
            time.sleep(1)
            print(f"sms enviado para {telefone} com sucesso!")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Erro no processamento: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

subscriber_sms = Subscriber("minha-fila-sms", send_sms, dlq_enabled=True)
subscriber_sms.start()
