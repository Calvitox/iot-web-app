from django import template
import json
register = template.Library()

@register.filter("jsonify")
def jsonify(value):
    return json.dumps(value)