old = input("old number ")
new = input("new number ")
answer = 0
old = int(old)
new = int(new)
def percentage_changed(old, new):
    if (old > new):
        answer = new / old
        answer = 1 - answer
        answer = int(answer)
        answer = str(answer)
        return answer
    if (new > old):
        increase = new - old
        increase = increase / old
        answer = increase * 100
        answer = int(answer)
        answer = str(answer)
        return answer
def inde(old, new):
    if (old > new):
        eee = "decrease"
    if (new > old):
        eee = "increase"
    return eee
print(percentage_changed(old, new) + " percent " + inde(old, new))