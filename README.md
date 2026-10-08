# Computer Science Concept Simulator

An interactive micro-project that demonstrates three important computer science concepts from different subjects in one common application.
The project is built using Python and Streamlit. Each concept is implemented as a separate section so that users can interact with the concept and observe the result.

## Proposed Project Title
Computer Science Concept Simulator

## Problem Statement
Students often learn theoretical concepts from different computer science subjects separately, which can make it difficult to understand how these concepts work in practical situations.
This project provides a single interactive application that demonstrates three concepts through  

implementation:
1. Kleene's Theorem
2. Greedy Algorithm
3. Structural Hazards
Each concept is implemented in a separate module of the application. Users can provide inputs, run the corresponding algorithm or simulation, and observe the results.
The project aims to make these theoretical concepts easier to understand through practical implementation and interactive visualization.

Objectives
- To implement and demonstrate Kleene's Theorem using Regular Expressions and Finite Automata.
- To implement a Greedy Algorithm using the Activity Selection Problem.
- To simulate Structural Hazards in a processor pipeline.
- To provide separate sections for each concept within one common application.
- To allow users to interact with the concepts through a simple user interface.
- To demonstrate theoretical concepts through practical implementation.

## Project Overview

             COMPUTER SCIENCE CONCEPT SIMULATOR
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       KLEENE           GREEDY          STRUCTURAL
     THEOREM          ALGORITHM           HAZARD
          |                |                |
          v                v                v
    Regex → NFA       Activity          Pipeline
      Testing         Selection        Simulation

1. Kleene's Theorem

Kleene's Theorem establishes the relationship between Regular Expressions and Finite Automata.
In this project, a Regular Expression is converted into a finite automaton, and the generated automaton is used to test whether a given input string is accepted.

Implementation
The module supports:
- Regular Expression input
- Union |
- Concatenation
- Kleene Star *
- Positive Closure +
- Parentheses
- Finite Automaton generation
- Input string testing
- Accept/Reject result

Working Flow:
Regular Expression
        |
        v
   Regex Parser
        |
        v
 Finite Automaton
        |
        v
   Input String
        |
        v
  Accept / Reject

Example
Regular Expression:
(a|b)*
Input String:
abba
Expected Output:
ACCEPTED
Another example:
Input String: abc
Expected output:
REJECTED

2. Greedy Algorithm

A Greedy Algorithm makes the best available choice at each step with the goal of obtaining an optimal solution.
For this project, the Activity Selection Problem is used to demonstrate the greedy approach.
Greedy Strategy
The algorithm selects the activity that has the earliest finishing time, provided that it does not overlap with the previously selected activity.

Example
Activity    Start    Finish

A1            1        2
A2            3        4
A3            0        6
A4            5        7
A5            8        9

The algorithm selects:
A1 → A2 → A4 → A5
Final result:
Maximum compatible activities = 4

Working Flow:
Activities
     |
     v
Sort by Finish Time
     |
     v
Select Earliest Finishing Activity
     |
     v
Check Next Activity
     |
     v
Select / Reject
     |
     v
Final Selected Activities

3. Structural Hazards

A Structural Hazard occurs in a processor pipeline when two or more instructions require the same hardware resource at the same time.
This project demonstrates structural hazards using a simplified five-stage processor pipeline.

Pipeline Stages:
IF → ID → EX → MEM → WB
Where:
- IF = Instruction Fetch
- ID = Instruction Decode
- EX = Execute
- MEM = Memory Access
- WB = Write Back

Implementation
The module:
- Displays instructions moving through pipeline stages.
- Shows cycle-by-cycle execution.
- Identifies resource conflicts.
- Detects structural hazards.
- Inserts a stall to resolve the conflict.
- Displays the final pipeline execution.

Example
Instruction 1: LOAD
Instruction 2: COMPUTE
Instruction 3: COMPUTE
Instruction 4: LOAD
The application displays the pipeline execution in a table and highlights the inserted STALL when a resource conflict is detected.
The application also displays a hazard message:
Structural Hazard Detected

A shared resource is required by two instructions
in the same cycle.

STALL inserted to resolve the structural hazard.

## Technologies Used
- Python
- Streamlit

## Project Structure
computer-science-concept-simulator/
│
├── app.py
├── kleene.py
├── greedy.py
├── structural_hazard.py
├── requirements.txt
├── README.md
└── .venv/

## File Description
File	                    Purpose
app.py	                Main Streamlit application and user interface
kleene.py	            Regular Expression to Finite Automaton implementation
greedy.py	            Activity Selection Greedy Algorithm
structural_hazard.py	Pipeline and Structural Hazard simulation
requirements.txt	    Project dependencies
README.md	            Project documentation


