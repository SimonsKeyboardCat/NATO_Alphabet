import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
data.to_dict()
pandas_dict = pandas.DataFrame(data)

while True:
    word = input("Enter a word: ")
    word_list = []
    for letter in word:
        temp = letter.capitalize()
        word_list.append(temp)

    code_list = []
    for char in word_list:
        for (index, row) in pandas_dict.iterrows():
            if row.letter == char:
                code_list.append(row.code)

    print(code_list)
