def seqSearch(ary, fData) :
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fData :
            pos = ibreak
    return pos


dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
findData = 333
position = seqSearch(dataAry, findData)
if position == -1:
    print("없어요")
else:
    print(dataAry[position])