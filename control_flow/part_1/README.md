## **PART 1: Treasure Island Adventure Game**

### If/Else Decision Making

Text-based adventure games use decision trees to create branching storylines. Each choice leads to different outcomes. This teaches sequential decision-making and if/else logic.

![Treasure Island flowchart](./img/treasure_island.png)

### Game Flow (Based on Flowchart)

```python
Welcome to Treasure Island!
Your mission is to find the treasure.

Decision 1: left or right? → If Left, continue. Otherwise → Fall into a hole. Game Over.

Decision 2 (if Left): swim or wait? → If Wait, continue. Otherwise → Attacked by trout. Game Over.

Decision 3 (if Wait): Which door? (red/blue/yellow)
  - If Red → Burned by fire. Game Over.
  - If Yellow → You Win!
  - Otherwise (Blue) → Eaten by beasts. Game Over.
```

### Assignment Requirements

**Level 1: Basic Structure**



Create a text-based adventure game that implements the above flowchart. Your program should:

1. Welcome the player and set the scene
2. Ask "Do you go left or right?"
    - If player chooses "right" or anything else → Print "You fall into a hole. Game Over."
    - If player chooses "left" → Continue to next decision
3. Ask "Do you swim or wait?"
    - If player chooses "swim" or anything else → Print "You are attacked by a trout. Game Over."
    - If player chooses "wait" → Continue to next decision
4. Ask "Which door do you choose? (red/blue/yellow)"
    - If player chooses "red" → Print "You are burned by fire. Game Over."
    - If player chooses "blue" → Print "You are eaten by beasts. Game Over."
    - If player chooses "yellow" → Print "You found the treasure! You Win!"
    - Otherwise → Print "Invalid choice. Game Over."
5. Make input case-insensitive (e.g., "LEFT", "Left", "left" all work)

### Sample Output

```python
=== WELCOME TO TREASURE ISLAND ===
Your mission is to find the treasure.

You are on a beach with a strange island ahead. You see a path splitting into two directions.

Do you go left or right? left
You go left. The path opens to a river.

Do you swim or wait? wait
You wait by the river. Suddenly, you hear mysterious sounds...

A cave reveals three doors: one glowing red, one deep blue, one bright yellow.
Which door do you choose? (red/blue/yellow) yellow

⭐ CONGRATULATIONS! ⭐
You found the treasure and escaped the island!
=== GAME OVER ===
```

### Sample Output (Game Over Scenario)

```python
=== WELCOME TO TREASURE ISLAND ===
Your mission is to find the treasure.

Do you go left or right? right
You fall into a hole!
Game Over. Try again!
```

### Hints

- Use `input()` to get player choices
- Use `.lower()` to convert input to lowercase for easier comparison
- Use simple `if-elif-else` statements (not nested yet)
- Use `print()` with descriptive messages for each outcome
- You can add ASCII art or emojis to make it more fun

---

# Solution:

[control_flow_part_1.ipynb](https://colab.research.google.com/drive/1PDf1Qggz6D_oNjGGke6APAsrYiZFYbet?usp=sharing)