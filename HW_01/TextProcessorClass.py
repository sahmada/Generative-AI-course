import re
import json
import string
from collections import Counter

class TextProcessor:
    def __init__(self, file_path, output_json):
        self.file_path = file_path
        self.output_json = output_json
        self.stop_words = set([
            "و", "در", "به", "از", "که", "این", "را", "با", "است", "برای",
            "آن", "یک", "هم", "تا", "نیز", "اما", "یا", "بر", "اگر", "هر",
            "چون", "باید", "می", "شد", "کند", "کرد", "شده", "دیگر", "همه",
            "نیک", "اینجا", "اینها", "آنان", "خود"
        ])

    def read_file(self):
        """Read content from the text file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"The file '{self.file_path}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
        return ""

    def clean_text(self, text):
        """Remove emails, URLs, punctuation, and normalize whitespace."""
        if not text:
            return ""

        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        url_pattern = r"https?://\S+|www\.\S+"
        text = re.sub(email_pattern, '', text)
        text = re.sub(url_pattern, '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def remove_stopwords(self, text):
        """Remove Persian stop words from text."""
        if not text:
            return ""

        pattern = r'\b(?:' + '|'.join(map(re.escape, self.stop_words)) + r')\b'
        cleaned_text = re.sub(pattern, '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text

    def count_word_frequencies(self, text):
        """Count word frequencies in the cleaned text."""
        if not text:
            return {}

        words = text.split()
        return dict(Counter(words))

    def save_to_json(self, word_counts):
        """Save word frequencies to a JSON file."""
        try:
            with open(self.output_json, 'w', encoding='utf-8') as json_file:
                json.dump(word_counts, json_file, ensure_ascii=False, indent=4)
            print(f"The word frequencies have been saved to '{self.output_json}'.")
        except Exception as e:
            print(f"Error saving to JSON file: {e}")

    def process(self):
        """Run the full text processing pipeline."""
        print("Starting text processing...")
        text = self.read_file()
        if not text:
            print("The input file is empty or could not be read.")
            return

        cleaned = self.clean_text(text)
        filtered = self.remove_stopwords(cleaned)
        word_counts = self.count_word_frequencies(filtered)
        self.save_to_json(word_counts)
        print("Completed text processing.")