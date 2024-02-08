# Create an Audiobook 

An audiobook is a recording or voiceover of a book or other work read aloud. You can listen to audiobooks on any smartphone, tablet, computer, home speaker system, or in-car entertainment system.

PyPDF2 allows manipulation of pdf in memory. This python library is capable of tasks such as:

- extract information about the document, such as title, author, etc.
- document division by page
- merge documents per page
- cropping pages
- merge multiple pages into one page
- encrypt and decrypt PDF files

-----

## Installation

```
pip install PyPDF2 pyttsx3
```
Firstly import the `PyPDF2 pyttsx3` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import PyPDF2
import pyttsx3
```
Imports the necessary libraries `PyPDF2` for handling PDF files and `pyttsx3` for text-to-speech conversion.

```python
pdfReader = PyPDF2.PdfFileReader(open("file.pdf", "rb"))
```
Opens a PDF file named "file.pdf" in binary read mode and creates a `PdfFileReader` object to read its contents.

```python
speaker = pyttsx3.init()
```
Initializes the text-to-speech engine using `pyttsx3`.

```python
all_text = ""
```
Initializes an empty string to store all the extracted text from the PDF pages.

```python
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    all_text += text
    speaker.say(text)
    speaker.runAndWait()
```
Iterates over each page in the PDF file. Extracts the text content from each page using `getPage(page_num).extractText()` method. Appends the extracted text to the `all_text` variable. Uses the `say()` method of the `speaker` object to convert the text to speech and the `runAndWait()` method to wait until the speech is completed for each page.

```python
speaker.stop()
```
Stops the speech playback.

```python
engine = pyttsx3.init()
```
Initializes a new instance of the text-to-speech engine using `pyttsx3`.

```python
engine.save_to_file(all_text, "audio.mp3")
```
Saves the synthesized speech from the `all_text` variable to an audio file named "audio.mp3" using the `save_to_file()` method.

```python
engine.runAndWait()
```
Runs the text-to-speech engine to synthesize the speech and save it to the audio file specified. Then waits until the speech is completed.

```python
```



-----