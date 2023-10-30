from flask import jsonify, request
from app import app, mongo
import translate

# Define the MongoDB collection for translations
translations_collection = mongo.db.translations

# Define the translate_function() function
# Rename the translate_function to something else
def translate_text(voice_data):
    """Translates the voice data to English (you can replace 'en' with the desired target language).
    
    Args:
        voice_data: The voice data to translate.
    
    Returns:
        The translated text.
    """
    try:
        # Translate the voice data to English
        translated_text = translate.translate(voice_data, to='en')
        # Return the translated text as a string.
        return translated_text
    except Exception as e:
        return str(e)

# Define the translate route
# Define the translate route
@app.route('/translate', methods=['POST'])
def translate():
    voice_data = request.json.get('voice_data')

    if not isinstance(voice_data, str):
        return jsonify({'error': 'Voice data must be a string'})

    # Translate the voice data using the translate_text() function
    translated_text = translate_text(voice_data)

    # Save both the voice data and translated text in the MongoDB collection
    translation_data = {
        "voice_data": voice_data,
        "translated_text": translated_text
    }
    translations_collection.insert_one(translation_data)

    return jsonify({'translation': translated_text})
