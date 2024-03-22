from django.contrib import admin

from .models import DeployedContract


class DeployedContractAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'contract_id',
        'last_updated',
    ]
    list_display_links = [
        'id',
        'contract_id',
        'last_updated',
    ]
    readonly_fields = [
        'contract_id',
        'last_updated',
    ]
    search_fields = [
        'id',
        'contract_id',
        'last_updated',
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
        'id',
        'contract_id',
        'last_updated',
    ]


# register model in admin
admin.site.register(DeployedContract, DeployedContractAdmin)
