import datetime
from translation_history import TranslationHistory
import translators as ts


class Translator:
    @staticmethod
    def translate_text(tr_history: TranslationHistory):
        tr_history.trg_text = ts.translate_text(query_text=tr_history.src_text, from_language=tr_history.src_lang,
                                                to_language=tr_history.trg_lang)
        tr_history.date = datetime.datetime.now()
        return tr_history


if __name__ == '__main__':
    history1 = TranslationHistory("hello world", 'bing', 'fa', 'en')
    print(history1)
    print(ts.translate_text(history1.src_text, history1.translator, history1.src_lang, history1.trg_lang))
