from huffman import huffman_encode, huffman_decode

def secure_system():
    text = input("Enter the text to be encoded: ")

    encoded_text, root = huffman_encode(text)
    print("Encoded string:", encoded_text)

    decoded_text = huffman_decode(encoded_text, root)

    if text == decoded_text:
        print("Decoding successful! The original text matches the input.")
    else:
        print("Error! The decoded text does not match the original.")

if __name__ == "__main__":
    secure_system()
