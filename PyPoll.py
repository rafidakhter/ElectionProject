
#Packages:

import csv
import os


'''
    Pseudocode.
    The data wneed to be retrived
    1. The total number o votes cast
    2. A complete list of candidates who received votes
    3. the percentage of votes of each candidate won
    4. the total number of votes each candidate won
    5. winner of the election

# Creating class for each object in the voting system
    # Election -> total, candidates
    #candidate -> total vote recieved, county where they are voted
    # vote -> contain voter ID, county, candidate
'''

#proposed code
# voter class
class Vote():

    def __init__(self, voterId, county, candidate):
    
        self.voterId= voterId
        self.county = county
        self.candidate = candidate

# Candidate class
class Candidate():

    def __init__(self, name):

        self.name = name
        self.county = {}
        self.total = 0
    
    def addVote(self, vote):
        countyName =vote.county
        if not countyName in self.county:
            self.county[countyName] = 1
        else:
            self.county[countyName] += 1
        self.total += 1
    
    def getPercentage(self, totalVotes):
        
        percentage = (self.total / totalVotes) * 100

        return percentage
        

# Election     
class Election():
    
    def __init__(self):

        self.totalVotes = 0
        self.candidates = {}
    
    def addCandidates(self, candidateName):
        
        newCandidate = Candidate(candidateName)
        self.candidates[candidateName] = newCandidate
    
    def addVote(self, vote):
        candidateName = vote.candidate
        
        if not candidateName in self.candidates:
            
            self.addCandidates(candidateName)
        
        currentCandidate = self.candidates[candidateName]
        currentCandidate.addVote(vote)
        self.totalVotes += 1



election = Election()

# importing data from csv fine

file_to_load = os.path.join("Resources", "election_results.csv")



with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)
     # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for data in file_reader:
        # 2. Add to the total vote count.
        vote = Vote(data[0], data[1], data[2])
        election.addVote(vote)

    # 3. Print the total votes.

total_votes = election.totalVotes

electionsummaryData = []

outputData=[]

for candidate in election.candidates:
    candidateVoteTotal = election.candidates[candidate].total
    candidateVotePercentage = round(election.candidates[candidate].getPercentage(total_votes), 2)
    candidateData = (candidateVotePercentage, candidateVoteTotal, candidate)
    electionsummaryData.append(candidateData)
    outputData.append(f'{candidate}: {candidateVotePercentage}% ({candidateVoteTotal}) \n')


electionsummaryData.sort(key=lambda tup: tup[0],reverse=True)
winner = electionsummaryData[0]
vPercent = winner[0]
vCount = winner[1]
name = winner[2]
line = '------------------------------------------\n'
summary = (f'winner: {name} \nWinning Vote Count:{vCount}\nWinning Percentage: {vPercent}% votes\n')

outputData.append(line)
outputData.append(summary)
outputData.append(line)

output ="".join(outputData)



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write(output)