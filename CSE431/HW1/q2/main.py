# 1 <= T <= 100
# 0 <= S <= 1,000,000
# 0 <= k <= 100
# Output Format: T lines, each indicating the amount of CloudCoinsTM you would get

COIN_LOOPBACK = 1_000_000
def loopback(input_coins):
    if (input_coins > COIN_LOOPBACK):
        return input_coins % COIN_LOOPBACK
    elif (input_coins < 0):
        return COIN_LOOPBACK + input_coins
    else:
        return input_coins

# main line processing function
def process_account(account_coins, seconds):
    for second in range(seconds):
        if account_coins % 2:
            account_coins = loopback(odd(account_coins))
        else:
            account_coins = loopback(even(account_coins))
    print(account_coins)

def odd(coins):
    coins -= 15
    coins *= 2
    return coins

def even(coins):
    coins -= 99
    coins *= 3
    return coins

# given template
num_tests = int(input())
for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0]) # Starting bet
    k = int(line[1]) # Number of rounds
    process_account(S, k)
