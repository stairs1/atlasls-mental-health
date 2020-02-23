from django.contrib import admin

from api.models import Survey, Answer, JournalStub

admin.site.register(Survey)
admin.site.register(Answer)
admin.site.register(JournalStub)
