# Kerala Government Agentic AI Prototype

This is a prototype of a multi-agent system designed for government service automation in Kerala.

## Features
- **Multilingual Support:** Native Malayalam and English processing.
- **Orchestrator Agent:** Automated intent classification and routing.
- **Departmental Agents:** Specialized agents for Revenue and Tax.
- **Scalable Architecture:** Easily add new departments and workflows.

## How to Run
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main program:
   ```bash
   python3 main.py
   ```

## Project Structure
- `main.py`: Interactive CLI for testing the system.
- `agents/`: Contains specialized AI agents.
- `utils/`: NLP and language detection utilities.

## Future Roadmap
- Integration with Gemini 1.5 Pro for advanced reasoning.
- Database integration for real-time document retrieval (RAG).
- Web-based UI with voice support.
