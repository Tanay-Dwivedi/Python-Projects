# Generate Text

Text generation involves generating text using machine learning techniques. The purpose of text generation is to automatically generate text that is indistinguishable from a text written by a human.

-----

## Installation

```
pip install pipeline transformers
```
Firstly import the `pipeline transformers` libraries through the terminal that will help in the program.

-----

## Code Break:

This code utilizes the Hugging Face `transformers` library to generate text using the GPT-2 model. Let's break it down:

```python
from transformers import pipeline
```
Imports the `pipeline` function from the `transformers` library, which allows for easy access to various natural language processing tasks.

```python
model = pipeline("text-generation", model="gpt2")
```
Creates a text generation pipeline using the GPT-2 model. This pipeline will generate text based on the input provided.

```python
sentence = model(
    "Hi, My name is John Cena, I am here",
    do_sample=True,
    top_k=50,
    temperature=0.9,
    max_length=100,
    num_return_sentences=2,
)
```
Generates text based on the input sentence "Hi, My name is John Cena, I am here" using the GPT-2 model. The parameters specified:
- `do_sample=True`: Allows for sampling from the predicted probability distribution.
- `top_k=50`: Limits the sampling to the top 50 most likely tokens.
- `temperature=0.9`: Controls the randomness of the sampling process. A higher temperature results in more randomness.
- `max_length=100`: Specifies the maximum length of the generated text.
- `num_return_sentences=2`: Generates 2 different sentences.

```python
for i in sentence:
    print(i["generated_text"])
```
Iterates over the generated sentences and prints each one. Each item in `sentence` is a dictionary containing the generated text under the key "generated_text". This loop prints out the generated sentences.

-----