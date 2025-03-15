n = int(input())
card = list(map(int, input().split(' ')))
card.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

for target in targets:

    # 시작점, 끝점 설정
    left, right = 0, n - 1

    # 양 끝점 안에 담이 있는지 확인
    if target < card[left] or target > card[right]:
        print("0 ", end = "")
        continue

    while left <= right:
        mid = (left + right) // 2
        if card[mid] == target:
            break
        elif card[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left > right:
        print("0 ", end = "")
    else:
        print("1 ", end = "")