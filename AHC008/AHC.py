from curses import COLOR_WHITE


N = int(input())

Pet = []

for Ni in range(N):
  Pet.append(list(map(int,input().split())))

M = int (input())
Hum = []

for Mi in range(M):
  Hum.append(list(map(int,input().split())))

InputStr=[]

#動物の種類集計
PCow = 0
PPig = 0
PRab = 0
PDog = 0
PCat = 0
for Ni in range(N):
  Ptype = Pet[Ni][2]
  if Ptype == 1:
    PCow += 1
  elif Ptype == 2:
    PPig += 1
  elif Ptype == 3:
    PRab += 1
  elif Ptype == 4:
    PDog += 1
  elif Ptype == 5:
    PCat += 1


for Turn in range(1,301):
  #アウトプット
  OUTStr=''

  #壁作成予定リスト
  MakeWallList = []

  #犬対策
  if PDog > 0:
    MakeWallList.append([2,2])
    for i in range(1, PDog + 2):
      if not [1,i] in MakeWallList:
        MakeWallList.append([1,i])

    
  print(MakeWallList)

  for Out in range(M):
    OUTStr += '.'
  print(OUTStr)

  #ペットの行動インプット
  InputStr = list(map(str,input().split()))
  for Ni in range(N):
    for PKoud in range(len(InputStr[Ni])):
      ChuPKoud = InputStr[Ni][PKoud]
      if ChuPKoud == 'U':
        Pet[Ni][0] += -1
      elif ChuPKoud == 'D':
        Pet[Ni][0] += 1
      elif ChuPKoud == 'L':
        Pet[Ni][1] += -1
      elif ChuPKoud == 'R':
        Pet[Ni][1] += 1