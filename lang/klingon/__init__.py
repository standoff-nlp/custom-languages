# new language from scratch
from spacy.language import Language

# https://spacy.io/usage/adding-languages#language-subclass
class KlingonDefaults(Language.Defaults):
    pass
    '''lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "custom_sr"
    lex_attr_getters[NORM] = add_lookups(
        Language.Defaults.lex_attr_getters[NORM], BASE_NORMS, NORM_EXCEPTIONS
    )
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS'''


class Klingon(Language):
    lang = "klingon"
    Defaults = KlingonDefaults


__all__ = ["Klingon"]
