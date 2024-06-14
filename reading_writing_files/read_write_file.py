# f = open("funny.txt", "r")
# f_out = open("funny_wc.txt", "w")
# for line in f:
#     tokens = line.split(' ')
#     f_out.write(f"wordCount: {str(len(tokens))} {line}")

# f.close()
# f_out.close()

# with open("funny.txt", "r") as f:
#     print(f.read())

# print(f.closed)


def convert_smileys(text):
    text = text.replace(":(", "🙁")  # Convert :( to 🙁
    text = text.replace(":)", "🙂")  # Convert :) to 🙂
    return text

# Example usage:
text_with_smileys = "I feel sad :( but also happy :)"
converted_text = convert_smileys(text_with_smileys)
print(converted_text)
