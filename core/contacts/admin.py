from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'message_id',
        'name',
        'subject',
        'reference',
        'message',
        'last_updated',
        'publish',
    ]
    list_display_links = [
        'message_id',
        'name',
        'subject',
        'reference',
        'message',
        'last_updated',
        'publish',
    ]
    list_filter = ['publish']
    readonly_fields = ['message_id']
    search_fields = [
        'message_id',
        'name',
        'subject',
        'reference',
        'message',
        'last_updated',
        'publish',
    ]
    list_per_page = 50
    view_on_site = True
    show_full_result_count = True
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    fields = [
        'message_id',
        'name',
        'subject',
        'reference',
        'message',
        'last_updated',
        'publish',
    ]


# register model in admin
admin.site.register(Contact, ContactAdmin)
