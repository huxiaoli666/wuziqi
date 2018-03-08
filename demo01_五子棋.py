import random
#五子棋
chessMap=[]
#制作棋盘
def makeMap(size):
	for i in range(size):
		list=[]
		for j in range(size):
			list.append('口')
		chessMap.append(list)
# 显示棋盘
# def printMap():
# 	for m in range(size):
# 		for n in range(size):
# 			print(chessMap[m][n],end='')
# 	print()	
def showMap():
	for i in range(size):
		for j in range(size):
			print(chessMap[i][j],end='')
		print()
#下棋
def playChess(playName,playStyle,chessStyle):
	while True:
		#人下棋
		if playStyle==1:
			x=int(input("请%s输入落子的横坐标：\t"%(playName)))
			y=int(input("请%s输入落子的纵坐标：\t"%(playName)))
			if chessMap[x][y]!='口':
				print("该位置已有棋子，请重新输入！")
			else:
				chessMap[x][y]=chessStyle
				showMap()
				whoWin(x,y,chessStyle,playName)
				break
		#电脑下棋
		elif playStyle==2:
			x=random.randint(0,len(chessMap)-1)
			y=random.randint(0,len(chessMap)-1)
			if chessMap[x][y]!='口':
				print("该位置已有棋子，请重新输入！")
			else:
				chessMap[x][y]=chessStyle
				showMap()
				whoWin(x,y,chessStyle,playName)
				break

#谁赢谁输
def whoWin(x,y,chessStyle,playName):
	#行 根据输入的坐标，判断坐标所在行的情况
	row = x
	line = 0
	num = 0
	for i in range(len(chessMap)):
		if chessMap[x][line]==chessStyle:
			num = num+1
			if num>=5:
				print('恭喜'+playName+'玩家赢了！(行五子)')
				exit()
		else:
			num = 0
		line = line+1
	#列 根据输入的坐标，判断坐标所在列的情况
	row = 0
	line = y
	num = 0
	for i in range(len(chessMap)):
		if chessMap[row][y]==chessStyle:
			num = num+1
			if num>=5:
				print('恭喜'+playName+'玩家赢了！(列五子)')
				exit()
		else:
			num = 0
		row = row+1
	#右上角  根据输入的坐标，从第一行的第一列往下遍历
	if y>=x:
		row = 0  
		line = y-x
		num = 0
		for i in range(len(chessMap)-line):
			if chessMap[row][line]==chessStyle:
				num = num+1
				if num>=5:
					print('恭喜'+playName+'玩家赢了！(右上角五子)')
					exit()
			else:
				num = 0
			row = row+1
			line = line+1
	#左下角  根据输入的坐标，从第一行的第一列往下遍历
	if x>y:
		row = x-y
		line = 0
		num = 0
		for i in range(len(chessMap)-row):
			if chessMap[row][line]==chessStyle:
				num = num+1
				if num>=5:
					print('恭喜'+playName+'玩家赢了！(左下角五子)')
					exit()
			else:
				num = 0
			row = row+1
			line = line+1
	#左上角 根据输入的坐标，从第一行的最后一列往下遍历
	if (x+y)<len(chessMap):
		row = 0
		line = x+y
		num = 0
		for i in range(line+1):
			if chessMap[row][line]==chessStyle:
				num = num+1
				if num>=5:
					print('恭喜'+playName+'玩家赢了！(左上角五子)')
					exit()
			else:
				num = 0
			row = row+1
			line = line-1
	#右下角 根据输入的坐标，从最后一列的第一行开始往下遍历
	row = x+y-len(chessMap)+1
	line = len(chessMap)-1
	num = 0
	for i in range(len(chessMap)-row):
		if chessMap[row][line]==chessStyle:
			num = num+1
			if num>=5:
				print('恭喜'+playName+'玩家赢了！(右下角五子)')
				exit()
		else:
			num = 0
		row = row+1
		line = line-1





while True:
	size=input("请输入棋盘大小且是大于10的数字：\t")
	if size.isdigit():
		size=int(size)
		if size>10:
			makeMap(size)
			# printMap()
			showMap()
			break
		else:
			print("您输入的不是大于10的数字，请重新输入：")
	else:
		print("您输入的不是纯数字，请重新输入！")
while True:
	playStyle=int(input("请输入对弈方式：\n1.人人对弈\t 2.人机对弈"))
	if playStyle==1:
		print("----提示：您选择的是人人对弈！----")
		playerName1=input("请为玩家1取名字：")
		playerName2=input("请为玩家2取名字：")
		break
	elif playStyle==2:
		print("----提示：您选择的是人机对弈！----")
		playerName1=input("请为玩家1取名字：")
		playerName2=input("请为玩家2(电脑)取名字：")
		break
	else:
		print("----输入错误，请重新输入！----")
while True:
	chessStyle1=input("请%s玩家选择棋子的样式：\n(提示：最好是中文符)"%(playerName1))
	chessStyle2=input("请%s玩家选择棋子的样式"%(playerName2))
	if chessStyle1!=chessStyle2:
		print("----游戏开始！----")
		break
	else:
		print("两位玩家的棋子样式一样，请重新选择不一样的！")
while True:
	if playStyle==1:
		playChess(playerName1,playStyle,chessStyle1)
		playChess(playerName2,playStyle,chessStyle2)
	elif playStyle==2:
		playChess(playerName1,1,chessStyle1)
		playChess(playerName2,playStyle,chessStyle2)


