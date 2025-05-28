from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu plain_text hoặc key'}), 400
        plain_text = data['plain_text']
        key = int(data['key'])
        if key < 0:
            return jsonify({'error': 'Key phải là số không âm'}), 400
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except ValueError:
        return jsonify({'error': 'Key phải là số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu cipher_text hoặc key'}), 400
        cipher_text = data['cipher_text']
        key = int(data['key'])
        if key < 0:
            return jsonify({'error': 'Key phải là số không âm'}), 400
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except ValueError:
        return jsonify({'error': 'Key phải là số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu plain_text hoặc key'}), 400
        plain_text = data['plain_text']
        key = data['key']
        if not key.isalpha():
            return jsonify({'error': 'Key phải là chuỗi chữ cái'}), 400
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu cipher_text hoặc key'}), 400
        cipher_text = data['cipher_text']
        key = data['key']
        if not key.isalpha():
            return jsonify({'error': 'Key phải là chuỗi chữ cái'}), 400
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500

# RAILFENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu plain_text hoặc key'}), 400
        plain_text = data['plain_text']
        key = int(data['key'])
        if key < 1:
            return jsonify({'error': 'Key phải là số nguyên dương'}), 400
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except ValueError:
        return jsonify({'error': 'Key phải là số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu cipher_text hoặc key'}), 400
        cipher_text = data['cipher_text']
        key = int(data['key'])
        if key < 1:
            return jsonify({'error': 'Key phải là số nguyên dương'}), 400
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except ValueError:
        return jsonify({'error': 'Key phải là số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from .playfair_cipher import PlayFairCipher

# Thêm đoạn sau vào trong hàm main
PLAYFAIR_CIPHER_ALGORITHM = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def create_matrix():
    data = request.json
    key = data['key']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})