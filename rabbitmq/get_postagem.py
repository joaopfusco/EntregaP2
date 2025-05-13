import requests

def get_postagem(postagem_id): 
    url = f'http://localhost:8000/postagens/{postagem_id}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        postagem = response.json()
        return postagem
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None
