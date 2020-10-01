import random

def StartGame():
    Jogadores = []
    for x in range(4):
        Jogadores.append(Player(x+1, True, 300, 0))

    DadosPropriedades = open("gameConfig (1).txt")
    Propriedades = []
    for y in DadosPropriedades:
        aux = y.replace("  "," ")
        aux = aux.replace("\n","")
        aux = aux.split(" ")
        Propriedades.append(Property('',int(aux[0]), int(aux[1])))

    emJogo = [str(q.name) for q in Jogadores]
    numRodadas = 1
    timeOut = False
    executandoJogo = True

    while (executandoJogo):
        if numRodadas < 1000 and len(emJogo) >= 2:
            for jogador in Jogadores:
                #DebugShowPlayerInfo(jogador)
                dado = random.randint(1,6)
                jogador.step = jogador.step + dado

                if jogador.step > len(Propriedades):
                    jogador.step = jogador.step - len(Propriedades)
                    jogador.money = jogador.money + 100

                if Propriedades[jogador.step-1].owner == "":
                    jogador.PlayerDecision(Propriedades[jogador.step-1])

                if Propriedades[jogador.step-1].owner != "" and Propriedades[jogador.step-1].owner != jogador.name:
                    PayPlayer(Jogadores,Propriedades[jogador.step-1],jogador)
                    if jogador.money <= 0:
                        PlayerGameOver(Jogadores,jogador, Propriedades,emJogo)


            numRodadas = numRodadas +1

        if len(emJogo) < 2:
            executandoJogo = False
            vencedor = emJogo[0]
        if numRodadas >= 1000:
            vencedor = getRicherPlayer(Jogadores)
            timeOut = True
            executandoJogo = False
            

    return [int(vencedor),numRodadas,timeOut]
            
class Player:
    def __init__(self,name,inGame,money,step):
        self.name = name
        self.inGame = inGame
        self.money = money
        self.step = step

    def PlayerDecision(self, Property):
        aux = self.name
        #print(aux)
        rand = random.randint(0,100)
        if aux == 1 and self.money > Property.buyPrice:
            Property.owner = self.name
            self.money = self.money - Property.buyPrice
        if aux == 2 and self.money > Property.buyPrice and Property.rentPrice > 50:
            Property.owner = self.name
            self.money = self.money - Property.buyPrice
        if aux == 3 and self.money > Property.buyPrice and (self.money - Property.buyPrice > 80):
            Property.owner = self.name
            self.money = self.money - Property.buyPrice
        if aux == 4 and self.money > Property.buyPrice and rand>=50:
            Property.owner = self.name
            self.money = self.money - Property.buyPrice

class Property:
    def __init__(self,owner,buyPrice,rentPrice):
        self.owner = owner
        self.buyPrice = buyPrice
        self.rentPrice = rentPrice

def CleanProperties(Properties,playerName):
    for x in range (len(Properties)):
        if Properties[x].owner == playerName:
            Properties[x].owner = ''

def PlayerGameOver(Players,player, Properties,RemainingPlayers):
    player.inGame = False
    RemainingPlayers.remove(str(player.name))
    CleanProperties(Properties,player.name)
    for x in range (len(Players)):
        if Players[x].name == player.name:
            Players.pop(x)
            break
    

def PayPlayer(Players,Property,Payer):
    Payer.money = Payer.money - Property.rentPrice
    for x in range (len(Players)):
        if Players[x].name == Property.owner:
            aux = x
    if Players[aux].name != Payer.name:
        Players[aux].money = Players[aux].money + Property.rentPrice

def getRicherPlayer(Players):
    aux = Player(999,True,-1,0)
    for x in Players:
        if aux.money < x.money:
            aux = x
    return aux.name

def DebugShowPlayerInfo(Player):
    print("\n\n")
    print(" Turno do jogador ", Player.name)
    print(" Dinheiro do jogador: ", Player.money)
    print(" O jogador está na casa: ", Player.step)

def getMostWinner(WinnerList):
    aux = [-1,-1]
    for x in range (len(WinnerList)-1):
        if aux[0] < WinnerList[x]:
            aux[1] = x
            aux[0] = WinnerList[x]
    return aux[1]+1

def getWinPercentage(WinCountList,QtyGames):
    for x in range (len(WinCountList)):
        WinCountList[x] = round(100* (WinCountList[x]/QtyGames),2)
    return WinCountList
        
