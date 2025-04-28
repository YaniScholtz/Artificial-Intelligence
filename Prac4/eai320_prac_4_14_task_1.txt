# Practical 4 - EAI 320
# Group 14
# Yani Scholtz      22510657
# Lethabo Mashigo   22587242
# -----------------------------------------------------------------
import random
import numpy as np


"""
COMMENTED CODE BEGIN 

#Number of R,P and S in the data.csv file
Count_S = 0
Count_P = 0
Count_R = 0
Total_Count = 0


# initialising the different columns
Xt_2 = []
Yt_2 = []
Xt_1 = []
Yt_1 = []
Yt = []

#Putting this initialised flag to call it later to only read the data.csv once
initialized = False



#Function to read from data.csv
def initialize(): 
    global Count_S, Count_P, Count_R, Total_Count
    global Xt_2, Yt_2, Xt_1, Yt_1, Yt
    global prob_S, prob_R, prob_P
    global conditional_probabilitiesYt_1, conditional_probabilitiesXt_1,conditional_probabilitiesYt_2, conditional_probabilitiesXt_2
    

    # Read data from CSV
    with open("data1.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                sequence = row[0].strip()
                char_after_comma = row[1].strip()

                #Read in the values of Yt, X_1, Y_1, X_2, Y_2
                if len(sequence) == 4:
                    Xt_2.append(sequence[0])
                    Yt_2.append(sequence[1])
                    Xt_1.append(sequence[2])
                    Yt_1.append(sequence[3])
                    Yt.append(char_after_comma)

                #Get the count from the last column
                if char_after_comma == "S":
                    Count_S += 1
                elif char_after_comma == "R":
                    Count_R += 1
                elif char_after_comma == "P":
                    Count_P += 1
                Total_Count += 1

    #Work out the probabilities for the "prior probabilty"       
    prob_S = Count_S / Total_Count
    prob_R = Count_R / Total_Count
    prob_P = Count_P / Total_Count

    #Prints to get the values of the probs to hardcode them laster
    print("prob_S:", prob_S)
    print("prob_R:", prob_R)
    print("prob_P:", prob_P)
    print("Total_Count:", Total_Count)

# Calculate conditional probabilities


#Get Y_t

# Dictionary to store the conditional porbability
#Starting with 1 to rectify and make sure that the probabilities are not 0  
conditional_probabilitiesYt_1 = {
    "R": {"R": 1, "P": 1, "S": 1},
    "P": {"R": 1, "P": 1, "S": 1},
    "S": {"R": 1, "P": 1, "S": 1},
}

# For loop to calculate the conditional porbability based on what the causal and effect
for i in range(len(Yt)):
    if Yt[i] == "R":
        if Yt_1[i] == "R":
            conditional_probabilitiesYt_1["R"]["R"] += 1
        elif Yt_1[i] == "P":
            conditional_probabilitiesYt_1["R"]["P"] += 1
        elif Yt_1[i] == "S":
            conditional_probabilitiesYt_1["R"]["S"] += 1
    elif Yt[i] == "P":
        if Yt_1[i] == "R":
            conditional_probabilitiesYt_1["P"]["R"] += 1
        elif Yt_1[i] == "P":
            conditional_probabilitiesYt_1["P"]["P"] += 1
        elif Yt_1[i] == "S":
            conditional_probabilitiesYt_1["P"]["S"] += 1
    elif Yt[i] == "S":
        if Yt_1[i] == "R":
            conditional_probabilitiesYt_1["S"]["R"] += 1
        elif Yt_1[i] == "P":
            conditional_probabilitiesYt_1["S"]["P"] += 1
        elif Yt_1[i] == "S":
            conditional_probabilitiesYt_1["S"]["S"] += 1

#This is using the laplace method so adding 3 for the R P S
total_R = Count_R + 1 + 1 + 1  # Add 1 for each R, P, S
total_P = Count_P + 1 + 1 + 1  # Add 1 for each R, P, S
total_S = Count_S + 1 + 1 + 1  # Add 1 for each R, P, S



#Working out the conditional probs
conditional_probabilitiesYt_1["R"]["R"] = (
    conditional_probabilitiesYt_1["R"]["R"] / total_R
)
conditional_probabilitiesYt_1["R"]["P"] = (
    conditional_probabilitiesYt_1["R"]["P"] / total_R
)
conditional_probabilitiesYt_1["R"]["S"] = (
    conditional_probabilitiesYt_1["R"]["S"] / total_R
)


conditional_probabilitiesYt_1["P"]["R"] = (
    conditional_probabilitiesYt_1["P"]["R"] / total_P
)
conditional_probabilitiesYt_1["P"]["P"] = (
    conditional_probabilitiesYt_1["P"]["P"] / total_P
)
conditional_probabilitiesYt_1["P"]["S"] = (
    conditional_probabilitiesYt_1["P"]["S"] / total_P
)


conditional_probabilitiesYt_1["S"]["R"] = (
    conditional_probabilitiesYt_1["S"]["R"] / total_S
)
conditional_probabilitiesYt_1["S"]["P"] = (
    conditional_probabilitiesYt_1["S"]["P"] / total_S
)
conditional_probabilitiesYt_1["S"]["S"] = (
    conditional_probabilitiesYt_1["S"]["S"] / total_S
)

#Now do the exact same but with Xt_1
conditional_probabilitiesXt_1 = {
    "R": {"R": 1, "P": 1, "S": 1},
    "P": {"R": 1, "P": 1, "S": 1},
    "S": {"R": 1, "P": 1, "S": 1},
}

for i in range(len(Yt)):
    if Yt[i] == "R":
        if Xt_1[i] == "R":
            conditional_probabilitiesXt_1["R"]["R"] += 1
        elif Xt_1[i] == "P":
            conditional_probabilitiesXt_1["R"]["P"] += 1
        elif Xt_1[i] == "S":
            conditional_probabilitiesXt_1["R"]["S"] += 1
    elif Yt[i] == "P":
        if Xt_1[i] == "R":
            conditional_probabilitiesXt_1["P"]["R"] += 1
        elif Xt_1[i] == "P":
            conditional_probabilitiesXt_1["P"]["P"] += 1
        elif Xt_1[i] == "S":
            conditional_probabilitiesXt_1["P"]["S"] += 1
    elif Yt[i] == "S":
        if Xt_1[i] == "R":
            conditional_probabilitiesXt_1["S"]["R"] += 1
        elif Xt_1[i] == "P":
            conditional_probabilitiesXt_1["S"]["P"] += 1
        elif Xt_1[i] == "S":
            conditional_probabilitiesXt_1["S"]["S"] += 1

conditional_probabilitiesXt_1["R"]["R"] = (
    conditional_probabilitiesXt_1["R"]["R"] / total_R
)
conditional_probabilitiesXt_1["R"]["P"] = (
    conditional_probabilitiesXt_1["R"]["P"] / total_R
)
conditional_probabilitiesXt_1["R"]["S"] = (
    conditional_probabilitiesXt_1["R"]["S"] / total_R
)

# Normalizing counts to probabilities for move "P"
conditional_probabilitiesXt_1["P"]["R"] = (
    conditional_probabilitiesXt_1["P"]["R"] / total_P
)
conditional_probabilitiesXt_1["P"]["P"] = (
    conditional_probabilitiesXt_1["P"]["P"] / total_P
)
conditional_probabilitiesXt_1["P"]["S"] = (
    conditional_probabilitiesXt_1["P"]["S"] / total_P
)

# Normalizing counts to probabilities for move "S"
conditional_probabilitiesXt_1["S"]["R"] = (
    conditional_probabilitiesXt_1["S"]["R"] / total_S
)
conditional_probabilitiesXt_1["S"]["P"] = (
    conditional_probabilitiesXt_1["S"]["P"] / total_S
)
conditional_probabilitiesXt_1["S"]["S"] = (
    conditional_probabilitiesXt_1["S"]["S"] / total_S
)

#Do the exact same for Yt_2
conditional_probabilitiesYt_2 = {
    "R": {"R": 1, "P": 1, "S": 1},
    "P": {"R": 1, "P": 1, "S": 1},
    "S": {"R": 1, "P": 1, "S": 1},
}

for i in range(len(Yt)):
    if Yt[i] == "R":
        if Yt_2[i] == "R":
            conditional_probabilitiesYt_2["R"]["R"] += 1
        elif Yt_2[i] == "P":
            conditional_probabilitiesYt_2["R"]["P"] += 1
        elif Yt_2[i] == "S":
            conditional_probabilitiesYt_2["R"]["S"] += 1
    elif Yt[i] == "P":
        if Yt_2[i] == "R":
            conditional_probabilitiesYt_2["P"]["R"] += 1
        elif Yt_2[i] == "P":
            conditional_probabilitiesYt_2["P"]["P"] += 1
        elif Yt_2[i] == "S":
            conditional_probabilitiesYt_2["P"]["S"] += 1
    elif Yt[i] == "S":
        if Yt_2[i] == "R":
            conditional_probabilitiesYt_2["S"]["R"] += 1
        elif Yt_2[i] == "P":
            conditional_probabilitiesYt_2["S"]["P"] += 1
        elif Yt_2[i] == "S":
            conditional_probabilitiesYt_2["S"]["S"] += 1

conditional_probabilitiesYt_2["R"]["R"] = (
    conditional_probabilitiesYt_2["R"]["R"] / total_R
)
conditional_probabilitiesYt_2["R"]["P"] = (
    conditional_probabilitiesYt_2["R"]["P"] / total_R
)
conditional_probabilitiesYt_2["R"]["S"] = (
    conditional_probabilitiesYt_2["R"]["S"] / total_R
)


conditional_probabilitiesYt_2["P"]["R"] = (
    conditional_probabilitiesYt_2["P"]["R"] / total_P
)
conditional_probabilitiesYt_2["P"]["P"] = (
    conditional_probabilitiesYt_2["P"]["P"] / total_P
)
conditional_probabilitiesYt_2["P"]["S"] = (
    conditional_probabilitiesYt_2["P"]["S"] / total_P
)

# Normalizing counts to probabilities for move "S"
conditional_probabilitiesYt_2["S"]["R"] = (
    conditional_probabilitiesYt_2["S"]["R"] / total_S
)
conditional_probabilitiesYt_2["S"]["P"] = (
    conditional_probabilitiesYt_2["S"]["P"] / total_S
)
conditional_probabilitiesYt_2["S"]["S"] = (
    conditional_probabilitiesYt_2["S"]["S"] / total_S
)

#Do the same for Xt_2
conditional_probabilitiesXt_2 = {
    "R": {"R": 1, "P": 1, "S": 1},
    "P": {"R": 1, "P": 1, "S": 1},
    "S": {"R": 1, "P": 1, "S": 1},
}

for i in range(len(Yt)):
    if Yt[i] == "R":
        if Xt_2[i] == "R":
            conditional_probabilitiesXt_2["R"]["R"] += 1
        elif Xt_2[i] == "P":
            conditional_probabilitiesXt_2["R"]["P"] += 1
        elif Xt_2[i] == "S":
            conditional_probabilitiesXt_2["R"]["S"] += 1
    elif Yt[i] == "P":
        if Xt_2[i] == "R":
            conditional_probabilitiesXt_2["P"]["R"] += 1
        elif Xt_2[i] == "P":
            conditional_probabilitiesXt_2["P"]["P"] += 1
        elif Xt_2[i] == "S":
            conditional_probabilitiesXt_2["P"]["S"] += 1
    elif Yt[i] == "S":
        if Xt_2[i] == "R":
            conditional_probabilitiesXt_2["S"]["R"] += 1
        elif Xt_2[i] == "P":
            conditional_probabilitiesXt_2["S"]["P"] += 1
        elif Xt_2[i] == "S":
            conditional_probabilitiesXt_2["S"]["S"] += 1

conditional_probabilitiesXt_2["R"]["R"] = (
    conditional_probabilitiesXt_2["R"]["R"] / total_R
)
conditional_probabilitiesXt_2["R"]["P"] = (
    conditional_probabilitiesXt_2["R"]["P"] / total_R
)
conditional_probabilitiesXt_2["R"]["S"] = (
    conditional_probabilitiesXt_2["R"]["S"] / total_R
)


conditional_probabilitiesXt_2["P"]["R"] = (
    conditional_probabilitiesXt_2["P"]["R"] / total_P
)
conditional_probabilitiesXt_2["P"]["P"] = (
    conditional_probabilitiesXt_2["P"]["P"] / total_P
)
conditional_probabilitiesXt_2["P"]["S"] = (
    conditional_probabilitiesXt_2["P"]["S"] / total_P
)


conditional_probabilitiesXt_2["S"]["R"] = (
    conditional_probabilitiesXt_2["S"]["R"] / total_S
)
conditional_probabilitiesXt_2["S"]["P"] = (
    conditional_probabilitiesXt_2["S"]["P"] / total_S
)
conditional_probabilitiesXt_2["S"]["S"] = (
    conditional_probabilitiesXt_2["S"]["S"] / total_S

    print("Conditional Probabilities of Yt_2:")
    print(conditional_probabilitiesYt_2)
    print("\nConditional Probabilities of Yt_1:")
    print(conditional_probabilitiesYt_1)
    print("\nConditional Probabilities of Xt_1:")
    print(conditional_probabilitiesXt_1)
    print("\nConditional Probabilities of Xt_2:")
    print(conditional_probabilitiesXt_2)
    
    COMMENTED CODE ENDS
    """


