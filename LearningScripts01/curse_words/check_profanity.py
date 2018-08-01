def read_text ():
    quotes = open("/home/dhiraj/Python/Repositories/Python/LearningScripts01/curse_words/movie_quotes.txt")
    content_of_file =quotes.read()
    print(content_of_file)
    quotes.close()

read_text()
