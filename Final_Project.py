

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from functools import partial
import random

qtCreatorFile = "Game123.ui"  # Enter UI file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

####Designed shapes and answers####
p_star_key = {1:[0,0,1,1,0], 2:[0,0,0,1,1], 3:[1,0,0,0,1], 4:[1,1,0,0,0], 5:[0,1,1,0,0]}
p_star_pos = {1:(425,175), 2:(590,300), 3:(530,490), 4:(330,490), 5:(260,300)}
p_hexapound_key = {1:[0,1,0,1,0,1], 2:[1,0,1,0,1,0], 3:[0,1,0,1,0,1], 4:[1,0,1,0,1,0], 5:[0,1,0,1,0,1], 6:[1,0,1,0,1,0]}
p_hexapound_pos = {1:(500,150), 2:(587,300), 3:(500,450), 4:(327,450), 5:(240,300), 6:(327,150)}
p_tree_key = {1: [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1], 2: [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0], 3: [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0], 4: [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0], 5: [0,0,0,1,0,1,0,0,0,0,0,0,0,0,0], 6: [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0], 7: [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0], 8: [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0], 9: [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0], 10: [0,0,0,0,0,0,0,0,1,0,1,0,0,0,0], 11: [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0], 12: [0,0,0,0,0,0,0,0,0,0,1,0,1,0,0], 13: [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0], 14: [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], 15: [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]}
p_tree_pos = {1: (400, 50), 2: (500, 130), 3: (425, 120), 4: (530, 240), 5: (440, 220), 6: (570, 350), 7: (440, 320), 8: (440, 450), 9: (360, 450), 10: (360, 320), 11: (230, 350), 12: (360, 220), 13: (270, 240), 14: (375, 120), 15: (300, 130)}
p_hanger_key = {1: [0,1,0,0,0,0,0], 2: [1,0,1,0,0,0,0], 3: [0,1,0,1,0,0,0], 4: [0,0,1,0,1,0,0], 5: [0,0,0,1,0,1,1], 6: [0,0,0,0,1,0,1], 7: [0,0,0,0,1,1,0]}
p_hanger_pos = {1: (350, 190), 2: (380, 160), 3: (420, 160), 4: (435, 210), 5: (400, 250), 6: (600, 360), 7: (200, 360)}
p_phone_key = {1: [0,1,0,0,0,0,0,0,0,0,0,0,1], 2: [1,0,1,0,0,0,0,0,0,0,0,0,0], 3: [0,1,0,1,0,0,0,0,0,0,0,0,0], 4: [0,0,1,0,1,0,0,0,0,0,0,0,0], 5: [0,0,0,1,0,1,0,0,0,0,0,0,0], 6: [0,0,0,0,1,0,1,0,0,0,0,0,0], 7: [0,0,0,0,0,1,0,1,0,0,0,0,0], 8: [0,0,0,0,0,0,1,0,1,0,0,0,0],9: [0,0,0,0,0,0,0,1,0,1,0,0,0], 10: [0,0,0,0,0,0,0,0,1,0,1,0,0], 11: [0,0,0,0,0,0,0,0,0,1,0,1,0], 12: [0,0,0,0,0,0,0,0,0,0,1,0,1], 13: [1,0,0,0,0,0,0,0,0,0,0,1,0]}
p_phone_pos = {1: (350, 130), 2: (300, 200), 3: (300, 300), 4: (380, 400), 5: (500, 500), 6: (600, 500), 7: (680, 440), 8: (640, 370), 9: (560, 350), 10: (530, 430), 11: (370, 270), 12: (450, 240), 13: (430, 160)}
p_shroom_key = {1: [0,1,0,0,0,0,0,0,0,1], 2: [1,0,1,0,0,0,0,0,0,0], 3: [0,1,0,1,0,0,0,0,0,0], 4: [0,0,1,0,1,0,0,0,0,0], 5: [0,0,0,1,0,1,0,0,0,0], 6: [0,0,0,0,1,0,1,0,0,0], 7: [0,0,0,0,0,1,0,1,0,0], 8: [0,0,0,0,0,0,1,0,1,0],9: [0,0,0,0,0,0,0,1,0,1], 10: [1,0,0,0,0,0,0,0,1,0]}
p_shroom_pos = {1: (420, 120), 2: (580, 160), 3: (650, 250), 4: (490, 300), 5: (510, 480), 6: (420, 500), 7: (330, 480), 8: (350, 300), 9: (190, 250), 10: (260, 160)}
p_pine_key = {1: [0,1,0,0,0,0,0,0,0,0,1], 2: [1,0,1,0,0,0,0,0,0,0,0], 3: [0,1,0,1,0,0,0,0,0,0,0], 4: [0,0,1,0,1,0,0,0,0,0,0], 5: [0,0,0,1,0,1,0,0,0,0,0], 6: [0,0,0,0,1,0,1,0,0,0,0], 7: [0,0,0,0,0,1,0,1,0,0,0], 8: [0,0,0,0,0,0,1,0,1,0,0],9: [0,0,0,0,0,0,0,1,0,1,0], 10: [0,0,0,0,0,0,0,0,1,0,1], 11: [1,0,0,0,0,0,0,0,0,1,0]}
p_pine_pos = {1: (420, 70), 2: (450, 190), 3: (530, 90), 4: (490, 250), 5: (540, 400), 6: (480, 500), 7: (360, 500), 8: (300, 400), 9: (350, 250), 10: (310, 90), 11: (390, 190)}
p_guitar_key = {1: [0,1,0,0,0,0,0,0,0,0,1], 2: [1,0,1,0,0,0,0,0,0,0,0], 3: [0,1,0,1,0,0,0,0,0,0,0], 4: [0,0,1,0,1,0,0,0,0,0,0], 5: [0,0,0,1,0,1,0,0,0,0,0], 6: [0,0,0,0,1,0,1,0,0,0,0], 7: [0,0,0,0,0,1,0,1,0,0,0], 8: [0,0,0,0,0,0,1,0,1,0,0],9: [0,0,0,0,0,0,0,1,0,1,0], 10: [0,0,0,0,0,0,0,0,1,0,1], 11: [1,0,0,0,0,0,0,0,0,1,0]}
p_guitar_pos = {1: (750, 30), 2: (770, 130), 3: (700, 160), 4: (420, 300), 5: (200, 570), 6: (240, 400), 7: (80, 360), 8: (290, 290), 9: (380, 150), 10: (400, 250), 11: (680, 120)}
p_fish_key = {1: [0,1,0,0,0,0,0,0,0,1], 2: [1,0,1,0,0,0,0,0,0,0], 3: [0,1,0,1,0,0,0,0,0,0], 4: [0,0,1,0,1,0,0,0,0,0], 5: [0,0,0,1,0,1,0,0,0,0], 6: [0,0,0,0,1,0,1,0,0,0], 7: [0,0,0,0,0,1,0,1,0,0], 8: [0,0,0,0,0,0,1,0,1,0],9: [0,0,0,0,0,0,0,1,0,1], 10: [1,0,0,0,0,0,0,0,1,0]}
p_fish_pos = {1: (300, 210), 2: (540, 280), 3: (620, 200), 4: (580, 315), 5: (640, 410), 6: (540, 350), 7: (310, 380), 8: (210, 330), 9: (260, 310), 10: (210, 290)}
p_future_key = {}
p_future_pos = {}

