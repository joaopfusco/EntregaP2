import time
from subscriber import Subscriber
from get_postagem import get_postagem

def send_email(ch, method, properties, body):
    postagem_id = int(body.decode('utf-8'))
    postagem = get_postagem(postagem_id) 

    for participante in postagem["evento"]["participantes"]:
        texto = f"Nova postagem de {postagem["autor"]["nome"]} no evento {postagem["evento"]["nome"]}. Conteudo: {postagem["conteudo"]}"
        email = participante["usuario"]["email"]
        print(f"Enviando email para {email} com o texto: {texto}")
        time.sleep(1)
        print(f"Email enviado para {email} com sucesso!")

subscriber_email = Subscriber("minha-fila-email", send_email)
subscriber_email.start()
