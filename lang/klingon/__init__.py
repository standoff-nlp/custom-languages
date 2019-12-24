# The four files below can be edited for the new language
from spacy.lang.klingon.stop_words import STOP_WORDS
from spacy.lang.klingon.tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from spacy.lang.klingon.norm_exceptions import NORM_EXCEPTIONS
from spacy.lang.klingon.lex_attrs import LEX_ATTRS

# These files are part of spaCy and do not need to be edited
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from spacy.lang.norm_exceptions import BASE_NORMS
from spacy.language import Language
from spacy.attrs import LANG, NORM
from spacy.util import update_exc, add_lookups


# https://spacy.io/usage/adding-languages#language-subclass
class KlingonDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "klingon"
    lex_attr_getters[NORM] = add_lookups(
        Language.Defaults.lex_attr_getters[NORM], BASE_NORMS, NORM_EXCEPTIONS
    )
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS


class Klingon(Language):
    lang = "klingon"
    Defaults = KlingonDefaults


__all__ = ["Klingon"]
