import time

def duration():
    start = time.time()
    for x in range(1000000):
        pass
    end = time.time()
    d = end - start
    print(d)
    return d


def average(list):
	number = sum(list)
	anwser = number / len(list)
	print('This is the average      %f' % anwser)

i = 0
z = []
while i < 100:
    d = duration()
    z.append(d)
    i = i + 1

average(z)