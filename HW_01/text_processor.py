from TextProcessorClass import TextProcessor

# Define the input and output file paths
input_file = "input.txt"
output_file = "word_frequencies.json"

# Create an instance of TextProcessor and process the text
processor = TextProcessor(input_file, output_file)
processor.process()