import random
espadas = "♠"
copas = "♥"
ouros = "♦"
paus = "♣"
UM = ás = "A"
rei = reis = "K"
dama = damas = "Q"
valete = "J"

class card:
    def __init__(self, value, naipe):
        if value == "A" or value == "a" or value == "as" or value == "ás":
            self.value = 1
        elif value == "j" or value == "J":
            self.value = 11
        elif value == "q" or value == "Q":
            self.value = 12
        elif value == "k" or value == "K":
            self.value = 13
        else:
            self.value = value
        self.naipe = naipe
        
    def __str__(self):
        if self.value == 1:
            a = "A"
        elif self.value == 11:
            a = "J"
        elif self.value == 12:
            a = "Q"
        elif self.value == 13:
            a = "K"
        else:
            a = str(self.value)
        b = str(" de ")
        c = str(self.naipe)
        
        return (a+b+c)
    def __repr__(self):
        return self.__str__()
    
class deck:
    def __init__(self):
        self.barai = self.criar_deck()
    def __str__(self):
        return str(self.barai)
    def __repr__(self):
        return str(self.barai)
        
    def criar_deck(self):
        deck = []
        for cont in [espadas, copas, ouros, paus]:
            for cont2 in range(1,14):
                carta = card(cont2,cont)
                deck.append(carta)
        return deck

    def embaralhar(self):
        random.shuffle(self.barai)
        return True
    def comprar(self):
        return self.barai.pop(0)

class mao:
    def __init__(self):
        cartas = []
        self.cartas = cartas

    def comprar(self, deck, cartas = 1):
        self.cartas.append(deck.comprar())
        
    def __str__(self):
        return(str(self.cartas))
    
    def __repr__(self):
        return (self.__str__())

class player:
    def __init__(self,  mao, nome="Player"):
        self.mao = mao
        self.nome = nome

    def __str__(self):
        textin = "O jogador "
        textin+= self.nome
        textin+= " tem "
        textin+= str(len(self.mao.cartas))
        textin+= " carta(s)"
        return(textin)
