# Extract Keywords

Keywords play an important role when reading a long text to understand the subject and context of the text. Search engines also analyze an article’s keywords before indexing it.


-----

## Installation

```
pip install rake-nltk
```
Firstly import the `rake-nltk` library through the terminal that will help in the program.

-----

# Code Break:

```python
from rake_nltk import Rake
```

This line imports the `Rake` class from the `rake_nltk` library, which is used for keyword extraction using the RAKE (Rapid Automatic Keyword Extraction) algorithm.

```python
rake_nltk_var = Rake()
```

An instance of the `Rake` class is created and assigned to the variable `rake_nltk_var`. This instance will be used to perform keyword extraction.

```python
text = """ I am a programmer from India, and I am here to guide you 
with Data Science, Machine Learning, Python, and C++ for free. 
I hope you will learn a lot in your journey towards Coding, 
Machine Learning and Artificial Intelligence with me."""
```

A multi-line string containing the text from which keywords will be extracted is assigned to the variable `text`.

```python
rake_nltk_var.extract_keywords_from_text(text)
```

The `extract_keywords_from_text` method is called on the `Rake` instance, and it takes the provided text as input. This method preprocesses the text and extracts potential keywords using the RAKE algorithm.

```python
keyword_extracted = rake_nltk_var.get_ranked_phrases()
```

The `get_ranked_phrases` method is called on the `Rake` instance to obtain the ranked phrases based on their significance as keywords. The result is assigned to the variable `keyword_extracted`.

```python
print(keyword_extracted)
```

The extracted keywords are printed to the console. These keywords are ranked based on their significance in the input text.

-----