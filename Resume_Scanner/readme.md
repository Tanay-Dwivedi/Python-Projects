# Resume Scanner

A resume scanner is an application that scans all the keywords on a resume to match the skills and qualifications needed for a particular job.

-----

## Installation

```
pip install resume-parser
```
Firstly import the `resume-parser` library through the terminal that will help in the program.

-----

## Code Break:

```python
def scan_resume(resume):
```

This line defines a function named `scan_resume` that takes a single parameter `resume`, representing the filename of a resume document.

```python
    from resume_parser import resumeparse
```

This line imports the `resumeparse` module from the `resume_parser` library.

```python
    data = resumeparse.read_file(resume)
```

The `resumeparse.read_file()` function is used to read information from the specified resume file (`resume`) and store it in the `data` variable.

```python
    for i, j in data.items():
```

This line starts a `for` loop that iterates through the key-value pairs in the `data` dictionary.

```python
        print(f"{i}:>>{j}")
```

Within the loop, this line prints each key-value pair in a formatted string to the console.

```python
scan_resume("resume.docx")
```

Finally, the function is called with the filename "resume.docx" to scan information from the provided resume file.

This script defines a function (`scan_resume`) that utilizes the `resumeparse` library to extract information from a resume document and then prints the extracted data. The function is then called with the filename "resume.docx" for demonstration purposes.

-----