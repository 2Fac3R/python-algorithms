# A Guide to Prompt Engineering for Software Development

## 1. What is Prompt Engineering?

**Prompt Engineering** is the art and science of designing effective inputs (prompts) for a Large Language Model (LLM) like Gemini or ChatGPT to generate the most accurate, relevant, and useful output possible.

**Analogy:** Think of the LLM as an extremely fast but context-free junior programmer. Your role as a "prompt engineer" is to be an excellent tech lead: you must provide clear, specific, and context-aware instructions to get high-quality work.

The golden rule is: *"Garbage In, Garbage Out"*. A vague or poor prompt will produce a vague or poor result.

---

## 2. Fundamental Principles for LLMs (General)

These principles apply to any modern LLM.

#### a. Be Specific and Clear
Avoid ambiguity. The more precise you are, the better the result.

- **Bad:** `"Fix this code."`
- **Good:** `"My Python function throws a `TypeError` on line 15 when the `user` variable is `None`. Refactor the function to handle this case gracefully and return `None` if the user does not exist."`

#### b. Provide Context
The model doesn't know your project. Give it the necessary information to understand the problem.

- **Bad:** `"Create a function that validates an email."`
- **Good:** `"I'm using Python 3.10. I need a function called `is_valid_email` that takes a string and returns `True` if it matches the standard email format (user@domain.com) and `False` otherwise. I don't need to use external libraries, only the `re` module for regular expressions."`

#### c. Define a Persona or Role
Tell the model how you want it to act. This adjusts its tone, style, and the focus of its response.

- **Example:** `"Act as a senior Go developer specializing in concurrency. Review my following code and suggest improvements to avoid race conditions."`
- **Example:** `"Act as a cybersecurity expert. Analyze this login function and point out potential security vulnerabilities."`

#### d. Use Examples (Few-Shot Prompting)
Show the model exactly what you want. This is one of the most powerful techniques.

- **Example:** `"Convert the following code comments to a standard Python docstring format. For example, if I give you `# Get user by ID`, you should return `"""Get user by ID."""`. Now, convert the following: ..."`

#### e. Break Down Complex Tasks
Don't ask the model to build an entire application at once. Divide it into logical, manageable steps.

- **Bad:** `"Create a REST API for a blog."`
- **Good:** `"First, define a SQLAlchemy model in Python for a `Post` table with fields for `id`, `title`, `content`, and `created_at`. Then, create an API route with FastAPI to get all posts (`GET /posts`)."`

#### f. Iterate and Refine
Your first prompt doesn't have to be perfect. Treat the interaction as a conversation. If the output isn't what you expected, tell the model why and ask it to correct its response.

- **Example:** `"The code you generated works, but it uses a `for` loop. Can you refactor it to use a list comprehension, which is more idiomatic in Python?"`

---

## 3. Specific Guide for Gemini CLI in Software Development

Using a CLI tool like this, integrated with your file system and terminal, opens up new possibilities.

#### a. Leverage File Context (`@`)
This is the most powerful feature. Instead of copying and pasting code, reference files directly.

- **Bad:** `"Review this code: class User... (pastes 50 lines)"`
- **Good:** `"Analyze my solution for the palindrome challenge in `@training/challenges/01_a_valid_palindrome.py` and suggest efficiency improvements."`

#### b. Use Precise Action Verbs
Be direct about the action you want to perform. This helps the model choose the correct tool (`write_file`, `replace`, `run_shell_command`, etc.).

- **Useful Verbs:** `Create`, `write`, `replace`, `add`, `delete`, `run`, `read`, `list`.
- **Example:** `"Replace the contents of `@config.json` with the following text: {...}"`
- **Example:** `"Run `npm install` to install the dependencies listed in `@package.json`."`

#### c. Build Iteratively
Use the conversation to build upon what has already been done.

- **Example:** `"Ok, the function you just created in `@utils.py` is correct. Now, add type hinting to its parameters and return value."`
- **Example:** `"Based on the folder structure we created, now generate a `README.md` file in the project root."`

#### d. Combine Analysis and Action
Use the model's ability to reason and then act.

- **Example:** `"Analyze the Dockerfile at `@Dockerfile` to determine which port the application exposes. Then, run `docker run` to start the container, mapping that port to local port 8080."`

#### e. Be Explicit About Location
Even though the model has context, being explicit about file paths prevents ambiguity.

- **Good:** `"Create a new exam for the graphs topic at `exams/11_exam_graphs.md`."`
- **Acceptable but less clear:** `"Create the next graph exam."`

---

## 4. Best Practices Summary Table

| Principle | Bad Prompt (Example) | Good Prompt (Example) |
|:---|:---|:---|
| **Specificity** | `"It doesn't work."` | `"The `get_user` function returns a `KeyError` when the ID does not exist."` |
| **Context** | `"Write a test."` | `"Using the `pytest` framework, write a test for the `add(a, b)` function in `@utils.py` that verifies the case for negative numbers."` |
| **Persona** | `"How do I make this better?"` | `"Act as a Python performance expert. How can I optimize this function to use less memory?"` |
| **Decomposition** | `"Make me a TODO app."` | `"First, create the HTML with an input and a `<ul>` list. Then, write the JavaScript to add an `<li>` to the list when a button is pressed."` |
| **Referencing (CLI)** | `(Pastes 50 lines of code)` | `"Refactor the `DataManager` class in `@data/manager.py` to follow the Singleton pattern."` |