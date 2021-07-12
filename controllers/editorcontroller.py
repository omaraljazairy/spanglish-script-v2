import logging
from models.language import Language
from models.category import Category
from models.translation import Translation
from models.sentence import Sentence
from models.verb import Verb
from models.word import Word
from dataclasses import dataclass

@dataclass
class EditorController:
    """ responsable for the edit functions required by the view and returned 
    by the models. """

    language: Language = None
    category: Category = None
    translation: Translation = None
    word: Word = None
    sentence: Sentence = None
    verb: Verb = None

    logger = logging.getLogger('controller')
    logger.info("controller started")


    def insert_word(self, word: str, language_name:str, language_code:str, category: str, translation: str) -> bool:
        """ takes four required params, word, language_code and category and
         translation. It will return true if success, else false. """

        self.logger.debug("word received: %s", word)
        self.logger.debug("language_code received: %s", language_code)
        self.logger.debug("category received: %s", category)
        self.logger.debug("translation received: %s", translation)

        language_object = Language(name=language_name, code=language_code)
        category_object = Category(category=category)
        new_word = Word(word=word, category=category_object)
        translation_object = Translation(language=language_object, translation=translation, word=new_word)

        self.logger.debug("translation object: %s", translation_object)


        return True



