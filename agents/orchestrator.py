import os
from typing import Dict
from utils.nlp_engine import detect_language

class OrchestratorAgent:
    def __init__(self):
        self.departments = {
            "revenue": "Handles property records, land ceiling, and certificates.",
            "tax": "Manages property tax, professional tax, and payments.",
            "documentation": "Assists with deed registration and certificates.",
            "administration": "Handles general inquiries and grievances."
        }
        # In a real implementation, we would initialize the LLM here.
        # self.llm = ...

    def route_request(self, user_input: str) -> Dict[str, str]:
        """
        Routes the user input to the correct department agent.
        Includes language detection and context understanding.
        """
        lang = detect_language(user_input)
        
        # This is a placeholder for LLM-based intent classification.
        # The LLM would be prompted with the user input and the list of departments.
        
        # Mocking the classification for demonstration:
        lower_input = user_input.lower()
        target_dept = "administration" # Default
        
        if any(kw in lower_input for kw in ["revenue", "land", "ഭൂമി", "രേഖകൾ", "possession", "കൈവശാവകാശം"]):
            target_dept = "revenue"
        elif any(kw in lower_input for kw in ["tax", "നികുതി", "പണം", "taxation"]):
            target_dept = "tax"
        elif any(kw in lower_input for kw in ["document", "രജിസ്ട്രേഷൻ", "സർട്ടിഫിക്കറ്റ്", "certificate"]):
            target_dept = "documentation"
            
        return {
            "detected_language": lang,
            "target_department": target_dept,
            "routing_reason": f"Classified as {target_dept} based on keyword mapping (Mocked LLM behavior)."
        }

    def process(self, user_input: str) -> str:
        routing = self.route_request(user_input)
        dept = routing["target_department"]
        lang = routing["detected_language"]
        
        if lang == "malayalam":
            return f"നിങ്ങളുടെ അഭ്യർത്ഥന {dept} വിഭാഗത്തിലേക്ക് മാറ്റിയിരിക്കുന്നു. അവർ നിങ്ങളെ സഹായിക്കും."
        else:
            return f"Your request has been routed to the {dept} department. They will assist you."

if __name__ == "__main__":
    orchestrator = OrchestratorAgent()
    # Test English
    print(orchestrator.process("I want to pay my property tax"))
    # Test Malayalam
    print(orchestrator.process("എനിക്ക് ഭൂമിയുടെ രേഖകൾ വേണം"))
