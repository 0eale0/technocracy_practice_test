from django.contrib import admin
from logic.models import User, Note, Category, NoteCategory, UserNote


admin.site.register(User)
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(NoteCategory)
admin.site.register(UserNote)