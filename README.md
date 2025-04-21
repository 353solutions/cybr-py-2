# Python Workshop @ CyberArk

Miki Tebeka
📬 [miki@353solutions.com](mailto:miki@353solutions.com), 𝕏 [@tebeka](https://twitter.com/tebeka), 👨 [mikitebeka](https://www.linkedin.com/in/mikitebeka/), ✒️[blog](https://www.ardanlabs.com/blog/)

[Syllabus](https://docs.google.com/document/d/1p_GIXY2FXOauoPM2QITLdi5UpoCo6oH-9NdOlXehv6w/edit)

#### Shameless Plugs

- [LinkedIn Learning Classes](https://www.linkedin.com/learning/instructors/miki-tebeka)
- [Books](https://pragprog.com/search/?q=miki+tebeka)

---

## Day 1: Getting Started

### Agenda

- Intro to Python and its ecosystem
- Working with the Python REPL
- Working with text: str/bytes, formatting
- Collections: list, tuple, dict & set
- Slicing & List comprehensions
- Control flow & logic
- Iteration & iteration utilities

### Code

TBD


<!--
### Exercises

#### Word Frequency

What is the most common word in `data/road.txt` ignoring case?

#### Stocks

Look at data/stocks.csv

You can read the content using the following code:

```python
with open('data/stocks.csv') as fp:
    data = fp.read()
```

Answer the following questions:
- Print sorted unique list of symbols (CSCO ...)
- Print how many stocks of CSCO we own (symbol)
- Print how much money we've invested (price * volume)

Using the data from `data/prices.csv`, print how much we've gained or lost.
-->

### Links

- [How to Think Like a Computer Scientist: Interactive Edition](https://runestone.academy/ns/books/published/thinkcspy/index.html)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
    - [text](https://docs.python.org/3/tutorial/introduction.html#text)
    - [lists](https://docs.python.org/3/tutorial/introduction.html#lists)
    - [Errors & exceptions](https://docs.python.org/3/tutorial/errors.html)
- [pythontutor](https://pythontutor.com/) - Visualize Python execution
- [itertools module](https://docs.python.org/3/library/itertools.html#itertools.count)
    - Read and understand the "Itertools Recipes" section
- Iterators
    - [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators) in the Python tutorial
    - [itertools](https://docs.python.org/3/library/itertools.html) - Iterator utilities (good reading ☺)
    - [Generator Tricks for System Programmers](http://www.dabeaz.com/generators/)
    - [Generators: The Final Frontier](https://www.youtube.com/watch?v=D1twn9kLmYg)
- [Python Type Conversion](https://www.mermaidchart.com/raw/493b268f-89ca-4129-b83a-8d8cd64602e0?theme=light&version=v0.1&format=svg)
- [List of Unicode Characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
- [Project Euler](https://projecteuler.net/)
- [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Google Colab](https://colab.research.google.com/) - Notebooks in the cloud
- Programming Exercises:
    - [exercism](https://exercism.org/tracks/python/exercises)
    - [LeetCode](https://leetcode.com/problemset/all/)
    - [Codewars](https://www.codewars.com/kata)
    - [Project Euler](https://projecteuler.net/archives)


### Data & Other

- [http.log.gz](data/http.log.gz)
- [road.txt](data/road.txt)
- ☺
- ♡

<!--
---

# Day 2: Working with Python

### Agenda

- List comprehensions
- Defining & calling functions
- Working with files
- Handling resources using `with`
- Error handling
- Modules & packages (imports)
- Calling REST APIs


### Code

TBD


### Exercises

#### Count Errors

How many requests in [http.log.gz](data/http.log.gz) resulted in an error (status code >= 400)?
Use `gzip.open` to read the file.

Example lines:
```
uplherc.upl.com - - [01/Aug/1995:00:00:08 -0400] "GET /images/ksclogo-medium.gif HTTP/1.0" 304 0
uplherc.upl.com - - [01/Aug/1995:00:00:08 -0400] "GET /images/MOSAIC-logosmall.gif HTTP/1.0" 304 0
uplherc.upl.com - - [01/Aug/1995:00:00:08 -0400] "GET /images/USA-logosmall.gif HTTP/1.0" 304 0
ix-esc-ca2-07.ix.netcom.com - - [01/Aug/1995:00:00:09 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1713
uplherc.upl.com - - [01/Aug/1995:00:00:10 -0400] "GET /images/WORLD-logosmall.gif HTTP/1.0" 304 0
slppp6.intermind.net - - [01/Aug/1995:00:00:10 -0400] "GET /history/skylab/skylab.html HTTP/1.0" 200 1687
piweba4y.prodigy.com - - [01/Aug/1995:00:00:10 -0400] "GET /images/launchmedium.gif HTTP/1.0" 200 11853
slppp6.intermind.net - - [01/Aug/1995:00:00:11 -0400] "GET /history/skylab/skylab-small.gif HTTP/1.0" 200 9202
```

<!--
#### Stock Tweets

related

#### Generate QR Code

Write a function `generate_qrs(input_file, output_dir)` that will generate a QR code for data in `input_file` and save it in `output_dir`.

- Use [QR Code Generator API](https://goqr.me/api/doc/create-qr-code/) to generate the QR code
- QR should contains `MCARD` format
- Output file name should be `first-last.png` (e.g. `bugs-bunny.png`)

Example MCARD: `MECARD:N:Bunny,Bugs;TEL:555-555-5555;EMAIL:bugs@looney.com;;`
Example API: `https://api.qrserver.com/v1/create-qr-code/?data=MECARD:N:Bunny,Bugs;TEL:555-555-5555;EMAIL:bugs@looney.com;;`
-->
