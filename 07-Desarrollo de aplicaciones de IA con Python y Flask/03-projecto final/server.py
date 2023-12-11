"""
Este módulo implementa una aplicación Flask para la detección de emociones.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route ('/')
def index () -> str:
    """
    Ruta principal que renderiza la plantilla index.html.
    """
    return render_template ('index.html')

@app.route ('/analyze_emotion', methods = ['POST'])
def analyze_emotion ():
    """
    Ruta para analizar la emoción basada en la entrada del usuario.
    """
    if request.method == 'POST':
        text_to_analyze = request.form.get ('text_to_analyze')
        result = emotion_detector (text_to_analyze)

        if result ['dominant_emotion'] is None:
            return jsonify({'message': "¡Texto no válido! ¡Inténtalo de nuevo!"})

        return jsonify (result)

if __name__ == '__main__':
    app.run(debug=True)

