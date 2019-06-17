from django.apps import AppConfig
# from django.contrib.auth.models import Permission
# from django.db.models.signals import post_migrate



# def define_user_permissions(sender, **kwargs):
#     permissions = [
#         Permission.objects.get(codename='add_view'),
#         Permission.objects.get(codename='view'),
#     ]
#     create_group('managers', permissions)

class PostsConfig(AppConfig):
    name = 'posts'
    #
    # def ready(self):
    #     post_migrate.connect(define_company_groups, sender=self)
