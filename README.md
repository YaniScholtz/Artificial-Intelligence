# AI Search and Optimization Practicals

This repository contains practical projects for the **Artificial Intelligence Fundamentals (EAI320)** course.  
It explores core AI concepts including search algorithms, evolutionary optimization, and probabilistic prediction agents.

---

## Project Descriptions

### 1. SearchTree (Tree.py)

- Implements a search tree with **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** traversal.
- Supports node creation and tree traversal for problem-solving.

### 2. Genetic Algorithm Solver (Task1.py)

- Solves an optimization problem using **Genetic Algorithms (GA)**.
- Includes:
  - Random population generation
  - Fitness evaluation
  - Selection, crossover, and mutation operations
  - Fitness progress tracking across generations

### 3. Bayesian Prediction Agent (eai320_prac_4_14_task_1.py)

- Trains a prediction agent using historical **Rock-Paper-Scissors** sequence data.
- Uses **Bayesian conditional probability** models.
- Predicts opponent moves and selects optimal winning strategies.
- Performance benchmarked against baseline bots (e.g., only_rock, beat_common).

---

## Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `matplotlib`
- Dataset file: `data1.csv` (required for agent training)

Install dependencies with:

```bash
pip install numpy matplotlib
