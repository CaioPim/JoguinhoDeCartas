import testecarta as baralho

def main():
    deck = baralho.deck()
    deck.embaralhar
    mao = baralho.mao()
    mao.comprar(deck, 5)
    jogador = baralho.player(mao)
    print(jogador)
    print(jogador.mao)

    return True

main()