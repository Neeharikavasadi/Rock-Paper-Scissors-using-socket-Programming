# 🪨📄✂️ Rock-Paper-Scissors using Socket Programming

A multiplayer Rock-Paper-Scissors game built using Python's socket programming and Pygame, allowing players to compete against each other in real-time.

## 🚀 Features and Functionality

- **Real-time Multiplayer Gameplay**: Two players can connect and play against each other.
- **User-friendly Interface**: Developed with Pygame, featuring intuitive buttons for selecting moves.
- **Game Logic**: Implements standard Rock-Paper-Scissors rules with win/loss determination.
- **Server-Client Architecture**: Utilizes Python's socket library to handle connections and game state.

##  🛠️ Technology Stack

- **Python**: The programming language used for development.
- **Pygame**: For creating the graphical user interface.
- **Socket Programming**: For networking between the client and server.
- **Pickle**: For serializing game state data.

## 📋 Prerequisites

- Python 3.x installed on your machine.
- Pygame library. You can install it via pip:

```bash
pip install pygame
```

## 📂Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/Neeharikavasadi/Rock-Paper-Scissors-using-socket-Programming.git
```

2. Navigate to the project directory:

```bash
cd Rock-Paper-Scissors-using-socket-Programming/CN-PROJECT
```

3. Start the server:

```bash
python server.py
```

4. In a new terminal, run the client:

```bash
python client.py
```

## 
Here's a more visually appealing and well-structured version of your README.md file:

markdown
Copy code
# 🪨📄✂️ Rock-Paper-Scissors using Socket Programming

A **real-time multiplayer Rock-Paper-Scissors game** built with Python's socket programming and Pygame. Compete with friends in a fun and interactive way!

---

## 🚀 Features

- **Real-time Multiplayer Gameplay**: Connect two players for a competitive match.
- **Intuitive User Interface**: Smooth and easy-to-use interface powered by Pygame.
- **Classic Game Logic**: Implements standard Rock-Paper-Scissors rules (Rock > Scissors > Paper > Rock).
- **Server-Client Architecture**: Leverages Python's socket programming for seamless networking.
- **State Management**: Uses Pickle for efficient game state serialization.

---

## 🛠️ Technology Stack

- **Programming Language**: Python
- **GUI Framework**: Pygame
- **Networking**: Socket Programming
- **Serialization**: Pickle

---

## 📋 Prerequisites

1. **Python 3.x** installed on your system.
2. Install **Pygame** using pip:

   ```bash
   pip install pygame
📂 Installation Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/Neeharikavasadi/Rock-Paper-Scissors-using-socket-Programming.git
Navigate to the project directory:

bash
Copy code
cd Rock-Paper-Scissors-using-socket-Programming/CN-PROJECT
Start the server:

bash
Copy code
python server.py
Run the client in a new terminal:

bash
Copy code
python client.py
🎮  Usage Guide

1. Start the server by running `server.py`. This will wait for players to connect.
2. Open two terminals (or two instances of the client).
3. In one terminal, run `client.py` to connect as Player 1.
4. In the other terminal, run `client.py` again to connect as Player 2.
5. Both players will see a menu screen. Click to start the game.
6. Choose your move (Rock, Paper, or Scissors) by clicking the corresponding button.
7. The results will be displayed after both players make their moves.

##🛠️ API Documentation

### Classes

- **🎮Game**: Manages game logic and state.
  - **Methods**:
    - `get_player_move(p)`: Returns the move of the specified player.
    - `play(player, move)`: Records the player's move.
    - `connected()`: Checks if the game is ready.
    - `bothWent()`: Checks if both players have made their move.
    - `winner()`: Determines the winner of the game.

- **🌐Network**: Handles client-server communication.
  - **Methods**:
    - `getP()`: Returns the player number.
    - `connect()`: Connects to the server.
    - `send(data)`: Sends data to the server and receives the response.

- **🖱️Button**: Represents a button in the game interface.
  - **Methods**:
    - `draw(win)`: Draws the button on the game window.
    - `click(pos)`: Checks if the button has been clicked.

## 🤝Contributing Guidelines 

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

