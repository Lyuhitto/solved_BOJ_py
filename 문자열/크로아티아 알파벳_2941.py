def count_croatia(sentence: str):
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    result = sentence
    for w in croatia:
        result = result.replace(w, '+')
    print(len(result))


a = input()
count_croatia(a)
