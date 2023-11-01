#-*-coding: utf-8-*-
from ast import Not
import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup
import time
import os
import numpy as np

def Program(soup,tier):
    Name=[]
    Pickrate=[]
    Winrate=[]
    Top3=[]
    for i in soup.select("td.character > div > a"):
        Name.append(i.text)

    for i in soup.select("td.text-center.pickrate.sort > b"):
        Pickrate.append(i.text.strip())

    for i in soup.select("td.text-center.winrate > b"):
        Winrate.append(i.text.strip())

    for i in soup.select("td:nth-child(5)"):
        Top3.append(i.text.strip())

    for i in range(0,78):
        line=[]
        for j in range(1):
            line.append(i)
            line.append(Name[i])
            line.append(Pickrate[i].strip("%"))
            line.append(Winrate[i].strip("%"))
            line.append(Top3[i].strip("%"))
        tier.append(line)

def Soloteir(tier):
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    tr=[]
    for i in tier:
        pr=np.array(i).T[2]
        wr=np.array(i).T[3]
        to3=np.array(i).T[4]
        if wr=="-" or pr=="-":
            tr.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=41.00:
            t1.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=35.00:
            t2.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=30.00:
            t3.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=27.00:
            t4.append(f"{i[1]}")
        else:
            t5.append(f"{i[1]}")

    print('\033[96m'f"{'='*20}1티어{'='*20}")    
    for i in t1:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[92m'f"{'='*20}2티어{'='*20}")
    for i in t2:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[33m'f"{'='*20}3티어{'='*20}")
    for i in t3:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[90m'f"{'='*20}4티어{'='*20}")
    for i in t4:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[31m'f"{'='*20}5티어{'='*20}")
    for i in t5:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print(f"{'='*20}RIP{'='*20}")
    for i in tr:
        print(f"\t\t{i}")
    
def Duoteir(tier):
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    tr=[]
    for i in tier:
        pr=np.array(i).T[2]
        wr=np.array(i).T[3]
        to3=np.array(i).T[4]
        if wr=="-" or pr=="-":
            tr.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=70.00:
            t1.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=61.00:
            t2.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=55.00:
            t3.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=50.00:
            t4.append(f"{i[1]}")
        else:
            t5.append(f"{i[1]}")

        
    print('\033[96m'f"{'='*20}1티어{'='*20}")    
    for i in t1:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[92m'f"{'='*20}2티어{'='*20}")
    for i in t2:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[33m'f"{'='*20}3티어{'='*20}")
    for i in t3:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[90m'f"{'='*20}4티어{'='*20}")
    for i in t4:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[31m'f"{'='*20}5티어{'='*20}")
    for i in t5:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print(f"{'='*20}RIP{'='*20}")
    for i in tr:
        print(f"\t\t{i}")

def Squrdteir(tier):
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    tr=[]
    for i in tier:
        pr=np.array(i).T[2]
        wr=np.array(i).T[3]
        to3=np.array(i).T[4]
        if wr=="-" or pr=="-":
            tr.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=85.00:
            t1.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=80.00:
            t2.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=75.00:
            t3.append(f"{i[1]}")
        elif float(pr)+float(wr)+float(to3)>=65.00:
            t4.append(f"{i[1]}")
        else:
            t5.append(f"{i[1]}")

        
    print('\033[96m'f"{'='*20}1티어{'='*20}")    
    for i in t1:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[92m'f"{'='*20}2티어{'='*20}")
    for i in t2:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[33m'f"{'='*20}3티어{'='*20}")
    for i in t3:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[90m'f"{'='*20}4티어{'='*20}")
    for i in t4:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[31m'f"{'='*20}5티어{'='*20}")
    for i in t5:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print(f"{'='*20}RIP{'='*20}")
    for i in tr:
        print(f"\t\t{i}")

def Cobaltteir(tier):
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    tr=[]
    for i in tier:
        pr=np.array(i).T[2]
        wr=np.array(i).T[3]
        if wr=="-" or pr=="-":
            tr.append(f"{i[1]}")
        elif float(pr)+float(wr)>=61.00:
            t1.append(f"{i[1]}")
        elif float(pr)+float(wr)>=58.00:
            t2.append(f"{i[1]}")
        elif float(pr)+float(wr)>=53.00:
            t3.append(f"{i[1]}")
        elif float(pr)+float(wr)>=49.00:
            t4.append(f"{i[1]}")
        else:
            t5.append(f"{i[1]}")

        
    print('\033[96m'f"{'='*20}1티어{'='*20}")    
    for i in t1:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[92m'f"{'='*20}2티어{'='*20}")
    for i in t2:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[33m'f"{'='*20}3티어{'='*20}")
    for i in t3:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[90m'f"{'='*20}4티어{'='*20}")
    for i in t4:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print('\033[31m'f"{'='*20}5티어{'='*20}")
    for i in t5:
        print(f"\t\t{i}")
    print('\033[0m',end="")
    print(f"{'='*20}RIP{'='*20}")
    for i in tr:
        print(f"\t\t{i}")

def CharcterName(Chname,KRname,ENname):
    for i in range(57):
        line=[]
        for j in range(1):
            line.append(KRname[i])
            line.append(ENname[i])
            Chname.append(line)

while(1):
    os.system("title 이터널리턴")
    print(f"\033[32m{'='*53}\033[0m")
    now=datetime.datetime.now()
    print(f"      \033[33m현재시간: {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초\033[0m")
    print("\t\033[35m이터널리턴 도우미v0.1.0-Alpha3")
    print("\t     원하는 모드를 선택하세요\033[0m")
    print("\t\t\033[96m제작자: 함수아\033[0m")
    # print("\t     \033[96m버전정보: 0.1.0-Alpha2\033[0m")
    print("   \033[31m 본 프로그램은 테스트 목적으로 제작되었습니다")
    print("    상업적 목적으로 배포시 법적 책임이 따릅니다!\033[0m")
    print(f"\033[32m{'='*53}\033[0m")
    menu=input("\033[35m1.실험체 티어 2.전적검색 3.패치노트 4.실험체 검색\n5.공식홈페이지 6.아이템 도감 7.이밴트 8.종료\n\033[33m입력: \033[0m")
    print(f"\033[32m{'='*53}\033[0m")
    if menu.isnumeric():
        menu=int(menu)
        if menu == 1:
            os.system("cls")
            while(1):
                tier=[]
                print(f"\033[32m{'='*61}\033[0m")
                sel = input("\033[33m1.솔로\n2.듀오\n3.스쿼드\n4.코발트\n5.초기화면으로 돌아가기\n입력: \033[0m")
                print(f"\033[32m{'='*61}\033[0m")
                if sel.isnumeric():
                    sel = int(sel)
                    if sel == 1:
                        res = requests.get(
                            "https://dak.gg/bser/statistics?type=OVER_DIAMOND&teamMode=SOLO&hl=ko-KR")
                        soup = BeautifulSoup(res.text, "html.parser")
                        Program(soup,tier)
                        Soloteir(tier)
                        input("\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                        os.system("cls")
                        break
                    elif sel == 2:
                        res = requests.get(
                            "https://dak.gg/bser/statistics?type=OVER_DIAMOND&teamMode=DUO&hl=ko-KR")
                        soup = BeautifulSoup(res.text, "html.parser")
                        Program(soup,tier)
                        Duoteir(tier)
                        input("\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                        os.system("cls")
                        break
                    elif sel == 3:
                        res = requests.get(
                            "https://dak.gg/bser/statistics?type=OVER_DIAMOND&teamMode=SQUAD&hl=ko-KR")
                        soup = BeautifulSoup(res.text, "html.parser")
                        Program(soup,tier)
                        Squrdteir(tier)
                        input("\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                        os.system("cls")
                        break
                    elif sel == 4:
                        res = requests.get(
                            "https://dak.gg/bser/statistics?type=OVER_DIAMOND&teamMode=COBALT&hl=ko-KR")
                        soup = BeautifulSoup(res.text, "html.parser")
                        Program(soup,tier)
                        Cobaltteir(tier)
                        input("\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                        os.system("cls")
                        break
                    elif sel == 5:
                        print("\033[32m초기 화면으로 돌아갑니다.\033[0m")
                        time.sleep(0.7)
                        os.system("cls")
                        break
                    else:
                        print("\033[31m잘못 입력하셨습니다!\033[0m")
                        time.sleep(0.7)
                        os.system("cls")
                        pass
                else:
                    print("\033[31m잘못 입력하셨습니다!\033[0m")
                    time.sleep(0.7)
                    os.system("cls")
                    pass
        elif menu == 2:
            while(1):
                os.system("cls")
                print(f"\033[32m{'='*53}\033[0m")
                Nameinput=input("\033[35m플레이어 닉네임을 입력하세요: \033[0m")
                print(f"\033[32m{'='*53}\033[0m")
                if Nameinput == "":
                    print("\033[31m다시 입력해주세요!\033[0m")
                    time.sleep(0.7)
                    pass
                else:
                    url=f"https://dak.gg/bser/players/{Nameinput}/matches?season=NORMAL&hl=ko-KR"
                    webbrowser.open(url)
                    input("\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                    time.sleep(0.7)
                    os.system("cls")
                    break
        elif menu == 3:
            os.system("cls")
            res = requests.get(
                "https://www.inven.co.kr/board/er/5772")
            soup = BeautifulSoup(res.text, "html.parser")
            print(f"\033[32m{'='*53}\033[0m")
            for j in range(6):
                for i in soup.select(f"tr:nth-child({j}) > td.tit > div > div > a"):
                    url = i.get("href")
                    Name = i.text.replace(" ", "")
                    Name = Name.replace("\n", " ")
                    print(f"\033[36m{j}.{Name}\033[0m")
            print("\033[36m6. 초기화면으로 돌아가기\033[0m")
            print(f"\033[32m{'='*53}\033[0m")
            while(1):
                View = input("\033[35m원하는 번호를 선택하세요: \033[0m")
                if View.isnumeric():
                    View=int(View)
                    if View == 1:
                        for i in soup.select("tr:nth-child(1) > td.tit > div > div > a"):
                            url = i.get("href")
                            webbrowser.open(url)
                    elif View == 2:
                        for i in soup.select("tr:nth-child(2) > td.tit > div > div > a"):
                            url = i.get("href")
                            webbrowser.open(url)
                    elif View == 3:
                        for i in soup.select("tr:nth-child(3) > td.tit > div > div > a"):
                            url = i.get("href")
                            webbrowser.open(url)
                    elif View == 4:
                        for i in soup.select("tr:nth-child(4) > td.tit > div > div > a"):
                            url = i.get("href")
                            webbrowser.open(url)
                    elif View == 5:
                        for i in soup.select("tr:nth-child(5) > td.tit > div > div > a"):
                            url = i.get("href")
                            webbrowser.open(url)
                    elif View == 6:
                        print("\033[32m초기 화면으로 돌아갑니다.\033[0m")
                        time.sleep(0.7)
                        os.system("cls")
                        break
                    else:
                        print("\033[31m잘못 입력하셨습니다!\033[0m")
                        time.sleep(0.7)
                        pass
                else:
                    print("\033[31m잘못 입력하셨습니다!\033[0m")
                    time.sleep(0.7)
                    pass                     
        elif menu == 4:
            while(1):
                os.system("cls")
                print(f"\033[32m{'='*53}\033[0m")
                Character = input("\033[35m1.루트찾기\n2.실험체 가이드\n3.실험체 정보\n4.초기화면으로 돌아가기\n입력: \033[0m")
                print(f"\033[32m{'='*53}\033[0m")
                if Character.isnumeric():
                    Character=int(Character)
                    Chname=[]
                    KRname=['나딘', '나타폰', '니키', '다니엘', '띠아', '라우라', '레녹스', '레온', '로지', '루크', '리다이린', '리오', '마르티나', '마이', '마커스', '매그너스', '바바라', '버니스', '비앙카', '셀린', '쇼우', '쇼이치', '수아', '시셀라', '실비아', '아델라', '아드리아나', '아디나', '아야', '아이솔', '알렉스', '얀', '에스텔', '에이든', '에키온', '엘레나', '엠마', '요한', '윌리엄', '유키', '이바', '일레븐', '자히르', '재키', '제니', '카밀로', '칼라', '캐시', '클로에', '키아라', '펠릭스', '프리야', '피오라', '피올로', '하트', '현우', '혜진']
                    ENname=['Nadine', 'Nathapon', 'Nicky', 'Daniel', 'Tia', 'Laura', 'Lenox', 'Leon', 'Rozzi', 'Luke', 'LiDailin', 'Rio', 'Martina', 'Mai', 'Markus', 'Magnus', 'Barbara', 'Bernice', 'Bianca', 'Celine', 'Xiukai', 'Shoichi', 'Sua', 'Sissela', 'Silvia', 'Adela', 'Adriana', 'Adina', 'Aya', 'Isol', 'Alex', 'Jan', 'Estelle', 'Aiden', 'Echion', 'Elena', 'Emma', 'Johann', 'William', 'Yuki', 'Eva', 'Eleven', 'Zahir', 'Jackie', 'Jenny', 'Camilo', 'Karla', 'Cathy', 'Chloe', 'Chiara', 'Felix', 'Priya', 'Fiora', 'Piolo', 'Hart', 'Hyunwoo', 'Hyejin']
                    CharcterName(Chname,KRname,ENname)
                    if Character == 1:
                        os.system("cls")
                        print(f"\033[32m{'='*53}\033[0m")
                        print("\033[35m\t\t\t루트찾기\033[0m")
                        print("\033[96m\t  한글 검색/영문 검색 모두 가능합니다\n     영문검색시 앞글자는 대문자로 검색해주세요\033[0m")
                        print(f"\033[32m{'='*53}\033[0m")
                        CharacterName = input("\033[35m실험체 이름을 입력해주세요: \033[0m")
                        for i in range(56):
                            if CharacterName == Chname[i][0] or CharacterName == Chname[i][1]:
                                url = f"https://dak.gg/bser/routes?character={Chname[i][1]}&hl=ko-KR"
                                webbrowser.open(url)
                                input(
                                    "\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                                break
                            elif CharacterName not in KRname and CharacterName not in ENname:
                                print("\033[31m존재하지 않는 실험체입니다!\033[0m")
                                time.sleep(0.7)
                                os.system("cls")
                                break
                        time.sleep(0.7)
                        os.system("cls")
                        break
                    elif Character == 2:
                        os.system("cls")
                        print(f"\033[32m{'='*53}\033[0m")
                        print("\033[35m\t\t     실험체 가이드\033[0m")
                        print("\033[96m\t  한글 검색/영문 검색 모두 가능합니다\n     영문검색시 앞글자는 대문자로 검색해주세요\033[0m")
                        print(f"\033[32m{'='*53}\033[0m")
                        CharacterName = input("\033[35m실험체 이름을 입력해주세요: \033[0m")
                        for i in range(56):
                            if CharacterName == Chname[i][0] or CharacterName == Chname[i][1]:
                                url = f"https://dak.gg/bser/characters/{Chname[i][1]}?hl=ko-KR"
                                webbrowser.open(url)
                                input(
                                    "\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                                break
                            elif CharacterName not in KRname and CharacterName not in ENname:
                                print("\033[31m존재하지 않는 실험체입니다!\033[0m")
                                time.sleep(0.7)
                                os.system("cls")
                                break
                        time.sleep(0.7)
                        os.system("cls")
                        break
                    elif Character == 3:
                        os.system("cls")
                        print(f"\033[32m{'='*53}\033[0m")
                        print("\033[35m\t\t     실험체 정보\033[0m")
                        print("\033[96m\t  한글 검색/영문 검색 모두 가능합니다\n     영문검색시 앞글자는 대문자로 검색해주세요\033[0m")
                        print(f"\033[32m{'='*53}\033[0m")
                        CharacterName = input("\033[35m실험체 이름을 입력해주세요: \033[0m")
                        for i in range(56):
                            if CharacterName == Chname[i][0] or CharacterName == Chname[i][1]:
                                url = f"https://er.inven.co.kr/db/character/{Chname[i][1]}"
                                webbrowser.open(url)
                                input(
                                    "\033[32m초기화면으로 돌아가시려면 아무키나 누르세요\033[0m")
                                break
                            elif CharacterName not in KRname and CharacterName not in ENname:
                                print("\033[31m존재하지 않는 실험체입니다!\033[0m")
                                time.sleep(0.7)
                                os.system("cls")
                                break
                        time.sleep(0.7)
                        os.system("cls")
                        break
                    elif Character == 4:
                        print("\033[33m초기 화면으로 돌아갑니다.\033[0m")
                        time.sleep(0.7)
                        os.system("cls")
                        break
                    else:
                        print("\033[31m잘못 입력하셨습니다!\033[0m")
                        time.sleep(0.7)
                        os.system("cls")
                        pass
                else:
                    print("\033[31m잘못 입력하셨습니다!\033[0m")
                    time.sleep(0.7)
                    os.system("cls")
                    pass
        elif menu == 5:
            url = f"https://playeternalreturn.com/main"
            webbrowser.open(url)
            time.sleep(0.7)
            os.system("cls")
            pass
        elif menu == 6:
            url = f"https://er.op.gg/items?&utm_source=playeternalreturn&utm_medium=referral&utm_campaign=wiki"
            webbrowser.open(url)
            time.sleep(0.7)
            os.system("cls")
            pass
        elif menu == 7:
            url = f"https://playeternalreturn.com/posts/news?categoryPath=event"
            webbrowser.open(url)
            time.sleep(0.7)
            os.system("cls")
            pass
        elif menu == 8:
            print("\033[35m\t\t프로그램이 종료됩니다\033[0m")
            time.sleep(0.7)
            exit()
        else:
            print("\033[31m잘못 입력하셨습니다!\033[0m")
            time.sleep(0.7)
            os.system("cls")
            pass
    else:
        print("\033[31m잘못 입력하셨습니다!\033[0m")
        time.sleep(0.7)
        os.system("cls")
        pass
