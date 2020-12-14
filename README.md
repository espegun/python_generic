# python_generic
Main Python functionality - no frameworks or special libraries


[Python style guide](https://www.python.org/dev/peps/pep-0008/) Les den, bruk det, få færre kommentarer i PR'ene.<br/>

`my_dict.get("some_key", "return_if_key_is_missing")`  Great to set default values when reading from dicts.<br/>


`sys.path.append("../../xls-transformer")` Add the folder to `path`to make modules in other folders available for `import`<br/>.



`print("It's true!" if condition else "It's false")`  if-else one-liner.  


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




[Installing Python on Ubuntu](http://ubuntuhandbook.org/index.php/2020/10/python-3-9-0-released-install-ppa-ubuntu/)<br/>
