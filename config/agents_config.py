
AGENTS_CONFIG = {
    "auth": {
        "tools": ["login_step1", "login_step2"],
        "description": "Autenticazione OTP",
        "requires_auth": False
    },
    "data": {
        "tools": ["get_customer_details", "get_last_invoices", "get_services"],
        "description": "Accesso a dati personali, contratti e servizi",
        "requires_auth": True
    }
}
