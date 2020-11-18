#-----------------------------------------------------------------------
# gambler.py
#-----------------------------------------------------------------------

import stdio
import sys
import random

# Accept integer command-line arguments stake, goal, and trialCount.
# Run trialCount experiments that start with stake dollars and
# terminate on 0 dollars or goal.  Write to standard output the
# percentage of wins and the average number of bets per experiment.

# stake = int(sys.argv[1])
# goal = int(sys.argv[2])
# trials = int(sys.argv[3])
# times = int(sys.argv[4])

stake = 5
goal = 25
trials = 100
times = 100

# Run trialCount experiments that start with stake and terminate on
# 0 or goal.
bets = 0
wins = 0
left = 0

for t in range(trials):
    # Run one experiment.
    cash = stake
    i = 0   #每轮下注的次数
    while cash > 0 and cash < goal and i < times:
        # Simulate one bet.
        i += 1
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
    left += cash
    print('cash:',cash,'次数:',i)

stdio.writeln(str(100 * wins//trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(bets//trials))
stdio.writeln('left: ' + str(left//trials))

#-----------------------------------------------------------------------

# python gambler.py 10 20 1000
# 49% wins
# Avg # bets: 99

# python gambler.py 50 250 100
# 21% wins
# Avg # bets: 12712

# python gambler.py 500 2500 100
# 21% wins
# Avg # bets: 1002424

