import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open("file.pdf", "rb"))

speaker = pyttsx3.init()

all_text = ""

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    all_text += text
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()

engine = pyttsx3.init()
engine.save_to_file(all_text, "audio.mp3")
engine.runAndWait()
