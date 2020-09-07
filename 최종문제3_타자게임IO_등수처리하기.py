import func

func.openRank()

while True:
   print("1.문제불러오기  2.타자게임  3.등수목록  4.종료하기")
   menu = input("메뉴를 선택하세요\n")
   if menu=='1':
       func.quizOpen()
   elif menu=='2':
       func.quiz()
   elif menu=='3':
       func.rankList() 
   elif menu=='4':
       answer = input('정말 종료하시겠습니까?(Y)')
       if answer == 'Y' or answer=='y':
           break
   else:
       print("메뉴를 잘못 선택하셨습니다.")

func.closeRank()
