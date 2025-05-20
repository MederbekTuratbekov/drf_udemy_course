from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from nested_admin import NestedTabularInline, NestedModelAdmin
from .models import UserProfile, Category, Course, Lesson, Exam, Questions, Options, Assignment, Certificate, Review, Favorite, Cart


# Инлайн для Options (связь с Questions)
class OptionsInlines(NestedTabularInline, TranslationInlineModelAdmin):
    model = Options
    extra = 3

# Инлайн для Questions (связь с Exam)
class QuestionsInlines(NestedTabularInline, TranslationInlineModelAdmin):
    model = Questions
    extra = 1
    inlines = [OptionsInlines]  # Вложение Options в Questions

@admin.register(Exam)
class ExamAdmin(NestedModelAdmin, TranslationAdmin):
    inlines = [QuestionsInlines]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# Остальной код без изменений
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
