import streamlit as st
import time
import json
import streamlit.components.v1 as components

# Simulation of Department Agent Class with Malayalam support
class DepartmentAgent:
    def __init__(self, name, malayalam_name, description, capabilities):
        self.name = name
        self.malayalam_name = malayalam_name
        self.description = description
        self.capabilities = capabilities

    def process_query(self, query):
        st.write(f"🔍 **{self.malayalam_name} ({self.name})** ഏജന്റ് അപേക്ഷ പരിശോധിക്കുന്നു...")
        time.sleep(1)
        if any(w in query.lower() for w in ["bill", "electricity", "വൈദ്യുതി"]):
            return {
                "status": "success",
                "message": "നിങ്ങളുടെ ജനുവരി മാസത്തെ വൈദ്യുതി ബില്ല് ₹1,450 ആണ്. ഇത് അടയ്ക്കണോ? (Your Jan bill is ₹1,450. Pay now?)",
                "action_required": "payment_confirmation"
            }
        elif any(w in query.lower() for w in ["scholarship", "വിദ്യ", "സ്കോളർഷിപ്പ്", "പഠനം"]):
            return {
                "status": "info",
                "message": "സ്കോളർഷിപ്പിന് അപേക്ഷിക്കാൻ വരുമാന സർട്ടിഫിക്കറ്റ് ആവശ്യമാണ്. (Need Income Certificate from Revenue Dept for Scholarship.)",
                "sub_task": "request_income_certificate"
            }
        elif any(w in query.lower() for w in ["income", "revenue", "വരുമാനം", "റവന്യൂ"]):
            return {
                "status": "success",
                "message": "നിങ്ങളുടെ വരുമാന സർട്ടിഫിക്കറ്റ് (ID: KER-REV-551) തയ്യാറായിക്കഴിഞ്ഞു. (Income Certificate KER-REV-551 generated.)",
                "data": {"certificate_id": "KER-REV-551"}
            }
        else:
            return {"status": "error", "message": "ക്ഷമിക്കണം, ഈ അപേക്ഷ കൈകാര്യം ചെയ്യാൻ എനിക്ക് കൂടുതൽ വിവരങ്ങൾ വേണം."}

class Orchestrator:
    def __init__(self):
        self.agents = {
            "Revenue": DepartmentAgent("Revenue", "റവന്യൂ", "Land records and certificates", ["income_cert"]),
            "Education": DepartmentAgent("Education", "വിദ്യാഭ്യാസം", "Scholarships and admissions", ["scholarship"]),
            "KSEB": DepartmentAgent("KSEB", "വൈദ്യുതി ബോർഡ്", "Electricity bills and connections", ["bill_pay"])
        }

    def route_and_execute(self, query):
        st.info(f"🎙️ **ജന-സേവനം (Jana-Sevanam)**: \"{query}\" എന്ന അപേക്ഷ സ്വീകരിച്ചു.")
        time.sleep(1)
        
        if any(w in query.lower() for w in ["scholarship", "വിദ്യ", "സ്കോളർഷിപ്പ്", "പഠനം"]):
            st.write("🎯 **Orchestrator**: Identified 'Education' intent.")
            edu_resp = self.agents["Education"].process_query(query)
            
            if edu_resp.get("sub_task") == "request_income_certificate":
                st.write("🔄 **Orchestrator**: Education Agent needs Income Certificate. Contacting Revenue Agent...")
                rev_resp = self.agents["Revenue"].process_query("Generate income certificate")
                st.write(f"✅ **Orchestrator**: {rev_resp['message']}")
                st.success("🎉 **വിജയിച്ചു!**: സ്കോളർഷിപ്പ് അപേക്ഷ സമർപ്പിച്ചു. (Success! Scholarship application submitted.)")
            else:
                st.write(f"✅ **Orchestrator**: {edu_resp['message']}")
        
        elif any(w in query.lower() for w in ["bill", "electricity", "വൈദ്യുതി"]):
            st.write("🎯 **Orchestrator**: Identified 'Electricity' intent.")
            elec_resp = self.agents["KSEB"].process_query(query)
            st.write(f"✅ **Orchestrator**: {elec_resp['message']}")
            if elec_resp.get("action_required") == "payment_confirmation":
                if st.button("ബില്ല് അടയ്ക്കുക (Pay ₹1,450)"):
                    st.success("💰 ബില്ല് അടച്ചു! രസീത് ഉടൻ ലഭിക്കും. (Payment successful!)")
        else:
            st.warning("❓ **Jana-Sevanam**: ക്ഷമിക്കണം, ഏത് വകുപ്പാണ് ഇത് കൈകാര്യം ചെയ്യുന്നത് എന്ന് വ്യക്തമല്ല.")

