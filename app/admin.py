from django.contrib import admin

from .models import Bolimlar,Fan,Vazifa,Question,Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Bolimlar)
admin.site.register(Fan)
admin.site.register(Vazifa)
admin.site.register(Question, QuestionAdmin)
