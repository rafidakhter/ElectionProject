
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


proposed code
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
        if not county in self.county:
            county[countyName] = 1
        else:
            county[countyName] += 1
        total += 1

# Election     
class Election():
    
    def __init__(self):

        self.totalVotes = 0
        self.candidates = {}
    
    def addCandidates(self, candidateName):
        
        self.candidates[candidateName] = newCandidate
    
    def addVote(self, vote):
        candidateName = vote.candidate
        
        if not candidateName in self.candidates:
            newCandidate = new Candidate(candidateName)
            addCandidates(candidateName)
        
        currentCandidate = self.candidates[candidateName]
        currentCandidate.addVote(vote)
        
        self.totalVotes += 1


election = new Election     
data = [ ]
for data in dataList:

    vote = new Vote(data[0], data[1], data[3])
    election.addVote(vote)
'''



# importing data from csv fine
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load, 'r') as election_data:

    #to do :perform analysis
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

