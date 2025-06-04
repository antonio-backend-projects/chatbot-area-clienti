
from langchain_core.tools import tool
from actions import data_actions

@tool
def get_customer_details(username: str) -> dict:
    """Recupera i dettagli del cliente autenticato."""
    return data_actions.get_customer_profile(username)

@tool
def get_last_invoices(username: str) -> dict:
    """Restituisce l'elenco delle ultime fatture."""
    return data_actions.get_invoices_list(username)

@tool
def get_services(username: str) -> dict:
    """Restituisce i servizi attivi del cliente."""
    return data_actions.get_services_list(username)
