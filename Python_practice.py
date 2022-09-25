""" counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1]) """
""" 
for county in counties:
    print(county) """
""" 
for item in counties_dict.keys():
    print(item)

for item in counties_dict.values():
    print(item) """

""" for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

    ALTERNATIVE METHOD
    for county, voters in counties_dict.items():
        print(f"{county} county has {voters} registered voters.")

for county_dict in voting_data:
    print(county_dict) """



""" counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value) """




""" candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. The total number of votes in the election was {total_votes}. You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate) """


counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county, voters in counties_dict.items():
        print(f"{county} count has {voters:,} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for dict in voting_data:
    print(f'{dict["county"]} county has {dict["registered_voters"]:,} registered voters.')