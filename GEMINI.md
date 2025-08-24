# GEMINI.md - Project Context

## 1. User Information
- **Operating System:** linux
- **Working Directory:** `/home/genr/Documents/code/python/python-algorithms`
- **Date:** Saturday, August 9, 2025

## 2. Project Overview
The user's goal is to create a comprehensive, practical training plan for Python technical interviews, aiming for a "powerful level". The project is structured around **problem-solving techniques**, providing a pattern-based approach to interview preparation. It includes five main components for each topic:
1.  **Theory:** Detailed explanations of concepts and techniques.
2.  **Challenges:** Practical coding exercises with tests.
3.  **Solutions:** Optimal solutions for the challenges.
4.  **Exams:** Short evaluations to reinforce understanding.
5.  **Cheatsheets:** Concise summaries for quick review.

Additionally, the project contains a dynamic `index.html` for easy navigation and a guide on Prompt Engineering.

## 3. File Structure
The project has been restructured to focus on techniques. The final structure is as follows:

```
/home/genr/Documents/code/python/python-algorithms/
├── GEMINI.md
├── index.html
├── prompt_engineering/
│   └── prompt_engineering_guide.md
├── training/
│   ├── fundamentals/
│   │   ├── 00_big_o_notation.md
│   │   └── 00_python_fundamentals.md
│   ├── techniques/
│   │   ├── 01_two_pointers.md
│   │   ├── ... (all 17 technique theory files)
│   ├── challenges/
│   │   ├── 01_a_valid_palindrome.py
│   │   ├── ... (all challenge files)
│   └── solutions/
│       └── (Contains corresponding solution files for all challenges)
├── exams/
│   ├── 00_exam_big_o.md
│   ├── ... (all exam files)
│   └── solutions/
│       └── (Contains corresponding solution files for all exams)
└── cheatsheets/
    ├── 00_big_o_cheatsheet.md
    └── ... (and so on for all topics)
```

## 4. Key Logic & File Descriptions
- **`training/fundamentals/`**: Contains the prerequisite theory for the entire course (Big O, Python basics).
- **`training/techniques/`**: The core of the plan. Each file explains a specific problem-solving pattern (e.g., Sliding Window, Backtracking).
- **`training/challenges/`**: Python files for each problem, containing a docstring with instructions and self-verifying tests.
- **`training/solutions/`**: Optimal solutions for each challenge.
- **`exams/`**: Short quizzes to test understanding of each technique.
- **`cheatsheets/`**: Condensed summaries for quick review.
- **`index.html`**: A dynamic, single-page web interface to navigate all training materials, rendering Markdown and code with syntax highlighting.
- **`prompt_engineering/`**: A guide on effective prompting for LLMs in a software development context.

## 5. User Preferences & Goals
- The primary goal is to achieve a "powerful level" in Python for technical interviews by mastering problem-solving patterns.
- All created documents must be in English.
- The user prefers an iterative development process, where feedback and discussions lead to a more refined and complete final product.

## 6. Recent Activity
- Refocused the entire training plan to be centered around **problem-solving techniques** rather than just data structures.
- Completed a comprehensive list of 17 essential techniques, from foundational patterns to advanced algorithms.
- Generated all associated materials (theory, challenges, solutions, exams, cheatsheets) for new techniques like Linked List Manipulation, Intervals, Tries, Divide and Conquer, Advanced Graphs, and Bit Manipulation.
- Created and debugged a dynamic `index.html` file that serves as a complete navigator for the project, capable of rendering Markdown and Python files with syntax highlighting.
- The last action was to update this `GEMINI.md` file before creating a Git checkpoint.