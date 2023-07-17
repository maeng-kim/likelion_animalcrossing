import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input("너의 이름은? : ")
island = input("섬 이름을 새로 지어달라구리: ")

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    
    # 0. 게임 종료
    if answer_action == "0":
        print("게임종료.")
        break


    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("상점에 온걸 환경해구리!")
        print("현재 상점에는 이런 물건들이 있어구리\n")
        a =1
        for i in store:
            print(a,". ", i, ": ", store[i], "벨")
            a += 1
            time.sleep(0.1)
        s = int(input("어떤 물건을 구입하겠어구리? (숫자로 입력)"))

        if s == 1:
            print("가습기을(를) 구입하셨습니다!")
            my_pocket.append('가습기')
            print("남은 벨: ", my_bell - store['가습기'])
            if my_bell < store['가습기']:
                print("돈이 부족하다구리")
            store.pop('가습기')
        elif s == 2:
            print("강아지 인형을(를) 구입하셨습니다!")
            my_pocket.append('강아지 인형')
            print("남은 벨: ", my_bell - store['강아지 인형'])
            if my_bell < store['강아지 인형']:
                print("돈이 부족하다구리")
            store.pop('강아지 인형')
        elif s== 3:
            print("강의실 책상을(를) 구입하셨습니다!")
            my_pocket.append('강의실 책상')
            print("남은 벨: ", my_bell - store['강의실 책상'])
            if my_bell < store['강의실 책상']:
                print("돈이 부족하다구리")
            store.pop('강의실 책상')
        elif s==4:
            print("몬스테라을(를) 구입하셨습니다!")
            my_pocket.append('몬스테라')
            print("남은 벨: ", my_bell - store['몬스테라'])
            if my_bell < store['몬스테라']:
                print("돈이 부족하다구리")
            store.pop('몬스테라')

        

        
            



    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
       print("우리 마을에 있는 주민이야")
       b = 1
       for j in animal:
          print(b, ". ", j)
          b += 1
       answer_animal = int(input("어떤 주민을 찾아갈까? "))
       animal_list = list(animal.keys())
       print(animal_list[answer_animal-1], "에게 무엇을 할까?")
       answer_animal_action = int(input("1. 말걸기 2. 선물하기 3. 때리기"))


       if answer_animal_action==1:
            # 2-1. 말걸기를 선택한경우
           
            if answer_animal ==1:
               print("릴리안: 어머 ", name, " 왔구나 ~ 반가워!\n 어제는 어찌나 벚꽃이 이쁘던지 기분이 참 좋더라니까\n", name, "도 놀러다녀오는 건 어때? 그렇지 뭐")
               animal['릴리안'] += 1
               print("릴리안 친밀도 +1")

            elif answer_animal==2:
               print("탁호: 안녀엉~ ",name,"아~ 반가워어~\n 오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
               animal['탁호'] +=1
               print("탁호 친밀도 +1")

            elif answer_animal==3:
                print("미첼: ", name,"아~! 반가워! 오늘 날씨 되게 좋지않아?\n 마구마구 산책을 하고싶어져 동글")
                animal['미첼'] += 1
                print("미첼 친밀도 +1")
            elif answer_animal==4:
                print("리처드: ", name, "야아~\n 나무를 흔들었더니 100벨이 나왔어어~\n", name, "도 한 번 흔들어봐아~ 그래유")
                animal['리처드'] +=1
                print("리처드 호감도 +1") 
      
  

        # 2-1. 선물하기를 선택한 경우
       elif answer_animal_action == 2:
            print("내 주머니엔 이렇게 있어")
            d=1
            print(my_pocket)
            for q in my_pocket:
                print(d, " . ", q)
                d +=1

            select = input("어떤것을 선물할까? (숫자로 입력)")
            print(answer_animal, " 에게 ", my_pocket[select-1], " 을(를) 선물했다!")
            print(answer_animal, "친밀도 +1")
            animal[answer_animal] +=1
            del my_pocket[select-1]
            
           



        # 2-3. 떄리기를 선택한 경우
       elif answer_animal_action == 3:
            print(answer_animal, " 을(를) 때렸습니다. 친밀도 -1")
            animal[answer_animal] -=1




    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        print("나무를 흔듭니다.")
        result = random.random(1,3)

        # 100벨이 떨어질경우
        if result == 1:
            print("100벨이 나왔다구리!")
            my_bell+=1

        # 사과가 떨어질경우
        elif result == 2:
            print("사과가 떨어졌다구리!\n 획득한 사과는 너의 주머니에 들어간다구리!\n선물도 가능하다구리~!")
            my_pocket.append["사과"]

        # 벌이 나타날경우
        elif result == 3:
            print("응..?\n벌이 나타났습니다!\n아야.. 벌에게 물렸어")




    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        print("내 정보\n")

        # 이름 출력
        print("- 이름 : ", name)

        # 남은 벨 출력
        print("- 남은 벨 : ", my_bell)

        # 주머니 출력
        print("- 내 주머니 : ", my_pocket)

        # 주민 친밀도 출력
        print("- 주민과 친밀도 : ")
        c = 1
        for k in animal:
            print(c, ". ", k, " : ", animal[k])

        
        
        
    # 잘못된 입력을 했을경우
    else:
        print("다시 선택해!")
       

