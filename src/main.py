# import os
# import shutil
#
#
# apps_dir = '/home/oybek/fintech/aksiyamix/src/apps'
#
# for app in os.listdir(apps_dir):
#     app_dir = os.path.join(apps_dir, app)
#     for file in os.listdir(app_dir):
#         if file.endswith('.py'):
#             os.remove(os.path.join(app_dir, file))
#         else:
#             shutil.rmtree(os.path.join(app_dir, file))
#

# import os
#
# apps_dir = '/home/oybek/fintech/aksiyamix/src/apps'
#
# for app in os.listdir(apps_dir):
#     app_dir = os.path.join(apps_dir, app)
#     os.mkdir(os.path.join(app_dir, 'migrations'))
#     open(os.path.join(app_dir, 'migrations/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'models'))
#     open(os.path.join(app_dir, 'models/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'views'))
#     open(os.path.join(app_dir, 'views/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'serializers'))
#     open(os.path.join(app_dir, 'serializers/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'signals'))
#     open(os.path.join(app_dir, 'signals/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'translations'))
#     open(os.path.join(app_dir, 'translations/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'validators'))
#     open(os.path.join(app_dir, 'validators/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'utils'))
#     open(os.path.join(app_dir, 'utils/__init__.py'), 'w')
#     os.mkdir(os.path.join(app_dir, 'tasks'))
#     open(os.path.join(app_dir, 'tasks/__init__.py'), 'w')
#     open(os.path.join(app_dir, 'admin.py'), 'w')
#     open(os.path.join(app_dir, 'tests.py'), 'w')
#     open(os.path.join(app_dir, 'apps.py'), 'w')
#     open(os.path.join(app_dir, 'urls.py'), 'w')

import os

apps_dir = '/home/oybek/fintech/aksiyamix/src/apps'

for app in os.listdir(apps_dir):
    app_dir = os.path.join(apps_dir, app)
    apps_file = os.path.join(app_dir, 'apps.py')
    with open(apps_file, 'w') as f:
        f.write(f"""from django.apps import AppConfig


class {app.title()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{app}'
""")
