# Python Workshop @ CyberArk

Miki Tebeka
📬 [miki@353solutions.com](mailto:miki@353solutions.com), 𝕏 [@tebeka](https://twitter.com/tebeka), 👨 [mikitebeka](https://www.linkedin.com/in/mikitebeka/), ✒️[blog](https://www.ardanlabs.com/blog/)

[Syllabus](https://docs.google.com/document/d/1p_GIXY2FXOauoPM2QITLdi5UpoCo6oH-9NdOlXehv6w/edit)

#### Shameless Plugs

- [LinkedIn Learning Classes](https://www.linkedin.com/learning/instructors/miki-tebeka)
- [Books](https://pragprog.com/search/?q=miki+tebeka)

[Colab notebook](https://colab.research.google.com/drive/11YGDyd5RB_qE3tTrB8RJQX5tPE_NMgUU)

---

## Day 1: Getting Started

### Agenda

- Intro to Python and its ecosystem
- Working with the Python REPL
- Working with text: str/bytes, formatting
- Iteration & iteration utilities

### Code

- [basics.py](basics.py) - Variables, conditions, looping
- [strings.py](strings.py) - Working with text
- [looping.py](looping.py) - Looping utilities

### Exercises

Solve [Euler 4](https://projecteuler.net/problem=4)  
Solution: 906609

Solve [Euler 8](https://projecteuler.net/problem=8)  
Solution: 23514624000


### Links

- IDEs
    - [PyCharm](https://www.jetbrains.com/pycharm/)
    - [VSCode](https://code.visualstudio.com/) + [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Google Colab](https://colab.research.google.com/) - Notebooks in the cloud
- [How to Think Like a Computer Scientist: Interactive Edition](https://runestone.academy/ns/books/published/thinkcspy/index.html)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
    - [text](https://docs.python.org/3/tutorial/introduction.html#text)
    - [lists](https://docs.python.org/3/tutorial/introduction.html#lists)
    - [Errors & exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Type Conversion](https://www.mermaidchart.com/raw/493b268f-89ca-4129-b83a-8d8cd64602e0?theme=light&version=v0.1&format=svg)
- [List of Unicode Characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
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

# Day 2: Working with Python

### Agenda

- Collections: list, tuple, dict & set
- Slicing & List comprehensions
- Control flow & logic
- List comprehensions
- Defining & calling functions
- Working with files


### Code

- [euler4.py](euler4.py)
- [euler8.py](euler8.py)
- [data_types.py](data_types.py) - Data types (list, tuple, dict)
- [list_comprehension.py](list_comprehension.py) - List comprehension
- [funcs.py](funcs.py) - Defining & calling functions
- [sync.py](sync.py) - Working with files


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

### Links

- [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)
- [List comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) in the Python tutorial
- [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) in the Python tutorial
- [pathlib](https://docs.python.org/3/library/pathlib.html) module - Handling file paths
- [shutil](https://docs.python.org/3/library/shutil.html) module - shell like utlities
- [mypy](https://mypy.readthedocs.io/en/stable/) - Static type checker
- [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)

### Data & Other

- [http.log.gz](data/http.log.gz)
- `https://api.github.com/users/tebeka`

# Day 3: Working with Python

### Agenda

- Handling resources using `with`
- Error handling
- Modules & packages (imports)
- Calling REST APIs
- OO Basics
	- Classes and instances
	- Methods
	- Special methods
	- Inheritance


### Code

TBD


### Exercises


#### Stock Tweets

Write a function `related_stocks(symbol)` that returns a list of stocks mentioned when you query this symbol on stocktweets.com.

To find about `AAPL` use `https://api.stocktwits.com/api/2/streams/symbol/AAPL.json`


### Links

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) in the Python tutorial
- [Modules](https://docs.python.org/3/tutorial/modules.html) in the Python tutorial
- [JSON](https://www.json.org/json-en.html) specification
- Python's [json](https://docs.python.org/3/library/json.html) module
- [A typical HTTP session](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Session)
- [Classes](https://docs.python.org/3/tutorial/classes.html) in the Python tutorial
- [Beyond PEP8](https://www.youtube.com/watch?v=wf-BqAjZb8M)


### Data & Other

- `https://api.github.com/users/tebeka`
