from shannon_fano import shannon_fano_encode, shannon_fano_decode

def secure_system():
    text = input("Enter the text to be encoded: ")

    encoded_text, codes = shannon_fano_encode(text)
    print("Encoded string:", encoded_text)

    decoded_text = shannon_fano_decode(encoded_text, codes)

    if text == decoded_text:
        print("Decoding successful! The original text matches the input.")
    else:
        print("Error! The decoded text does not match the original.")

if __name__ == "__main__":
    secure_system()
