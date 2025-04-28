import csv
import random
import numpy as np

# Initialize counts and data storage
Count_S = 0
Count_P = 0
Count_R = 0
Total_Count = 0


# initialising the differen moves
Xt_2 = []
Yt_2 = []
Xt_1 = []
Yt_1 = []
Yt = []

initialized = False


def initialize():  # this function to read from the data csv
    global Count_S, Count_P, Count_R, Total_Count
    global Xt_2, Yt_2, Xt_1, Yt_1, Yt
    global prob_S, prob_R, prob_P
    global conditional_probabilitiesYt_1, conditional_probabilitiesXt_1
    global conditional_probabilitiesYt_2, conditional_probabilitiesXt_2

    # Read data from CSV and process for both probabilities and sequences
    with open("data1.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                sequence = row[0].strip()
                char_after_comma = row[1].strip()

                if len(sequence) == 4:
                    Xt_2.append(sequence[0])
                    Yt_2.append(sequence[1])
                    Xt_1.append(sequence[2])
                    Yt_1.append(sequence[3])
                    Yt.append(char_after_comma)

                if char_after_comma == "S":
                    Count_S += 1
                elif char_after_comma == "R":
                    Count_R += 1
                elif char_after_comma == "P":
                    Count_P += 1
                Total_Count += 1

    # Calculate the probabilities of Yt
    prob_S = Count_S / Total_Count if Total_Count > 0 else 0  # getting the prior prob
    prob_R = Count_R / Total_Count if Total_Count > 0 else 0
    prob_P = Count_P / Total_Count if Total_Count > 0 else 0

    print("prob_S:", prob_S)
    print("prob_R:", prob_R)
    print("prob_P:", prob_P)
    print("Total_Count:", Total_Count)

    # Calculate conditional probabilities
    def calculate_conditional_probabilities(
        Yt, prev_values, total_counts
    ):  # conditional probs
        conditional_probabilities = {
            "R": {"R": 1, "P": 1, "S": 1},  # Start with 1 to apply Laplace smoothing
            "P": {"R": 1, "P": 1, "S": 1},
            "S": {"R": 1, "P": 1, "S": 1},
        }

        for i in range(len(Yt)):
            if Yt[i] in conditional_probabilities:
                if prev_values[i] in conditional_probabilities[Yt[i]]:
                    conditional_probabilities[Yt[i]][prev_values[i]] += 1

        for key in conditional_probabilities:
            total_with_smoothing = (
                total_counts[key] + 3
            )  # Adding 3 for Laplace smoothing
            for subkey in conditional_probabilities[key]:
                conditional_probabilities[key][subkey] /= total_with_smoothing

        return conditional_probabilities

    conditional_probabilitiesYt_1 = calculate_conditional_probabilities(
        Yt, Yt_1, {"R": Count_R, "P": Count_P, "S": Count_S}
    )
    conditional_probabilitiesXt_1 = calculate_conditional_probabilities(
        Yt, Xt_1, {"R": Count_R, "P": Count_P, "S": Count_S}
    )
    conditional_probabilitiesYt_2 = calculate_conditional_probabilities(
        Yt, Yt_2, {"R": Count_R, "P": Count_P, "S": Count_S}
    )
    conditional_probabilitiesXt_2 = calculate_conditional_probabilities(
        Yt, Xt_2, {"R": Count_R, "P": Count_P, "S": Count_S}
    )

    print("Conditional Probabilities of Yt_2:")
    print(conditional_probabilitiesYt_2)
    print("\nConditional Probabilities of Yt_1:")
    print(conditional_probabilitiesYt_1)
    print("\nConditional Probabilities of Xt_1:")
    print(conditional_probabilitiesXt_1)
    print("\nConditional Probabilities of Xt_2:")
    print(conditional_probabilitiesXt_2)


prob_S = 0.324269
prob_R = 0.341328
prob_P = 0.334403
Total_Count = 1000000

conditional_probabilitiesYt_2 = {
    "R": {"R": 0.8639355933097199, "P": 0.06785495603973855, "S": 0.06820945065054156},
    "P": {"R": 0.06974157162251873, "P": 0.8614797581383109, "S": 0.06877867023917035},
    "S": {"R": 0.07156646272265259, "P": 0.071116223417378, "S": 0.8573173138599695},
}

conditional_probabilitiesYt_1 = {
    "R": {"R": 0.8656582613357708, "P": 0.06764987651282772, "S": 0.06669186215140142},
    "P": {"R": 0.0688743623021118, "P": 0.8621824967255373, "S": 0.06894314097235098},
    "S": {"R": 0.07050254107662703, "P": 0.07079242117728327, "S": 0.8587050377460897},
}

conditional_probabilitiesXt_1 = {
    "R": {"R": 0.26596177903559887, "P": 0.26656822849374945, "S": 0.46746999247065163},
    "P": {"R": 0.4703922776505206, "P": 0.26424466068192554, "S": 0.2653630616675538},
    "S": {"R": 0.2628904129866285, "P": 0.4734636354665219, "S": 0.26364595154684956},
}

conditional_probabilitiesXt_2 = {
    "R": {"R": 0.3312913271868069, "P": 0.33114777151796937, "S": 0.3375609012952237},
    "P": {"R": 0.33686297494662176, "P": 0.3313756332123227, "S": 0.33176139184105546},
    "S": {"R": 0.33166292495189226, "P": 0.3364922040755909, "S": 0.3318448709725169},
}
