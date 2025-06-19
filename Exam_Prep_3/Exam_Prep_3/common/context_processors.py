# app/context_processors.py
from Exam_Prep_3.author.models import Author


def author_profile(request):

    return { 'author_profile': Author.objects.exists() }