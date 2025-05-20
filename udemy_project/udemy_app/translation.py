from modeltranslation.translator import TranslationOptions, register
from .models import UserProfile, Category, Course, Lesson, Assignment, Exam, Questions, Options, Review


@register(UserProfile)
class TeacherProfileTranslationOptions(TranslationOptions):
    fields = ('bio',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'course_description')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson_title',)

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('assignment_title', 'assignment_description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('exam_title',)

@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('question_text',)

@register(Options)
class OptionsTranslationOptions(TranslationOptions):
    fields = ('option_text',)

@register(Review)
class ReviewTranslateOptions(TranslationOptions):
    fields = ('comment',)
