import sys


n = int(input())
for i in range(n):
    classroom = list(map(int, sys.stdin.readline().strip().split()))
    members_number = classroom[0]
    average = sum(classroom[1:]) / members_number
    passed_member = 0
    for j in classroom[1:]:
        if j > average:
            passed_member += 1
    result = passed_member / members_number * 100
    print("%0.3f%%" % result)
