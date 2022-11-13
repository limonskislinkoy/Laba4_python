import main
print("Выберите метод сортировки: 1 - quicksort  2- brushsort  3-блочная  4-пирамидальная")
choise = int(input())
s = list(map(int, input().split()))
if choise == 1:
    main.quiksort(s)
    print(*s)
if choise == 2:
    main.brushsort(s)
    print(*s)

if choise == 3:
    s = main.basket(s)
    print(*s)
if choise == 4:
    main.heapsort(s)
    print(*s)