
from langchain_core.tools import tool
from actions import auth_actions

@tool
def login_step1(username: str) -> str:
    """Invia un OTP all'utente per iniziare il login."""
    result = auth_actions.send_otp(username)
    return result.get("message", "Errore nell'invio OTP")

@tool
def login_step2(otp: str) -> str:
    """Valida un codice OTP per completare il login."""
    result = auth_actions.validate_otp(otp)
    return result.get("message", "Errore nella validazione OTP")
