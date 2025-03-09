from arithmetic import arithmetic_encode, arithmetic_decode

def secure_system():
    text = input("Enter the text to be encoded: ")

    encoded_value, intervals = arithmetic_encode(text)
    print("Encoded value:", encoded_value)

    decoded_text = arithmetic_decode(encoded_value, intervals, len(text))

    if text == decoded_text:
        print("Decoding successful! The original text matches the input.")
    else:
        print("Error! The decoded text does not match the original.")

if __name__ == "__main__":
    secure_system()
