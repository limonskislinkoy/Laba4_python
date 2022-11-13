import math


def quiksort(mas,left=-1,right=-1):

    if left==-1 and right==-1:
        left = 0
        right = len(mas)-1
    oldleft = left
    oldright = right
    med=(left+right)//2
    while left<=right:
        #print(med)
        while(mas[left]<mas[med]):
            #print(left)
            left+=1

        while(mas[right]>mas[med]):
            right-=1

        if(left<=right):
            t=mas[left]
            #print(mas, left,right , oldleft ,oldright)
            mas[left]=mas[right]
            mas[right]=t
            left+=1
            right-=1
        else:
            break
    #print(left,right)

    #print(mas)
    if (oldleft<right):
        quiksort(mas,oldleft,right)
    if (oldright>left):
        quiksort(mas,left,oldright)


def brushsort(mas):
    stop=False
    delta = len(mas) - 1
    while not stop:
        delta=math.ceil(math.sqrt(delta)-1)
        delta=max(1,delta)
        if delta==1:
            stop=True
        #print(delta)
        for i in range(len(mas)-delta):
            if mas[i]>mas[i+delta]:
                if(delta==1):
                    stop=False
                mas[i],mas[i+delta]=mas[i+delta],mas[i]


def basket(mas):
    maxx= max(mas)
    minn= min(mas)
    step=(maxx-minn)/10
    a0=[]
    a1=[]
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []

    for i in range(len(mas)):
        num = mas[i]//step
        if num == 0:
            a0.append(mas[i])
        if num == 1:
            a1.append(mas[i])
        if num == 2:
            a2.append(mas[i])
        if num == 3:
            a3.append(mas[i])
        if num == 4:
            a4.append(mas[i])
        if num == 5:
            a5.append(mas[i])
        if num == 6:
            a6.append(mas[i])
        if num == 7:
            a7.append(mas[i])
        if num == 8:
            a8.append(mas[i])
        if num >= 9:
            a9.append(mas[i])

    quiksort(a0)
    quiksort(a1)
    quiksort(a2)
    quiksort(a3)
    quiksort(a4)
    quiksort(a5)
    quiksort(a6)
    quiksort(a7)
    quiksort(a8)
    quiksort(a9)
    a =[]
    for i in a0: a.append(i)
    for i in a1: a.append(i)
    for i in a2: a.append(i)
    for i in a3: a.append(i)
    for i in a4: a.append(i)
    for i in a5: a.append(i)
    for i in a6: a.append(i)
    for i in a7: a.append(i)
    for i in a8: a.append(i)
    for i in a9: a.append(i)

    return a


def heapsort(mas):
    build_max_heap(mas)
    for i in range(len(mas) - 1, 0, -1):
        mas[0], mas[i] = mas[i], mas[0]
        max_heapify(mas, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(mas):
    length = len(mas)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(mas, index=start, size=length)
        start = start - 1


def max_heapify(mas, index, size):
    l = left(index)
    r = right(index)
    if (l < size and mas[l] > mas[index]):
        largest = l
    else:
        largest = index
    if (r < size and mas[r] > mas[largest]):
        largest = r
    if (largest != index):
        mas[largest], mas[index] = mas[index], mas[largest]
        max_heapify(mas, largest, size)




