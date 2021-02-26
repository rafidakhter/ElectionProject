# Module 3 - Python- Election Module

# ElectionProject

Col. Uni - bootcamp module 3 Python election project

# Project Summary:

This git repository is for a mock election vote counting algorithm created using python.

# Election outcome:

The total votes cast was 369,711, the largest turnout was in Denver where the votes accounted for 83% of the total vote followed by Jefferson and Arapahoe. Dina DeGette was the winner of the election with a majority vote of 73.81%. majority of which is coming from Denver. The other candidates Charles Casper Stockham and Raymon Anthony Doane were far behind with only 23% and 3.14% consecutively. The chart below shows details about the election:

## Election Results

---

Total Votes: 369711

---

### County Votes:

---

**Jefferson:** 10.51% 38855
**Denver:** 82.78% 306055
**Arapahoe:** 6.71% 24801

---

**Larget County Turnout:** Denver

---

**Diana DeGette:**

**Overall data:** 73.81% (272892)

**county data:**

**Jefferson:** 17963, %votes= 6.58
**Denver:** 239282, %votes= 87.68
**Arapahoe:** 15647, %votes= 5.73

---

**Charles Casper Stockham:**

**Overall data:** 23.05% (85213)

**county data:**

**Jefferson:** 19723, %votes= 23.15
**Denver:** 57188, %votes= 67.11
**Arapahoe:** 8302, %votes= 9.74

---

**Raymon Anthony Doane:**

**Overall data:** 3.14% (11606)

**county data:**

**Jefferson:** 1169, %votes= 10.07
**Denver:** 9585, %votes= 82.59
**Arapahoe:** 852, %votes= 7.34

---

**winner**: Diana DeGette
**Winning Vote Count**: 272892
**Winning Percentage:** 73.81% votes

# Code overview:

## Version and packages:

Python version 3.7.6

packages used are csv, os

## Code Description:

The main file of this repository is PyPoll.py

The input to this script is the location to election votes data stored in a CSV file '/Resources/election_results.csv'

Each line in the CSV file is converted to a vote object and input to the election object' addVote method. The keeps track and updates all the information of the number of votes each candidate is receiving.

The PyPoll.py file can be used for any election by following the steps mentions below:

1. Save a .csv file containing the vote data in Resourses folder, and an output .txt file in analysis folder
2. Change ''elction_result.csv" to the name of the CSV you will use in line 140 of the PyPoll.py file and Change ''election_analysis.txt" to the text file you created

   Example: line 140 fileName = "example_output.csv"

   Example: line 141 outputFileName = "example_output.txt"

3. Use the correct CSV format:
   1. line 1 headers - Ballot Id, County, Candidate
   2. Data starting from line 2
   3. No validation implemented to check the format of the data, hence the data needs to be pre-processed before implemented into the algorithm.
