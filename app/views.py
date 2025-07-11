from django.shortcuts import render

def index(request):

    # PLACAR DA ÚLTIMA PARTIDA:
    partida = {
        "competicao": "Eliminatórias da Copa do Mundo",
        "data": "10/06",
        "status": "Encerrado",
        "casa": {
            "nome": "Brasil",
            "bandeira": "blog/brasil.png",
            "gols": 1
        },
        "visitante": {
            "nome": "Paraguai",
            "bandeira": "blog/paraguai.png",
            "gols": 0
        },
        "artilheiro": "Vinícius Júnior 44'"
    }

    # iNFORMAÇÕES DA PAGINA:
    inicio = {
        "titulo": "Bem-vindo ao site da Seleção Brasileira!",
        "subtitulo": "Orgulho nacional, paixão mundial. A única pentacampeã do mundo.", 
        "historia": "Com cinco títulos mundiais e ídolos imortais como Pelé, Ronaldo, Ronaldinho e Neymar, a Seleção Brasileira encanta gerações com futebol arte.",
    }

    return render(request, 'blog/index.html', {"partida":partida, "inicio": inicio})

def jogadores(request):

    elenco = [

        {"nome": "Alisson", "idade": 32, "posicao": "Goleiro", "imagem": "blog/alisson.jpg", "nascimento": "Novo Hamburgo, RS"},
        {"nome": "Danilo", "idade": 33, "posicao": "Zagueiro", "imagem": "blog/danilo.jpg", "nascimento": "Bicas, MG"},
        {"nome": "Marquinhos", "idade": 31, "posicao": "Zagueiro", "imagem": "blog/marquinhos.webp", "nascimento": "São Paulo, SP"},
        {"nome": "Vanderson", "idade": 26, "posicao": "Lateral-Direito", "imagem": "blog/vanderson.png", "nascimento": "Rondonópolis, MT"},
        {"nome": "Alex Sandro", "idade": 34, "posicao": "Lateral-Esquerdo", "imagem": "blog/alexsandro.webp", "nascimento": "Catanduva, SP"},
        {"nome": "Casemiro", "idade": 33, "posicao": "Volante", "imagem": "blog/casemiro.jpg", "nascimento": "São José dos Campos, SP"},
        {"nome": "Bruno Guimarães", "idade": 29, "posicao": "Meio‑Campista", "imagem": "blog/bruno.jpg", "nascimento": "Rio de Janeiro, RJ"},
        {"nome": "Gerson", "idade": 28, "posicao": "Meio‑Campista", "imagem": "blog/gerson.webp", "nascimento": "Belford Roxo, RJ"},
        {"nome": "Vinícius Júnior", "idade": 24, "posicao": "Atacante", "imagem": "blog/vini.jpg", "nascimento": "São Gonçalo, RJ"},
        {"nome": "Raphinha", "idade": 28, "posicao": "Atacante", "imagem": "blog/raphinha.jpg", "nascimento": "Porto Alegre, RS"},
        {"nome": "Richarlison", "idade": 28, "posicao": "Atacante", "imagem": "blog/richarlison.jpg", "nascimento": "Nova Venécia, ES"},
        {"nome": "Gabriel Martinelli", "idade": 23, "posicao": "Atacante", "imagem": "blog/martinelli.png", "nascimento": "Guarulhos, SP"},
        {"nome": "Matheus Cunha", "idade": 25, "posicao": "Atacante", "imagem": "blog/cunha.jpg", "nascimento": "João Pessoa, PB"},
    ]

    return render(request, 'blog/jogadores.html', {'elenco': elenco})


def sobre(request):

    sobre = [
        {
            "titulo": "Sobre o Projeto", "subtitulo": "Site da seleção brasileira.", "criador": "Desenvolvido por Gustavo Lunnyê e Otton Pierre."
        }
    ]

    return render(request, 'blog/sobre.html', {'sobre':sobre})