## Installation
Step 1: Clone or Download the Project
If the project is available on GitHub:
git clone <repository-url>
Enter the project directory:
cd computer-science-concept-simulator

Step 2: Create a Virtual Environment
python -m venv .venv

Step 3: Activate the Virtual Environment
Windows Git Bash
source .venv/Scripts/activate
Windows Command Prompt
.venv\Scripts\activate

Step 4: Install Dependencies
pip install -r requirements.txt
Running the Application
Start the Streamlit application using:
streamlit run app.py
The application will provide a local URL similar to:
http://localhost:8501
Open the URL in a web browser.

## Application Sections
The application contains three separate sections:
1. Kleene's Theorem
2. Greedy Algorithm
3. Structural Hazard

Section 1: Kleene's Theorem
Users can:
1. Enter a Regular Expression.
2. Generate the finite automaton.
3. View the transition structure.
4. Enter an input string.
5. Check whether the string is accepted or rejected.

Section 2: Greedy Algorithm
Users can:
1. View the available activities.
2. Run the Greedy Algorithm.
3. Observe the selection process.
4. View selected activities.
5. View the maximum number of compatible activities.

Section 3: Structural Hazard
Users can:
1. Select processor instructions.
2. Simulate the pipeline.
3. View pipeline stages cycle-by-cycle.
4. Identify structural hazards.
5. Observe the inserted stall.

## Testing
Test Case 1 — Kleene's Theorem
Input:
Regular Expression: (a|b)*
String: abba
Expected Output:
ACCEPTED

Test Case 2 — Kleene's Theorem
Input:
Regular Expression: (a|b)*
String: abc
Expected Output:
REJECTED

Test Case 3 — Greedy Algorithm
Input Activities:
A1 → 1 - 2
A2 → 3 - 4
A3 → 0 - 6
A4 → 5 - 7
A5 → 8 - 9
Expected Output:
Selected Activities:
A1 → A2 → A4 → A5
Maximum compatible activities: 4

Test Case 4 — Structural Hazard
Input:
LOAD
COMPUTE
COMPUTE
LOAD
Expected Output:
Structural Hazard Detected
STALL inserted
Expected Outcomes

### After completing the project, the user should be able to:
- Understand the relationship between Regular Expressions and Finite Automata.
- Observe how a Greedy Algorithm makes decisions.
- Understand how pipeline resource conflicts create Structural Hazards.
- Observe how a stall is used to resolve a pipeline resource conflict.
- Interact with all three concepts through one common application.

### Key Features
- Simple interactive interface
- Three independent concept modules
- Practical implementation of theoretical concepts
- Step-by-step algorithm execution
- Finite Automaton testing
- Greedy Activity Selection
- Pipeline simulation
- Structural Hazard detection
- Stall visualization

## Overall System Flow
                         USER
                          |
                          v
             COMPUTER SCIENCE CONCEPT
                    SIMULATOR
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
       KLEENE           GREEDY        STRUCTURAL
       THEOREM         ALGORITHM        HAZARD
          |               |               |
          v               v               v
     Regex → NFA      Activities       Pipeline
          |           Selection          Stages
          v               |               |
    Test String            v               v
          |            Selected        Resource
          v            Activities        Conflict
   ACCEPT / REJECT                         |
                                           v
                                         STALL

## Learning Outcomes
Theory of Computation
The project demonstrates:
- Regular Expressions
- Finite Automata
- Kleene's Theorem
- String acceptance

### Design and Analysis of Algorithms
The project demonstrates:
- Greedy strategy
- Activity Selection Problem
- Sorting by finishing time
- Step-by-step selection

### Computer Architecture
The project demonstrates:
- Instruction pipeline
- Pipeline stages
- Shared hardware resources
- Structural hazards
- Pipeline stalls

## Future Improvements
The project can be extended in the future by adding:
- Graphical visualization of the Finite Automaton.
- More Regular Expression operations.
- More Greedy Algorithm problems.
- Custom activity input.
- More processor instructions.
- Different types of pipeline hazards.
- Interactive pipeline diagrams.
- Performance comparison with and without stalls.
- Additional computer science algorithms.

## Conclusion
The Computer Science Concept Simulator combines three theoretical concepts into one practical application.
The project demonstrates:
1. Kleene's Theorem through Regular Expression and Finite Automaton processing.
2. Greedy Algorithm through the Activity Selection Problem.
3. Structural Hazards through processor pipeline simulation and stall handling.
By implementing these concepts as separate interactive modules, the project provides a simple and practical way to understand theoretical computer science concepts through an interactive application.
