from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'id',
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'show_likes',)
    list_editable = ('new_building',)
    list_filter = (
        'active',
        'new_building',
        'rooms_number',
        'floor',
        'has_balcony')
    raw_id_fields = ('liked_by',)

    def show_likes(self, obj):
        return list(obj.liked_by.all())


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complaint_subject',)
    list_display = ('user', 'complaint_subject')


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('owner',)
    list_display = (
        'id',
        'owner',
        'owner_pure_phone',
        'show_flats')
    raw_id_fields = ('owned_flats',)

    def show_flats(self, obj):
        return list(obj.owned_flats.all())


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
