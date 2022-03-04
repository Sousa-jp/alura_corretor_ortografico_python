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


def gerador_turbinado(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letras(fatias)
    palavras_geradas += inverte_letras(fatias)

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


def troca_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras


def inverte_letras(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras


def novo_corretor(palavra, vocabulario):
    palavras_geradas = gerador_palavras(palavra)
    palavras_turbinadas = gerador_turbinado(palavras_geradas)
    todas_palavras = set(palavras_turbinadas + palavras_geradas)
    candidatos = [palavra]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            candidatos.append(palavra)

    palavra_correta = max(candidatos, key=probabilidade)
    return palavra_correta


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


with open('artigos.txt', "r", encoding='utf-8') as f:
    artigos = f.read()

lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
lista_normalizada = normalizacao(lista_palavras)
total_palavras = len(set(lista_normalizada))
frequencia = nltk.FreqDist(lista_normalizada)

palavra_exemplo = 'lgóica'
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)
correcao = corretor(palavra_exemplo)
print(correcao)
