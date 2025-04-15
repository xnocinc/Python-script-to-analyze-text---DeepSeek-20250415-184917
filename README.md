# Python script to analyze text - DeepSeek

**Model Used:** `deepseek-r1:latest`

**Filename:** `text-analyzer.py`

**Prompt:**

```
Write a Python script that counts the number of words, sentences, and characters in a given text.
```

**Reasoning:**

```
Okay, so I need to write a Python script that counts the number of words, sentences, and characters in a given text. Let me think about how to approach this.

First, for counting words, I can split the text into words using the split() method. But wait, what if there are multiple spaces or punctuation? Oh right, because sometimes sentences end with periods, commas, etc., so splitting on whitespace alone might not be enough. Hmm, maybe I should first remove any leading and trailing whitespace and then split on non-word characters.

Wait, actually, the split() method without arguments splits on any whitespace and returns a list of words. So if I use text.split(), that should handle multiple spaces by treating them as a single separator. But wait, what about apostrophes in contractions like "don't"? Splitting would treat it as part of a word, which is correct.

So for words, len(text.split()) should give the count.

Next, sentences. Sentences are typically separated by periods. So I can split on '.' and then filter out any empty strings that might result from trailing punctuation. For example, if the text ends with a period, splitting would include an empty string after it. So I'll split on '.', strip each substring of whitespace, and count only those that aren't empty.

So something like [s.strip() for s in text.split('.') if s.strip()] gives me the list of sentences. Then len() of that list is the number of sentences.

For characters, it's straightforward: len(text) gives the total number of characters, including spaces, punctuation, etc.

Wait, but what about whitespace characters? Well, using len(text) includes all characters as they are, so that's correct.

Putting it all together:

- words = len(text.split())
- sentences = len([s.strip() for s in text.split('.') if s.strip()])
- characters = len(text)

Then print the results.

I should also consider case sensitivity and other edge cases, like empty strings or texts with no words/sentences. But split() handles that by returning an empty list, which when passed to len(), gives 0 correctly.

So I'll write the code accordingly.
```