pre_sets = dict()
pre_sets[1] = [5, 'Star', p_star_pos, p_star_key]
pre_sets[2] = [6, 'Hexagon with an Asterisk inside', p_hexapound_pos, p_hexapound_key]
pre_sets[3] = [15, 'Christmas Tree', p_tree_pos, p_tree_key]
pre_sets[4] = [7, 'Coat Hanger', p_hanger_pos, p_hanger_key]
pre_sets[5] = [13, 'Telephone', p_phone_pos, p_phone_key]
pre_sets[6] = [10, 'Mushroom', p_shroom_pos, p_shroom_key]
pre_sets[7] = [11, 'Pineapple', p_pine_pos, p_pine_key]
pre_sets[8] = [11, 'Electric Guitar', p_guitar_pos, p_guitar_key]
pre_sets[9] = [10, 'Fish', p_fish_pos, p_fish_key]
pre_sets[10] = [0, "the future of this application's creators", p_future_pos, p_future_key]

####Start the game####

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bigList = []
        self.tempT = ()
        self.answer = {}
        self.shapeName = ''
        self.score = 0
        self.numOfDots = 0      #the amount of dots of the game can be changed
        self.dotNum1 = 0        #keep track of the frist dot pressed
        self.dotNum2 = 0        #keep track of the second dot pressed
        self.initSet()
        self.initUserInput()
        self.scoreBoard.setText(str(self.score))
        self.Dot01.clicked.connect(partial(self.pushed, self.Dot01))
        self.Dot02.clicked.connect(partial(self.pushed, self.Dot02))
        self.Dot03.clicked.connect(partial(self.pushed, self.Dot03))
        self.Dot04.clicked.connect(partial(self.pushed, self.Dot04))
        self.Dot05.clicked.connect(partial(self.pushed, self.Dot05))
        self.Dot06.clicked.connect(partial(self.pushed, self.Dot06))
        self.Dot07.clicked.connect(partial(self.pushed, self.Dot07))
        self.Dot08.clicked.connect(partial(self.pushed, self.Dot08))
        self.Dot09.clicked.connect(partial(self.pushed, self.Dot09))
        self.Dot10.clicked.connect(partial(self.pushed, self.Dot10))
        self.Dot11.clicked.connect(partial(self.pushed, self.Dot11))
        self.Dot12.clicked.connect(partial(self.pushed, self.Dot12))
        self.Dot13.clicked.connect(partial(self.pushed, self.Dot13))
        self.Dot14.clicked.connect(partial(self.pushed, self.Dot14))
        self.Dot15.clicked.connect(partial(self.pushed, self.Dot15))
        self.Submit.clicked.connect(self.checkAnswer)
        self.RefreshAnother.clicked.connect(self.refresh)
        self.Reset.clicked.connect(self.reset)

    def initUserInput(self): #initialize the matrix to be filled with 0
        self.userInput = {}
        n = 1
        while n <= self.numOfDots:
            self.userInput[n] = [0] * self.numOfDots
            n += 1

    def initSet(self):
        r = random.randint(1,10)
        self.numOfDots = pre_sets[r][0]
        self.shapeName = pre_sets[r][1]
        self.answer = pre_sets[r][3]
        self.shape_Name.setText(self.shapeName)
        if r == 1:
            self.moveStar()
        elif r == 2:
            self.moveHexapound()
        elif r == 3:
            self.moveTree()
        elif r == 4:
            self.moveHanger()
        elif r == 5:
            self.movePhone()
        elif r == 6:
            self.moveShroom()
        elif r == 7:
            self.movePine()
        elif r == 8:
            self.moveGuitar()
        elif r == 9:
            self.moveFish()
        elif r == 10:
            self.moveFuture()

    def pushed(self, btn):
        self.dotNum2 = int(btn.objectName()[-2:])
        if self.dotNum1 != 0:
            self.userInput[self.dotNum1][self.dotNum2-1] = 1
            self.userInput[self.dotNum2][self.dotNum1-1] = 1
        self.dotNum1 = self.dotNum2
        t = (btn.x()+20, btn.y()+120)
        if t != self.tempT:
            self.bigList.append(t)
            self.update()
            self.tempT = t
        #Below can be used for debugging
        #self.shape_Name.setText(str(self.userInput))
        #self.roundResult.setText(str(t))

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        if len(self.bigList) >= 2:
            n = 0
            condition = True
            while condition:
                if n+1 == len(self.bigList):
                    condition = False
                else:
                    qp.drawLine(self.bigList[n][0], self.bigList[n][1], self.bigList[n+1][0], self.bigList[n+1][1])
                    n += 1

    def checkAnswer(self):
        if self.userInput == self.answer:
            self.roundResult.setText('Correct!')
            self.score = self.score + 1
            self.scoreBoard.setText(str(self.score))
        else:
            self.roundResult.setText('Wrong! Try again!')

    def reset(self):
        self.bigList = []
        self.tempT = ()
        self.dotNum1 = 0  # keep track of the frist dot pressed
        self.dotNum2 = 0  # keep track of the second dot pressed
        self.scoreBoard.setText(str(self.score))
        self.initUserInput()
        self.update()

    def refresh(self):
        self.bigList = []
        self.tempT = ()
        self.answer = {}
        self.shapeName = ''
        self.numOfDots = 0  # the amount of dots of the game can be changed
        self.dotNum1 = 0  # keep track of the frist dot pressed
        self.dotNum2 = 0  # keep track of the second dot pressed
        self.scoreBoard.setText(str(self.score))
        self.initSet()
        self.initUserInput()
        self.update()

    def moveStar(self):
        self.Dot01.move(p_star_pos[1][0], p_star_pos[1][1])
        self.Dot02.move(p_star_pos[2][0], p_star_pos[2][1])
        self.Dot03.move(p_star_pos[3][0], p_star_pos[3][1])
        self.Dot04.move(p_star_pos[4][0], p_star_pos[4][1])
        self.Dot05.move(p_star_pos[5][0], p_star_pos[5][1])
        self.Dot06.move(860, 580)
        self.Dot07.move(860, 580)
        self.Dot08.move(860, 580)
        self.Dot09.move(860, 580)
        self.Dot10.move(860, 580)
        self.Dot11.move(860, 580)
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def moveHexapound(self):
        self.Dot01.move(p_hexapound_pos[1][0], p_hexapound_pos[1][1])
        self.Dot02.move(p_hexapound_pos[2][0], p_hexapound_pos[2][1])
        self.Dot03.move(p_hexapound_pos[3][0], p_hexapound_pos[3][1])
        self.Dot04.move(p_hexapound_pos[4][0], p_hexapound_pos[4][1])
        self.Dot05.move(p_hexapound_pos[5][0], p_hexapound_pos[5][1])
        self.Dot06.move(p_hexapound_pos[6][0], p_hexapound_pos[6][1])
        self.Dot07.move(860, 580)
        self.Dot08.move(860, 580)
        self.Dot09.move(860, 580)
        self.Dot10.move(860, 580)
        self.Dot11.move(860, 580)
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def moveTree(self):
        self.Dot01.move(p_tree_pos[1][0], p_tree_pos[1][1])
        self.Dot02.move(p_tree_pos[2][0], p_tree_pos[2][1])
        self.Dot03.move(p_tree_pos[3][0], p_tree_pos[3][1])
        self.Dot04.move(p_tree_pos[4][0], p_tree_pos[4][1])
        self.Dot05.move(p_tree_pos[5][0], p_tree_pos[5][1])
        self.Dot06.move(p_tree_pos[6][0], p_tree_pos[6][1])
        self.Dot07.move(p_tree_pos[7][0], p_tree_pos[7][1])
        self.Dot08.move(p_tree_pos[8][0], p_tree_pos[8][1])
        self.Dot09.move(p_tree_pos[9][0], p_tree_pos[9][1])
        self.Dot10.move(p_tree_pos[10][0], p_tree_pos[10][1])
        self.Dot11.move(p_tree_pos[11][0], p_tree_pos[11][1])
        self.Dot12.move(p_tree_pos[12][0], p_tree_pos[12][1])
        self.Dot13.move(p_tree_pos[13][0], p_tree_pos[13][1])
        self.Dot14.move(p_tree_pos[14][0], p_tree_pos[14][1])
        self.Dot15.move(p_tree_pos[15][0], p_tree_pos[15][1])

    def moveHanger(self):
        self.Dot01.move(p_hanger_pos[1][0], p_hanger_pos[1][1])
        self.Dot02.move(p_hanger_pos[2][0], p_hanger_pos[2][1])
        self.Dot03.move(p_hanger_pos[3][0], p_hanger_pos[3][1])
        self.Dot04.move(p_hanger_pos[4][0], p_hanger_pos[4][1])
        self.Dot05.move(p_hanger_pos[5][0], p_hanger_pos[5][1])
        self.Dot06.move(p_hanger_pos[6][0], p_hanger_pos[6][1])
        self.Dot07.move(p_hanger_pos[7][0], p_hanger_pos[7][1])
        self.Dot08.move(860, 580)
        self.Dot09.move(860, 580)
        self.Dot10.move(860, 580)
        self.Dot11.move(860, 580)
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def movePhone(self):
        self.Dot01.move(p_phone_pos[1][0], p_phone_pos[1][1])
        self.Dot02.move(p_phone_pos[2][0], p_phone_pos[2][1])
        self.Dot03.move(p_phone_pos[3][0], p_phone_pos[3][1])
        self.Dot04.move(p_phone_pos[4][0], p_phone_pos[4][1])
        self.Dot05.move(p_phone_pos[5][0], p_phone_pos[5][1])
        self.Dot06.move(p_phone_pos[6][0], p_phone_pos[6][1])
        self.Dot07.move(p_phone_pos[7][0], p_phone_pos[7][1])
        self.Dot08.move(p_phone_pos[8][0], p_phone_pos[8][1])
        self.Dot09.move(p_phone_pos[9][0], p_phone_pos[9][1])
        self.Dot10.move(p_phone_pos[10][0], p_phone_pos[10][1])
        self.Dot11.move(p_phone_pos[11][0], p_phone_pos[11][1])
        self.Dot12.move(p_phone_pos[12][0], p_phone_pos[12][1])
        self.Dot13.move(p_phone_pos[13][0], p_phone_pos[13][1])
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def moveShroom(self):
        self.Dot01.move(p_shroom_pos[1][0], p_shroom_pos[1][1])
        self.Dot02.move(p_shroom_pos[2][0], p_shroom_pos[2][1])
        self.Dot03.move(p_shroom_pos[3][0], p_shroom_pos[3][1])
        self.Dot04.move(p_shroom_pos[4][0], p_shroom_pos[4][1])
        self.Dot05.move(p_shroom_pos[5][0], p_shroom_pos[5][1])
        self.Dot06.move(p_shroom_pos[6][0], p_shroom_pos[6][1])
        self.Dot07.move(p_shroom_pos[7][0], p_shroom_pos[7][1])
        self.Dot08.move(p_shroom_pos[8][0], p_shroom_pos[8][1])
        self.Dot09.move(p_shroom_pos[9][0], p_shroom_pos[9][1])
        self.Dot10.move(p_shroom_pos[10][0], p_shroom_pos[10][1])
        self.Dot11.move(860, 580)
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def movePine(self):
        self.Dot01.move(p_pine_pos[1][0], p_pine_pos[1][1])
        self.Dot02.move(p_pine_pos[2][0], p_pine_pos[2][1])
        self.Dot03.move(p_pine_pos[3][0], p_pine_pos[3][1])
        self.Dot04.move(p_pine_pos[4][0], p_pine_pos[4][1])
        self.Dot05.move(p_pine_pos[5][0], p_pine_pos[5][1])
        self.Dot06.move(p_pine_pos[6][0], p_pine_pos[6][1])
        self.Dot07.move(p_pine_pos[7][0], p_pine_pos[7][1])
        self.Dot08.move(p_pine_pos[8][0], p_pine_pos[8][1])
        self.Dot09.move(p_pine_pos[9][0], p_pine_pos[9][1])
        self.Dot10.move(p_pine_pos[10][0], p_pine_pos[10][1])
        self.Dot11.move(p_pine_pos[11][0], p_pine_pos[11][1])
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def moveGuitar(self):
        self.Dot01.move(p_guitar_pos[1][0], p_guitar_pos[1][1])
        self.Dot02.move(p_guitar_pos[2][0], p_guitar_pos[2][1])
        self.Dot03.move(p_guitar_pos[3][0], p_guitar_pos[3][1])
        self.Dot04.move(p_guitar_pos[4][0], p_guitar_pos[4][1])
        self.Dot05.move(p_guitar_pos[5][0], p_guitar_pos[5][1])
        self.Dot06.move(p_guitar_pos[6][0], p_guitar_pos[6][1])
        self.Dot07.move(p_guitar_pos[7][0], p_guitar_pos[7][1])
        self.Dot08.move(p_guitar_pos[8][0], p_guitar_pos[8][1])
        self.Dot09.move(p_guitar_pos[9][0], p_guitar_pos[9][1])
        self.Dot10.move(p_guitar_pos[10][0], p_guitar_pos[10][1])
        self.Dot11.move(p_guitar_pos[11][0], p_guitar_pos[11][1])
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)

    def moveFuture(self):
        self.Dot01.move(860, 650)
        self.Dot02.move(860, 650)
        self.Dot03.move(860, 650)
        self.Dot04.move(860, 650)
        self.Dot05.move(860, 650)
        self.Dot06.move(860, 650)
        self.Dot07.move(860, 650)
        self.Dot08.move(860, 650)
        self.Dot09.move(860, 650)
        self.Dot10.move(860, 650)
        self.Dot11.move(860, 650)
        self.Dot12.move(860, 650)
        self.Dot13.move(860, 650)
        self.Dot14.move(860, 650)
        self.Dot15.move(860, 650)

    def moveFish(self):
        self.Dot01.move(p_fish_pos[1][0], p_fish_pos[1][1])
        self.Dot02.move(p_fish_pos[2][0], p_fish_pos[2][1])
        self.Dot03.move(p_fish_pos[3][0], p_fish_pos[3][1])
        self.Dot04.move(p_fish_pos[4][0], p_fish_pos[4][1])
        self.Dot05.move(p_fish_pos[5][0], p_fish_pos[5][1])
        self.Dot06.move(p_fish_pos[6][0], p_fish_pos[6][1])
        self.Dot07.move(p_fish_pos[7][0], p_fish_pos[7][1])
        self.Dot08.move(p_fish_pos[8][0], p_fish_pos[8][1])
        self.Dot09.move(p_fish_pos[9][0], p_fish_pos[9][1])
        self.Dot10.move(p_fish_pos[10][0], p_fish_pos[10][1])
        self.Dot11.move(860, 580)
        self.Dot12.move(860, 580)
        self.Dot13.move(860, 580)
        self.Dot14.move(860, 580)
        self.Dot15.move(860, 580)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
