
from utils.database import db_query
import json

def get_customer_profile(username):
    result = db_query("SELECT details FROM customers WHERE username = %s", (username,))
    return json.loads(result[0][0]) if result else {'error': 'Dettagli non trovati'}

def get_invoices_list(username):
    result = db_query("SELECT invoices FROM invoices WHERE username = %s", (username,))
    return json.loads(result[0][0]) if result else {'error': 'Fatture non trovate'}

def get_services_list(username):
    result = db_query("SELECT services FROM services WHERE username = %s", (username,))
    return json.loads(result[0][0]) if result else {'error': 'Servizi non trovati'}
