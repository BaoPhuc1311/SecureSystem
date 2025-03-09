from collections import Counter
from decimal import Decimal, getcontext

def compute_intervals(text):
    freq = Counter(text)
    total_chars = sum(freq.values())
    
    probabilities = {char: Decimal(count) / Decimal(total_chars) for char, count in freq.items()}
    
    intervals = {}
    low = Decimal("0.0")
    for char, prob in sorted(probabilities.items()):
        high = low + prob
        intervals[char] = (low, high)
        low = high
    
    return intervals

def arithmetic_encode(text):
    getcontext().prec = 50
    intervals = compute_intervals(text)
    low, high = Decimal("0.0"), Decimal("1.0")

    for char in text:
        char_low, char_high = intervals[char]
        range_size = high - low
        
        high = low + range_size * char_high
        low = low + range_size * char_low
    
    return (low + high) / 2, intervals

def arithmetic_decode(encoded_value, intervals, text_length):
    getcontext().prec = 50
    decoded_text = ""
    low, high = Decimal("0.0"), Decimal("1.0")

    for _ in range(text_length):
        value_range = high - low
        target = (encoded_value - low) / value_range

        for char, (char_low, char_high) in sorted(intervals.items(), key=lambda x: x[1]):
            if char_low <= target < char_high:
                decoded_text += char
                high = low + value_range * char_high
                low = low + value_range * char_low
                break
    
    return decoded_text
