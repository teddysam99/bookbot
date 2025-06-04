def count_words(book):
	book = book.split()
	num_words = len(book)
	return num_words


def lower_case(book):
	dict = {}
	lowercasebook = book.lower()
	for l in lowercasebook:
		if l not in dict:
			dict[l] = 1
		else:
			dict[l] +=1
		
	return(dict)



def sort_on(dict):
    return dict["num"] 

def sorted_list(dict):
	list = []
	itemss = dict.items()

	for char, num in itemss:
		if char.isalpha() == True:
			dict2 = {}
			dict2["char"] = char
			dict2["num"] = num
			list.append(dict2)

	list.sort(reverse=True,key=sort_on)

	return list



