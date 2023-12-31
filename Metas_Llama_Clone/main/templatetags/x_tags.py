from django import template
from main.models import question,answer

register = template.Library()


@register.simple_tag
def quess(id):
    print("Hello")
    x = question.objects.get(id = id)
    print(x.ques)
    return x.ques

@register.simple_tag
def anss(id):
    x = answer.objects.get(id = id)
    print(x.ans)
    return x.ans