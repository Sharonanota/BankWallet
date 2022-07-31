from django.contrib import admin
from .models import Account, Card, Loan, Notification, Receipt, Reward, Transaction, Wallet
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","address",)
    search_fields =("firstname","lastname")
    
admin.site.register(Customer,CustomerAdmin)  
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)


# Register your models here.
