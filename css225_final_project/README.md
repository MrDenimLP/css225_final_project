# Detective's Investigation

## Overview
Detective's Investigation is an interactive Python-based text adventure that guides players through a murder mystery. Players collect evidence, interact with NPCs, and make decisions to solve the case.

---

## Table of Contents
1. [Where the Code is Hosted](#where-the-code-is-hosted)
2. [Languages and Technologies](#languages-and-technologies)
3. [System Requirements](#system-requirements)
4. [Coding and Naming Conventions](#coding-and-naming-conventions)
5. [How to Run, Build, and Deploy](#how-to-run-build-and-deploy)
6. [Architecture Overview](#architecture-overview)
7. [How to Start the Program](#how-to-start-the-program)

---

## Where the Code is Hosted
The source code for this project is hosted on **GitHub**. Clone the repository using:
```bash
git clone <repository_url>

---

## Languages and Technologies
- Programing Language: Python 3.8+
- Dependencies: None (uses Python's Standard Library)

---

## System Requirements
- Operating System: Cross-platform (Windows, macOS, Linux)
- Python Version: 3.8 or newer
- Hardware Requirements: Minimum 4GB RAM for smooth excution.

---

## Coding and Naming Conventions
- File Names: Use snake_case (e.g. main_name.py, global_database.py).
- Functions and Variables: Descriptive names in snake_case (e.g. start_game, player_name).
- Global Variables: Centralized in global_database.py.
- Commenting: Inline and comments are used for clarity and maintainability.

---

## How to Run, Build, and Deploy
1. Clone the Repository:
```bash
git clone <repository_url>
cd <repository_url>

2. Verify Python Installation: Ensure Python 3.8+ is installed by running:
```bash
python --version

If not installed, download Python from python.org.

3. Run the Game: From the project directory, execute either:
```bash
python main_game.py

or

```bash
python3 main_game.py

---

## Architecture Overview
- Main Entry Points:
main_game.py initializes the game and starts Chapter 1.

- Chapters:
Each chapter (chapter1.py to chapter5.py) is a self-contained module, focusing on a specific stage of the narrative.

- Global Utilities:
global_database.py contains shared resources such as NPC name lists, random weapon selectors, and city names.

- Player Management:
player.py includes the Player class for tracking player progress and evidence collection.

- Loading Effects:
loading.py provides visual feedback during transitions with a progress bar.

---

## How to Start the Program
To start the game:
1. Open a terminal or command prompt.
2. Navigate to the project directory using the 'cd' command.
3. Run either of the following commands:
```bash
python main_game.py

or

```bash
python3 main_game.py

4. Enter your name when prompted, and the game begins.

---

## Contribution Guidelines
Contributions to improve or expand the game are welcome. Follow these steps:
1. Fork the repository.
2. Create a feature branch: git checkout -b feature-name
3. Commit your changes: git commit -m "Description of changes"
4. Push to the branch: git push origin feature-name
5. Open a pull request.

---

## License
This project is licensed under the MIT License.

