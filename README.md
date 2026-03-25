# 🐜 Langton’s Ants Simulation

This project implements a simulation of **Langton’s Ant**, a two-dimensional Turing machine that exhibits complex emergent behavior from simple rules. The simulation is extended to include **multiple ants and pheromone-based interactions**, making the system more dynamic and unpredictable.

---

## 🚀 Features

* Simulation of **two ants** moving on a 2D grid
* Implementation of standard **Langton’s Ant movement rules**
* **Pheromone-based behavior**:

  * Self-pheromone recognition (biased straight movement)
  * Cross-pheromone interaction (altered probabilities)
  * Pheromone replacement and decay over time
* Real-time visualization using a simulation interface

---

## ⚙️ Rules Implemented

### Basic Movement

* On **white cell**:

  * Turn 90° clockwise
  * Flip cell color
  * Move forward

* On **black cell**:

  * Turn 90° counter-clockwise
  * Flip cell color
  * Move forward

---

### Pheromone Behavior

* Ants leave **unique pheromones** on visited cells
* **Self-pheromone** → 80% chance to move straight
* **Other ant’s pheromone** → reduced straight movement probability
* **Pheromone decay** over time
* New pheromone **replaces existing ones** on the same cell

---

## 🛠️ Technologies Used

Python · Pygame · NumPy 

---

## 📌 Key Learnings

* Understanding **emergent behavior** from simple rule-based systems
* Implementing **probabilistic decision-making**
* Designing simulations with **object-oriented programming (OOP)**
* Handling **state transitions and time-based decay systems**

---

## 🔗 References

* Langton’s Ant (Wikipedia)
* Pygame Documentation

---

## 👨‍💻 Author

**Sidharth K**
2nd Year Undergraduate 

---

⭐ Feel free to explore and experiment with the simulation!
