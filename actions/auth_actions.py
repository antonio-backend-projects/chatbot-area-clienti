
import random
from utils.database import db_query
import logging

logger = logging.getLogger(__name__)

def send_otp(username):
    try:
        user = db_query("SELECT * FROM users WHERE username = %s", (username,))
        if user:
            otp = str(random.randint(100000, 999999))
            success = db_query(
                "UPDATE users SET otp = %s, status = 'pending' WHERE username = %s",
                (otp, username)
            )
            if success:
                logger.info(f"OTP sent to {username}: {otp}")
                return {'status': 'OK', 'message': f'OTP inviato a {username}'}
        return {'status': 'KO', 'message': 'Utente non trovato'}
    except Exception as e:
        logger.error(f"Error in send_otp: {str(e)}")
        return {'status': 'KO', 'message': 'Errore nel sistema'}

def validate_otp(otp):
    try:
        user = db_query(
            "SELECT username FROM users WHERE otp = %s AND status = 'pending'",
            (otp,)
        )
        if user:
            username = user[0][0]
            success = db_query(
                "UPDATE users SET status = 'verified' WHERE otp = %s",
                (otp,)
            )
            if success:
                logger.info(f"OTP validated for {username}")
                return {'status': 'OK', 'message': 'Login completato', 'username': username}
        return {'status': 'KO', 'message': 'OTP non valido'}
    except Exception as e:
        logger.error(f"Error in validate_otp: {str(e)}")
        return {'status': 'KO', 'message': 'Errore di validazione'}
