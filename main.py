import sys

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	if len(sys.argv) != 2: 
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	
	path = sys.argv[1]
	book = get_book_text(path)
	return book


from stats import count_words
from stats import lower_case
from stats import sorted_list

book = main()
count=count_words(book)
char=lower_case(book)



slc =sorted_list(char)

print(f"============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print(f"----------- Word Count ----------")
print(f"Found {count} total words ")
print(f" --------- Character Count -------")
for item in slc:
	if item["char"].isalpha(): 
		print (f"{item['char']}: {item['num']}")
print(f"============= END ===============")



