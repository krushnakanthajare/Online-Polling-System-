# MODULE 4: DATA PERSISTENCE & STATISTICAL ANALYSIS

from datetime import datetime
import json
import csv
import statistics
from pathlib import Path

class PollSystemAdvanced:
    """Advanced polling system with data persistence and analytics"""
    
    def __init__(self):
        """Initialize with file paths"""
        self.voters_set = set()
        self.votes_list = []
        self.vote_count = {}
        self.poll_question = ""
        self.options = []
        
        # File paths
        self.data_dir = Path("poll_data")
        self.data_dir.mkdir(exist_ok=True)
        self.csv_file = self.data_dir / "polls_database.csv"
        self.json_file = self.data_dir / "poll_metadata.json"
        self.report_file = self.data_dir / "poll_report.txt"
    
    def create_poll(self):
        """Create a new poll"""
        print("=" * 70)
        print("POLLING SYSTEM - MODULE 4 (With Analytics & Data Persistence)")
        print("=" * 70)
        
        try:
            self.poll_question = input("\nEnter the poll question: ").strip()
            if not self.poll_question:
                raise ValueError("Poll question cannot be empty")
            
            while True:
                option_count = int(input("How many options? (2-5): "))
                if 2 <= option_count <= 5:
                    break
                else:
                    print("Please enter between 2 and 5")
            
            print("\nEnter the options:")
            for i in range(option_count):
                option = input(f"Option {i+1}: ").strip()
                if not option:
                    raise ValueError(f"Option {i+1} cannot be empty")
                self.options.append(option)
                self.vote_count[option] = 0
        
        except ValueError as e:
            print(f"Error: {e}")
            self.create_poll()
    
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
            print(f"Error: {e}")
            return None
    
    def display_poll_options(self):
        """Display all polling options"""
        print(f"\n Poll: {self.poll_question}")
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
                print(f"{result}")
    
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
    
    def save_to_csv(self):
        """Save poll results to CSV file"""
        try:
            # Check if file exists to decide on header
            file_exists = self.csv_file.exists()
            
            with open(self.csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                
                # Write header if new file
                if not file_exists or file.tell() == 0:
                    writer.writerow(['Date', 'Question', 'Total_Votes', 'Option', 'Votes', 'Percentage'])
                
                # Write data for each option
                total_votes = len(self.votes_list)
                poll_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                for option, count in self.vote_count.items():
                    percentage = (count / total_votes * 100) if total_votes > 0 else 0
                    writer.writerow([poll_date, self.poll_question, total_votes, option, count, f"{percentage:.2f}"])
            
            print(f"✓ Data saved to CSV: {self.csv_file}")
        
        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")
    
    def save_metadata_to_json(self):
        """Save poll metadata to JSON file"""
        try:
            metadata = {
                "poll_date": datetime.now().isoformat(),
                "poll_question": self.poll_question,
                "options": self.options,
                "total_voters": len(self.voters_set),
                "total_votes": len(self.votes_list),
                "results": self.vote_count,
                "vote_details": self.votes_list
            }
            
            # Load existing data or create new
            try:
                with open(self.json_file, 'r') as f:
                    all_polls = json.load(f)
            except:
                all_polls = []
            
            all_polls.append(metadata)
            
            with open(self.json_file, 'w') as f:
                json.dump(all_polls, f, indent=2)
            
            print(f"✓ Metadata saved to JSON: {self.json_file}")
        
        except Exception as e:
            print(f" Error saving metadata: {e}")
    
    def calculate_statistics(self):
        """Calculate statistical measures"""
        if len(self.votes_list) == 0:
            return None
        
        vote_values = list(self.vote_count.values())
        
        stats = {
            "total_votes": len(self.votes_list),
            "total_voters": len(self.voters_set),
            "mean_votes": statistics.mean(vote_values),
            "median_votes": statistics.median(vote_values),
            "mode_votes": self.vote_count[max(self.vote_count, key=self.vote_count.get)],
            "std_dev": statistics.stdev(vote_values) if len(vote_values) > 1 else 0,
            "voter_participation": (len(self.voters_set) / len(self.votes_list)) * 100
        }
        
        return stats
    
    def generate_analytics_report(self):
        """Generate detailed analytics report"""
        print("\n" + "=" * 70)
        print("STATISTICAL ANALYSIS & ANALYTICS REPORT")
        print("=" * 70)
        
        if len(self.votes_list) == 0:
            print("No votes recorded yet!")
            return
        
        stats = self.calculate_statistics()
        
        print(f"\n📊 POLL SUMMARY")
        print(f"Question: {self.poll_question}")
        print(f"Poll Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print(f"\n📈 VOTING STATISTICS")
        print(f"Total Voters: {stats['total_voters']}")
        print(f"Total Votes: {stats['total_votes']}")
        print(f"Average votes per option: {stats['mean_votes']:.2f}")
        print(f"Median votes: {stats['median_votes']:.2f}")
        print(f"Standard Deviation: {stats['std_dev']:.2f}")
        print(f"Voter Participation Rate: {stats['voter_participation']:.1f}%")
        
        print(f"\n VOTE DISTRIBUTION")
        sorted_votes = sorted(self.vote_count.items(), key=lambda x: x[1], reverse=True)
        max_votes = sorted_votes[0][1]
        
        for option, count in sorted_votes:
            percentage = (count / len(self.votes_list)) * 100
            bar_length = int(count / max_votes * 30) if max_votes > 0 else 0
            bar = "█" * bar_length + "░" * (30 - bar_length)
            print(f"{option:20} : {count:2} ({percentage:5.1f}%) {bar}")
        
        print(f"\n WINNER")
        winner = sorted_votes[0]
        print(f"Option: {winner[0]}")
        print(f"Votes: {winner[1]}")
        print(f"Winning Percentage: {(winner[1]/len(self.votes_list)*100):.2f}%")
        
        # Check if it's a close call
        if len(sorted_votes) > 1:
            runner_up = sorted_votes[1]
            margin = winner[1] - runner_up[1]
            print(f"Margin over runner-up: {margin} votes")
        
        print(f"\n DETAILED VOTE HISTORY (First 15)")
        print("-" * 70)
        print(f"{'#':<4} {'Voter Name':<20} {'Choice':<20} {'Time':<12}")
        print("-" * 70)
        
        for idx, vote in enumerate(self.votes_list[:15], 1):
            print(f"{idx:<4} {vote['voter_name']:<20} {vote['choice']:<20} {vote['timestamp']:<12}")
        
        if len(self.votes_list) > 15:
            print(f"... and {len(self.votes_list) - 15} more votes")
        
        print("\n" + "=" * 70)
    
    def save_analytics_report(self):
        """Save analytics report to text file"""
        try:
            with open(self.report_file, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("POLLING SYSTEM - ANALYTICS REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Poll Question: {self.poll_question}\n")
                f.write(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Voters: {len(self.voters_set)}\n")
                f.write(f"Total Votes: {len(self.votes_list)}\n\n")
                
                stats = self.calculate_statistics()
                f.write("STATISTICAL MEASURES\n")
                f.write("-" * 70 + "\n")
                f.write(f"Mean votes per option: {stats['mean_votes']:.2f}\n")
                f.write(f"Median votes: {stats['median_votes']:.2f}\n")
                f.write(f"Standard Deviation: {stats['std_dev']:.2f}\n")
                f.write(f"Voter Participation: {stats['voter_participation']:.1f}%\n\n")
                
                f.write("VOTE DISTRIBUTION\n")
                f.write("-" * 70 + "\n")
                sorted_votes = sorted(self.vote_count.items(), key=lambda x: x[1], reverse=True)
                for option, count in sorted_votes:
                    percentage = (count / len(self.votes_list)) * 100
                    f.write(f"{option}: {count} votes ({percentage:.2f}%)\n")
                
                f.write("\n" + "=" * 70 + "\n")
                f.write("VOTE HISTORY\n")
                f.write("=" * 70 + "\n")
                for idx, vote in enumerate(self.votes_list, 1):
                    f.write(f"{idx}. {vote['voter_name']} voted for {vote['choice']} at {vote['timestamp']}\n")
            
            print(f"✓ Report saved to: {self.report_file}")
        
        except Exception as e:
            print(f" Error saving report: {e}")
    
    def display_results(self):
        """Display detailed polling results"""
        print("\n" + "=" * 70)
        print("DETAILED POLLING RESULTS")
        print("=" * 70)
        
        if len(self.votes_list) == 0:
            print("No votes recorded yet!")
            return
        
        print(f"\n Poll: {self.poll_question}")
        print(f"Total Voters: {len(self.voters_set)}")
        print(f"Total Votes: {len(self.votes_list)}\n")
        
        sorted_votes = sorted(self.vote_count.items(), key=lambda x: x[1], reverse=True)
        max_votes = sorted_votes[0][1]
        
        print("Vote Distribution:")
        for option, count in sorted_votes:
            percentage = (count / len(self.votes_list)) * 100
            bar_length = int(count / max_votes * 25) if max_votes > 0 else 0
            bar = "█" * bar_length + "░" * (25 - bar_length)
            print(f"{option:15} : {count:2} votes ({percentage:5.1f}%) {bar}")
        
        winner = sorted_votes[0]
        print(f"\n Winner: {winner[0]} with {winner[1]} votes")
    
    def run(self):
        """Main polling system loop"""
        self.create_poll()
        
        print("\n" + "=" * 70)
        print("VOTING STARTED")
        print("=" * 70)
        
        while True:
            if self.process_vote():
                if not self.ask_continue_voting():
                    break
        
        self.display_results()
        self.generate_analytics_report()
        
        # Save data
        print("\n" + "=" * 70)
        print("SAVING DATA")
        print("=" * 70)
        self.save_to_csv()
        self.save_metadata_to_json()
        self.save_analytics_report()
        
        print("\n" + "=" * 70)
        print("Thank you for voting! Data saved successfully.")
        print("=" * 70)


# Main program
if __name__ == "__main__":
    poll_system = PollSystemAdvanced()
    poll_system.run()
