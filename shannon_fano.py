from collections import Counter

def shannon_fano_recursive(symbols, codes, prefix=""):
    if len(symbols) == 1:
        codes[symbols[0][0]] = prefix or "0"
        return
    
    total_weight = sum(freq for _, freq in symbols)
    cumulative_weight = 0
    split_index = 0
    
    for i, (_, freq) in enumerate(symbols):
        cumulative_weight += freq
        if cumulative_weight >= total_weight / 2:
            split_index = i + 1
            break
    
    shannon_fano_recursive(symbols[:split_index], codes, prefix + "0")
    shannon_fano_recursive(symbols[split_index:], codes, prefix + "1")

def shannon_fano_coding(text):
    frequency = Counter(text)
    symbols = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    codes = {}
    shannon_fano_recursive(symbols, codes)
    return codes

def shannon_fano_encode(text):
    codes = shannon_fano_coding(text)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes

def shannon_fano_decode(encoded_text, codes):
    reversed_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    buffer = ""
    
    for bit in encoded_text:
        buffer += bit
        if buffer in reversed_codes:
            decoded_text += reversed_codes[buffer]
            buffer = ""
    
    return decoded_text