# After running the commented code the hard coded values can now be saved in variables.
Count_S = 324269
Count_P = 334403
Count_R = 341328
Total_Count = 1000000

prob_S = 0.324269
prob_R = 0.341328
prob_P = 0.334403

# Dictionary used for easy extraction of different values

# Conditional probability for Yt-2
conditional_probabilitiesYt_2 = {
    "R": {"R": 0.8639355933097199, "P": 0.06785495603973855, "S": 0.06820945065054156},
    "P": {"R": 0.06974157162251873, "P": 0.8614797581383109, "S": 0.06877867023917035},
    "S": {"R": 0.07156646272265259, "P": 0.071116223417378, "S": 0.8573173138599695},
}

# Conditional probability for Yt-1
conditional_probabilitiesYt_1 = {
    "R": {"R": 0.8656582613357708, "P": 0.06764987651282772, "S": 0.06669186215140142},
    "P": {"R": 0.0688743623021118, "P": 0.8621824967255373, "S": 0.06894314097235098},
    "S": {"R": 0.07050254107662703, "P": 0.07079242117728327, "S": 0.8587050377460897},
}

# Conditional probability for Xt-1
conditional_probabilitiesXt_1 = {
    "R": {"R": 0.26596177903559887, "P": 0.26656822849374945, "S": 0.46746999247065163},
    "P": {"R": 0.4703922776505206, "P": 0.26424466068192554, "S": 0.2653630616675538},
    "S": {"R": 0.2628904129866285, "P": 0.4734636354665219, "S": 0.26364595154684956},
}
# Conditional probability for Xt-2
conditional_probabilitiesXt_2 = {
    "R": {"R": 0.3312913271868069, "P": 0.33114777151796937, "S": 0.3375609012952237},
    "P": {"R": 0.33686297494662176, "P": 0.3313756332123227, "S": 0.33176139184105546},
    "S": {"R": 0.33166292495189226, "P": 0.3364922040755909, "S": 0.3318448709725169},
}


