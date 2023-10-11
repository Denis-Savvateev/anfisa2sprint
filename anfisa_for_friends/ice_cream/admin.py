from django.contrib import admin

# Register your models here.
# Из модуля models импортируем модели
from .models import Category, Wrapper, Topping, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )


# ...и регистрируем их в админке:
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)
admin.site.register(IceCream, IceCreamAdmin)
