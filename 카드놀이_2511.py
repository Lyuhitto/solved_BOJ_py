"""
TODO 노션에 적기
"""
import sys


r = sys.stdin.readline


a_card = list(map(int, r().split()))
b_card = list(map(int, r().split()))
a_score = 0
b_score = 0
win = 'D'
card_round = []
for i in range(len(a_card)):
    if a_card[i] > b_card[i]:
        card_round.append('A')
        a_score += 3
    elif a_card[i] < b_card[i]:
        card_round.append('B')
        b_score += 3
    else:
        card_round.append('D')
        a_score += 1
        b_score += 1

if a_score > b_score:
    win = 'A'
elif a_score < b_score:
    win = 'B'
else:
    if 'A' in card_round or 'B' in card_round:
        for r in range(len(card_round)-1, -1, -1):
            if card_round[r] != 'D':
                win = card_round[r]
                break

print(f"{a_score} {b_score}")
print(win)
