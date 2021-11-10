
import re

product_review = '''this is a fine milk, but the product
line appears to be limited in available colors. I could only find white.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)
sentences = [match[0] for match in matches]


word_pattern = re.compile(r"([\w\_']+)([\s,.])?")
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]
    print(words)

def get_matches_for_pattern(pattern, string):
    matches = pattern.findall(string)
    return [match[0] for match in matches]

product_review = '...'

sentence_pattern = re.compile(r'(.*?\.)(\s|$)',re.DOTALL)
sentences = get_matches_for_pattern(
    sentence_pattern,
    product_review,
)

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    worlds = get_matches_for_pattern(
        word_pattern,
        sentence
    )
    print(words)
