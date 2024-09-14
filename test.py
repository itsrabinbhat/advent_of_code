import re
def split_number_words(text):
    # Define the regex pattern to match the possible number words
    pattern = r'(?=(eight|nine|seven|six|five|four|three|two|one))'
    
    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)
    
    return matches

# Example usage
text = 'eighthree'
print(split_number_words(text))  # Output: ['eight', 'three']
