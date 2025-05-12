def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	path = "./books/frankenstein.txt"
	bookContent = get_book_text(path)
	return(bookContent)

def count_words():
	num_words = 0
	text = "Fly me to the moon and let me play amoung the stars"
	words = text.split()
	if words in text:
		num_words +=1

	print(f"{num_words} words found in document")

count_words()
