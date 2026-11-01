# MODULE 2: VOTER TRACKING & DUPLICATE PREVENTION

import os
from datetime import datetime

# Initialize data structures
voting = True
voters_set = set()  # Track unique voters
votes_list = []     # Store all votes with details
vote_count = {}     # Count votes per option
poll_question = ""
options = []

print("=" * 60)
print("POLLING SYSTEM - MODULE 2 (With Voter Tracking)")
print("=" * 60)

# Setup poll
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

# Input options and initialize counters
print("\nEnter the options:")
for i in range(option_count):
    option = input(f"Option {i+1}: ")
    options.append(option)
    vote_count[option] = 0

# Voting process with voter tracking
print("\n" + "=" * 60)
print("VOTING STARTED")
print("=" * 60)

while voting:
    print(f"\nPoll: {poll_question}")
    
    # Get voter name
    voter_name = input("Enter your name: ").strip()
    
    # Check if already voted
    if voter_name in voters_set:
        print(f"{voter_name}, you have already voted!")
        continue
    
    # Display options
    print("\nOptions:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get and validate vote
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{option_count}): "))
            if 1 <= choice <= option_count:
                selected_option = options[choice - 1]
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Enter a valid number!")
    
    # Record vote
    voters_set.add(voter_name)
    vote_count[selected_option] += 1
    
    vote_record = {
        "voter_name": voter_name,
        "choice": selected_option,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    votes_list.append(vote_record)
    print(f"✓ Vote recorded for {selected_option}!")
    
    # Ask to continue
    again = input("\nNext voter? (y/n): ").lower()
    if again == 'n':
        voting = False

# Display results
print("\n" + "=" * 60)
print("DETAILED POLLING RESULTS")
print("=" * 60)

print(f"\nPoll Question: {poll_question}")
print(f"Total Voters: {len(voters_set)}")
print(f"Total Votes Cast: {len(votes_list)}\n")

# Sort results by vote count (descending)
sorted_votes = sorted(vote_count.items(), key=lambda x: x[1], reverse=True)

print("Results:")
for option, count in sorted_votes:
    percentage = (count / len(votes_list) * 100) if len(votes_list) > 0 else 0
    bar = "█" * count + "░" * (max(vote_count.values()) - count if vote_count else 0)
    print(f"{option:15} : {count:2} votes ({percentage:5.1f}%) {bar}")

# Display winner
if len(votes_list) > 0:
    winner = sorted_votes[0]
    print(f"\nWinner: {winner[0]} with {winner[1]} votes")

# Show vote history
print("\n" + "=" * 60)
print("VOTE HISTORY (First 10 votes)")
print("=" * 60)
print(f"{'Voter Name':<20} {'Choice':<20} {'Time':<10}")
print("-" * 50)
for i, vote in enumerate(votes_list[:10]):
    print(f"{vote['voter_name']:<20} {vote['choice']:<20} {vote['timestamp']:<10}")

if len(votes_list) > 10:
    print(f"... and {len(votes_list) - 10} more votes")

print("\n" + "=" * 60)
print("Thank you for voting!")
print("=" * 60)
