def rps(p1, p2):
    options = ["rock", "paper", "scissors"]
    outcomes = ["Draw!", "Player 1 won!", "Player 2 won!"]
    print(options.index(p1)-options.index(p2))
    return outcomes[options.index(p1) - options.index(p2)]







res = rps('scissors','paper')
print(res)