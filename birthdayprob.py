import matplotlib.pyplot as plt

DAYS = 365
x = list(range(1, 366))
y = []

def calculate_prob(n):
    #returns probability of birthday overlap when there's n people
    prob = 1
    for i in range(n):
        prob *= (DAYS - i) / DAYS
    return 1 - prob

def drawplot(x, y):
    #draw and save plot of birthday problem
    for i in x:
        y.append(calculate_prob(i))
    plt.plot(x, y)
    plt.savefig('birthdayprob')

drawplot(x, y)

