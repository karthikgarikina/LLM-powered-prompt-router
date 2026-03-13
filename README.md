# LLM-Powered Prompt Router

A Python-based AI service that intelligently routes user requests to
specialized AI personas using intent classification.\
This project demonstrates a practical **LLM system design pattern** used
in real-world AI applications: **Intent Detection → Prompt Routing →
Expert Response Generation**.

------------------------------------------------------------------------

## Project Objective
Instead of using one large prompt for every task, this system first
**classifies the user's intent** and then routes the request to a
**specialized AI persona** designed for that task.

This improves: - Response accuracy - Prompt clarity - System
scalability - Cost efficiency

------------------------------------------------------------------------

## System Architecture

User Message\
→ Intent Classifier (LLM #1)\
→ Router selects Expert Prompt\
→ Response Generator (LLM #2)\
→ Final Response Returned\
→ Request Logged to JSONL file

------------------------------------------------------------------------

## Features

-   Intent classification using LLM
-   Prompt routing to specialized AI personas
-   Structured JSON parsing from model output
-   Graceful fallback for malformed responses
-   Request logging for observability
-   Modular Python architecture

------------------------------------------------------------------------

## Expert Personas

The system includes four specialized AI personas:

### Code Expert

Provides production-quality code with best practices and error handling.

### Data Analyst

Explains numerical patterns, statistical insights, and suggests data
visualizations.

### Writing Coach

Gives feedback on clarity, tone, and structure without rewriting the
text.

### Career Advisor

Provides actionable career advice and professional guidance.

------------------------------------------------------------------------

## Project Structure

    LLM-powered-prompt-router
    │
    ├── main.py
    ├── classifier.py
    ├── router.py
    ├── prompts.py
    ├── logger.py
    ├── requirements.txt
    ├── route_log.jsonl
    └── .env

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

    git https://github.com/karthikgarikina/LLM-powered-prompt-router
    cd LLM-powered-prompt-router

### 2. Add API key

Create `.env` file:

    GROQ_API_KEY=your_api_key_here

### 3. Run docker

    docker compose run --rm prompt-router    

------------------------------------------------------------------------

## Running the Application

Start the CLI interface:

Example:

    You: how do i sort a list in python

    Intent: code
    Confidence: 0.94

    Response:
    Use Python's built-in sort() method...

Exit the program:

    exit

------------------------------------------------------------------------

## Logging

Every request is logged to:

    route_log.jsonl

Example log entry:

``` json
{
  "intent": "code",
  "confidence": 0.91,
  "user_message": "how do i sort a list in python",
  "final_response": "Use Python's built-in sort() method..."
}
```

This enables **observability and debugging of routing decisions**.

------------------------------------------------------------------------
## Video demo
https://www.youtube.com/watch?v=sCYpETsqmeI

----------------------------------------------------

## Example Test Inputs

You can test the system using the following prompts:

-   how do i sort a list of objects in python?
-   explain this sql query
-   this paragraph sounds awkward
-   i'm preparing for a job interview
-   what's the average of these numbers: 12, 45, 23, 67
-   help me make this better
-   hey
-   how do i structure a cover letter?
-   my boss says my writing is too verbose

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Groq LLM API
-   python-dotenv
-   JSON / JSONL logging

------------------------------------------------------------------------

## Key Concepts Demonstrated

-   Prompt engineering
-   Intent classification with LLMs
-   Multi-prompt routing architecture
-   Structured LLM output handling
-   Fault-tolerant JSON parsing
-   Observability in AI systems

------------------------------------------------------------------------

## Future Improvements

-   Confidence threshold handling
-   Web API using FastAPI
-   Web UI interface
-   Support for additional expert personas
-   Analytics dashboard for router logs

------------------------------------------------------------------------

