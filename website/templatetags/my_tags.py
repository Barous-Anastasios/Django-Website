from django import template

register = template.Library()

@register.simple_tag
def get_correct_counts(qs, sub_category):
    qs = qs.filter(sub_category=sub_category)
    return qs.count()

register.filter('get_correct_counts', get_correct_counts)

@register.simple_tag
def get_correct_subs(qs, sub_category):
    qs = qs.filter(sub_category=sub_category).order_by("year")
    return qs

register.filter('get_correct_subs', get_correct_subs)
