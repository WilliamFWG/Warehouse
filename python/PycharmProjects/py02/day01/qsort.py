from random import randint

def qsort(seq):
    if len(seq)<2:
        return seq
    smaller=[]
    larger=[]
    tag=seq[0]
    for item in seq:
        if item==tag:continue
        elif item>tag:smaller.append(item)
        else:larger.append(item)
    return qsort(smaller)+[tag]+qsort(larger)

if __name__ == '__main__':
    numlist = [randint(1, 100) for i in range(10)]
    print(numlist)
    print(qsort(numlist))