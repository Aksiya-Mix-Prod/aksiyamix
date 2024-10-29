from django.contrib import admin
from .models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id_generate', 'company', 'title', 'status', 'discount_type',
        'currency', 'price', 'old_price', 'is_active', 'start_date', 'end_date'
    )
    list_filter = (
        'status', 'discount_type', 'currency', 'is_active', 'delivery', 'installment'
    )
    search_fields = ('title', 'company__name', 'id_generate')
    ordering = ('-ordering',)

    readonly_fields = (
        'id_generate', 'ordering', 'view_counts', 'like_counts',
        'dislike_counts', 'comment_counts', 'spam_counts',
        'quantity', 'remainder'
    )



    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('company', 'category', 'first_category', 'second_category')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.id_generate = obj.generate_unique_id()
        super().save_model(request, obj, form, change)
