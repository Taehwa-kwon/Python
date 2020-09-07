import functionM as fm

fm.rankLoad()

while True:
   print('''
       1.문제불러오기 
       2.문제txt저장하기
       3.문제추가 
       4.문제 피클로 저장 
       5.피클 문제 읽기
       6.타자게임 
       7.등수리스트 
       8.종료하기''')
   menu = input("메뉴를 선택하세요\n")
   if menu=='1':
      fm.wordLoadTxt()
   elif menu=='2':
      fm.wordSaveTxt()
   elif menu=='3':
      fm.wordAppend()
   elif menu=='4':
      fm.wordSavePik() 
   elif menu=='5':
      fm.wordLoadPik()
   elif menu=='6':
      fm.game()      
   elif menu=='7':
      fm.rankList()
   elif menu=='8':
      fm.endGame()
      break



