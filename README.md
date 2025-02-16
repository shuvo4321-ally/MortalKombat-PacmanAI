

# 🎮 AI Game Decision-Making with Alpha-Beta Pruning  

This project implements **game AI decision-making** using the **alpha-beta pruning algorithm** for two different scenarios:  
1️⃣ **Mortal Kombat battle simulation** (Scorpion vs. Sub-Zero).  
2️⃣ **Pacman decision tree with a “dark magic” strategy** for optimal decision-making.  



## 🚀 Features  

![Image](https://github.com/user-attachments/assets/f4f559be-311a-48d8-b173-f6bb6ed675d1)
### **🔹 Part 1: Mortal Kombat Battle Simulation**  
- Simulates a **3-round turn-based battle** between **Scorpion** and **Sub-Zero**.  
- Uses **alpha-beta pruning** to determine the winner of each round.  
- Generates a **game decision tree (depth = 5, branching factor = 2)**.  
- The starting player is determined via **user input (0 = Scorpion, 1 = Sub-Zero)**.  
- Outputs:  
  - **Round-by-round winners**  
  - **Final game winner**  

**Example:**  
```
Enter starting player (0 for Scorpion, 1 for Sub-Zero): 0
Game Winner: Scorpion
Total Rounds Played: 3
Winner of Round 1: Sub-Zero
Winner of Round 2: Scorpion
Winner of Round 3: Scorpion
```
![Image](https://github.com/user-attachments/assets/6d32b3e9-92cd-4b5e-9883-4ca1d03675c7)
### **🔹 Part 2: Pacman Decision Tree with Dark Magic**  
- Simulates a **Pacman vs. Ghost** game using a **decision tree**.  
- Uses **alpha-beta pruning** to determine the best path for Pacman.  
- Introduces **"dark magic"**, allowing Pacman to control the Ghost’s move **at a cost (c)**.  
- Compares **minimax values with and without dark magic** to decide if using it is beneficial.  
- Outputs the **best path and final score** based on different cost values.  

**Example:**  
```
Using dark magic is advantageous. Best path: Right, Value: 5
Not using dark magic is better. Value: 3
```
## 🛠️ Technologies Used  
- **Python**  
- **Alpha-Beta Pruning Algorithm**  
- **Minimax Decision-Making**  
- **Game Tree Search**  

## 🎮 How to Run  
1️⃣ **Mortal Kombat Battle Simulation**  
- Run the script and **enter the starting player** (`0` for Scorpion, `1` for Sub-Zero).  
- The game will simulate **three rounds** and display the winner.  

2️⃣ **Pacman Dark Magic Strategy**  
- Call `pacman_game(c)` with different **cost values (c)**.  
- The program will analyze the **best decision** and print whether **using dark magic** is beneficial.  

## 🔥 Future Improvements  
- Expand the **game decision tree** with more strategies.  
- Visualize the **alpha-beta pruning process**.  
- Add **more complex game scenarios** for testing.  

---

### 🔹 **Suggested Repository Names**  
1. **AlphaBeta-GameAI**  
2. **GameTree-DecisionAI**  
3. **MortalPac-AlphaBeta**  
4. **BattleAndMaze-AI**  
5. **AI-Strategy-Games**  


