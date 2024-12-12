#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    #Generate prime numbers up to n using the Sieve of Eratosthenes.
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def simulate_round(n):
    #Simulate a single round of the game.
    primes = sieve_of_eratosthenes(n)
    if not primes:
        return "Ben"  # If there are no primes, Ben wins
    return "Maria" if len(primes) % 2 == 1 else "Ben"

def isWinner(x, nums):
    #Determine the winner of multiple rounds of the game.
    if x <= 0 or not nums:
        return None
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = simulate_round(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None