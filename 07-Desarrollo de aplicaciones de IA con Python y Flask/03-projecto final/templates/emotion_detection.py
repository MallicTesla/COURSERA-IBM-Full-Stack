import requests

from flask import Flask

app = Flask(__name__)

def emotion_detector(text_to_analyze):
    # URL de la API de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Encabezados requeridos
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Formato de entrada en JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Realizar la solicitud POST a la API
    # response = requests.post(url, json=input_json, headers=headers)
    response = requests.post(url, json=input_json, headers=headers, timeout=60)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Obtener el atributo 'text' del objeto de respuesta (assumiendo que el resultado es un JSON)
        result_text = response.json().get('text')
        return result_text
    else:
        # Si la solicitud no fue exitosa, imprimir el código de estado de la respuesta
        print(f"Error en la solicitud: {response.status_code}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    text_to_analyze = "I love this new technology."
    result = emotion_detector(text_to_analyze)
    
    if result is not None:
        print(f"Resultado de la detección de emociones: {result}")
