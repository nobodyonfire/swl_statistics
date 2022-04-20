import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from termcolor import colored
import os


from .functions import *
from .plotfunctions import *


BluePlayer = "SafSouf"
RedPlayer = "MutigerGoblin"

xatt = ['CRIT', 'TOUCHE', 'SURGE', 'MISS']
xdef = ['BLOCKED', 'SURGE', 'MISS']
colors = {'b':'blue','r':'red','n':'grey'}

attRedDice = [1/8,5/8,1/8,1/8]
attBlackDice = [1/8,3/8,1/8,3/8]
attWhiteDice = [1/8,1/8,1/8,5/8]
defRedDice = [3/6,1/6,2/6]
defWhiteDice = [1/6,1/6,4/6]

def main():

    csv_path = "././polls/csv/"
    mainDf = pd.read_csv(os.path.join(csv_path,"swlcsv.csv"), sep=";")


    returnDict = calculations()

    return returnDict


def calculations():
    numberDiceLaunched = count_number_dice(player=None,attOrDef=None,colorDice=None)

    numberDiceLaunchedBlue = count_number_dice(player='b',attOrDef=None,colorDice=None)
    numberDiceLaunchedBlueAtt = count_number_dice(player='b',attOrDef='att',colorDice=None)
    numberDiceLaunchedBlueDef = count_number_dice(player='b',attOrDef='def',colorDice=None)

    numberDiceLaunchedRed = count_number_dice(player='r',attOrDef=None,colorDice=None)
    numberDiceLaunchedRedAtt = count_number_dice(player='r',attOrDef='att',colorDice=None)
    numberDiceLaunchedRedDef = count_number_dice(player='r',attOrDef='def',colorDice=None)

    #Blue Player
    numberDiceBlueRedAttLaunched = count_number_dice(player='b',attOrDef='att',colorDice='r')
    numberDiceBlueBlackAttLaunched = count_number_dice(player='b',attOrDef='att',colorDice='b')
    numberDiceBlueWhiteAttLaunched = count_number_dice(player='b',attOrDef='att',colorDice='w')
    numberDiceBlueRedDefLaunched = count_number_dice(player='b',attOrDef='def',colorDice='r')
    numberDiceBlueWhiteDefLaunched = count_number_dice(player='b',attOrDef='def',colorDice='w')

    #Red Player
    numberDiceRedRedAttLaunched = count_number_dice(player='r',attOrDef='att',colorDice='r')
    numberDiceRedBlackAttLaunched = count_number_dice(player='r',attOrDef='att',colorDice='b')
    numberDiceRedWhiteAttLaunched = count_number_dice(player='r',attOrDef='att',colorDice='w')
    numberDiceRedRedDefLaunched = count_number_dice(player='r',attOrDef='def',colorDice='r')
    numberDiceRedWhiteDefLaunched = count_number_dice(player='r',attOrDef='def',colorDice='w')

    #general
    numberDiceRedAttLaunched = numberDiceRedRedAttLaunched + numberDiceBlueRedAttLaunched
    numberDiceBlackAttLaunched = numberDiceRedBlackAttLaunched + numberDiceBlueBlackAttLaunched
    numberDiceWhiteAttLaunched = numberDiceRedWhiteAttLaunched + numberDiceBlueWhiteAttLaunched
    numberDiceRedDefLaunched = numberDiceRedRedDefLaunched + numberDiceBlueRedDefLaunched
    numberDiceWhiteDefLaunched = numberDiceRedWhiteDefLaunched + numberDiceBlueWhiteDefLaunched



    #Blue player probability
    attBlueRedDice,attBlueRedDiceSize = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r')
    attBlueBlackDice,attBlueBlackDiceSize = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b')
    attBlueWhiteDice,attBlueWhiteDiceSize = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w')
    defBlueRedDice,defBlueRedDiceSize = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r')
    defBlueWhiteDice,defBlueWhiteDiceSize = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w')

    BlueListSize = [attBlueRedDiceSize,attBlueBlackDiceSize,attBlueWhiteDiceSize,defBlueRedDiceSize,defBlueWhiteDiceSize]
    BlueListSize = function_resize_for_bins(BlueListSize)

    #Red player probability
    attRedRedDice,attRedRedDiceSize = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r')
    attRedBlackDice,attRedBlackDiceSize = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b')
    attRedWhiteDice,attRedWhiteDiceSize= calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w')
    defRedRedDice,defRedRedDiceSize = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r')
    defRedWhiteDice,defRedWhiteDiceSize = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w')

    RedListSize = [attRedRedDiceSize,attRedBlackDiceSize,attRedWhiteDiceSize,defRedRedDiceSize,defRedWhiteDiceSize]
    RedListSize = function_resize_for_bins(RedListSize)

    attRedList = [attBlueRedDice,attRedDice,attRedRedDice]
    attBlackList = [attBlueBlackDice,attBlackDice,attRedBlackDice]
    attWhiteList = [attBlueWhiteDice,attWhiteDice,attRedWhiteDice]
    defRedList = [defBlueRedDice,defRedDice,defRedRedDice]
    defWhiteList = [defBlueWhiteDice,defWhiteDice,defRedWhiteDice]


     #Blue player probability
    #round1
    attBlueRedDiceRound1,attBlueRedDiceRound1Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=1)
    attBlueBlackDiceRound1,attBlueBlackDiceRound1Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b',round=1)
    attBlueWhiteDiceRound1,attBlueWhiteDiceRound1Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w',round=1)
    defBlueRedDiceRound1,defBlueRedDiceRound1Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r',round=1)
    defBlueWhiteDiceRound1,defBlueWhiteDiceRound1Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w',round=1)

    BlueListSizeRound1 = [attBlueRedDiceRound1Size,attBlueBlackDiceRound1Size,attBlueWhiteDiceRound1Size,
                        defBlueRedDiceRound1Size,defBlueWhiteDiceRound1Size]
    BlueListSizeRound1 = function_resize_for_bins(BlueListSizeRound1)

    #round2
    attBlueRedDiceRound2,attBlueRedDiceRound2Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=2)
    attBlueBlackDiceRound2,attBlueBlackDiceRound2Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b',round=2)
    attBlueWhiteDiceRound2,attBlueWhiteDiceRound2Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w',round=2)
    defBlueRedDiceRound2,defBlueRedDiceRound2Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r',round=2)
    defBlueWhiteDiceRound2,defBlueWhiteDiceRound2Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w',round=2)

    BlueListSizeRound2 = [attBlueRedDiceRound2Size,attBlueBlackDiceRound2Size,attBlueWhiteDiceRound2Size,
                        defBlueRedDiceRound2Size,defBlueWhiteDiceRound2Size]
    BlueListSizeRound2 = function_resize_for_bins(BlueListSizeRound2)

    #round3
    attBlueRedDiceRound3,attBlueRedDiceRound3Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=3)
    attBlueBlackDiceRound3,attBlueBlackDiceRound3Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b',round=3)
    attBlueWhiteDiceRound3,attBlueWhiteDiceRound3Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w',round=3)
    defBlueRedDiceRound3,defBlueRedDiceRound3Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r',round=3)
    defBlueWhiteDiceRound3,defBlueWhiteDiceRound3Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w',round=3)

    BlueListSizeRound3 = [attBlueRedDiceRound3Size,attBlueBlackDiceRound3Size,attBlueWhiteDiceRound3Size,
                        defBlueRedDiceRound3Size,defBlueWhiteDiceRound3Size]
    BlueListSizeRound3 = function_resize_for_bins(BlueListSizeRound3)

    #round4
    attBlueRedDiceRound4,attBlueRedDiceRound4Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=4)
    attBlueBlackDiceRound4,attBlueBlackDiceRound4Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b',round=4)
    attBlueWhiteDiceRound4,attBlueWhiteDiceRound4Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w',round=4)
    defBlueRedDiceRound4,defBlueRedDiceRound4Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r',round=4)
    defBlueWhiteDiceRound4,defBlueWhiteDiceRound4Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w',round=4)

    BlueListSizeRound4 = [attBlueRedDiceRound4Size,attBlueBlackDiceRound4Size,attBlueWhiteDiceRound4Size,
                        defBlueRedDiceRound4Size,defBlueWhiteDiceRound4Size]
    BlueListSizeRound4 = function_resize_for_bins(BlueListSizeRound4)

    #round5
    attBlueRedDiceRound5,attBlueRedDiceRound5Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=5)
    attBlueBlackDiceRound5,attBlueBlackDiceRound5Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b',round=5)
    attBlueWhiteDiceRound5,attBlueWhiteDiceRound5Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w',round=5)
    defBlueRedDiceRound5,defBlueRedDiceRound5Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r',round=5)
    defBlueWhiteDiceRound5,defBlueWhiteDiceRound5Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w',round=5)

    BlueListSizeRound5 = [attBlueRedDiceRound5Size,attBlueBlackDiceRound5Size,attBlueWhiteDiceRound5Size,
                        defBlueRedDiceRound5Size,defBlueWhiteDiceRound5Size]
    BlueListSizeRound5 = function_resize_for_bins(BlueListSizeRound5)

    #round6
    attBlueRedDiceRound6,attBlueRedDiceRound6Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=6)
    attBlueBlackDiceRound6,attBlueBlackDiceRound6Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='b',round=6)
    attBlueWhiteDiceRound6,attBlueWhiteDiceRound6Size = calculate_y_proba_dice(player='b',attOrDef='att',colorDice='w',round=6)
    defBlueRedDiceRound6,defBlueRedDiceRound6Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='r',round=6)
    defBlueWhiteDiceRound6,defBlueWhiteDiceRound6Size = calculate_y_proba_dice(player='b',attOrDef='def',colorDice='w',round=6)

    BlueListSizeRound6 = [attBlueRedDiceRound6Size,attBlueBlackDiceRound6Size,attBlueWhiteDiceRound6Size,
                        defBlueRedDiceRound6Size,defBlueWhiteDiceRound6Size]
    BlueListSizeRound6 = function_resize_for_bins(BlueListSizeRound6)

    #Red player probability
    #round1
    attRedRedDiceRound1,attRedRedDiceRound1Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r',round=1)
    attRedBlackDiceRound1,attRedBlackDiceRound1Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b',round=1)
    attRedWhiteDiceRound1,attRedWhiteDiceRound1Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w',round=1)
    defRedRedDiceRound1,defRedRedDiceRound1Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r',round=1)
    defRedWhiteDiceRound1,defRedWhiteDiceRound1Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w',round=1)

    RedListSizeRound1 = [attRedRedDiceRound1Size,attRedBlackDiceRound1Size,attRedWhiteDiceRound1Size,
                        defRedRedDiceRound1Size,defRedWhiteDiceRound1Size]
    RedListSizeRound1 = function_resize_for_bins(RedListSizeRound1)

    #round2
    attRedRedDiceRound2,attRedRedDiceRound2Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r',round=2)
    attRedBlackDiceRound2,attRedBlackDiceRound2Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b',round=2)
    attRedWhiteDiceRound2,attRedWhiteDiceRound2Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w',round=2)
    defRedRedDiceRound2,defRedRedDiceRound2Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r',round=2)
    defRedWhiteDiceRound2,defRedWhiteDiceRound2Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w',round=2)

    RedListSizeRound2 = [attRedRedDiceRound2Size,attRedBlackDiceRound2Size,attRedWhiteDiceRound2Size,
                        defRedRedDiceRound2Size,defRedWhiteDiceRound2Size]
    RedListSizeRound2 = function_resize_for_bins(RedListSizeRound2)

    #round3
    attRedRedDiceRound3,attRedRedDiceRound3Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r',round=3)
    attRedBlackDiceRound3,attRedBlackDiceRound3Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b',round=3)
    attRedWhiteDiceRound3,attRedWhiteDiceRound3Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w',round=3)
    defRedRedDiceRound3,defRedRedDiceRound3Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r',round=3)
    defRedWhiteDiceRound3,defRedWhiteDiceRound3Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w',round=3)

    RedListSizeRound3 = [attRedRedDiceRound3Size,attRedBlackDiceRound3Size,attRedWhiteDiceRound3Size,
                        defRedRedDiceRound3Size,defRedWhiteDiceRound3Size]
    RedListSizeRound3 = function_resize_for_bins(RedListSizeRound3)

    #round4
    attRedRedDiceRound4,attRedRedDiceRound4Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r',round=4)
    attRedBlackDiceRound4,attRedBlackDiceRound4Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b',round=4)
    attRedWhiteDiceRound4,attRedWhiteDiceRound4Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w',round=4)
    defRedRedDiceRound4,defRedRedDiceRound4Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r',round=4)
    defRedWhiteDiceRound4,defRedWhiteDiceRound4Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w',round=4)

    RedListSizeRound4 = [attRedRedDiceRound4Size,attRedBlackDiceRound4Size,attRedWhiteDiceRound4Size,
                        defRedRedDiceRound4Size,defRedWhiteDiceRound4Size]
    RedListSizeRound4 = function_resize_for_bins(RedListSizeRound4)

    #round5
    attRedRedDiceRound5,attRedRedDiceRound5Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r',round=5)
    attRedBlackDiceRound5,attRedBlackDiceRound5Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b',round=5)
    attRedWhiteDiceRound5,attRedWhiteDiceRound5Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w',round=5)
    defRedRedDiceRound5,defRedRedDiceRound5Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r',round=5)
    defRedWhiteDiceRound5,defRedWhiteDiceRound5Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w',round=5)

    RedListSizeRound5 = [attRedRedDiceRound5Size,attRedBlackDiceRound5Size,attRedWhiteDiceRound5Size,
                        defRedRedDiceRound5Size,defRedWhiteDiceRound5Size]
    RedListSizeRound5 = function_resize_for_bins(RedListSizeRound5)

    #round6
    attRedRedDiceRound6,attRedRedDiceRound6Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='r',round=6)
    attRedBlackDiceRound6,attRedBlackDiceRound6Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='b',round=6)
    attRedWhiteDiceRound6,attRedWhiteDiceRound6Size = calculate_y_proba_dice(player='r',attOrDef='att',colorDice='w',round=6)
    defRedRedDiceRound6,defRedRedDiceRound6Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='r',round=6)
    defRedWhiteDiceRound6,defRedWhiteDiceRound6Size = calculate_y_proba_dice(player='r',attOrDef='def',colorDice='w',round=6)

    RedListSizeRound6 = [attRedRedDiceRound6Size,attRedBlackDiceRound6Size,attRedWhiteDiceRound6Size,
                        defRedRedDiceRound6Size,defRedWhiteDiceRound6Size]
    RedListSizeRound6 = function_resize_for_bins(RedListSizeRound6)




    #Round1
    attRedListRound1 = [attBlueRedDiceRound1,attRedDice,attRedRedDiceRound1]
    attBlackListRound1 = [attBlueBlackDiceRound1,attBlackDice,attRedBlackDiceRound1]
    attWhiteListRound1 = [attBlueWhiteDiceRound1,attWhiteDice,attRedWhiteDiceRound1]
    defRedListRound1 = [defBlueRedDiceRound1,defRedDice,defRedRedDiceRound1]
    defWhiteListRound1 = [defBlueWhiteDiceRound1,defWhiteDice,defRedWhiteDiceRound1]
    #Round2
    attRedListRound2 = [attBlueRedDiceRound2,attRedDice,attRedRedDiceRound2]
    attBlackListRound2 = [attBlueBlackDiceRound2,attBlackDice,attRedBlackDiceRound2]
    attWhiteListRound2 = [attBlueWhiteDiceRound2,attWhiteDice,attRedWhiteDiceRound2]
    defRedListRound2 = [defBlueRedDiceRound2,defRedDice,defRedRedDiceRound2]
    defWhiteListRound2 = [defBlueWhiteDiceRound2,defWhiteDice,defRedWhiteDiceRound2]
    #Round3
    attRedListRound3 = [attBlueRedDiceRound3,attRedDice,attRedRedDiceRound3]
    attBlackListRound3 = [attBlueBlackDiceRound3,attBlackDice,attRedBlackDiceRound3]
    attWhiteListRound3 = [attBlueWhiteDiceRound3,attWhiteDice,attRedWhiteDiceRound3]
    defRedListRound3 = [defBlueRedDiceRound3,defRedDice,defRedRedDiceRound3]
    defWhiteListRound3 = [defBlueWhiteDiceRound3,defWhiteDice,defRedWhiteDiceRound3]
    #Round4
    attRedListRound4 = [attBlueRedDiceRound4,attRedDice,attRedRedDiceRound4]
    attBlackListRound4 = [attBlueBlackDiceRound4,attBlackDice,attRedBlackDiceRound4]
    attWhiteListRound4 = [attBlueWhiteDiceRound4,attWhiteDice,attRedWhiteDiceRound4]
    defRedListRound4 = [defBlueRedDiceRound4,defRedDice,defRedRedDiceRound4]
    defWhiteListRound4 = [defBlueWhiteDiceRound4,defWhiteDice,defRedWhiteDiceRound4]
    #Round5
    attRedListRound5 = [attBlueRedDiceRound5,attRedDice,attRedRedDiceRound5]
    attBlackListRound5 = [attBlueBlackDiceRound5,attBlackDice,attRedBlackDiceRound5]
    attWhiteListRound5 = [attBlueWhiteDiceRound5,attWhiteDice,attRedWhiteDiceRound5]
    defRedListRound5 = [defBlueRedDiceRound5,defRedDice,defRedRedDiceRound5]
    defWhiteListRound5 = [defBlueWhiteDiceRound5,defWhiteDice,defRedWhiteDiceRound5]
    #Round6
    attRedListRound6 = [attBlueRedDiceRound6,attRedDice,attRedRedDiceRound6]
    attBlackListRound6 = [attBlueBlackDiceRound6,attBlackDice,attRedBlackDiceRound6]
    attWhiteListRound6 = [attBlueWhiteDiceRound6,attWhiteDice,attRedWhiteDiceRound6]
    defRedListRound6 = [defBlueRedDiceRound6,defRedDice,defRedRedDiceRound6]
    defWhiteListRound6 = [defBlueWhiteDiceRound6,defWhiteDice,defRedWhiteDiceRound6]


    #Blue Player
    #round 1
    numberDiceBlueRedAttLaunchedRound1 = count_number_dice(player='b',attOrDef='att',colorDice='r',round=1)
    numberDiceBlueBlackAttLaunchedRound1 = count_number_dice(player='b',attOrDef='att',colorDice='b',round=1)
    numberDiceBlueWhiteAttLaunchedRound1 = count_number_dice(player='b',attOrDef='att',colorDice='w',round=1)
    numberDiceBlueRedDefLaunchedRound1 = count_number_dice(player='b',attOrDef='def',colorDice='r',round=1)
    numberDiceBlueWhiteDefLaunchedRound1 = count_number_dice(player='b',attOrDef='def',colorDice='w',round=1)
    #round 2
    numberDiceBlueRedAttLaunchedRound2 = count_number_dice(player='b',attOrDef='att',colorDice='r',round=2)
    numberDiceBlueBlackAttLaunchedRound2 = count_number_dice(player='b',attOrDef='att',colorDice='b',round=2)
    numberDiceBlueWhiteAttLaunchedRound2 = count_number_dice(player='b',attOrDef='att',colorDice='w',round=2)
    numberDiceBlueRedDefLaunchedRound2 = count_number_dice(player='b',attOrDef='def',colorDice='r',round=2)
    numberDiceBlueWhiteDefLaunchedRound2 = count_number_dice(player='b',attOrDef='def',colorDice='w',round=2)
    #round 1
    numberDiceBlueRedAttLaunchedRound3 = count_number_dice(player='b',attOrDef='att',colorDice='r',round=3)
    numberDiceBlueBlackAttLaunchedRound3 = count_number_dice(player='b',attOrDef='att',colorDice='b',round=3)
    numberDiceBlueWhiteAttLaunchedRound3 = count_number_dice(player='b',attOrDef='att',colorDice='w',round=3)
    numberDiceBlueRedDefLaunchedRound3 = count_number_dice(player='b',attOrDef='def',colorDice='r',round=3)
    numberDiceBlueWhiteDefLaunchedRound3 = count_number_dice(player='b',attOrDef='def',colorDice='w',round=3)
    #round 2
    numberDiceBlueRedAttLaunchedRound4 = count_number_dice(player='b',attOrDef='att',colorDice='r',round=4)
    numberDiceBlueBlackAttLaunchedRound4 = count_number_dice(player='b',attOrDef='att',colorDice='b',round=4)
    numberDiceBlueWhiteAttLaunchedRound4 = count_number_dice(player='b',attOrDef='att',colorDice='w',round=4)
    numberDiceBlueRedDefLaunchedRound4 = count_number_dice(player='b',attOrDef='def',colorDice='r',round=4)
    numberDiceBlueWhiteDefLaunchedRound4 = count_number_dice(player='b',attOrDef='def',colorDice='w',round=4)
    #round 1
    numberDiceBlueRedAttLaunchedRound5 = count_number_dice(player='b',attOrDef='att',colorDice='r',round=5)
    numberDiceBlueBlackAttLaunchedRound5 = count_number_dice(player='b',attOrDef='att',colorDice='b',round=5)
    numberDiceBlueWhiteAttLaunchedRound5 = count_number_dice(player='b',attOrDef='att',colorDice='w',round=5)
    numberDiceBlueRedDefLaunchedRound5 = count_number_dice(player='b',attOrDef='def',colorDice='r',round=5)
    numberDiceBlueWhiteDefLaunchedRound5 = count_number_dice(player='b',attOrDef='def',colorDice='w',round=5)
    #round 2
    numberDiceBlueRedAttLaunchedRound6 = count_number_dice(player='b',attOrDef='att',colorDice='r',round=6)
    numberDiceBlueBlackAttLaunchedRound6 = count_number_dice(player='b',attOrDef='att',colorDice='b',round=6)
    numberDiceBlueWhiteAttLaunchedRound6 = count_number_dice(player='b',attOrDef='att',colorDice='w',round=6)
    numberDiceBlueRedDefLaunchedRound6 = count_number_dice(player='b',attOrDef='def',colorDice='r',round=6)
    numberDiceBlueWhiteDefLaunchedRound6 = count_number_dice(player='b',attOrDef='def',colorDice='w',round=6)


    #Red Player
    #round 1
    numberDiceRedRedAttLaunchedRound1 = count_number_dice(player='r',attOrDef='att',colorDice='r',round=1)
    numberDiceRedBlackAttLaunchedRound1 = count_number_dice(player='r',attOrDef='att',colorDice='b',round=1)
    numberDiceRedWhiteAttLaunchedRound1 = count_number_dice(player='r',attOrDef='att',colorDice='w',round=1)
    numberDiceRedRedDefLaunchedRound1 = count_number_dice(player='r',attOrDef='def',colorDice='r',round=1)
    numberDiceRedWhiteDefLaunchedRound1 = count_number_dice(player='r',attOrDef='def',colorDice='w',round=1)
    #round 2
    numberDiceRedRedAttLaunchedRound2 = count_number_dice(player='r',attOrDef='att',colorDice='r',round=2)
    numberDiceRedBlackAttLaunchedRound2 = count_number_dice(player='r',attOrDef='att',colorDice='b',round=2)
    numberDiceRedWhiteAttLaunchedRound2 = count_number_dice(player='r',attOrDef='att',colorDice='w',round=2)
    numberDiceRedRedDefLaunchedRound2 = count_number_dice(player='r',attOrDef='def',colorDice='r',round=2)
    numberDiceRedWhiteDefLaunchedRound2 = count_number_dice(player='r',attOrDef='def',colorDice='w',round=2)
    #round 3
    numberDiceRedRedAttLaunchedRound3 = count_number_dice(player='r',attOrDef='att',colorDice='r',round=3)
    numberDiceRedBlackAttLaunchedRound3 = count_number_dice(player='r',attOrDef='att',colorDice='b',round=3)
    numberDiceRedWhiteAttLaunchedRound3 = count_number_dice(player='r',attOrDef='att',colorDice='w',round=3)
    numberDiceRedRedDefLaunchedRound3 = count_number_dice(player='r',attOrDef='def',colorDice='r',round=3)
    numberDiceRedWhiteDefLaunchedRound3 = count_number_dice(player='r',attOrDef='def',colorDice='w',round=3)
    #round 4
    numberDiceRedRedAttLaunchedRound4 = count_number_dice(player='r',attOrDef='att',colorDice='r',round=4)
    numberDiceRedBlackAttLaunchedRound4 = count_number_dice(player='r',attOrDef='att',colorDice='b',round=4)
    numberDiceRedWhiteAttLaunchedRound4 = count_number_dice(player='r',attOrDef='att',colorDice='w',round=4)
    numberDiceRedRedDefLaunchedRound4 = count_number_dice(player='r',attOrDef='def',colorDice='r',round=4)
    numberDiceRedWhiteDefLaunchedRound4 = count_number_dice(player='r',attOrDef='def',colorDice='w',round=4)
    #round 5
    numberDiceRedRedAttLaunchedRound5 = count_number_dice(player='r',attOrDef='att',colorDice='r',round=5)
    numberDiceRedBlackAttLaunchedRound5 = count_number_dice(player='r',attOrDef='att',colorDice='b',round=5)
    numberDiceRedWhiteAttLaunchedRound5 = count_number_dice(player='r',attOrDef='att',colorDice='w',round=5)
    numberDiceRedRedDefLaunchedRound5 = count_number_dice(player='r',attOrDef='def',colorDice='r',round=5)
    numberDiceRedWhiteDefLaunchedRound5 = count_number_dice(player='r',attOrDef='def',colorDice='w',round=5)
    #round 6
    numberDiceRedRedAttLaunchedRound6 = count_number_dice(player='r',attOrDef='att',colorDice='r',round=6)
    numberDiceRedBlackAttLaunchedRound6 = count_number_dice(player='r',attOrDef='att',colorDice='b',round=6)
    numberDiceRedWhiteAttLaunchedRound6 = count_number_dice(player='r',attOrDef='att',colorDice='w',round=6)
    numberDiceRedRedDefLaunchedRound6 = count_number_dice(player='r',attOrDef='def',colorDice='r',round=6)
    numberDiceRedWhiteDefLaunchedRound6 = count_number_dice(player='r',attOrDef='def',colorDice='w',round=6)



    df = mainDf.copy()
    df['statValue']=df['statValue'].str.replace(',','.')
    df['statValue'] = df['statValue'].astype(float)
    df.loc[df.statValue == 0, 'statValue'] = 0.3
    df = df[df['statValue'].notnull()]

    idxBlueAtt, fireGroupBlueAttList,idxBlueAttRound=count_number_dice_with_df(df,player='b',attOrDef='att',colorDice=None)
    idxBlueDef, fireGroupBlueDefList,idxBlueDefRound=count_number_dice_with_df(df,player='b',attOrDef='def',colorDice=None)

    idxRedAtt, fireGroupRedAttList,idxRedAttRound=count_number_dice_with_df(df,player='r',attOrDef='att',colorDice=None)
    idxRedDef, fireGroupRedDefList,idxRedDefRound=count_number_dice_with_df(df,player='r',attOrDef='def',colorDice=None)


    idxBlue, fireGroupBlueList,idxBlueRound=count_number_dice_with_df(df,player='b',attOrDef=None,colorDice=None)
    idxRed, fireGroupRedList,idxRedRound=count_number_dice_with_df(df,player='r',attOrDef=None,colorDice=None)


    generalLuckBlue = '%0.2f'%round(100*np.mean(fireGroupBlueList),2)
    luckBlueAtt = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att'),2)
    luckBlueDef = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def'),2)

    generalLuckRed = '%0.2f'%round(100*np.mean(fireGroupRedList),2)
    luckRedAtt = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att'),2)
    luckRedDef = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def'),2)

    #Blue 
    luckBlueRound1 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef=None,round=1),2)
    luckBlueRound2 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef=None,round=2),2)
    luckBlueRound3 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef=None,round=3),2)
    luckBlueRound4 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef=None,round=4),2)
    luckBlueRound5 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef=None,round=5),2)
    luckBlueRound6 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef=None,round=6),2)

    #Red
    luckRedRound1 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef=None,round=1),2)
    luckRedRound2 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef=None,round=2),2)
    luckRedRound3 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef=None,round=3),2)
    luckRedRound4 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef=None,round=4),2)
    luckRedRound5 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef=None,round=5),2)
    luckRedRound6 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef=None,round=6),2)

    #Blue ATT
    luckBlueAttRound1 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att',round=1),2)
    luckBlueAttRound2 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att',round=2),2)
    luckBlueAttRound3 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att',round=3),2)
    luckBlueAttRound4 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att',round=4),2)
    luckBlueAttRound5 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att',round=5),2)
    luckBlueAttRound6 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='att',round=6),2)

    #Red ATT
    luckRedAttRound1 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att',round=1),2)
    luckRedAttRound2 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att',round=2),2)
    luckRedAttRound3 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att',round=3),2)
    luckRedAttRound4 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att',round=4),2)
    luckRedAttRound5 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att',round=5),2)
    luckRedAttRound6 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='att',round=6),2)

    #Blue DEF
    luckBlueDefRound1 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def',round=1),2)
    luckBlueDefRound2 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def',round=2),2)
    luckBlueDefRound3 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def',round=3),2)
    luckBlueDefRound4 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def',round=4),2)
    luckBlueDefRound5 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def',round=5),2)
    luckBlueDefRound6 = '%0.2f'%round(100*count_luck_per_round(df,player='b',attOrDef='def',round=6),2)

    #Red DEF
    luckRedDefRound1 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def',round=1),2)
    luckRedDefRound2 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def',round=2),2)
    luckRedDefRound3 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def',round=3),2)
    luckRedDefRound4 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def',round=4),2)
    luckRedDefRound5 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def',round=5),2)
    luckRedDefRound6 = '%0.2f'%round(100*count_luck_per_round(df,player='r',attOrDef='def',round=6),2)



    print("\n")
    print(colored("Total", 'green'))
    print("Number of Dice Launched : ",numberDiceLaunched)
    print("\n")
    print(colored(BluePlayer, 'blue'))
    print("Number of Dice Launched : ",numberDiceLaunchedBlue)
    print("Number of Attack Dice Launched : ",numberDiceLaunchedBlueAtt)
    print("Number of Defence Dice Launched : ",numberDiceLaunchedBlueDef)
    print("\n")
    print(colored(RedPlayer, 'red'))
    print("Number of Dice Launched by  : ",numberDiceLaunchedRed)
    print("Number of Attack Dice Launched by : ",numberDiceLaunchedRedAtt)
    print("Number of Defence Dice Launched by : ",numberDiceLaunchedRedDef)
    print("\n")


    print("\n")
    print(colored("General Luck", 'green'))
    print("\n")
    print(colored(BluePlayer, 'blue'))
    print("\n")
    print("           General","   Attaque" ,"   Defence" ,)
    print("\n")
    print("general : ", generalLuckBlue,"%   ",luckBlueAtt,"%   ",luckBlueDef,"%",)
    print("\n")
    print("Round 1 : ", luckBlueRound1,"%   ",luckBlueAttRound1,"%   ",luckBlueDefRound1,"%",)
    print("Round 2 : ", luckBlueRound2,"%   ",luckBlueAttRound2,"%   ",luckBlueDefRound2,"%",)
    print("Round 3 : ", luckBlueRound3,"%   ",luckBlueAttRound3,"%   ",luckBlueDefRound3,"%",)
    print("Round 4 : ", luckBlueRound4,"%   ",luckBlueAttRound4,"%   ",luckBlueDefRound4,"%",)
    print("Round 5 : ", luckBlueRound5,"%   ",luckBlueAttRound5,"%   ",luckBlueDefRound5,"%",)
    print("Round 6 : ", luckBlueRound6,"%   ",luckBlueAttRound6,"%   ",luckBlueDefRound6,"%",)

    print("\n")
    print(colored(RedPlayer, 'red'))
    print("\n")
    print("           General","   Attaque" ,"   Defence" ,)
    print("\n")
    print("general : ", generalLuckRed,"%   ",luckRedAtt,"%   ",luckRedDef,"%",)
    print("\n")
    print("Round 1 : ", luckRedRound1,"%   ",luckRedAttRound1,"%   ",luckRedDefRound1,"%",)
    print("Round 2 : ", luckRedRound2,"%   ",luckRedAttRound2,"%   ",luckRedDefRound2,"%",)
    print("Round 3 : ", luckRedRound3,"%   ",luckRedAttRound3,"%   ",luckRedDefRound3,"%",)
    print("Round 4 : ", luckRedRound4,"%   ",luckRedAttRound4,"%   ",luckRedDefRound4,"%",)
    print("Round 5 : ", luckRedRound5,"%   ",luckRedAttRound5,"%   ",luckRedDefRound5,"%",)
    print("Round 6 : ", luckRedRound6,"%   ",luckRedAttRound6,"%   ",luckRedDefRound6,"%",)


    print("\n")

    df = mainDf.copy()
    df['statValue']=df['statValue'].str.replace(',','.')
    df['statValue'] = df['statValue'].astype(float)
    df.loc[df.statValue == 0, 'statValue'] = 0.3
    df = df[df['statValue'].notnull()]

    df = df[df['unité']!= "supress"]

    df =df.sort_values(by=['statValue'], ascending=False)


    print("\n")
    print(colored("Classement Meilleurs Jets :", 'green'))
    print("\n")
    print(1,"er   -","   joueur :",df.iloc[0]["player"],"   att/def :",df.iloc[0]["att/def"],"   round :",df.iloc[0]["round"],"   unit :",df.iloc[0]["unité"])
    print(2,"nd   -","   joueur :",df.iloc[1]["player"],"   att/def :",df.iloc[1]["att/def"],"   round :",df.iloc[1]["round"],"   unit :",df.iloc[1]["unité"])
    print(3,"ième -","   joueur :",df.iloc[2]["player"],"   att/def :",df.iloc[2]["att/def"],"   round :",df.iloc[2]["round"],"   unit :",df.iloc[2]["unité"])



    ############################
    # PLOTTING #
    ############################

    labelsFirtPie = ["Red Attack","Black Attack","White Attack","Red Def","White Def"]
    labelsSecondPie = ["Red Attack","Black Attack","White Attack","Red Def","White Def"]
    valueFirstPie = [numberDiceBlueRedAttLaunched,numberDiceBlueBlackAttLaunched,numberDiceBlueWhiteAttLaunched,numberDiceBlueRedDefLaunched,numberDiceBlueWhiteDefLaunched]
    valueSecondPie = [numberDiceRedRedAttLaunched,numberDiceRedBlackAttLaunched,numberDiceRedWhiteAttLaunched,numberDiceRedRedDefLaunched,numberDiceRedWhiteDefLaunched]
    color = ["#FF0000","2E2E2E","F6F6F6","B50000","D7D7D7"]

    pie_chart(labelsFirtPie,labelsSecondPie,valueFirstPie,valueSecondPie,color,color, title = "Dés Utilisés Par Joueur",colorFirstPieText="blue",colorSecondPieText="red")    

    labelFirstPie = ["Red Attack","Black Attack","White Attack"]
    labelSecondPie = ["Red Def","White Def"]
    valueFirstPie = [numberDiceRedAttLaunched,numberDiceBlackAttLaunched,numberDiceWhiteAttLaunched]
    valueSecondPie = [numberDiceRedDefLaunched,numberDiceWhiteDefLaunched]
    colorFirstPie = ["#FF0000","2E2E2E","F6F6F6"]
    colorSecondPie = ["B50000","D7D7D7"]

    print("\n")
    print(colored("Number Of Attack Dice", 'green'))
    print(numberDiceRedAttLaunched+numberDiceBlackAttLaunched+numberDiceWhiteAttLaunched)
    print(colored("Number Of Defence Dice", 'green'))
    print(numberDiceRedDefLaunched+numberDiceWhiteDefLaunched)
    print(colored("Ratio touche qui doivent être défendues", 'green'))
    print((numberDiceRedDefLaunched+numberDiceWhiteDefLaunched)/(numberDiceRedAttLaunched+numberDiceBlackAttLaunched+numberDiceWhiteAttLaunched))

    pie_chart(labelFirstPie,labelSecondPie,valueFirstPie,valueSecondPie,colorFirstPie,colorSecondPie, title = "Attaque versus Defence",textFirstPie="Attack",textSecondPie="Defence",xTextFirstPie = 0.19,xTextSecondPie = 0.81)

    subplot_all_dice(xatt,xdef,BlueListSize,RedListSize,attRedList,attBlackList,attWhiteList,
                 defRedList,defWhiteList,title = "General Dice launch",blue = BluePlayer,red = RedPlayer )


    #ROUND 1
    subplot_all_dice(xatt,xdef,BlueListSizeRound1,RedListSizeRound1,attRedListRound1,attBlackListRound1,attWhiteListRound1,
                 defRedListRound1,defWhiteListRound1,title = "Round 1",blue = BluePlayer,red = RedPlayer )



    labelsFirtPie = ["Red Attack","Black Attack","White Attack","Red Def","White Def"]
    labelsSecondPie = ["Red Attack","Black Attack","White Attack","Red Def","White Def"]
    valueFirstPie = [numberDiceBlueRedAttLaunchedRound1,numberDiceBlueBlackAttLaunchedRound1,numberDiceBlueWhiteAttLaunchedRound1,numberDiceBlueRedDefLaunchedRound1,numberDiceBlueWhiteDefLaunchedRound1]
    valueSecondPie = [numberDiceRedRedAttLaunchedRound1,numberDiceRedBlackAttLaunchedRound1,numberDiceRedWhiteAttLaunchedRound1,numberDiceRedRedDefLaunchedRound1,numberDiceRedWhiteDefLaunchedRound1]
    color = ["#FF0000","2E2E2E","F6F6F6","B50000","D7D7D7"]

    pie_chart(labelsFirtPie,labelsSecondPie,valueFirstPie,valueSecondPie,color,color, title = "Dices Used From Player - Round 1",colorFirstPieText="blue",colorSecondPieText="red")





    #Luck throw 

    plot_for_luck_thorw(str(BluePlayer + " Throw "),idxBlue, fireGroupBlueList,idxBlueRound)
    plot_for_luck_thorw(str(RedPlayer + " Throw "),idxRed, fireGroupRedList,idxRedRound)

    plot_for_luck_thorw(str(BluePlayer + " Attack Throw "),idxBlueAtt, fireGroupBlueAttList,idxBlueAttRound)
    plot_for_luck_thorw(str(BluePlayer + " Defend Throw "),idxBlueDef, fireGroupBlueDefList,idxBlueDefRound)

    plot_for_luck_thorw(str(RedPlayer + " Attack Throw "),idxRedAtt, fireGroupRedAttList,idxRedAttRound)
    plot_for_luck_thorw(str(RedPlayer + " Defend Throw "),idxRedDef, fireGroupRedDefList,idxRedDefRound)

    df = mainDf.copy()
    df['statValue']=df['statValue'].str.replace(',','.')
    df['statValue'] = df['statValue'].astype(float)
    df.loc[df.statValue == 0, 'statValue'] = 0.3
    df = df[df['statValue'].notnull()]

    df = df[df['unité']!= "supress"]

    df =df.sort_values(by=['statValue'], ascending=False)

    if(df.iloc[0]["player"]=='b'):
        playerBestThorw0=BluePlayer
    else: 
        playerBestThorw0=RedPlayer
    
    if(df.iloc[1]["player"]=='b'):
        playerBestThorw1=BluePlayer
    else: 
        playerBestThorw1=RedPlayer
    
    if(df.iloc[2]["player"]=='b'):
        playerBestThorw2=BluePlayer
    else: 
        playerBestThorw2=RedPlayer
    



    returnDict  = {
        'BluePlayer':BluePlayer,
        'RedPlayer':RedPlayer,

        'numberDiceLaunched':numberDiceLaunched,

        'numberDiceLaunchedBlue':numberDiceLaunchedBlue,
        'numberDiceLaunchedBlueAtt':numberDiceLaunchedBlueAtt,
        'numberDiceLaunchedBlueDef':numberDiceLaunchedBlueDef,

        'numberDiceLaunchedRed':numberDiceLaunchedRed,
        'numberDiceLaunchedRedAtt':numberDiceLaunchedRedAtt,
        'numberDiceLaunchedRedDef':numberDiceLaunchedRedDef,

        'luckBlueGeneral':[float(generalLuckBlue),float(luckBlueAtt),float(luckBlueDef)],
        'luckBlueRound1':[float(luckBlueRound1),float(luckBlueAttRound1),float(luckBlueDefRound1)],
        'luckBlueRound2':[float(luckBlueRound2),float(luckBlueAttRound2),float(luckBlueDefRound2)],
        'luckBlueRound3':[float(luckBlueRound3),float(luckBlueAttRound3),float(luckBlueDefRound3)],
        'luckBlueRound4':[float(luckBlueRound4),float(luckBlueAttRound4),float(luckBlueDefRound4)],
        'luckBlueRound5':[float(luckBlueRound5),float(luckBlueAttRound5),float(luckBlueDefRound5)],
        'luckBlueRound6':[float(luckBlueRound6),float(luckBlueAttRound6),float(luckBlueDefRound6)],

        'luckRedGeneral':[float(generalLuckRed),float(luckRedAtt),float(luckRedDef)],
        'luckRedRound1':[float(luckRedRound1),float(luckRedAttRound1),float(luckRedDefRound1)],
        'luckRedRound2':[float(luckRedRound2),float(luckRedAttRound2),float(luckRedDefRound2)],
        'luckRedRound3':[float(luckRedRound3),float(luckRedAttRound3),float(luckRedDefRound3)],
        'luckRedRound4':[float(luckRedRound4),float(luckRedAttRound4),float(luckRedDefRound4)],
        'luckRedRound5':[float(luckRedRound5),float(luckRedAttRound5),float(luckRedDefRound5)],
        'luckRedRound6':[float(luckRedRound6),float(luckRedAttRound6),float(luckRedDefRound6)],

        '1BestThrow':[playerBestThorw0,df.iloc[0]["att/def"],df.iloc[0]["round"],df.iloc[0]["unité"]],
        '2BestThrow':[playerBestThorw1,df.iloc[1]["att/def"],df.iloc[1]["round"],df.iloc[1]["unité"]],
        '3BestThrow':[playerBestThorw2,df.iloc[2]["att/def"],df.iloc[2]["round"],df.iloc[2]["unité"]],


    }




    return returnDict
