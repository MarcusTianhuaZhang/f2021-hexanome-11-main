from shutil import move
from phase3 import Phase3
from phase4 import Phase4
from phase5 import Phase5
from command import *

def execute(i, p1, opponents, game):
    if i == 3:
        phase = Phase3(p1)
        index = phase.clickedTransportCard(p1.clicked[0], p1.clicked[1])
        print("• Setting up the command for phase3")
        p1.command = drawTCCommand(p1, index)
        print(" • Player's command is now drawTCCommand.")
        return p1, opponents, game
    elif i == 4:
        phase = Phase4(p1)
        index = phase.clickedTransportCard(p1.clicked[0], p1.clicked[1])
        print("• Setting up the command for phase4")
        p1.command = placeTCOnPathCommand(p1, index)
        print(" • Player's command is now placeTCOmPathCommand.")
        return p1, opponents, game
    elif i ==5 and p1.clicked[0] < 983:
        phase = Phase5(p1)
        p1.command = moveBootCommand(p1)
        return p1, opponents,game
    elif i == 6:
        from phase6 import Phase6
        phase = Phase6(p1)
        index = phase.clickedTransportCard(p1.clicked[0], p1.clicked[1])
        p1.command = removeTCCommand(p1,index)
        return p1, opponents,game
    #     p1.command = resetRoundCommand(p1)
    #     p1 = p1.command.execute(game)
    #     game.update(p1)
    #     tmp = []
    #     for a in opponents:
    #         a = resetRoundCommand(a).execute(game)
    #         tmp.append(a)
    #         game.update(a)
    #     opponents = tmp
    #     print("resetting round in Phase.py")
    else:
        return p1,opponents,game

                       
