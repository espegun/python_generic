# Generic Python
The core language and it's standard library - no frameworks or external libraries.

## The installation

`> python -c "import sys; print(sys.executable)"` Where is the location of `python.exe` for the current interpreter.
`> python -c "import site; print(site.getsitepackages())"` Where is `site-packages` of the current interpreter.
`> pip show <package name>` Shows where a package is located.  
`> python -m pip show <package name>` Shows where a package is located (using the current interpreter).  

Check `PATH`.  


## ...

[Python style guide](https://www.python.org/dev/peps/pep-0008/) Les den, bruk det, få færre kommentarer i PR'ene.  
[Python patterns](https://github.com/faif/python-patterns)  

`my_dict.get("some_key", "return_if_key_is_missing")`  Great to set default values when reading from dicts.<br/>


`sys.path.append("../../xls-transformer")` Add the folder to `path`to make modules in other folders available for `import`<br/>.



`print("It's true!" if condition else "It's false")`  if-else one-liner.  

## OOP in Python
https://realpython.com/python3-object-oriented-programming/

## os
Use bash commands from Python - the `subprocess` module also has options.  
```
with os.popen("ls -la") as f:
    output = f.read()
print(output)
```


## Sorting
```
from datetime import date
import datetime
my_items = [{"name": "Mathias", "dob": "06.11.2018"},
            {"name": "Espen", "dob": "27.11.1977"},
            {"name": "Gro", "dob": "16.02.1978"}]
sorted_items = sorted(my_items, key=lambda item: datetime.datetime.strptime(item["dob"], "%d.%m.%Y").date())
```

## Regular expressions
`recomp = re.compile(r'(a(.*)(c.*)\s')` # Compiling first is quicker  
`match_obj = recomp.match('abbcde f')` # Must match start.  
`match_obj.group(x)` x=None: "abbcde", x=1: "bb", x=2: "cde"  
`first, second = match_obj.groups()` ('bb', 'cde')  
`match_obj = re.search(r"a(.*)(c.*)\s", "zabbcde f")`  Match anywhere  
`new_text = re.sub(r"a", "A", "abcabc")`  AbcAbc  
`re.findall(r"a(bc.)d", "bc1bc2abc3abc4d")`  List of params  
`re.sub(r"(<A>.*</A>)(.*)(<B>.*</B>)", r"\3\2\1", r"<A>Aa</A>_<B>Bb</B>")`  

See examples of match, findall and sub in the [regex_testing](https://github.com/espegun/python_generic/tree/main/regex_testing) directory.


```
content = "xAbcdA___A123_Adsad"
PATTERN = r"A(.*?)A"
print(re.findall(PATTERN, content))
```  
--> `['bcd', '123_']` With non-greedy pattern (`?`), '?' <-- Grab as little as possible.  
--> `['bcdA___A123_']` With greedy pattern (no `?`)  


## Itertools
Get all the combinations of two lists  
```
years = [2014, 2015, 2016]
chars = list("ABC")
for y, c in product(years, chars):
    print(y, c)
```


## Generators
`next(iterator, default)` Returns the next item in `iterator` and the `default` if exhausted. May use it to find a single element in a list:  
`element = next((element = next((j for j in my_list if j.name == "Something"), None)`  

## Decorators
Add a wrapper function around another function, often used for logging and timing.  
[Tutorial](https://www.datacamp.com/community/tutorials/decorators-python)  
[Why decorators are pure genius](https://towardsdatascience.com/why-decorators-in-python-are-pure-genius-1e812949a81e) **READ IT**   
[Øyvind anbefale denne videoen om decorators](https://www.youtube.com/watch?v=MjHpMCIvwsY)  
[Repo example file](https://github.com/espegun/python_generic/blob/main/decorators.py)  
[Great premade decorators](https://towardsdatascience.com/10-fabulous-python-decorators-ab674a732871)  

## Links
[The Zen of Python - forklart](https://python.plainenglish.io/pythons-rules-programming-by-the-creator-of-the-code-26a6201ade4)  
[The ultimate cheat sheet - a README](https://github.com/gto76/python-cheatsheet)  
[Importany Python concepts LES](https://dacus-augustus.medium.com/top-12-most-important-python-concepts-24f59945a409)
[Installing Python on Ubuntu](http://ubuntuhandbook.org/index.php/2020/10/python-3-9-0-released-install-ppa-ubuntu/)

TBD: os module
`src_dir = os.path.join(os.getcwd(), "test", "src")`  
    

TBD: JSON
[Dette kan du, men sjekk det siste tipset](https://medium.com/pythonland/6-tricks-to-effectively-use-json-in-python-3d66381a71ea)
TBD:
Generelt eller i pysqlite3. SQL.
