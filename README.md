# Jana-Sevanam: multi-agent-govt-service-demo

An AI-powered "Agent of Agents" program prototype designed for the **Kerala State Government**. 

## 🚀 Overview
Jana-Sevanam is a voice-first, multi-agent system where a central **Orchestrator** coordinates between specialized departmental agents (Revenue, Education, KSEB) to fulfill citizen requests automatically.

## 📁 Repository Structure
- `app.py`: The functional Streamlit demo with voice integration.
- `BLUEPRINT.md`: Technical architecture and multi-agent logic.
- `STRATEGY.md`: Presentation slides for government stakeholders.
- `WALKTHROUGH.md`: Detailed explanation of the system and its features.
- `UI_MOCKUP.png`: Premium design mockup for the citizen mobile app.
- `DEMO_INTERFACE.png`: Screenshot of the live demo environment.

## 🛠️ How to Run
1. Install requirements:
   ```bash
   pip install streamlit
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

## 🎙️ Key Features
- **Voice Recognition**: Support for Malayalam and English queries using the Web Speech API.
- **Agent Orchestration**: Transparent hand-offs between departments (e.g., fetching a Revenue certificate for an Education scholarship).
- **Premium UI**: Kerala-themed aesthetics with professional branding.
