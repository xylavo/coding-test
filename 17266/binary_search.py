n = int(input())
m = int(input())
light = list(map(int, input().split(" ")))

left, right = 1, n
while left < right:
    # 가로등의 높이
    mid = (left + right) // 2
    # 마지막으로 불빛을 비춘 위치
    last_point = 0
    for target in light:
        if last_point < target - mid:
            break
        last_point = target + mid
    
    if last_point < n:
        left = mid + 1
    else:
        right = mid

print(left)