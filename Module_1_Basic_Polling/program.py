# MODULE 1: BASIC POLLING SYSTEM

import os

# Initialize variables
voting = True
poll_question = ""
options = []
vote_counts = []
option_count = 0

# Get poll setup
print("=" * 50)
print("POLLING SYSTEM - MODULE 1")
print("=" * 50)

poll_question = input("\nEnter the poll question: ")
while True:
    try:
        option_count = int(input("How many options? (2-5): "))
        if 2 <= option_count <= 5:
            break
        else:
            print("Please enter between 2 and 5 options")
    except ValueError:
        print("Enter a valid number")

# Input options
print("\nEnter the options:")
for i in range(option_count):
    option = input(f"Option {i+1}: ")
    options.append(option)
    vote_counts.append(0)

# Voting process
print("\n" + "=" * 50)
print("VOTING STARTED")
print("=" * 50)

while voting:
    print(f"\nQuestion: {poll_question}")
    print("\nOptions:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get vote
    while True:
        try:
            choice = int(input("\nEnter your choice (1-{}): ".format(option_count)))
            if 1 <= choice <= option_count:
                vote_counts[choice - 1] += 1
                print("✓ Vote recorded!")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Enter a valid number!")
    
    # Ask to vote again
    again = input("\nVote again? (y/n): ").lower()
    if again == 'n':
        voting = False

# Display results
print("\n" + "=" * 50)
print("POLLING RESULTS")
print("=" * 50)

total_votes = sum(vote_counts)
print(f"\nPoll: {poll_question}")
print(f"Total Votes: {total_votes}\n")

for i, option in enumerate(options):
    count = vote_counts[i]
    percentage = (count / total_votes * 100) if total_votes > 0 else 0
    print(f"{option}: {count} votes ({percentage:.1f}%)")

# Find winner
if total_votes > 0:
    max_votes = max(vote_counts)
    winner_index = vote_counts.index(max_votes)
    print(f"\n Winner: {options[winner_index]} with {max_votes} votes")

print("\n" + "=" * 50)
print("Thank you for voting!")
print("=" * 50)
