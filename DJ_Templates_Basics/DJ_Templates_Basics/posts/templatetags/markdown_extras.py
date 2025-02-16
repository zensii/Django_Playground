# pip install markdown

import markdown
from django import template
from django.utils.safestring import mark_safe   #marks_safe prevents injection attacks by disabling scripts

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))