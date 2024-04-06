class TranslationHistory:

    def __init__(self, src_text, translator, trg_lang, src_lang):
        self.src_text = src_text
        self.translator = translator
        self.trg_text = ""
        self.src_lang = src_lang
        self.trg_lang = trg_lang
        self.date = None

    def __str__(self):
        self_str = "\n"
        for attribute, value in self.__dict__.items():
            self_str += f"\033[92m{attribute.strip('_').replace('_', ' ')}: \033[93m{value}\033[0m\n"
        return self_str
