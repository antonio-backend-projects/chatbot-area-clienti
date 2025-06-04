from utils.database import db_query

def init_db():
    db_query("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50) PRIMARY KEY, otp VARCHAR(6), status VARCHAR(20))")
    db_query("CREATE TABLE IF NOT EXISTS customers (username VARCHAR(50) PRIMARY KEY, details TEXT)")
    db_query("CREATE TABLE IF NOT EXISTS invoices (username VARCHAR(50), invoices JSON)")
    db_query("CREATE TABLE IF NOT EXISTS services (username VARCHAR(50), services JSON)")

    # testuser
    db_query("INSERT IGNORE INTO users VALUES (%s, NULL, NULL)", ('testuser',))
    db_query("INSERT IGNORE INTO customers VALUES (%s, %s)", ('testuser', '{"name": "Mario Rossi", "email": "mario@example.com"}'))
    db_query("INSERT IGNORE INTO invoices VALUES (%s, %s)", ('testuser', '[{"id": "INV001", "amount": 99.99}]'))
    db_query("INSERT IGNORE INTO services VALUES (%s, %s)", ('testuser', '[{"service": "Fibra 1Gbps"}]'))

    # mario
    db_query("INSERT IGNORE INTO users VALUES (%s, NULL, NULL)", ('mario',))
    db_query("INSERT IGNORE INTO customers VALUES (%s, %s)", ('mario', '''{"name": "Mario Tommaseo", "email": "vmatteotti@live.com"}'''))
    db_query("INSERT IGNORE INTO invoices VALUES (%s, %s)", ('mario', '''[{"id": "INV001", "amount": 155.25}, {"id": "INV002", "amount": 349.5}, {"id": "INV003", "amount": 179.5}, {"id": "INV004", "amount": 369.19}, {"id": "INV005", "amount": 143.2}, {"id": "INV006", "amount": 68.38}, {"id": "INV007", "amount": 348.65}, {"id": "INV008", "amount": 303.77}, {"id": "INV009", "amount": 495.58}, {"id": "INV010", "amount": 499.6}]'''))
    db_query("INSERT IGNORE INTO services VALUES (%s, %s)", ('mario', '''[{"service": "E-commerce guida virtuali"}, {"service": "Convergenze ottimali next-generation"}, {"service": "Nicchie target valore aggiunto"}, {"service": "Architetture ottimali sexy"}, {"service": "Modelli spedizioni out-of-the-box"}]'''))

    # salvi
    db_query("INSERT IGNORE INTO users VALUES (%s, NULL, NULL)", ('salvi',))
    db_query("INSERT IGNORE INTO customers VALUES (%s, %s)", ('salvi', '''{"name": "Salvi Abatantuono", "email": "lidiarinaldi@hotmail.it"}'''))
    db_query("INSERT IGNORE INTO invoices VALUES (%s, %s)", ('salvi', '''[{"id": "INV001", "amount": 316.92}, {"id": "INV002", "amount": 203.64}, {"id": "INV003", "amount": 296.65}, {"id": "INV004", "amount": 36.83}, {"id": "INV005", "amount": 372.25}, {"id": "INV006", "amount": 341.45}, {"id": "INV007", "amount": 108.71}, {"id": "INV008", "amount": 381.51}, {"id": "INV009", "amount": 219.9}, {"id": "INV010", "amount": 396.42}, {"id": "INV011", "amount": 76.11}, {"id": "INV012", "amount": 223.53}, {"id": "INV013", "amount": 391.93}, {"id": "INV014", "amount": 44.46}, {"id": "INV015", "amount": 475.9}, {"id": "INV016", "amount": 273.38}, {"id": "INV017", "amount": 85.4}, {"id": "INV018", "amount": 169.51}, {"id": "INV019", "amount": 234.69}, {"id": "INV020", "amount": 379.79}]'''))
    db_query("INSERT IGNORE INTO services VALUES (%s, %s)", ('salvi', '''[{"service": "Webservices strategiche dinamiche"}, {"service": "Nicchie integrate real-time"}, {"service": "Metodologie transizionali scalabili"}, {"service": "Supply-chains marchi mondiali"}, {"service": "Supply-chains implementate b2c"}, {"service": "E-services estensioni scalabili"}, {"service": "Nicchie abilitate b2b"}, {"service": "Mercati utilizzo forti"}, {"service": "Convergenze exploit back-end"}, {"service": "Mercati deploy efficienti"}]'''))

    # monica
    db_query("INSERT IGNORE INTO users VALUES (%s, NULL, NULL)", ('monica',))
    db_query("INSERT IGNORE INTO customers VALUES (%s, %s)", ('monica', '''{"name": "Monica Gagliardi", "email": "celentanovittorio@tele2.it"}'''))
    db_query("INSERT IGNORE INTO invoices VALUES (%s, %s)", ('monica', '''[{"id": "INV001", "amount": 469.97}, {"id": "INV002", "amount": 151.6}, {"id": "INV003", "amount": 175.15}, {"id": "INV004", "amount": 355.49}, {"id": "INV005", "amount": 131.18}, {"id": "INV006", "amount": 59.3}, {"id": "INV007", "amount": 12.39}, {"id": "INV008", "amount": 48.88}, {"id": "INV009", "amount": 249.26}, {"id": "INV010", "amount": 121.33}, {"id": "INV011", "amount": 84.34}, {"id": "INV012", "amount": 99.86}, {"id": "INV013", "amount": 24.6}, {"id": "INV014", "amount": 304.91}, {"id": "INV015", "amount": 170.16}, {"id": "INV016", "amount": 187.84}, {"id": "INV017", "amount": 400.19}, {"id": "INV018", "amount": 138.7}, {"id": "INV019", "amount": 343.38}, {"id": "INV020", "amount": 451.13}, {"id": "INV021", "amount": 267.9}, {"id": "INV022", "amount": 311.98}, {"id": "INV023", "amount": 389.48}, {"id": "INV024", "amount": 155.73}, {"id": "INV025", "amount": 125.54}, {"id": "INV026", "amount": 35.72}, {"id": "INV027", "amount": 232.38}, {"id": "INV028", "amount": 439.97}, {"id": "INV029", "amount": 198.19}, {"id": "INV030", "amount": 296.84}]'''))
    db_query("INSERT IGNORE INTO services VALUES (%s, %s)", ('monica', '''[{"service": "Relazioni exploit forti"}, {"service": "Esperienze accrescitive efficienti"}, {"service": "Supply-chains integrate verticalizzate"}, {"service": "Tecnologie strategiche mondiali"}, {"service": "Nicchie ottimali back-end"}, {"service": "Contenuti deploy granulari"}, {"service": "E-services guida integrate"}, {"service": "Nicchie spedizioni mission-critical"}, {"service": "Funzionalità estensioni interattive"}, {"service": "Modelli estensioni sexy"}, {"service": "Contenuti transizionali rivoluzionari"}, {"service": "Supply-chains transizionali di impatto"}, {"service": "E-business evolutive scalabili"}, {"service": "Convergenze target virtuali"}, {"service": "Comunità transizionali mondiali"}]'''))

if __name__ == "__main__":
    init_db()
