import nltk


def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras


def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)

    return palavras_geradas


def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras


def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras


def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta


def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada] / total_palavras


def cria_dados_testes(nome_arquivo):
    lista_palavras_teste = []
    with open(nome_arquivo) as f:
        for linha in f:
            correta, errada = linha.split()
            lista_palavras_teste.append((correta, errada))

    return lista_palavras_teste


def avaliador(testes):
    numero_palavras = len(testes)
    acertou = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1

    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    print(f'{taxa_acerto}% de {numero_palavras} palavras')


with open('artigos.txt', "r", encoding='utf-8') as f:
    artigos = f.read()

lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
lista_normalizada = normalizacao(lista_palavras)
total_palavras = len(set(lista_normalizada))
frequencia = nltk.FreqDist(lista_normalizada)

palavra_exemplo = 'lgica'
correcao = corretor(palavra_exemplo)
print(correcao)
