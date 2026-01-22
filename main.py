from agents.orchestrator import OrchestratorAgent
from agents.revenue import RevenueAgent
from agents.tax import TaxAgent

def main():
    print("=== Kerala Government Agentic AI Service Prototype ===")
    print("Type your query in Malayalam or English (type 'exit' to quit)")
    
    orchestrator = OrchestratorAgent()
    revenue_agent = RevenueAgent()
    tax_agent = TaxAgent()
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
            
        # 1. Orchestrate
        routing = orchestrator.route_request(user_input)
        dept = routing["target_department"]
        lang = routing["detected_language"]
        
        print(f"[*] System: Routing to {dept.upper()} ({lang})")
        
        # 2. Delegate
        if dept == "revenue":
            response = revenue_agent.process_task(user_input, lang)
        elif dept == "tax":
            response = tax_agent.process_task(user_input, lang)
        else:
            response = orchestrator.process(user_input)
            
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
