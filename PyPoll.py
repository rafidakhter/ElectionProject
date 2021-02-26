
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
    6. The voter turnout for each county
    7. The percentage of votes for each county out of the total count
    8. The county witht the hight turn out

# Creating class for each object in the voting system
    # Election -> total, candidates
    # candidate -> total vote recieved, county where they are voted
    # vote -> contain voter ID, county, candidate
'''

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
        self.counties = {}
        self.total = 0
    
    def addVote(self, vote):
        countyName =vote.county
        if not countyName in self.counties:
            self.counties[countyName] = 1
        else:
            self.counties[countyName] += 1
        self.total += 1
    
    def getPercentage(self, totalVotes):
        
        percentage = (self.total / totalVotes) * 100

        return percentage
        
# Election     
class Election():
    
    def __init__(self):

        self.totalVotes = 0
        self.candidates = {}
        self.county={}
    
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

# cast Vote
def castVote(dataList):
    #excluding the headers
    headers = next(dataList)

    for data in dataList:
        vote = Vote(data[0], data[1], data[2])
        election.addVote(vote)

def summarizeCandidateData(election):
    # returns a sorted list
    candidatesData = [] # stores all the candidates data 
    totalElectionVote = election.totalVotes
    candidates= election.candidates
    
    # itterate through all the candidates and returns their data
    for candidate in candidates:

        candidateVoteTotal = candidates[candidate].total
        candidateVotePercentage = round(candidates[candidate].getPercentage(totalElectionVote), 2)
        countyData=candidates[candidate].counties
        candidateData = (candidateVotePercentage, candidateVoteTotal, candidate,countyData)
        candidatesData.append(candidateData)

    candidatesData.sort(key=lambda tup: tup[0], reverse=True)     # sorting the data 
    
    return candidatesData

def summarizeCountyData(election):
    # returns a dictionary containing county votes

    outputData = {}
    
    candidates = election.candidates
    for candidate in candidates:
        counties=candidates[candidate].counties
        for county in counties:

            if county in outputData:
                outputData[county] += counties[county]
            else:
                outputData[county] = counties[county]
    
    return outputData

def organizeOutputData(electionVoteSummary, countySummary,totalVotes):
    line = '-------------------------------------\n'
    # -------------- organizing County data into ouput format --------------------#
    strCountyData = 'County Votes:\n'
    maxCountyVote = 0
    maxCountyName=''
    for county in countySummary:
        if countySummary[county] > maxCountyVote:
            maxCountyVote = countySummary[county]
            maxCountyName= county
        strCountyData = strCountyData + f'{county}: {round(((countySummary[county]/totalVotes)*100),2)}% {countySummary[county]}\n'
    # --------------------organizing candidates data into ouput format --------------------#
    voteSummary=''
    for data in electionVoteSummary:
        voteSummary += f'{data[2]}: Overall data: {data[0]}% ({data[1]})\n{line}county data:\n{ line}'
        for countyData in data[3]:
            voteSummary += f'{countyData}: {data[3][countyData]}, %votes= {round((data[3][countyData]/data[1])*100,2)}\n'

    # --------------------organizing winner data into ouput format --------------------#
    winner = electionVoteSummary[0]
    winnerSummary = (f'winner: {winner[2]} \nWinning Vote Count: {winner[1]}\nWinning Percentage: {winner[0]}% votes\n')
    
    
    output = f'Election Results\n{line}Total Votes: {totalVotes}\n{line}\n{strCountyData}\n{line}Larget County Turnout: {maxCountyName}\n{line}\n{voteSummary}\n{line}{winnerSummary}'
    
    return output
# -----------------------------------------------------------Logic --------------------------------------------------------#

# clearing election object.
election = Election()

#----------------------------------------------importing data from csv file-------------------------------------------------#
file_to_load = os.path.join("Resources", "election_results.csv")


with open(file_to_load, 'r') as election_data:
    dataList = csv.reader(election_data)
    
#----------------------------------------------casting all the votes ---------------------------------------------------------#
    castVote(dataList)

totalVotes=election.totalVotes
#----------------------------------------------summararizing data from election ---------------------------------------------------------#
electionVoteSummary = summarizeCandidateData(election)
countySummary = summarizeCountyData(election)

#----------------------------------------------Organizing data  into output format ---------------------------------------------------------#
output= organizeOutputData(electionVoteSummary,countySummary,totalVotes)

print(output) # prints to the terminal
#----------------------------------------------Organizing data  into output format ---------------------------------------------------------#
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write(output)