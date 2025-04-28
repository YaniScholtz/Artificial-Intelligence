# L Mashigo          22587242
# Y Scholtz          22510657

import csv
import random
import matplotlib.pyplot as plt

CHROMOSOME_SIZE = 81

POPULATION_SIZE = 1000  # how many chromosomes in the the initial population                                       BEST:
MUTATION_RATE = 0.01  # determines how often offspring have random mutations to their representation (0-1)       BEST: 0.00
CROSSOVER_RATE = 0.5  # percentage
MAX_GENERATIONS = 5000

IDEAL_SOLUTION = []

# A population must consist of chromosomes, each chromosome must have 81 genes (R or P or S)

# ========================== READ CSV FILE DATA ==========================

filename = "data1.csv"  # change the filename accordingly

data = []
with open(filename, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

Dcount = 0
for row in data:
    Dcount = Dcount + 1

# All the possible histories.
# The histories, corresponding to the 81 different
# objects, should be in the same order as they would be visited by breadth first search (BFS)
# in a search tree of depth 4.
histories = [
    ["R", "R", "R", "R"],
    ["R", "R", "R", "P"],
    ["R", "R", "R", "S"],
    ["R", "R", "P", "R"],
    ["R", "R", "P", "P"],
    ["R", "R", "P", "S"],
    ["R", "R", "S", "R"],
    ["R", "R", "S", "P"],
    ["R", "R", "S", "S"],
    ["R", "P", "R", "R"],
    ["R", "P", "R", "P"],
    ["R", "P", "R", "S"],
    ["R", "P", "P", "R"],
    ["R", "P", "P", "P"],
    ["R", "P", "P", "S"],
    ["R", "P", "S", "R"],
    ["R", "P", "S", "P"],
    ["R", "P", "S", "S"],
    ["R", "S", "R", "R"],
    ["R", "S", "R", "P"],
    ["R", "S", "R", "S"],
    ["R", "S", "P", "R"],
    ["R", "S", "P", "P"],
    ["R", "S", "P", "S"],
    ["R", "S", "S", "R"],
    ["R", "S", "S", "P"],
    ["R", "S", "S", "S"],
    ["P", "R", "R", "R"],
    ["P", "R", "R", "P"],
    ["P", "R", "R", "S"],
    ["P", "R", "P", "R"],
    ["P", "R", "P", "P"],
    ["P", "R", "P", "S"],
    ["P", "R", "S", "R"],
    ["P", "R", "S", "P"],
    ["P", "R", "S", "S"],
    ["P", "P", "R", "R"],
    ["P", "P", "R", "P"],
    ["P", "P", "R", "S"],
    ["P", "P", "P", "R"],
    ["P", "P", "P", "P"],
    ["P", "P", "P", "S"],
    ["P", "P", "S", "R"],
    ["P", "P", "S", "P"],
    ["P", "P", "S", "S"],
    ["P", "S", "R", "R"],
    ["P", "S", "R", "P"],
    ["P", "S", "R", "S"],
    ["P", "S", "P", "R"],
    ["P", "S", "P", "P"],
    ["P", "S", "P", "S"],
    ["P", "S", "S", "R"],
    ["P", "S", "S", "P"],
    ["P", "S", "S", "S"],
    ["S", "R", "R", "R"],
    ["S", "R", "R", "P"],
    ["S", "R", "R", "S"],
    ["S", "R", "P", "R"],
    ["S", "R", "P", "P"],
    ["S", "R", "P", "S"],
    ["S", "R", "S", "R"],
    ["S", "R", "S", "P"],
    ["S", "R", "S", "S"],
    ["S", "P", "R", "R"],
    ["S", "P", "R", "P"],
    ["S", "P", "R", "S"],
    ["S", "P", "P", "R"],
    ["S", "P", "P", "P"],
    ["S", "P", "P", "S"],
    ["S", "P", "S", "R"],
    ["S", "P", "S", "P"],
    ["S", "P", "S", "S"],
    ["S", "S", "R", "R"],
    ["S", "S", "R", "P"],
    ["S", "S", "R", "S"],
    ["S", "S", "P", "R"],
    ["S", "S", "P", "P"],
    ["S", "S", "P", "S"],
    ["S", "S", "S", "R"],
    ["S", "S", "S", "P"],
    ["S", "S", "S", "S"],
]


objects = ["R", "P", "S"]

# -------------- FINDING IDEAL SOLUTION --------------#
# So based on the Yt given in data, the most ideal solution can be identified.
# This is solution that our GA must strive for
# So for each history, there is a most probable Yt
# Our Xt for that specific history must win again that


def find_optimal_solution():
    solution = []
    for i in range(
        len(histories)
    ):  # there are 81 possible histories, so for each history
        rcount = 0
        pcount = 0
        scount = 0  # track the possibilitity each object being the solution

        for j in range(len(data)):  # iterate through all the entries
            if (
                histories[i][0] + histories[i][1] + histories[i][2] + histories[i][3]
            ) == data[j][
                0
            ]:  # for the entries that match the history, count which Yt occurs the most
                if data[j][1] == "R":
                    rcount = rcount + 1
                elif data[j][1] == "P":
                    pcount = pcount + 1
                else:
                    scount = scount + 1

        # now we based on the most probable Yt for each history, we choose the winning object

        # print(f"{i} {histories[i][0] + histories[i][1] + histories[i][2] + histories[i][3]} \tRCOUNT: {rcount} \tPCOUNT: {pcount} \tSCOUNT: {scount}")
        if rcount == 0 and pcount == 0 and scount == 0:
            solution.append("X")
        elif (
            rcount > pcount and rcount > scount
        ):  # the most probable Yt is R, so to win given this history, P must be played
            solution.append("P")
        elif (
            pcount > rcount and pcount > scount
        ):  # the most probable Yt is P, so to win given this history, S must be played
            solution.append("S")
        else:
            solution.append(
                "R"
            )  # the most probable Yt is S, so to win given this history, R must be played

    return solution


IDEAL_SOLUTION = find_optimal_solution().copy()


# -------------- CREATING A POPULATION --------------#
# we must create a population according to the specified POPULATION_SIZE


def create_population():
    population = []

    # keep adding random chromosomes to the population until the population size is reached
    while len(population) < POPULATION_SIZE:

        chromosome = []  # each chromosome has 81 genes
        # populate the chromosome with random genes until theres 81 genes

        while len(chromosome) < CHROMOSOME_SIZE:
            rand_num = random.randint(0, 2)
            gene = objects[rand_num]

            chromosome.append(gene)

        population.append(
            chromosome
        )  # append the populated chromosome to the population

    return population


# -------------- DEFINING A FITNESS FUNCTION --------------#
# So a fitness function must be defined to evaluate each chromosome(individual)
# in the defined population


def fitness_function(population):  # returns the fitness score of the population
    fitness_scores = []

    for index in range(
        len(population)
    ):  # iterate through all chromosomes in population
        fitness = 0

        for i in range(CHROMOSOME_SIZE):  # iterate through each gene in the chromosome

            if population[index][i] == IDEAL_SOLUTION[i]:
                fitness += 1

        fitness_scores.append(fitness)

    return fitness_scores


# -------------- SELECTION --------------#
# this function must select the fittest chromosomes(individuals) from the initial population
# the fitness function can be used, perhaps the most fit n individuals will be used
# if we establish a threshold -- being the average, then all the chromosomes with fitness below threshold are eliminated


def selection(population):

    selected_pop = []
    pop_fitness = fitness_function(population)
    avg_fitness = sum(pop_fitness) / len(
        population
    )  # now we've obtained the average chromosome fitness level in this population

    for i in range(len(population)):

        if pop_fitness[i] >= (avg_fitness * 0.75):
            selected_pop.append(population[i])

    if (
        len(selected_pop) < 2
    ):  # there cannot be less than 2 chromosomes in the population
        return population

    # we want our selection to have an even number of chromosomes so that 2 chromosome parents can be crossed over

    pop_fitness = fitness_function(
        selected_pop
    )  # redefining the fitness to be of the new population

    if (
        len(selected_pop) % 2 != 0
    ):  # if there is an odd number of chromosomes in the new selection
        smallest = pop_fitness[
            0
        ]  # we want to remove the chromosome with the smallest fitness
        ind = 0

        for i in range(len(selected_pop)):
            if pop_fitness[i] < smallest:
                smallest = pop_fitness[i]
                ind = i

        pop_fitness.pop(ind)  # removing the chromosome with the smallest fitness
        selected_pop.pop(ind)

    return selected_pop


# -------------- CROSSOVER --------------#
# the new_pop will be used to crossover/merge chromosomes ideally crossing over
# 2 chromosomes at a time to create 2 new chromosomes
# the method described in the txb is splitting at a randoming index then crossing over
# the len(new_pop) == len(crossed_pop)


def Getting_Offspring(parent1, parent2):

    crossover_point = random.randint(  # gets a random index to crossover. the crossover happens AFTER the index
        1, len(parent1) - 1
    )
    offspring1 = []

    for i in range(crossover_point):

        offspring1.append(parent1[i])
    for i in range(crossover_point, len(parent2)):
        offspring1.append(parent2[i])

    offspring2 = []
    for i in range(crossover_point):

        offspring2.append(parent2[i])

    for i in range(crossover_point, len(parent1)):
        offspring2.append(parent1[i])

    return offspring1, offspring2


def crossover_function(selected_pop):
    new_pop = []

    size = len(
        selected_pop
    )  # we're going to "empty" selected_pop in the upcoming lines of code, so preserve the desired population size

    for add in range(
        2
    ):  # transfer the chromosomes with the highest 2 fitness scores into the offspring population
        pop_fitness = fitness_function(selected_pop)
        highest = pop_fitness[0]
        ind = 0
        for i in range(len(pop_fitness)):
            if pop_fitness[i] > highest:
                highest = pop_fitness[i]
                ind = i

        new_pop.append(selected_pop[ind])
        selected_pop.pop(
            ind
        )  # remove the highest from the rest of the populaton that will be crossed over

    while len(new_pop) < size:  # beginning of crossover
        parent1, parent2 = random.sample(selected_pop, 2)

        ind1 = selected_pop.index(
            parent1
        )  # we need to remove the parents that have already been used from the parents population
        selected_pop.pop(ind1)
        ind2 = selected_pop.index(parent2)
        selected_pop.pop(ind2)

        offspring1, offspring2 = Getting_Offspring(parent1, parent2)
        new_pop.extend([offspring1, offspring2])

    return new_pop[:size]


# -------------- MUTATION --------------#
# the purpose of this is to mutate a gene in a chromosome of the population
# this function will mutate a random gene with a random replacement
def mutation(population):
    # our mutation rate will influence how many genes we mutate in each single chromosome of the population  (there are 81 genes in a chromosome)
    # the rate is (0-1) so the number of genes we mutate in each chromosome = round(rate*81)

    num_to_mutate = round(MUTATION_RATE * CHROMOSOME_SIZE)

    pop_fitness = fitness_function(
        population
    )  # obtaining fitness of the current population
    avg_fitness = sum(pop_fitness) / len(population)

    for i in range(len(population)):  # accessing chromosomes in population
        if pop_fitness[i] < (
            avg_fitness * 0.35
        ):  # we only want to mutate genes in individuals with low fitness scores

            curr = 0
            while (
                curr < num_to_mutate
            ):  # here we will repeat this mutation process in the chromosome according to the num_to_mate

                index = random.randint(0, CHROMOSOME_SIZE - 1)  # any number from 0 - 80

                rand_num = random.randint(0, 2)  # replacing with a random object
                gene = objects[rand_num]

                population[i][index] = gene
                curr = curr + 1

    return population


# -------------- IMPLEMENTATION OF GA --------------#
# so this will be the execution of the genetic algorithm process


# this function will repeat through the process of (1)fitness calculation (2)selection  (3)crossover and (4)mutation until the solution has been obtained
def training_func(population):

    selected_pop = selection(population)  # ----(1) and (2)
    crossed_pop = crossover_function(selected_pop)  # ----(3)

    population = mutation(crossed_pop)  # ---(4)

    return population


fitness_progress = []  # Stores the highest score of the individual in each generation
avg_fitness_list = (
    []
)  # stores the avg fitness scores from all the individuals in one generation


def GeneticAlgorithm():
    global fitness_progress  # declaring the variables as global variables
    global avg_fitness_list

    init_population = create_population()  # initial population
    pop_fitness = fitness_function(init_population)
    selected_pop = selection(init_population)
    crossed_pop = crossover_function(selected_pop)

    num_generations = 0  # track how many generations it takes to reach solution

    population = mutation(crossed_pop)

    # first lets check if our chromosome with the highest fitness could be the solution
    pop_fitness = fitness_function(population)

    highest = pop_fitness[0]
    ind = 0
    for index in range(len(pop_fitness)):
        if pop_fitness[index] > highest:
            highest = pop_fitness[index]
            ind = index

    inital_highest_fitness = highest

    possible_solution = population[ind]
    found = True
    for i in range(len(possible_solution)):
        if IDEAL_SOLUTION[i] != "X" and possible_solution[i] != IDEAL_SOLUTION[i]:
            found = False

    # if the ideal solution hasn't been found yet, keep looking
    # from here we want to repeat (1)fitness calculation (2)selection (3)crossover and (4)mutation
    while (
        found == False and num_generations < MAX_GENERATIONS
    ):  # until the solution has been obtained/maximum generations
        found = True
        num_generations = num_generations + 1
        population = training_func(population)

        pop_fitness = []
        pop_fitness = fitness_function(population)

        highest = pop_fitness[0]
        ind = 0
        for i in range(len(pop_fitness)):
            if pop_fitness[i] > highest:
                highest = pop_fitness[i]
                ind = i

        # --------- GRAPHING PURPOSES ---------
        fitness_progress.append(
            highest
        )  # stores the highest fitness score in fitness_progress

        avg_fitness = round(
            sum(fitness_function(population)) / len(population), 1
        )  # calculates avg fitness of generation
        avg_fitness_list.append(
            avg_fitness
        )  # appends this avg value to avg_fitness_list
        # -------------------------------------

        # print(f"Generation: {num_generations} \tHIGHEST FITNESS: {highest}\n")
        possible_solution = population[ind]
        for i in range(len(possible_solution)):
            if IDEAL_SOLUTION[i] != "X" and possible_solution[i] != IDEAL_SOLUTION[i]:
                found = False

    print(f"INITIAL HIGHEST FITNESS WAS {inital_highest_fitness}")
    print(f"{num_generations} GENERATIONS TAKEN")

    return possible_solution


pop = GeneticAlgorithm()

unknown = 0
track = 0
notsame = 0

found = True

for i in range(len(pop)):
    if IDEAL_SOLUTION[i] != "X" and pop[i] != IDEAL_SOLUTION[i]:
        found = False
        notsame = notsame + 1
    elif IDEAL_SOLUTION[i] == "X":
        unknown = unknown + 1
    else:
        track = track + 1

if found == True:
    print("FOUND THE CORRECT SOLUTION")
    print(pop)
    print(f"MATCHING:   {track} out of 81")
    print(f"UNKNOWN:    {unknown} out of 81")
    print(f"WRONG:      {notsame} out of 81")
else:
    print("NOT FOUND !!!")
    print(pop)
    print(f"MATCHING:   {track} out of 81")
    print(f"UNKNOWN:    {unknown} out of 81")
    print(f"WRONG:      {notsame} out of 81")


# ------------------ GRAPHING -------------------------
generations = range(1, len(fitness_progress) + 1)
plt.plot(
    generations, fitness_progress, label="Fitness Progress (Best Individual)"
)  # plots the best fitness scores
plt.plot(
    generations, avg_fitness_list, label="Average Fitness Per Generation"
)  # plots the avg fitness scores

plt.xlabel("Number of generations")
plt.ylabel("Fitness Score")
plt.title("Fitness Progress and Average Fitness Per Generation")
plt.legend()
plt.grid(True)
plt.show()
