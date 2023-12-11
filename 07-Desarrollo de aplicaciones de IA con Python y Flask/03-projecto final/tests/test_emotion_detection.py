import unittest
from unittest.mock import MagicMock, patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    @patch('emotion_detection.requests.post')
    def test_emotion_detector_success(self, mock_post):
        # Configurar el objeto de respuesta simulado
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotion': {
                'anger': 0.1,
                'disgust': 0.2,
                'fear': 0.3,
                'joy': 0.4,
                'sadness': 0.5
            }
        }
        mock_post.return_value = mock_response

        # Llamar a la función bajo prueba
        result = emotion_detector("I am testing emotions")

        # Verificar el resultado esperado
        expected_result = {
            'anger': 0.1,
            'disgust': 0.2,
            'fear': 0.3,
            'joy': 0.4,
            'sadness': 0.5,
            'dominant_emotion': 'sadness'
        }
        self.assertEqual(result, expected_result)

    @patch('emotion_detection.requests.post')
    def test_emotion_detector_failure(self, mock_post):
        # Configurar el objeto de respuesta simulado para un error
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_post.return_value = mock_response

        # Llamar a la función bajo prueba
        result = emotion_detector("I am testing errors")

        # Verificar que el resultado sea None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
