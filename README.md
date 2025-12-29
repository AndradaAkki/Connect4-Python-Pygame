# 🔴 Connect 4 - Python & Pygame

A fully functional desktop implementation of the classic **Connect 4** strategy game. This project features a **Dual-Interface Design**, allowing the game to be played either via a command-line console or a graphical user interface (GUI) built with **Pygame**.

![Python](https://img.shields.io/badge/Language-Python_3.x-blue)
![GUI](https://img.shields.io/badge/GUI-Pygame-orange)
![Testing](https://img.shields.io/badge/Testing-Unittest-green)

## 📖 Overview
This application allows a human player to compete against a computer opponent. The project was architected to decouple the **Game Logic** from the **User Interface**, enabling two completely different rendering modes (Console vs. GUI) to run on the exact same backend engine.

## ✨ Key Features
* **Dual User Interfaces:**
    * **GUI Mode:** A responsive, mouse-driven interface built with `pygame` featuring real-time animations and visual feedback.
    * **Console Mode:** A text-based version for quick debugging and low-resource environments.
* **Smart Computer Opponent:** The AI employs a **Heuristic Strategy** that prioritizes:
    1.  **Winning:** Identifying immediate winning moves.
    2.  **Blocking:** Detecting and stopping the human player from winning on the next turn.
    3.  **Randomization:** Selecting valid moves when no critical threat is detected.
* **Robust Game Logic:**
    * Efficiently checks 6x7 matrices for vertical, horizontal, and diagonal win conditions.
    * Prevents invalid moves (e.g., placing chips in full columns) with custom exception handling.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Graphics Library:** `pygame` (for rendering the game board and handling mouse events).
* **Testing:** `unittest` (Comprehensive test suite for game logic).

## 📂 Project Structure
This project follows a modular design pattern:

| File | Responsibility |
| :--- | :--- |
| `Renderer.py` | **The GUI View.** Handles the Pygame window, drawing the grid/chips, and capturing mouse clicks. |
| `UI.py` | **The Console View.** Handles text input/output for the command-line version. |
| `game.py` | **The Controller.** Manages the flow of the game, switching turns, and triggering the AI. |
| `board.py` | **The Domain.** Manages the 6x7 matrix state and validates win conditions. |
| `player.py` | **Entity.** Defines player properties (Color, Name, Piece type). |
| `testing.py` | **QA.** Unit tests to verify logic correctness (e.g., ensuring the AI blocks wins). |

## 🚀 How to Run

### 1. Prerequisites
You need Python and Pygame installed:
```bash
pip install pygame numpy
