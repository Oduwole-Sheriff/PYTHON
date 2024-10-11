import nested_admin
from django.contrib import admin

from .models import (
    Attribute,
    AttributeValue,
    Category,
    Product,
    ProductImage,
    ProductLine,
    ProductType,
    SeasonalEvent,
)

admin.site.register(ProductLine)


class ProductImageInLine(nested_admin.NestedStackedInline):
    model = ProductImage
    extra = 1


class ProductLineInLine(nested_admin.NestedStackedInline):
    model = ProductLine
    inlines = [ProductImageInLine]
    extra = 1


class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProductLineInLine]
    list_display = (
        "name",
        "category",
        "stock_status",
        "is_active",
    )
    list_filter = (
        "category",
        "stock_status",
        "is_active",
    )
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)


class SeasonalEventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")


admin.site.register(SeasonalEvent, SeasonalEventAdmin)


class AttributeValueInLine(admin.TabularInline):
    model = AttributeValue
    extra = 1


class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInLine]


admin.site.register(Attribute, AttributeAdmin)


class ChildTypeInLine(admin.TabularInline):
    model = ProductType
    fk_name = "parent"
    extra = 1


class ParentTypeAdmin(admin.ModelAdmin):
    inlines = [ChildTypeInLine]


admin.site.register(ProductType, ParentTypeAdmin)


class ChildCategoryInLine(admin.TabularInline):
    model = Category
    fk_name = "parent"
    extra = 1


class ParentCategoryAdmin(admin.ModelAdmin):
    inlines = [ChildCategoryInLine]
    list_display = ("name", "parent_name")

    def parent_name(self, obj):
        return obj.parent.name if obj.parent else None


admin.site.register(Category, ParentCategoryAdmin)
