from django import template
from django.template import TemplateSyntaxError
import re

register = template.Library()

not_allowed_words = ['редиска', 'дурак']

@register.filter(name='censor_bad_words')
def censor_bad_words(value):
    if not isinstance(value, str):
        raise TemplateSyntaxError("Фильтр 'censor_bad_words' можно применять только к строкам.")

    for bad_word in not_allowed_words:
        bad_word_upper = bad_word.capitalize()
        bad_word_lower = bad_word.lower()

        def replace_word(match):
            word = match.group()
            length = len(word)
            return word[0] + '*' * (length - 1)

        pattern = re.compile(r'\b({}|{})\b'.format(bad_word_upper, bad_word_lower), re.IGNORECASE)

        value = pattern.sub(replace_word, value)
    return value
