import argparse

def main():
    parser = argparse.ArgumentParser(description="Read and print file contents.")
    parser.add_argument("path_to_file", help="Path to the file to read.")
    args = parser.parse_args()

    with open(args.path_to_file) as f: 
        fileContents = f.read()
        word_count = count_words(fileContents)
        chars_data = char_count(fileContents)
        generate_report(args.path_to_file, word_count, chars_data)

        print(f"Read file at path: {f}. \n Contents: {fileContents}")

def count_words(content):
    word_count = len(content.split())
    
    return word_count

def char_count(base_string):
    char_dict = {}

    for char in base_string.lower():
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def generate_report(text_file, word_count, data):

    print(f"--- Begin report of {text_file} ---")
    print(f"{word_count} words found in the document")

    for letter, value in data.items(): 
        print(f"The '{letter} character was found {value} times'")

    print(f"--- End report of ---")

if __name__ == "__main__":
    main()