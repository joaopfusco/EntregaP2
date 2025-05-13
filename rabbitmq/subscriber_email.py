import time
from subscriber import Subscriber
from get_postagem import get_postagem

def send_email(ch, method, properties, body):
    try:
        postagem_id = int(body.decode('utf-8'))
        postagem = get_postagem(postagem_id) 

        for participante in postagem["evento"]["participantes"]:
            texto = f"Nova postagem de {postagem["autor"]["nome"]} no evento {postagem["evento"]["nome"]}. Conteudo: {postagem["conteudo"]}"
            email = participante["usuario"]["email"]
            print(f"Enviando email para {email} com o texto: {texto}")
            time.sleep(1)
            print(f"Email enviado para {email} com sucesso!")
        
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Erro no processamento: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

subscriber_email = Subscriber("minha-fila-email", send_email, dlq_enabled=True)
subscriber_email.start()
