from django.shortcuts import render
import requests

def index(request):
    query = request.GET.get('query', '')
    filmes = []
    populares = []

    if query:
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "Coloque Sua API aqui",
            "query": query,
            "language": "pt-BR"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            filmes = data.get('results', [])
    else:

        url = "https://api.themoviedb.org/3/movie/popular"
        params = {
            "api_key": "Coloque Sua API aqui",
            "language": "pt-BR"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            populares = data.get('results', [])

    template_name = 'index.html'
    contexto = {
        'filmes': filmes,
        'populares': populares
    }
    return render(request, template_name, contexto)

def detalhes(request, filme_id):
    url = f"https://api.themoviedb.org/3/movie/{filme_id}"
    params = {
        "api_key": "Coloque Sua API aqui",
        "language": "pt-BR"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        filme = response.json()
    else:
        filme = {}

    template_name = 'detalhes.html'
    contexto = {
        'filme': filme
    }
    return render(request, template_name, contexto)
