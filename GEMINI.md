# GEMINI.md - Project Context

## 1. User Information
- **Operating System:** linux
- **Working Directory:** `/home/genr/Documents/code/python/python-algorithms`
- **Date:** Monday, August 25, 2025

## 2. Project Overview
The user's goal is to create a comprehensive, practical training plan for Python technical interviews, aiming for a "powerful level". The project is structured around **problem-solving techniques, design patterns, and cloud certification preparation**, providing a pattern-based approach to interview preparation. It includes four main modules: Fundamentals, Problem-Solving Techniques, Design Patterns, and AWS Cloud Practitioner.

Each topic within these modules contains up to five components:
1.  **Theory:** Detailed explanations of concepts.
2.  **Challenges/Hands-On Labs:** Practical exercises or guided labs.
3.  **Solutions:** Optimal solutions for challenges or explanations for labs.
4.  **Exams:** Short evaluations or practice questions.
5.  **Cheatsheets:** Concise summaries for quick review.

Additionally, the project contains a dynamic `index.html` for easy navigation and a guide on Prompt Engineering.

## 3. File Structure
The project has been restructured to focus on techniques, patterns, and cloud preparation. The final structure is as follows:

```
/home/genr/Documents/code/python/python-algorithms/
├── GEMINI.md
├── index.html
├── prompt_engineering/
│   └── prompt_engineering_guide.md
├── training/
│   ├── fundamentals/
│   ├── techniques/
│   ├── challenges/
│   └── solutions/
├── design_patterns/
│   ├── theory/
│   ├── challenges/
│   ├── solutions/
│   ├── exams/
│   └── cheatsheets/
├── aws_cloud_practitioner/
│   ├── 00_introduction_to_aws.md
│   ├── 01_domain_cloud_concepts/
│   ├── 02_domain_security_and_compliance/
│   ├── 03_domain_cloud_technology/
│   ├── 04_domain_billing_and_support/
│   ├── 05_practice_exam_1.md
│   ├── 06_practice_exam_2.md
│   └── 07_practice_exam_3.md
├── js/
│   ├── content_fundamentals.json
│   ├── content_techniques.json
│   ├── content_design_patterns.json
│   └── content_aws.json
├── exams/
│   ├── ... (all exam files)
│   └── solutions/
└── cheatsheets/
    └── ... (and so on for all topics)
```

## 4. Key Logic & File Descriptions
- **`training/`**: Contains the Fundamentals and Problem-Solving Techniques modules.
- **`design_patterns/`**: Contains the Design Patterns module, with theory, challenges, solutions, exams, and cheatsheets for 24 patterns.
- **`aws_cloud_practitioner/`**: Contains the AWS Cloud Practitioner study plan, structured by exam domains, including theory, key services, hands-on labs, exam questions, and cheatsheets.
- **`js/`**: Contains JSON data files for each module, used to dynamically build the `index.html` sidebar.
- **`index.html`**: A dynamic, single-page web interface that loads data from JSON files to navigate all training materials, rendering Markdown and Python files with syntax highlighting.
- **`prompt_engineering/`**: A guide on effective prompting for LLMs in a software development context.

## 5. User Preferences & Goals
- The primary goal is to achieve a "powerful level" in Python for technical interviews by mastering problem-solving patterns and design principles.
- All created documents must be in English.
- The user prefers an iterative development process.

## 6. Recent Activity
- Added a comprehensive **AWS Cloud Practitioner** study plan, including domain-specific content and practice exams.
- Refactored the `index.html` navigator to load all module data from external JSON files, improving modularity and maintainability.
- Fixed issues with exam solution display and formatting in the AWS section.
- Updated `README.md` and `GEMINI.md` to reflect the new content and structural changes.
- Created a Git checkpoint for the new module.
- The last action was to update this `GEMINI.md` file.