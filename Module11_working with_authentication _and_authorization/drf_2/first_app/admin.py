from django.contrib import admin
from first_app.models import Product, ProductReview
# Register your models here.
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display=['name', 'description', 'price']
    
@admin.register(ProductReview)
class ProductReviewAdminModel(admin.ModelAdmin):
    list_display=['product', 'user', 'rating', 'review','created_at','updated_at' ]