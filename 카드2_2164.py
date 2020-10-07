from sys import stdin
import collections
"""
계속되는 시간 초과로, collections 모듈을 사용함
"""


def card_deque(card: list) -> int:
    while len(card) > 1:
        card.popleft()
        card.append(card.popleft())
    return card[0]


card = collections.deque([i for i in range(1, int(stdin.readline())+1)])
print(card_deque(card))
