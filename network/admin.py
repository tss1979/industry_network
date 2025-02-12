from django.contrib import admin
from network.models import Plant, Product, Entrepreneur, Retail, Contact


@admin.action(description="Reset Credit")
def reset_credit(self, request, queryset):
    queryset.update(credit=0)


# Register your models here.
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'credit',)
    list_filter = ('name', 'contacts__city',)
    search_fields = ('name', 'contacts__city',)
    actions = [reset_credit]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
    actions = [reset_credit]


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'credit',)
    list_filter = ('name', 'contacts__city',)
    search_fields = ('name', 'city', 'contacts__city',)
    actions = [reset_credit]


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'credit',)
    list_filter = ('name', 'contacts__city',)
    search_fields = ('name', 'contacts__city',)
    actions = [reset_credit]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    list_filter = ('email', 'city',)
    search_fields = ('email', 'city',)
