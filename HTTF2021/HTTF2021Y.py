


from doctest import OutputChecker




def MoveStr_onediction(Outstr,Con):
  OutputStr = ''
  for Confor in range(Con):
    OutputStr += Outstr
  return OutputStr

#移動関数
#引数
#Start:移動開始位置
#Goal :移動終了位置
def MoveStr(Start , Goal):
  OutputStr = ''
  Xspec = Start[0] - Goal[0]
  Yspec = Start[1] - Goal[1]
  #左右
  if Xspec > 0:
    OutputStr += MoveStr_onediction('U',Xspec)
  elif Xspec < 0:
    OutputStr += MoveStr_onediction('D',Xspec*(-1))
  #上下
  if Yspec > 0:
    OutputStr += MoveStr_onediction('L',Yspec)
  elif Yspec < 0:
    OutputStr += MoveStr_onediction('R',Yspec*(-1))
  return OutputStr

#二点間の距離計測
def MoveDis(Start , Goal):
  Xspec = abs(Start[0] - Goal[0])
  Yspec = abs(Start[1] - Goal[1])
  return Xspec + Yspec

#三点間の距離計測
def Move3Dis(Start, Middle,Goal):
  return MoveDis(Start,Middle) + MoveDis(Middle,Goal)

#四点間の距離計測
def Move4Dis(Start, Middle1, Middle2, Goal):
  return MoveDis(Start,Middle1) + MoveDis(Middle1,Middle2) + MoveDis(Middle2,Goal)

#最適位置候補リストアップ
def FindOptimalPos(CardNum,CardPos,CPYet):
  OptimalPosList = []
  for Xspec in range(min([CardPos[CardNum - 1][0],CardPos[CardNum + 1][0]]),max([CardPos[CardNum - 1][0],CardPos[CardNum + 1][0]])+1):
    for Yspec in range(min([CardPos[CardNum - 1][1],CardPos[CardNum + 1][1]]),max([CardPos[CardNum - 1][1],CardPos[CardNum + 1][1]])+1):
      if not [Xspec,Yspec] in CardPos and not [Xspec,Yspec] in CPYet:
        OptimalPosList.append([Xspec,Yspec])
  # return [CardNum,OptimalPosList]
  
  return OptimalPosList

def Tanshuku(StartPos,GoalPos,CardNumber,CP,CPYet,KeepCard,OutputStr):
  #一番改善できるカード検索
  BestKaizenDis = 0

  ChangeCard = 0
  KaizenDisPos = [0,0]

  for CardSrach in range(CardNumber+1,99):
    if not CardSrach in KeepCard:
      CardPutList = FindOptimalPos(CardSrach,CP,CPYet)
      # print(CardSrach)
      for CardPut in CardPutList:
        if not Move3Dis(CP[CardSrach - 1],CP[CardSrach],CP[CardSrach + 1]) == MoveDis(CP[CardSrach - 1],CP[CardSrach + 1]):
          KaizenDis = Move3Dis(CP[CardSrach - 1],CP[CardSrach],CP[CardSrach + 1]) - Move3Dis(CP[CardSrach - 1],CardPut,CP[CardSrach + 1]) \
            - (Move4Dis(StartPos,CP[CardSrach],CardPut,GoalPos) - MoveDis(StartPos,GoalPos))
          if KaizenDis > BestKaizenDis:
            BestKaizenDis = KaizenDis
            ChangeCard = CardSrach
            KaizenDisPos = CardPut

  #カード改善動作
  if BestKaizenDis > 0:
    GetCardPos = CP[ChangeCard]
    Yet = CP[ChangeCard]
    CPYetsplit = CPYet
    CPYetsplit.append(CP[ChangeCard])
    KeepCardsplit=KeepCard
    KeepCardsplit.append(ChangeCard)
    CP[ChangeCard] = KaizenDisPos
    #カード取得
    # OutputStr += MoveStr(StartPos,GetCardPos)
    StartPos,OutputStr = Tanshuku(StartPos,GetCardPos,CardNumber,CP,CPYetsplit,KeepCard,OutputStr)
    # StartPos = GetCardPos
    OutputStr +='I'
    # OutputStr += MoveStr(StartPos,CP[ChangeCard])
    StartPos,OutputStr = Tanshuku(StartPos,CP[ChangeCard],CardNumber,CP,CPYet,KeepCardsplit,OutputStr)
    # StartPos = CP[ChangeCard]
    OutputStr +='O'
    StartPos,OutputStr = Tanshuku(StartPos,GoalPos,CardNumber,CP,CPYet,KeepCard,OutputStr)
  # print(BestKaizenDis)
  # print(ChangeCard)
  # print(KaizenDisPos)



  OutputStr += MoveStr(StartPos,GoalPos)
  return GoalPos,OutputStr

#カード初期位置
CIP = []

#ロボ位置
RoboPos = [0,0]

#出力文字列
OutputStr = ''

# i = CardCollect

for CardNumber in range(100):
  CIP.append(list(map(int,input().split())))

#カードの配置先
CP = CIP

#カードを取得
for CardNumber in range(100):
  RoboPos,OutputStr = Tanshuku(RoboPos,CP[CardNumber],CardNumber,CP,[],[],OutputStr)
  OutputStr += 'I'
  CP[CardNumber] = [21,21]

print(OutputStr)