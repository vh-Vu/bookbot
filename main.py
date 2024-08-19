def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    result = {}
    lower_string = string.lower()
    for char in lower_string:
        if char in result:
            result[char]+=1
        else:
            result[char]= 1
    return result

def print_a_report(path_to_file,words,report):
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{words} words found in the document \n')
    for record in report:
        print(f"The '{record[0]}' character was found {record[1]} times")
    print('--- End report ---')

def is_alpha_and_sort(characters):
    ls = []
    for char in characters:
        if char.isalpha(): #if alpha so list will append a tuple
            ls.append((char,characters[char]))
    return sorted(ls, reverse=True,key=lambda x: x[1])

def main():
    path_to_file = 'books/frankenstein.txt'
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
        f.close()
    string = count_characters(file_contents)
    ls = is_alpha_and_sort(string)
    print_a_report(path_to_file,count_words(file_contents),ls)

main()