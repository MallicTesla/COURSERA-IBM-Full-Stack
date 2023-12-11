import requests
import json

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
    response = requests.post(url, json=input_json, headers=headers, timeout=60)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Convertir el texto de respuesta en un diccionario
        result_dict = response.json()

        # Extraer el conjunto de emociones necesario
        emotions = result_dict.get('emotion', {})

        # Extraer las puntuaciones de las emociones
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        # Encontrar la emoción dominante
        dominant_emotion = max(emotions, key=emotions.get)

        # Devolver el formato de salida requerido
        result_output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

        return result_output

    else:
        # Manejo de error para status_code diferente de 200
        print(f"Error en la solicitud: {response.status_code}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

# Ejemplo de uso
if __name__ == "__main__":
    text_to_analyze = "I am so happy to be doing this."
    result = emotion_detector(text_to_analyze)
    
    if result is not None:
        print(f"Resultado de la detección de emociones: {result}")
