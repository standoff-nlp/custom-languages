12/28 ~ Now that we are able to create new language objects, I would like greater clarity on what files are needed.
To look at the existing language objects, I crawled the spacy/lang directory and gathered all of the imported files. 

Here is the full range of data imported for language objects:  
- NORM_EXCEPTIONS (de,hu,lb,uk,tr,fr,ru,ca,nl,hr,el,sr,fa,nb,es,sv,it,pl,lt,ro,xx,id,th,da,fi,vi,en)    
- STOP_WORDS (lb,uk,pt,tr,fr,ca,ga,bn,nb,pl,it,tl,ro,da,fi,en)
- LEX_ATTRS (hi,ar,ru,nl,el,sr,fa,es,te,ta,si,lb,zh,ur)    
- TAG_MAP (zh,ur,pt, ko,ja,el,fa,es,sv,it,lt,ro,th)  
- TOKENIZER_INFIXES (hu,tt,pt,fr,bn,sv,it,pl,id)  
- TOKENIZER_EXCEPTIONS (tt,ar,ru,nl,el,sr,tl,)    
- TOKENIZER_SUFFIXES (hu,fr,bn,sv,id),     
- TOKENIZER_PREFIXES (hu,pt,bn,id),     
- SYNTAX_ITERATORS (de, el, nb,sv,id)    
- MORPH_RULES (en, sv,da),  


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
