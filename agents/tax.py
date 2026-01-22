import json
import os

class TaxAgent:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'services.json')
        with open(self.data_path, 'r') as f:
            self.knowledge = json.load(f)['tax']

    def process_task(self, task_description: str, lang: str = "english") -> str:
        """
        Specialized logic for tax department.
        """
        if "property" in task_description.lower() or "വസ്തു" in task_description:
            service = self.knowledge['property_tax']
            formula = service['calculation_formula']
            if lang == "malayalam":
                return f"വസ്തു നികുതി കണക്കാക്കുന്ന രീതി: {formula}. അപേക്ഷിക്കുന്നതിന് വാർഡ് നമ്പർ, ഡോർ നമ്പർ എന്നിവ ആവശ്യമാണ്."
            else:
                return f"Property tax is calculated as: {formula}. You will need your Ward and Door numbers to proceed."
        if lang == "malayalam":
            return "നികുതി വകുപ്പ് നിങ്ങളുടെ അപേക്ഷ സ്വീകരിച്ചിരിക്കുന്നു. കുടിശ്ശിക പരിശോധിക്കുകയാണ്."
        return "The Tax department has received your request. We are checking for outstanding dues."

    def calculate_tax(self, property_area: float, zone: str) -> float:
        # Placeholder calculation
        rate = 10.0 if zone == "urban" else 5.0
        return property_area * rate
