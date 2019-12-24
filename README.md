# custom-languages

An experiment to see if it is possible to create a library of custom language objects that could be developed and imported independently from spaCy. 

12/24: currently not working 
```python 
from lang.klingon import Klingon
nlp = Klingon()  
```
will lazy load a new Language object.  However, if we add stop_words, they will not be included.  With nlp.to_disk(path) we can save the object to disk and load it with spacy.load(path).  We run into a conflict at that point:
```bash
~/anaconda3/envs/spacy22/lib/python3.7/site-packages/spacy/util.py in get_lang_class(lang)
     86             module = importlib.import_module(".lang.%s" % lang, "spacy")
     87         except ImportError as err:
---> 88             raise ImportError(Errors.E048.format(lang=lang, err=err))
     89         LANGUAGES[lang] = getattr(module, module.__all__[0])
     90     return LANGUAGES[lang]

ImportError: [E048] Can't import language klingon from spacy.lang: No module named 'spacy.lang.klingon'
```
This suggests the need for a custom load() function.
