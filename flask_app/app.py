from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

latin_to_osmanya = {
    # Single Vowels
    'á': '𐒀',
    'a': '𐒖',
    'e': '𐒗',
    'i': '𐒘',
    'o': '𐒙',
    'u': '𐒚',

    # Double Vowels
    'aa': '𐒛',
    'ee': '𐒜',
    'oo': '𐒝',

    # Consonants
    'b': '𐒁',
    't': '𐒂',
    'j': '𐒃',
    'x': '𐒄',
    'kh': '𐒅',
    'd': '𐒆',
    'r': '𐒇',
    's': '𐒈',
    'sh': '𐒉',
    'dh': '𐒊',
    'c': '𐒋',
    'g': '𐒌',
    'f': '𐒍',
    'q': '𐒎',
    'k': '𐒏',
    'l': '𐒐',
    'm': '𐒑',
    'n': '𐒒',
    'w': '𐒓',
    'h': '𐒔',
    'y': '𐒕',

    # Numbers
    '0': '𐒠',
    '1': '𐒡',
    '2': '𐒢',
    '3': '𐒣',
    '4': '𐒤',
    '5': '𐒥',
    '6': '𐒦',
    '7': '𐒧',
    '8': '𐒨',
    '9': '𐒩'
}

osmanya_to_latin = {v: k for k, v in latin_to_osmanya.items()}

def transliterate(text, latin_to_osmanya, osmanya_to_latin, direction):
    if direction == 'latin-to-osmanya':
        translation_dict = latin_to_osmanya
    else:
        translation_dict = osmanya_to_latin

    result = ''
    i = 0
    while i < len(text):
        letter = text[i]
        if i+1 < len(text) and letter.lower()+text[i+1].lower() in translation_dict:
            result += translation_dict[letter.lower()+text[i+1].lower()]
            i += 2
        elif letter.lower() in translation_dict:
            result += translation_dict[letter.lower()]
            i += 1
        else:
            result += letter
            i += 1
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        direction = request.form['direction']
        transliterated_text = transliterate(text, latin_to_osmanya, osmanya_to_latin, direction)
        return jsonify({'transliterated_text': transliterated_text})
    else:
        return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/resources/')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run()
