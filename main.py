import BankruptCore
import time

qtdPartidas = 300
qtdVitorias = [0,0,0,0]
totalRodadas = 0
qtdTimeOut = 0

if __name__ == '__main__':
    start_time = time.time()
    for i in range (qtdPartidas):
        Retorno = BankruptCore.StartGame()
        qtdVitorias[Retorno[0]-1] = qtdVitorias[Retorno[0]-1]+1
        totalRodadas = totalRodadas + Retorno[1]
        if Retorno[2]:
            qtdTimeOut = qtdTimeOut + 1
        
    elapsed_time = time.time() - start_time
    print("Tempo de execução: ",time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    print("Partidas executadas: ", qtdPartidas)
    print("Vitorias de cada jogador: ", qtdVitorias)
    print("Media de rodadas: ", totalRodadas//qtdPartidas)
    print("Partidas finalizadas por TimeOut: ",qtdTimeOut)
    print("Maior vencedor: Jogador",BankruptCore.getMostWinner(qtdVitorias))
    WinPercentage = BankruptCore.getWinPercentage(qtdVitorias,qtdPartidas)
    print("Porcentagem de vitória de cada jogador: \n","Jogador 1: ",WinPercentage[0],"%  Jogador 2: ",WinPercentage[1],"%  Jogador 3: ",WinPercentage[2],"%  Jogador 4: ",WinPercentage[3],"%")



input("Pressione enter para finalizar")
