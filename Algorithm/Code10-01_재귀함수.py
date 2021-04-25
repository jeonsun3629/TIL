def openBox() :
    global count
    print("상자 열기")
    count -= 1
    if count == 0:
        print("반지")
        return
    openBox()
    print("##상자 닫기##")

count = 10
openBox()
