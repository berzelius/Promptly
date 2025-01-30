# 📌 Generatore di Risposte con Gemini AI

Questo progetto utilizza **Google Gemini AI** per generare risposte a una serie di domande fornite in un file YAML. Le risposte vengono salvate in un file di output con timestamp. 

## 📋 Requisiti

Assicurati di avere installato:
- **Python 3.12** (o versione compatibile)
- **pipenv** per la gestione dell'ambiente virtuale
- Un account Google con accesso all'API di **Gemini AI**

## 🔑 Ottenere una API Key di Gemini

Per ottenere una chiave API di Google Gemini:

1. Vai sulla documentazione [Google AI for developers](https://ai.google.dev/gemini-api/docs/api-key?hl=it)
2. Accedi con il tuo account Google
3. Segui le istruzioni e crea un nuovo progetto se necessario su Google AI Studio
4. Abilita le API di Gemini nella console di Google Cloud
5. Genera una nuova chiave API e copiala
6. Salva la chiave nel file `.env` come segue:

```ini
GOOGLE_API_KEY=la_tua_api_key
```

## ⚙️ Setup del Progetto

### 1️⃣ Clona il repository

```sh
git clone https://github.com/TUO_USERNAME/NOME_REPO.git
cd NOME_REPO
```

### 2️⃣ Crea un ambiente virtuale con Pipenv

```sh
pipenv --python 3.12
pipenv install
```

### 3️⃣ Configura le variabili d'ambiente

Crea un file `.env` nella root del progetto e aggiungi la tua API Key di Google Gemini:

```ini
GOOGLE_API_KEY=la_tua_api_key
```

### 4️⃣ Prepara il file delle domande

Crea un file `domande.yml` con il seguente formato:

```yaml
domande:
  - "Qual è il significato della vita?"
  - "Spiegami la teoria della relatività."
  - "Come funziona il machine learning?"
```

## 🚀 Eseguire lo script

Una volta configurato tutto, esegui lo script con:

```sh
pipenv run python script.py
```

Se vuoi entrare nell'ambiente virtuale prima di eseguire il comando:

```sh
pipenv shell
python script.py
```

Il programma elaborerà le domande e salverà le risposte in un file all'interno della cartella `output/`, con un nome del tipo:

```
output/risposte_YYYYMMDD_HHMMSS.txt
```

## 📄 Struttura del progetto

```
📂 NOME_REPO
├── 📄 script.py          # Script principale
├── 📄 domande.yml        # File con le domande
├── 📄 Pipfile            # Configurazione di Pipenv
├── 📄 .env               # Variabili d'ambiente (NON VA VERSIONATO)
├── 📂 output/            # Cartella dove vengono salvate le risposte
├── 📄 .gitignore         # File per ignorare file non necessari
└── 📄 README.md          # Questo file
```

## 🛠 Risoluzione problemi

### ❌ Errore "API Key mancante!"
Assicurati di aver creato il file `.env` e di aver aggiunto correttamente la tua API Key.

### ❌ Errore "Modulo non trovato"
Verifica di aver installato correttamente le dipendenze con:
```sh
pipenv install
```

Se hai ancora problemi, prova a reinstallare l'ambiente virtuale:
```sh
pipenv --rm
pipenv install
```

## 📜 Licenza

Questo progetto è distribuito sotto la **GNU GPL v3 License**.

---

💡 **Autore:** [Berzelius](https://github.com/berzelius)

