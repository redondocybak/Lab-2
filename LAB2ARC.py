import random

def duplicates(birthdays):
    return len(birthdays) != len(set(birthdays))

def generate_birthdays(n):
    birthdays = [random.randint(1, 365) for x in range(n)]
    return birthdays

def experiment(n, numbertrials):
    numberduplicates = 0
    for x in range(numbertrials):
        birthdays = generate_birthdays(n)
        if duplicates(birthdays):
            numberduplicates += 1
    return numberduplicates

def main():
    numbertrials = 1000000
    results = []
    for n in range(5, 51, 5):
        numberduplicates = experiment(n, numbertrials)
        probability = numberduplicates / numbertrials
        results.append((n, probability))
    
    print("Results:")
    for n, probability in results:
        print(f"n = {n}: The probability that two people in a room will have the same birthday is = {probability:}")
    
    with open("birthday_paradox.txt", "w") as f:
        f.write("Results:")
        for n, probability in results:
            f.write(f"n = {n}: The probability that two people in a room will have the same birthday is = {probability:}\n")

main()