now_h, now_m, now_s = map(int, input().split(':'))
fire_h, fire_m, fire_s = map(int, input().split(':'))

# 전부 초로 바꿔서 계산해 버리자!
# 이때 다음날을 가리키는 경우를 생각해야한다

now = (now_h * 60 * 60) + (now_m * 60) + now_s
fire = (fire_h * 60 * 60) + (fire_m * 60) + fire_s
answer = fire - now if fire > now else (24 * 60 * 60) - now + fire

ans_h = answer // 60 // 60
ans_m = (answer // 60) % 60
ans_s = answer % 60

print(f"{str(ans_h).zfill(2)}:{str(ans_m).zfill(2)}:{str(ans_s).zfill(2)}")
