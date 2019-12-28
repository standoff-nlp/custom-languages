12/28 ~ Now that we are able to create new language objects, I would like greater clarity on what files are needed.
To look at the existing language objects, I crawled the spacy/lang directory and gathered all of the imported files. 

Here is the full range of data imported for language objects:
STOP_WORDS,
TOKENIZER_SUFFIXES, 
TOKENIZER_PREFIXES, 
TOKENIZER_INFIXES,
TOKENIZER_EXCEPTIONS,
LEX_ATTRS,
NORM_EXCEPTIONS,
MORPH_RULES,
SYNTAX_ITERATORS,
TAG_MAP

For reference, here is my code:
```python
from pathlib import Path
import spacy
import pandas as pd

spacy_path = Path(spacy.__file__.replace('__init__.py',''))
spacy_langs = spacy_path / 'lang'
langs = [x for x in spacy_langs.iterdir() if x.is_dir()] 
data = {}


for lang in langs:
	lang_name = str(lang).split('/')[-1]
	data[lang_name]= []
	try:
	    init = lang / '__init__.py'
	    with init.open() as f: 
	    	[data[lang_name].append(f.readline())for line in f if 'from' in line ]
	    
	except Exception as e:
		print(e)

df = pd.DataFrame(list(data.items())) 
df.to_csv('spacy_imports.csv')
```
