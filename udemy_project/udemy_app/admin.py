from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import UserProfile, Category, Course, Lesson, Exam, Questions, Options, Assignment, Certificate, Review, Favorite, Cart


class QuestionsInlines(admin.TabularInline, TranslationInlineModelAdmin):
    model = Questions
    extra = 1

class OptionsInlines(admin.TabularInline):
    model = Options
    extra = 3

@admin.register(Exam)
class MovieAdmin(TranslationAdmin):
    inlines = [QuestionsInlines, OptionsInlines]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# переводтор + регистрация кылуу
@admin.register(UserProfile, Category, Course, Lesson, Assignment, Review)
class TranslateAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Certificate)
admin.site.register(Favorite)
admin.site.register(Cart)
