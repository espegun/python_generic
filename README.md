# python_generic
Main Python functionality - no frameworks or special libraries


[Python style guide](https://www.python.org/dev/peps/pep-0008/) Les den, bruk det, få færre kommentarer i PR'ene.<br/>

`my_dict.get("some_key", "return_if_key_is_missing")`  Great to set default values when reading from dicts.<br/>


`sys.path.append("../../xls-transformer")` Add the folder to `path`to make modules in other folders available for `import`<br/>.



`print("It's true!" if condition else "It's false")`  One-liner if-else.  


## Regular expressions
`recomp = re.compile(r'(a(.*)(c.*)\s')` # Compiling first is quicker
`match_obj = recomp.match('abbcde f')` # Must match start.
`match_obj.group(x)` x=None: "abbcde", x=1: "bb", x=2: "cde"
`first, second = match_obj.groups()` ('bb', 'cde')
`match_obj = re.search(r"a(.*)(c.*)\s", "zabbcde f")` # Match anywhere
`new_text = re.sub(r"a", "A", "abcabc")` # AbcAbc
`re.findall(r"a(bc.)d", "bc1bc2abc3abc4d")`  # List of params
`re.sub(r"(<A>.*</A>)(.*)(<B>.*</B>)", r"\3\2\1", r"<A>Aa</A>_<B>Bb</B>")`












[Installing Python on Ubuntu](http://ubuntuhandbook.org/index.php/2020/10/python-3-9-0-released-install-ppa-ubuntu/)<br/>