# -----------AGENT---------------------------
if input == "":

    matches_amount = 0
    hold = ""  # Holding the winning move char
    history = []  # Variable where the 4 char sequence will be stored
    prev = np.random.choice(
        ["R", "P", "S"]
    )  # Choosing a random value because we don't know the other agent's move yet
else:
    if matches_amount < 2:  # Less than two moves then append new ply
        history.append(prev)  # Appends agent move
        history.append(input)  # Appends bot's move
        prev = np.random.choice(["R", "P", "S"])
        matches_amount += 1  # Increase matches so that two moves can be reached
    else:
        hold = prev  # Hold so that it does not overwrite
        history.append(hold)
        history.append(input)
        history = history[2:]
        x2, y2, x1, y1 = (
            history[-4],
            history[-3],
            history[-2],
            history[-1],
        )  # Extracting the 4 sequence values from the history to use it to
        # get thr conditional probabilities

        # Working out the P(R|sequence)
        p_R = (
            prob_R
            * conditional_probabilitiesYt_2["R"][y2]
            * conditional_probabilitiesXt_2["R"][x2]
            * conditional_probabilitiesYt_1["R"][y1]
            * conditional_probabilitiesXt_1["R"][x1]
        )

        # Working out the P(P|sequence)
        p_P = (
            prob_P
            * conditional_probabilitiesYt_2["P"][y2]
            * conditional_probabilitiesXt_2["P"][x2]
            * conditional_probabilitiesYt_1["P"][y1]
            * conditional_probabilitiesXt_1["P"][x1]
        )

        # Working out the P(S|sequence)
        p_S = (
            prob_S
            * conditional_probabilitiesYt_2["S"][y2]
            * conditional_probabilitiesXt_2["S"][x2]
            * conditional_probabilitiesYt_1["S"][y1]
            * conditional_probabilitiesXt_1["S"][x1]
        )
        # Saving the conditional probabilities in the variables
        probabilities = {"R": p_R, "P": p_P, "S": p_S}
        max_prob = max(
            probabilities.values()
        )  # Get the probability that has the max value and then use that char to find the winning move
        max_moves = (
            []
        )  # This array is for if there are probabilities that have equal value then a ply must be randomly chosen to play

        for move, prob in probabilities.items():
            if prob == max_prob:
                max_moves.append(move)

        next_move = random.choice(
            max_moves
        )  # Next_move is now saving the predicted move of the opponent

        # Determining the outputs that will win the predicted move
        if next_move == "R":
            prev = "P"
        elif next_move == "P":
            prev = "S"
        elif next_move == "S":
            prev = "R"


