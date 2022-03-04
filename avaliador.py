from corretor import corretor, lista_normalizada


def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    taxa_desconhecida = round(desconhecida * 100 / numero_palavras, 2)

    print(f'{taxa_acerto}% de {numero_palavras} palavras, desconhecida é {taxa_desconhecida}')
