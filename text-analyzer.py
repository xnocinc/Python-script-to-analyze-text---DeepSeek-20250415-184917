python
text = input("Enter text: ")
words = len(text.split())
sentences = len([s.strip() for s in text.split('.') if s.strip()])
characters = len(text)
print(f"Words: {words}")
print(f"Sentences: {sentences}")
print(f"Characters: {characters}")