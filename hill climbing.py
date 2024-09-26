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
