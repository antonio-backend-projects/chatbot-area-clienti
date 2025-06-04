# 🤖 Area Clienti Chatbot
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![LangChain](https://img.shields.io/badge/langchain-v0.2-yellow)

**Area Clienti Chatbot** è un assistente conversazionale **intelligente e modulare**, progettato per simulare un'interfaccia di assistenza clienti automatizzata. Il sistema è costruito con [LangChain v0.2](https://www.langchain.com/), sfrutta modelli OpenAI con agenti basati su *function calling* e consente di gestire in modo naturale e sicuro funzionalità come:

* **Autenticazione utente via OTP**
* **Accesso ai dati anagrafici**
* **Visualizzazione delle fatture recenti**
* **Consultazione dei servizi attivi**

Il progetto è stato sviluppato con l’obiettivo di **dimostrare competenze avanzate** nell’integrazione tra LLM, orchestrazione agentica, gestione sicura degli accessi, interazione con database relazionali e progettazione modulare del codice. Utilizza una **pipeline LangChain basata su LCEL (LangChain Expression Language)**, rendendo l'agente facilmente estendibile per scenari aziendali più ampi.

> Pensato come **progetto portfolio**, *Area Clienti Chatbot* dimostra la capacità di realizzare sistemi conversazionali robusti, sicuri e facilmente integrabili in ambienti reali (es. CRM, helpdesk, ERP).


---

## 📌 Caratteristiche principali

- 🔐 Login sicuro tramite codice OTP
- 👤 Accesso ai dettagli anagrafici
- 🧾 Visualizzazione delle ultime fatture
- 📄 Elenco dei servizi attivi
- 🧠 Orchestrazione tramite LangChain Expression Language (LCEL)  
- ⚙️ Tools definiti come funzioni invocabili da OpenAI (function-calling agent)
- 💬 Interfaccia a riga di comando (CLI)
- 🗄️ Archiviazione dati su MySQL

---

## ⚙️ Requisiti

- Python **3.11.9** (consigliato: gestito con `pyenv`)
- MySQL/MariaDB attivo
- API Key OpenAI valida

---

## 🚀 Setup ambiente con `pyenv`

```bash
cd /opt/area-clienti-chatbot

# Crea ambiente virtuale
pyenv virtualenv 3.11.9 area-clienti-chatbot

# Attiva l’ambiente
pyenv activate area-clienti-chatbot

# Oppure imposta come locale
pyenv local area-clienti-chatbot

# Installa le dipendenze
pip install -r requirements.txt
````

---

## 🔐 Configurazione ambiente

Copia `.env.example` in `.env` e inserisci i valori:

```ini
OPENAI_API_KEY=sk-...
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=customer_db
```
# ⚠️ Non condividere questo file! Contiene credenziali sensibili.


---

## 🗄️ Inizializzazione database

Esegui lo script per creare tabelle e dati utente di esempio:

```bash
python init_db.py
```

Utenti inclusi:

* `testuser`
* `Mario`
* `Lino`
* `Maria`

---

## 💬 Avvia chatbot CLI

```bash
python main.py
```

Esempio:

```
🔐 Benvenuto! Inizia con il login (es. 'login gianluca')

Tu: login gianluca
📨 OTP inviato a gianluca

Tu: 123456
🔐 Login completato

Tu: mostrami le mie ultime fatture
📊 [...]

Tu: che servizi ho attivi?
📄 Servizi attivi: Luce Casa, Gas Variabile

Tu: mostra l’anagrafica
👤 Nome: Mario Rossi | Email: mario@example.com | Telefono: 320...

```

---

## 📁 Struttura progetto

```
area-clienti-chatbot/
├── actions/           # Logica business: OTP, clienti, fatture, servizi
├── config/            # Configurazione dei gruppi di tools (autenticati/non)
├── tools/             # Tools LangChain registrati per ogni funzione
├── utils/             # Connessione DB, funzioni comuni
├── main.py            # Entry point CLI LangChain agent
├── init_db.py         # Script di inizializzazione e popolamento DB
├── .env.example       # Esempio configurazione ambiente
└── requirements.txt   # Dipendenze Python
```

---

## 🧩 Tecnologie usate

* [LangChain v0.2](https://python.langchain.com/docs/versions/v0_2/)
* [OpenAI GPT-4 Turbo](https://platform.openai.com/)
* MySQL / MariaDB
* Python 3.11.9
* `python-dotenv`, `langchain-openai`, `langchain-core`

---

## 🔭 Roadmap suggerita

* 🌐 API REST (FastAPI o Flask)
* 🧑‍🤝‍🧑 Supporto multiutente e ruoli
* 🧾 Log attività e cronologia conversazioni
* 🖼️ UI web o chatbot su Telegram/WhatsApp

---

## 📜 Licenza

Rilasciato sotto licenza [MIT](https://opensource.org/licenses/MIT).
Copyright © 2025

---