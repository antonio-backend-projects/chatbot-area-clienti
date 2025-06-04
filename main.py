
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from tools.auth import login_step1, login_step2
from tools.data import get_customer_details, get_last_invoices, get_services
from config.agents_config import AGENTS_CONFIG
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.2)

TOOLS_MAP = {
    "login_step1": login_step1,
    "login_step2": login_step2,
    "get_customer_details": get_customer_details,
    "get_last_invoices": get_last_invoices,
    "get_services": get_services
}

def get_tools_by_auth(authenticated):
    tools = []
    for group in AGENTS_CONFIG.values():
        if group["requires_auth"] and not authenticated:
            continue
        tools += [TOOLS_MAP[t] for t in group["tools"]]
    return tools

def chat_loop():
    session = {"authenticated": False, "username": None}
    print("🔐 Benvenuto! Inizia con il login (es. 'login testuser').")

    while True:
        user_input = input("\nTu: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Arrivederci!")
            break

        # Login step 1
        if not session["authenticated"]:
            if "login" in user_input.lower() and "otp" not in user_input:
                username = user_input.split()[-1]
                result = login_step1.invoke({"username": username})
                session["username"] = username
                print(f"\n📨 Assistente: {result}")
                continue
            elif user_input.isdigit() and len(user_input) == 6:
                result = login_step2.invoke({"otp": user_input})
                print(f"\n🔐 Assistente: {result}")
                if "completato" in result.lower():
                    session["authenticated"] = True
                continue
            else:
                print("⚠️ Devi prima autenticarti con login + username.")
                continue

        # Solo dopo autenticazione
        tools = get_tools_by_auth(session["authenticated"])
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.OPENAI_FUNCTIONS,
            verbose=True,
        )

        user_context = f"{user_input} (utente: {session['username']})"
        try:
            result = agent.invoke(user_context)
            print(f"\n🤖 Assistente: {result['output']}")
        except Exception as e:
            print("⚠️ Errore durante l'elaborazione:", str(e))

if __name__ == "__main__":
    chat_loop()
