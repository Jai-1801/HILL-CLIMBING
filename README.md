<h1>Ex 5 : Implement Simple Hill Climbing Algorithm</h1> 
<h3>Name:  JAI SURYA R        </h3>
<h3>Register Number: 212223230084      </h3>
<H3>Aim:</H3>
<p>Implement Simple Hill Climbing Algorithm and Generate a String by Mutating a Single Character at each iteration </p>
<h2> Theory: </h2>
<p>Hill climbing is a variant of Generate and test in which feedback from test procedure is used to help the generator decide which direction to move in search space.
Feedback is provided in terms of heuristic function
</p>


<h2>Algorithm:</h2>
<p>
<ol>
 <li> Evaluate the initial state.If it is a goal state then return it and quit. Otherwise, continue with initial state as current state.</li> 
<li>Loop until a solution is found or there are no new operators left to be applied in current state:
<ul><li>Select an operator that has not yet been applied to the current state and apply it to produce a new state</li>
<li>Evaluate the new state:
  <ul>
<li>if it is a goal state, then return it and quit</li>
<li>if it is not a goal state but better than current state then make new state as current state</li>
<li>if it is not better than current state then continue in the loop</li>
    </ul>
</li>
</ul>
</li>
</ol>

</p>
<hr>
<h3> Steps Applied:</h3>
<h3>Step-1</h3>
<p> Generate Random String of the length equal to the given String</p>
<h3>Step-2</h3>
<p>Mutate the randomized string each character at a time</p>
<h3>Step-3</h3>
<p> Evaluate the fitness function or Heuristic Function</p>
<h3>Step-4:</h3>
<p> Lopp Step -2 and Step-3  until we achieve the score to be Zero to achieve Global Minima.</p>

## PROGRAM:
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LENGTH 100

// Function to calculate the fitness score (number of different characters)
int calculate_fitness(char* goal, char* current) {
    int score = 0;
    for (int i = 0; i < strlen(goal); i++) {
        if (goal[i] != current[i]) {
            score++;
        }
    }
    return score;
}

// Function to mutate a random character in the string
void mutate_string(char* current, int length) {
    int random_index = rand() % length;
    // Generate a random ASCII character (space or alphabet)
    char random_char = (rand() % 27) + 'a';  // 26 letters + space
    if (random_char == 'a' + 26) {
        random_char = ' ';  // Replace 27th character with space
    }
    current[random_index] = random_char;
}

// Function to copy one string to another
void copy_string(char* source, char* destination, int length) {
    for (int i = 0; i < length; i++) {
        destination[i] = source[i];
    }
    destination[length] = '\0';
}

// Hill Climbing Algorithm
void hill_climbing(char* goal) {
    int length = strlen(goal);
    char current[MAX_LENGTH];
    char new_string[MAX_LENGTH];
    
    // Generate a random initial string
    for (int i = 0; i < length; i++) {
        current[i] = (rand() % 27) + 'a';  // random letter or space
        if (current[i] == 'a' + 26) {
            current[i] = ' ';
        }
    }
    current[length] = '\0';
    
    int current_fitness = calculate_fitness(goal, current);
    
    printf("Initial: %s | Score: %d\n", current, current_fitness);
    
    int iterations = 0;
    // Loop until the goal is achieved (fitness score is 0)
    while (current_fitness > 0) {
        copy_string(current, new_string, length);
        mutate_string(new_string, length);
        
        int new_fitness = calculate_fitness(goal, new_string);
        
        // If the new string has better fitness, update the current string
        if (new_fitness < current_fitness) {
            copy_string(new_string, current, length);
            current_fitness = new_fitness;
        }
        
        // Print the progress
        printf("Iteration %d: %s | Score: %d\n", iterations, current, current_fitness);
        iterations++;
    }

    printf("Goal achieved in %d iterations: %s\n", iterations, current);
}

// Main function
int main() {
    srand(time(0));  // Initialize random seed
    
    char goal[MAX_LENGTH];
    
    fgets(goal, MAX_LENGTH, stdin);
    goal[strcspn(goal, "\n")] = 0;  // Remove newline character from input
    
    hill_climbing(goal);
    
    return 0;
}
```

<hr>
<h2>Sample Input and Output</h2>
<h2>Sample String:</h2> Artificial Intelligence
<h2>Output:</h2>
Score: 643  Solution :  8RzF:oG ]%;CPORRMe!zGvk<br>
Score: 609  Solution :  8RzF:oG ]%;CPqRRMe!zGvk<br>
Score: 604  Solution :  8RzF:oG ]%;CPqRRMe!zGqk<br>
Score: 594  Solution :  8RzF:oG ]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
....................................................<br>
..................................................<br>
................................................<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 0  Solution :  Artificial Intelligence<br>

## RESULT:
 Thus the Simple Hill Climb Algorithm Implemented successfully.
