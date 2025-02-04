#!/usr/bin/python3
"""
Prime Game Module
"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_numbers(n):
    """Get all prime numbers up to n using Sieve of Eratosthenes"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
    return primes


def simulate_game(n):
    """
    Simulate a single game with maximum number n
    Returns: Winner of the game ('Maria' or 'Ben')
    """
    if n < 2:
        return 'Ben'
    
    # Get prime numbers up to n
    primes = get_prime_numbers(n)
    
    # If there are no prime numbers, Ben wins
    if not primes:
        return 'Ben'
    
    # The winner can be determined by the number of prime numbers
    # If the number of moves (prime numbers) is even, Ben wins
    # If the number of moves (prime numbers) is odd, Maria wins
    return 'Maria' if len(primes) % 2 == 1 else 'Ben'


    # # Get all numbers from 1 to n
    # numbers = set(range(1, n + 1))
    # primes = get_prime_numbers(n)

    # # Simulate the game
    # maria_turn = True
    # while primes:
    #     # Find the smallest available prime
    #     current_prime = None
    #     for prime in primes:
    #         if prime in numbers:
    #             current_prime = prime
    #             break

    #     if not current_prime:
    #         break

    #     # Remove the prime and its multiples
    #     multiples = set(range(current_prime, n + 1, current_prime))
    #     numbers -= multiples
    #     primes.remove(current_prime)

    #     # Switch turns
    #     maria_turn = not maria_turn

    # # If it's Maria's turn and no moves left, Ben wins
    # # If it's Ben's turn and no moves left, Maria wins
    # return 'Ben' if maria_turn else 'Maria'


def isWinner(x, nums):
    """
    Determine the winner of x rounds of the game
    Args:
        x: number of rounds
        nums: array of n values for each round
    Returns:
        Name of the player that won the most rounds
        None if winner cannot be determined
    """
    if not nums or x < 1:
        return None

    maria_wins = ben_wins = 0

    for n in nums[:x]:
        if n is None:
            continue
        winner = simulate_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
