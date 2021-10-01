"""
You are given two integer arrays persons and times. In an election, the 
ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at 
time t. Votes cast at time t will count towards our query. In the case of a tie, 
the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the 
persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at 
time t according to the mentioned rules.

"""
class TopVotedCandidate(object):
    
    def __init__(self, persons, times):
        # N time
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leads = []
        self.times = times
        votes = {}
        lead = -1
        for p in persons:
            votes[p] = votes.get(p, 0) + 1
            # update lead
            if votes[p] >= votes.get(lead, 0):
                lead = p
            self.leads.append(lead)
        
        
    def q(self, t):
        # logN time
        """
        :type t: int
        :rtype: int
        """
        # get floor time
        return self.leads[bisect.bisect(self.times, t)-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)