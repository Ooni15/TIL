arr = ['1', '2', '3', '4', '5','6']
path = []
n = 3

def run(lev, start) :
    if lev == n :
        print(*path)
        return

    for i in range(start, 6):
        path.append(arr[i])
        run(lev + 1, i)
        path.pop()

run(0, 0)


