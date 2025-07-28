import sys
from stats import get_book_text
from stats import count_char_nums
from stats import sort_my_dict
def main():
    num_arts = len(sys.argv)
    if not (num_arts==2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    test_words = get_book_text(sys.argv[1])      
    output1 = f'{len(test_words.split())}'
    #print(output1)
    output2 = count_char_nums(sys.argv[1])
    #print(output2)
    output3 = sort_my_dict(output2)
   # print(output1)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {output1} total words')
    print('--------- Character Count -------')
    for value in output3:
        print(f'{value['char']}: {value['num']}')
    print('============= END ===============')    
main()