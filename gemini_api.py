import os
import yaml
import google.generativeai as genai
from dotenv import load_dotenv # 📌 Importiamo dotenv per le variabili di ambiente
from datetime import datetime
from tqdm import tqdm  # 📌 Importiamo tqdm per la barra di avanzamento

# 📌 Carica le variabili d'ambiente dal file .env
load_dotenv()

# 📌 Recupera la API Key di Gemini
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("❌ API Key mancante! Assicurati di aver creato il file .env con GOOGLE_API_KEY.")

# 📌 Configura l'API di Gemini
genai.configure(api_key=API_KEY)

# 📌 Funzione per leggere il file YAML con le domande
def leggi_domande(file_yaml):
    with open(file_yaml, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("domande", [])

# 📌 Funzione per generare la risposta di Gemini
def ottieni_risposta(domanda):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(domanda)
    return response.text

# 📌 Funzione per scrivere le risposte in un file con timestamp
def scrivi_risposte_su_file(domande):
    # Crea la cartella output se non esiste
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Genera un timestamp per il file di output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_output = os.path.join(output_dir, f"risposte_{timestamp}.txt")

    # Scrive le risposte nel file con barra di avanzamento
    with open(file_output, "w", encoding="utf-8") as f:
        for domanda in tqdm(domande, desc="🟢 Elaborazione domande", unit="domanda"):
            risposta = ottieni_risposta(domanda)
            f.write(f"🟢 **Domanda:** {domanda}\n")
            f.write(f"🔵 **Risposta:**\n{risposta}\n")
            f.write("=" * 50 + "\n")  # Separatore tra domande

    return file_output

# 📌 Esegui il programma
if __name__ == "__main__":
    file_domande = "domande.yml"

    domande = leggi_domande(file_domande)
    if not domande:
        print("❌ Nessuna domanda trovata in 'domande.yml'.")
    else:
        print(f"📄 Sto generando risposte per {len(domande)} domande...")
        file_generato = scrivi_risposte_su_file(domande)
        print(f"✅ Risposte salvate in '{file_generato}'!")
