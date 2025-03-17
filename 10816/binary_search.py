n = int(input())
card = list(map(int, input().split(' ')))
card.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

for target in targets:

    # 양 끝점 안에 담이 있는지 확인
    if target < card[0] or target > card[n - 1]:
        print("0", end = " ")
        continue

    # target보다 작거나 같은 것 중 제일 오른쪽
    left, right = 0, n - 1
    while left < right:
        mid = (left + right + 1) // 2
        if card[mid] <= target:
            left = mid
        else:
            right = mid - 1
    
    right_most = right

    # target보다 크거나 같은 것 중 제일 왼쪽
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if card[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    left_most = right
    
    print(right_most - left_most + 1, end = " ")