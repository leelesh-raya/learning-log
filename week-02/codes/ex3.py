import random


capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}


for quiznum in range(10):
    quest = open(rf"C:\Users\Admin\Desktop\QUIZES\quiznum{quiznum+1}.txt", "w")
    answer = open(rf"C:\Users\Admin\Desktop\ANSWERS\quizanwer{quiznum+1}.txt", "w")

    quest.write(
        "Name:\n\nDate:\n\n" + " " * 20 + f"Sate capital quiz(form{quiznum+1})\n\n"
    )
    states = list(capitals.keys())
    random.shuffle(states)

    for questnum in range(50):
        correctans = capitals[states[questnum]]
        wrongans = list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans = random.sample(wrongans, 3)
        options = wrongans + [correctans]
        random.shuffle(options)

        quest.write(f"{questnum+1}.What is the capital of {states[questnum]}?\n")
        for i in range(4):
            quest.write(f"  {'ABCD'[i]}. {options[i]}")
        quest.write("\n\n")

        answer.write(f"{questnum+1}.{'ABCD'[options.index(correctans)]}\n")

    quest.close()
    answer.close()
