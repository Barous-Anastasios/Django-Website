from modeltranslation.translator import translator, TranslationOptions
from .models import *

class PersonTranslationOptions(TranslationOptions):
	fields = ("name", "description", "address",)

translator.register(Person, PersonTranslationOptions)

class PageTranslationOptions(TranslationOptions):
	fields = ("title", "friendlyurl", "short_title", "long_title")

translator.register(Page, PageTranslationOptions)

class LabDetailsTranslationOptions(TranslationOptions):
	fields = ("name", "description", "address")

translator.register(LabDetails, LabDetailsTranslationOptions)

class ContentTranslationOptions(TranslationOptions):
	fields = ("title", "description", "author")

translator.register(Content, ContentTranslationOptions)
