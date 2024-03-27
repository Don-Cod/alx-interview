# Lockboxes

![Lockboxes Illustration](https://upload.wikimedia.org/wikipedia/commons/6/63/Padlock_icon_black.svg)

Welcome to the Lockboxes repository! This repository contains solutions and explanations for the Lockboxes problem, a classic algorithmic challenge frequently encountered in coding interviews.

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Solution Approach](#solution-approach)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Lockboxes problem is a common algorithmic challenge where you're given a set of locked boxes, each containing keys to other boxes. The goal is to determine whether you can unlock all the boxes by iterating through the keys.

## Problem Statement
Given a list of lists where each list represents a box and contains keys to other boxes, implement a function `canUnlockAll(boxes)` to determine if all boxes can be unlocked. The function should return `True` if all boxes can be unlocked, otherwise `False`.

## Solution Approach
The solution to the Lockboxes problem typically involves using breadth-first search (BFS) or depth-first search (DFS) algorithms to explore the relationships between the boxes and their keys. By maintaining a set of visited boxes and iteratively traversing through the keys, we can determine if all boxes are accessible.

## Usage
To use the Lockboxes solution provided in this repository:
1. Clone this repository to your local machine:
	git clone https://github.com/Don-Cod/alx-interview.git
2. Navigate to the `0x01-lockboxes` directory:
	cd alx-interview/0x01-lockboxes
3. Run the Python script:
	python main.py
4. Follow the on-screen instructions to see the solution in action.

## Contributing
Contributions to this repository are welcome! If you have any improvements, suggestions, or bug fixes, feel free to open an issue or create a pull request. Let's work together to make this resource even better.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Explore the Lockboxes problem, refine your algorithmic skills, and unlock the potential within you! If you find this repository helpful, don't forget to ⭐️ star it!

