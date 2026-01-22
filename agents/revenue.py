import json
import os
from typing import Dict

class RevenueAgent:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'services.json')
        with open(self.data_path, 'r') as f:
            self.knowledge = json.load(f)['revenue']

    def process_task(self, task_description: str, lang: str = "english") -> str:
        """
        Specialized logic for revenue department using real data.
        """
        if "possession" in task_description.lower() or "കൈവശാവകാശ" in task_description:
            service = self.knowledge['possession_certificate']
            if lang == "malayalam":
                reqs = "\n- ".join(service['requirements_en']) # In real app, these would be translated
                return f"കൈവശാവകാശ സർട്ടിഫിക്കറ്റിനായി (Possession Certificate) അപേക്ഷിക്കുന്നതിന് താഴെ പറയുന്ന രേഖകൾ ആവശ്യമാണ്:\n- {reqs}\n\nഈ സേവനം ഇ-ഡിസ്ട്രിക്റ്റ് പോർട്ടൽ വഴി ലഭ്യമാണ്."
            else:
                reqs = "\n- ".join(service['requirements_en'])
                return f"To apply for a Possession Certificate, you need the following documents:\n- {reqs}\n\nThe process typically takes about 7 days after village officer verification."
        
        if lang == "malayalam":
            return "റവന്യൂ വിഭാഗം നിങ്ങളുടെ അപേക്ഷ പരിശോധിച്ച് വരികയാണ്. ഉടൻ തീരുമാനം അറിയിക്കുന്നതാണ്."
        return "The Revenue department is processing your request. We are verifying land records."

    def get_required_data(self) -> Dict[str, str]:
        return {
            "Bhoomi ID": "Required for land record verification",
            "Aadhar": "Required for identity verification"
        }
