from sys import stdin, stdout


word_list = list(
    set(
        [stdin.readline().strip() for _ in range(int(stdin.readline()))]
        )
    )
'''
리스트를 정렬할 때, key값으로 다중조건을 설정할 수 있다
예를 들어 아래의 경우, 원소의 길이를 우선 비교하고
길이가 같다면 abc 순서에 따라 다시 정렬한다.
'''
word_list.sort(key=lambda x: (len(x), x))
stdout.write('\n'.join(word_list))
