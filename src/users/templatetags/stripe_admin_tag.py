from django import template
register = template.Library()
from django.contrib.admin.templatetags import admin_modify

@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
    context = context or {}
    ctx = admin_modify.submit_row(context)
    if "show_send_welcome_email" in context:
        ctx["show_send_welcome_email"] = context["show_send_welcome_email"]
    return  ctx
