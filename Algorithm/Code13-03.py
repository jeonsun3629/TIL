def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start + end) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return pos

dataAry = [50, 105, 120, 150, 162, 168, 177, 188] # 이진 분류는 선정렬 필요**
findData = 162

print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1:
    print(findData, "이(가) 없어요")
else:
    print(findData, '은(는)', position, ' 위치에 있음')