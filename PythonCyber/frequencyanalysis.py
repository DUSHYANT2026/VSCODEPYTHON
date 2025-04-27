from collections import Counter
import matplotlib.pyplot as plt
import string

def frequency_analysis(text):
    # Remove non-alphabetic characters and convert to lowercase
    filtered = [c.lower() for c in text if c.isalpha()]
    total_letters = len(filtered)
    
    if total_letters == 0:
        return {}
    
    # Count letter frequencies
    freq = Counter(filtered)
    
    # Calculate percentages
    percentages = {letter: (count / total_letters) * 100 for letter, count in freq.items()}
    
    # Fill in missing letters with 0%
    for letter in string.ascii_lowercase:
        if letter not in percentages:
            percentages[letter] = 0.0
    
    return percentages

def plot_frequencies(frequencies, title="Letter Frequencies"):
    letters = sorted(frequencies.keys())
    values = [frequencies[letter] for letter in letters]
    
    plt.figure(figsize=(10, 5))
    plt.bar(letters, values)
    plt.title(title)
    plt.xlabel("Letters")
    plt.ylabel("Frequency (%)")
    plt.grid(True, axis='y')
    plt.show()

# Example usage
if __name__ == "__main__":
    # English letter frequencies for comparison (from Wikipedia)
    english_frequencies = {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0,
        'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15,
        'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5,
        'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1,
        'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0,
        'z': 0.074
    }
    
    sample_text = """The quick brown fox jumps over the lazy dog. This sentence contains 
    all the letters in the English alphabet. Frequency analysis is a technique used to 
    break substitution ciphers by examining how often letters appear in ciphertext."""
    
    # Analyze our sample text
    analysis = frequency_analysis(sample_text)
    
    # Print results
    print("Letter Frequency Analysis:")
    for letter, freq in sorted(analysis.items()):
        print(f"{letter}: {freq:.2f}%")
    
    # Plot comparison
    plot_frequencies(analysis, "Sample Text Frequencies")
    plot_frequencies(english_frequencies, "Standard English Frequencies")