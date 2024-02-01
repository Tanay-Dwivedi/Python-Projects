# Language Translator

Google Translator API helps us to create our translator using Python.

-----

## Installation

```
pip install google-trans-new
```
Firstly import the `google-trans-new` library through the terminal that will help in the program.

-----

## Code Break:

```python
from google_trans_new import google_translator
import streamlit as st
```

These lines import the necessary libraries and modules. `google_translator` is used for language translation, and `streamlit` is used for creating the web application.

```python
translator = google_translator()
```

An instance of the `google_translator` class is created.

```python
st.title("Language Translator")
```

The title "Language Translator" is displayed at the top of the Streamlit web app.

```python
text = st.text_input("Enter a text")
```

A text input widget is provided for the user to enter text.

```python
translate = translator.translate(text, lang_tgt="fr")
```

The entered text is translated into French using the `google_translator` instance.

```python
st.write(translate)
```

The translated text is displayed on the Streamlit web app.

In summary, this script creates a simple Streamlit web application for language translation using the `google_trans_new` library. Users can enter text, and the script translates the text into French and displays the translated text on the web app.

-----