import sys
import random

# 게임 방범 설명
print("출처: http://www.practicepython.org")
print("==================================")
print("가로, 세로, 대각선 방향으로                   ")
print("세점을 먼저 이어 놓으면 이기는")
print("게임으로 사용자(U)와 Computer(C)가")
print("번갈아 놓습니다.")
print("==================================\n")

# 3 x 3 정보를 담기 위한 저장소 선언
# 0 은 초기 상태
# 1 은 사용자가 선택한 곳
# 2 는 컴퓨터가 선택한 곳
dim=3
list4 = [0,0,0,0,0,0,0,0,0]

# 사용자 안내를 위한 박스를 그리고 그 안에 번호 넣기
def graph():
    k = 1
    for i in range(dim+1):
        print(" ---"*dim)
        for j in range(dim):
            if (i < dim):
                print("| "+str(k), end=" ")
                k = k + 1
        if (i != 3):
            print("|")

# 사용자 또는 컴퓨터가 수를 둘때 마다,
# 누가 이겼는지 체크
def game_wins(list4):
    #print(list4)
    for i in range(dim): 
        #checks to see if you win in a column
        if list4[i] == list4[i+3] == list4[i+6] == 1:
            print("You Won")
        elif list4[i] == list4[i+3] == list4[i+6] == 2:
            print("You Lost")
        #checks to see if you win in a row
        if list4[dim*i] == list4[dim*i+1] == list4[dim*i+2] == 1:
            print ("You Won")
        elif list4[dim*i] == list4[dim*i+1] == list4[dim*i+2] == 2:
            print("You Lost")
        #checks to see if you win in a diagonal
        if list4[0] == list4[4] == list4[8] == 1:
            print ("You Won")
        elif list4[0] == list4[4] == list4[8] == 2:
            print("You Lost")
        if list4[2] == list4[4] == list4[6] == 1:
            print ("You Won")
        elif list4[2] == list4[4] == list4[6] == 2:
            print("You Lost")

# 사용자 안내를 위한 박스를 그리고 그 안에 번호 또는 둔 수 표기
def graph_pos(list4):
    for idx in range(len(list4)):
        if (idx % 3 == 0):
            print(" ---"*dim)
        if (list4[idx] == 0):
            print("| "+str(idx+1), end=" ")
        elif (list4[idx] == 1):
            print("| "+"U", end=" ")
        else:
            print("| "+"C", end=" ")   
        if (idx % 3 == 2):
            print("|")
    print("\n")

# 게임 시작
go = input("Play TicTaeToe? Enter, or eXit?")
if (go == 'x' or go == 'X'):
    sys.exit(0)
graph()
print("\n")

while(1):  # 보드게임이 승부가 날때까지 무한 반복
        # 빈곳 선택
        pos = int(input("You : ")) - 1
        while (pos < 0 or pos > 8 or list4[pos] != 0):
            pos = int(input("Again : ")) - 1
        list4[pos] = 1
         
        # 보드를 갱신하여 그리고, 승부 체크
        graph_pos(list4)
        game_wins(list4)

        # 컴퓨터 차례로, 빈곳을 랜덤하게 선택하여 List에 저장
        pos = random.randrange(9)
        while (list4[pos] != 0):
            pos = random.randrange(9)
        print("Computer : " + str(pos+1))
        list4[pos] = 2
        
        # 보드를 갱신하여 그리고, 승부 체크
        graph_pos(list4)
        game_wins(list4)