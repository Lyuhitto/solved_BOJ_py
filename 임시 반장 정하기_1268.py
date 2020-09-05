import sys


n = int(input())
classes = [sys.stdin.readline().split() for _ in range(n)]
cnt = [0]*n
'''
for 1~n번 학생이:
    for 1~5학년 때까지:
        for 같은 반 이었던 학생 체크:
            if 학생 본인이라면:
                continue
            elif n번 학생과 다른 학생이 같은 반이었다면:
                해당 위치의 False값을 True로 바꾼다
    만약 1번 학생이 2번 학생과 2번, 3번 학생과 1번...n번 학생과 3번
    이런식으로 중복되면 답이 다르게 나오므로
    set을 사용한뒤 len으로 몇 명인지 세면 된다
'''
for student_id in range(n):
    student_set = []
    for grade in range(5):
        for other_std in range(n):
            if other_std == student_id:
                continue
            elif classes[student_id][grade] == classes[other_std][grade]:
                student_set.append(other_std)
    cnt[student_id] = len(set(student_set))
print(cnt.index(max(cnt)) + 1)
