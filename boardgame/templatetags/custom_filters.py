from django import template
import re

register = template.Library()

@register.filter
def to_snake_case(value: str) -> str:
    return re.sub(" ", "_", value).lower()