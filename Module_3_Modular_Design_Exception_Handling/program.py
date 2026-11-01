# MODULE 3: MODULAR DESIGN WITH EXCEPTION HANDLING

from datetime import datetime

class PollSystem:
    """Online Polling System with modular design"""
    
    def __init__(self):
        """Initialize the polling system"""
        self.voters_set = set()
        self.votes_list = []
        self.vote_count = {}
        self.poll_question = ""
        self.options = []
    
    def create_poll(self):
        """Create a new poll with question and options"""
        print("=" * 60)
        print("POLLING SYSTEM - MODULE 3 (Modular with Functions)")
        print("=" * 60)
        
        try:
            self.poll_question = input("\nEnter the poll question: ").strip()
            if not self.poll_question:
                raise ValueError("Poll question cannot be empty")
            
            while True:
                option_count = int(input("How many options? (2-5): "))
                if 2 <= option_count <= 5:
                    break
                else:
                    raise ValueError("Please enter between 2 and 5")
            
            print("\nEnter the options:")
            for i in range(option_count):
                option = input(f"Option {i+1}: ").strip()
                if not option:
                    raise ValueError(f"Option {i+1} cannot be empty")
                self.options.append(option)
                self.vote_count[option] = 0
        
        except ValueError as e:
            print(f"❌ Error: {e}")
            self.create_poll()  # Retry
    
    def validate_voter_name(self, name):
        """Validate voter name"""
        if not name or len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
        return name.strip()
    
    def check_duplicate_voter(self, voter_name):
        """Check if voter has already voted"""
        if voter_name in self.voters_set:
            raise ValueError(f"{voter_name} has already voted!")
        return True
    
    def validate_choice(self, choice):
        """Validate voter choice"""
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.options):
                return True, choice - 1
            else:
                return False, f"Please enter between 1 and {len(self.options)}"
        except ValueError:
            return False, "Please enter a valid number"
    
    def get_voter_info(self):
        """Get and validate voter information"""
        try:
            voter_name = input("Enter your name: ").strip()
            self.validate_voter_name(voter_name)
            self.check_duplicate_voter(voter_name)
            return voter_name
        except ValueError as e:
            print(f"❌ Error: {e}")
            return None
    
    def display_poll_options(self):
        """Display all polling options"""
        print(f"\n📋 Poll: {self.poll_question}")
        print("Options:")
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")
    
    def get_voter_choice(self):
        """Get and validate voter choice"""
        while True:
            choice = input(f"\nEnter your choice (1-{len(self.options)}): ")
            is_valid, result = self.validate_choice(choice)
            
            if is_valid:
                return result
            else:
                print(f"❌ {result}")
    
    def record_vote(self, voter_name, choice_index):
        """Record a single vote"""
        self.voters_set.add(voter_name)
        selected_option = self.options[choice_index]
        self.vote_count[selected_option] += 1
        
        vote_record = {
            "voter_name": voter_name,
            "choice": selected_option,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        self.votes_list.append(vote_record)
        print(f"✓ Vote recorded for {selected_option}!")
    
    def process_vote(self):
        """Complete voting process for one voter"""
        voter_name = self.get_voter_info()
        if voter_name is None:
            return False
        
        self.display_poll_options()
        choice_index = self.get_voter_choice()
        self.record_vote(voter_name, choice_index)
        return True
    
    def ask_continue_voting(self):
        """Ask if another voter wants to vote"""
        response = input("\nNext voter? (y/n): ").lower().strip()
        return response in ['y', 'yes']
    
    def display_results(self):
        """Display detailed polling results"""
        print("\n" + "=" * 60)
        print("DETAILED POLLING RESULTS")
        print("=" * 60)
        
        if len(self.votes_list) == 0:
            print("No votes recorded yet!")
            return
        
        print(f"\n📊 Poll: {self.poll_question}")
        print(f"Total Voters: {len(self.voters_set)}")
        print(f"Total Votes: {len(self.votes_list)}\n")
        
        # Sort by votes
        sorted_votes = sorted(self.vote_count.items(), key=lambda x: x[1], reverse=True)
        
        print("Vote Distribution:")
        max_votes = sorted_votes[0][1] if sorted_votes else 0
        for option, count in sorted_votes:
            percentage = (count / len(self.votes_list)) * 100
            bar_length = int(count / max_votes * 20) if max_votes > 0 else 0
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"{option:15} : {count:2} votes ({percentage:5.1f}%) {bar}")
        
        # Show winner
        winner = sorted_votes[0]
        print(f"\n🏆 Winner: {winner[0]} with {winner[1]} votes")
        
        # Show history
        print("\n" + "=" * 60)
        print("VOTE HISTORY (First 10)")
        print("=" * 60)
        print(f"{'Voter Name':<20} {'Choice':<20} {'Time':<10}")
        print("-" * 50)
        for vote in self.votes_list[:10]:
            print(f"{vote['voter_name']:<20} {vote['choice']:<20} {vote['timestamp']:<10}")
        
        if len(self.votes_list) > 10:
            print(f"... and {len(self.votes_list) - 10} more votes")
    
    def run(self):
        """Main polling system loop"""
        self.create_poll()
        
        print("\n" + "=" * 60)
        print("VOTING STARTED")
        print("=" * 60)
        
        while True:
            if self.process_vote():
                if not self.ask_continue_voting():
                    break
        
        self.display_results()
        print("\n" + "=" * 60)
        print("Thank you for voting!")
        print("=" * 60)


# Main program
if __name__ == "__main__":
    poll_system = PollSystem()
    poll_system.run()