# Save the winning output for the agent
output = prev


"""'
RESULTS FOR BOTS

Pool 1: 1 bots loaded
Pool 2: 4 bots loaded
Playing 100 matches per pairing.
Running matches in 8 threads
400 matches run
total run time: 6.45 seconds

beat_common.py: won 0.0% of matches (0 of 100)
    won 17.2% of rounds (17228 of 100000)
    avg score -514.5, net score -51454.0

only_paper.py: won 0.0% of matches (0 of 100)
    won 0.1% of rounds (96 of 100000)
    avg score -996.9, net score -99694.0

only_rock.py: won 0.0% of matches (0 of 100)
    won 0.1% of rounds (101 of 100000)
    avg score -997.0, net score -99696.0

only_scissors.py: won 0.0% of matches (0 of 100)
    won 0.1% of rounds (108 of 100000)
    avg score -996.9, net score -99686.0

eai320_prac_4_14_task_1.py: won 97.8% of matches (391 of 400)
    won 92.0% of rounds (368063 of 400000)
    avg score 876.3, net score 350530.0


PLAYING AGAINST BEAT_PREVIOUS

Pool 1: 1 bots loaded
Pool 2: 1 bots loaded
Playing 100 matches per pairing.
Running matches in 8 threads
100 matches run
total run time: 1.91 seconds

beat_previous.py: won 28.0% of matches (28 of 100)
    won 39.0% of rounds (38971 of 100000)
    avg score -0.3, net score -27.0

eai320_prac_4_14_task_1.py: won 42.0% of matches (42 of 100)
    won 39.0% of rounds (38998 of 100000)
    avg score 0.3, net score 27.0

    
---------DISCUSSION--------------

IMPLEMENTATION DISCUSSION:

The implemented algorithm used historical data from a game with three possible moves—Rock (R), Paper (P), and Scissors (S)—to do a sequence analysis and prediction. 
The method started by reading data from a CSV file called data1.csv. 
R,P,S was counted in the data and the prior probabilities of these moves were calculated.
The prior probabilities of each move were calculated using the prior probabilities already calculated.
Dictionaries were created containing the conditional probabilities of the moves so that the probability P(R|sequence) for example could be calculated. 
Working with sequences that have not been "seen" before, 1 was added to every sample to rectify the 0 issue. 
Finally the prior probabilities could be calculated and they were printed to save those values.
The prior probabilities and the conditional probabilities were hardcoded into the program to be used in predicting and winning future moves without being reliable on the data csv dataset. 
The agent kepts track of its moves during the game and used this information to predict the opponent's next move by using conditional probabilities that have been computed. 
The agent then decided which move would defeat the opponent's predicted move.The cases where multiple moves had identical maximum probabilities, the agent selected one at random.
The implementation's goal was to get trained by data and then predict the opponent's moves as well as win that move as well.

RESULT DISCUSSION:

The agent was tested against several bots: only_paper, only_rock, only_scissors,beat_common and beat_previous. It achieved a 100% win rate against the only_rock, only_paper and only_scissors where
these bots only won 0.1% of the rounds.
Playing against the beat_common bot, the agent won around 96% of the matches and 74.3% of the rounds, the beat_common bot won 0% matches and 17.6% of the rounds.
The bots that only output one type of move were easily won since it was easy to predict the outputs and win the moves since it stays the same.
Beat_common was less successful in winning 100% of the matches since there were different values playing against the agent instead of only one.   
When matched against the beat_previous bot, the agent only wins 38% of the matches and 41.5% of the rounds and the bot winning 30% of the and 41.5% of the rounds.
This is due to the fact that the agent implemented in task 1 is not a learning agent and is only trained by training data, it relies solely on hardcoded values.
In contrast, Task2 performed better in winning different bots since Task 2 is a learning agent.
"""