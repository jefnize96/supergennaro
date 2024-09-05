import streamlit as st
import requests
import json

# Titolo dell'applicazione
st.title("Chatbot Virtual Assistant con Ollama")

# Prompt per inserire il messaggio
messaggio = st.text_input("Inserisci il tuo messaggio:")

# Bottone per inviare il messaggio
if st.button('Invia'):
    if messaggio:
        # URL del server Ollama (sostituisci con il tuo indirizzo IP)
        url = 'http://34.31.140.228:11434/api/chat'  # Cambia con l'IP del tuo server Ollama

        # Dati da inviare alla API
        payload = {
            'model': 'llama3:latest',  # Specifica il modello che vuoi usare
            'prompt': messaggio
        }

        # Intestazioni HTTP
        headers = {
            'Content-Type': 'application/json'
        }

        try:
            # Invio della richiesta POST al server Ollama
            response = requests.post(url, headers=headers, data=json.dumps(payload))

            # Controlla lo stato della risposta
            if response.status_code == 200:
                # Estrai la risposta dal JSON
                data = response.json()
                risposta = data.get('message', {}).get('content', 'Nessuna risposta dal chatbot.')
                # Mostra la risposta del chatbot
                st.text_area("Risposta del chatbot:", risposta)
            else:
                st.write(f"Errore nella comunicazione con Ollama: {response.status_code}")
        except Exception as e:
            st.write(f"Errore: {e}")
    else:
        st.write("Per favore inserisci un messaggio.")

# Footer
st.write("Chatbot creato con Streamlit e Ollama")
