import sys


def guest_room_number(h, w, n):
    if not(1 <= h and w <= 99 and 1 <= n <= h * w):
        raise ValueError("Unvalid Values")
    if n % h == 0:
        return str(h) + str(n // h).zfill(2)
    else:
        return str((n % h)) + str((n // h) + 1).zfill(2)


for i in range(int(input())):
    height, width, guest = map(int, sys.stdin.readline().strip().split())
    print(guest_room_number(height, width, guest))
