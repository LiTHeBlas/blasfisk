from django.contrib import admin
from litheblas.blasbasen.models import User, Section, Post, MembershipAssignment, SpecialDiet
from litheblas.mailing.models import Membership as MailingMembership

class MembershipAssignmentInline(admin.TabularInline):
    model = MembershipAssignment
    
class MailingListInline(admin.TabularInline):
    model = MailingMembership

class UserAdmin(admin.ModelAdmin):
    inlines = [MembershipAssignmentInline, MailingListInline]
    
#     fieldsets = (
#         (None, {
#             'fields': (('first_name', 'nickname', 'last_name'), ('date_of_birth', 'personal_id_number'))
#         }),
#         ('Auth and perm', {
#             'fields':()
#         })
#     )

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Section)
#admin.site.register(MembershipAssignment)
admin.site.register(SpecialDiet)