# Robust Web Speech API Integration
def speech_recognition_component(lang_code):
    component_html = f"""
    <div style="text-align: center; font-family: sans-serif;">
        <button id="mic-btn" style="
            background-color: #1b5e20; 
            color: white; 
            border: none; 
            padding: 15px 40px; 
            border-radius: 50px; 
            cursor: pointer;
            font-size: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        ">
            <span id="mic-icon">🎤</span>
            <span id="btn-text">സംസാരിക്കൂ / Click to Speak</span>
        </button>
        <div id="status" style="color: #444; margin-top: 15px; font-weight: bold; font-size: 16px;">
            റെഡി... (Ready...)
        </div>
    </div>

    <script>
        const btn = document.getElementById('mic-btn');
        const btnText = document.getElementById('btn-text');
        const status = document.getElementById('status');
        const micIcon = document.getElementById('mic-icon');
        
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = '{lang_code}';
        recognition.continuous = false;
        recognition.interimResults = false;

        btn.onclick = () => {{
            try {{
                recognition.start();
                btn.style.backgroundColor = '#d32f2f';
                btnText.innerText = 'ശ്രദ്ധിക്കുന്നു... (Listening...)';
                status.innerText = 'പറയൂ, ഞാൻ കേൾക്കുന്നുണ്ട്...';
                micIcon.innerText = '🔴';
            }} catch (e) {{
                console.log("Recognition already started or error: ", e);
            }}
        }};

        recognition.onresult = (event) => {{
            const transcript = event.results[event.results.length - 1][0].transcript;
            status.innerText = 'കണ്ടെത്തി: ' + transcript;
            btn.style.backgroundColor = '#1b5e20';
            btnText.innerText = 'സംസാരിക്കൂ / Click to Speak';
            micIcon.innerText = '🎤';
            
            // Bridge to Streamlit: Update URL and reload
            const url = new URL(window.parent.location.href);
            url.searchParams.set('voice_input', transcript);
            window.parent.location.href = url.href;
        }};

        recognition.onspeechend = () => {{
            recognition.stop();
            btnText.innerText = 'പ്രോസസ്സ് ചെയ്യുന്നു...';
        }};

        recognition.onerror = (event) => {{
            status.innerText = 'പിശക്: ' + event.error;
            btn.style.backgroundColor = '#1b5e20';
            btnText.innerText = 'വീണ്ടും ശ്രമിക്കൂ';
            micIcon.innerText = '⚠️';
        }};
    </script>
    """
    return components.html(component_html, height=180)

def main():
    st.set_page_config(page_title="Jana-Sevanam Kerala Demo", page_icon="🌴", layout="wide")
    
    st.title("🌴 ജന-സേവനം (Jana-Sevanam)")
    st.markdown("### Kerala State Government: Agent of Agents AI")
    
    st.sidebar.title("Settings")
    lang_choice = st.sidebar.selectbox("Preferred Language", ["Malayalam", "English"])
    lang_code = "ml-IN" if lang_choice == "Malayalam" else "en-IN"
    
    if st.sidebar.button("Clear History / വീണ്ടും ആരംഭിക്കുക"):
        st.query_params.clear()
        st.rerun()

    st.subheader(f"🗣️ Voice Assistant ({lang_choice})")
    
    # 1. Capture Voice Input from URL Query Params
    query_params = st.query_params
    voice_input = query_params.get("voice_input", None)
    
    # 2. Render Voice Component
    speech_recognition_component(lang_code)
    
    # 3. Main Input Logic
    user_query = None
    
    # If voice input came in, use it and display it
    if voice_input:
        st.success(f"🎙️ ശബ്ദ സന്ദേശം: **{voice_input}**")
        user_query = voice_input
    
    # Text input as fallback/manual override
    chat_query = st.chat_input("ഇവിടെ ടൈപ്പ് ചെയ്യുക (Type here...)")
    if chat_query:
        user_query = chat_query

    # Quick Action Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Example: എനിക്ക് സ്കോളർഷിപ്പ് അപേക്ഷിക്കണം"):
            user_query = "എനിക്ക് സ്കോളർഷിപ്പ് അപേക്ഷിക്കണം"
    with col2:
        if st.button("Example: വൈദ്യുതി ബില്ല് എത്രയാണ്?"):
            user_query = "വൈദ്യുതി ബില്ല് എത്രയാണ്?"

    # 4. Process the Query
    if user_query:
        st.write("---")
        orch = Orchestrator()
        orch.route_and_execute(user_query)

if __name__ == "__main__":
    main()
