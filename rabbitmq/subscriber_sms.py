import time
from subscriber import Subscriber
from get_postagem import get_postagem

def send_sms(ch, method, properties, body):
    postagem_id = int(body.decode('utf-8'))
    postagem = get_postagem(postagem_id) 

    for participante in postagem["evento"]["participantes"]:
        texto = f"Nova postagem de {postagem["autor"]["nome"]} no evento {postagem["evento"]["nome"]}. Conteudo: {postagem["conteudo"]}"
        telefone = participante["usuario"]["telefone"]
        print(f"Enviando sms para {telefone} com o texto: {texto}")
        time.sleep(1)
        print(f"sms enviado para {telefone} com sucesso!")

subscriber_sms = Subscriber("minha-fila-sms", send_sms)
subscriber_sms.start()
