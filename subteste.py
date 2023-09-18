import requests

# URL da API
url = 'http://127.0.0.1:8000/api/posts/'

# Dados que você deseja enviar no corpo da solicitação POST
dados = {
    'nome': 'Nome do Produto',
    'quantidade': 10,
    'categoria': 'Categoria do Produto',
    'preco': 20.99,
    'lucro': 5.0,
    'imageUrl': 'http://example.com/imagem.jpg'
}






# Enviar a solicitação POST
try:
    response = requests.post(url, json=dados)

    # Verificar se a solicitação foi bem-sucedida (código de status HTTP 2xx)
    if response.status_code >= 200 and response.status_code < 300:
        print('Solicitação POST bem-sucedida!')
        print('Resposta da API:')
        print(response.json())
    else:
        print('Erro na solicitação POST. Código de status HTTP:', response.status_code)
        print('Resposta da API:')
        print(response.text)
except requests.exceptions.RequestException as e:
    print('Erro na solicitação POST:', e)
