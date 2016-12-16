import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'symposion_project.settings')
import django
django.setup()

from django.apps import apps

from symposion.schedule.models import Schedule


applications = ['symposion_conference',
                'symposion_proposals',
                'symposion_reviews',
                'symposion_schedule',
                'symposion_speakers',
                'symposion_sponsorship',]

f = open('out.txt', 'w')

for app in applications:
    f.write("\n")
    f.write("\n")
    print(app)
    f.write(str(app))
    app_models = apps.get_app_config(app).get_models()

    for model in app_models:
        f.write("\n")
        f.write("\n")
        print(model)
        f.write(str(model))

        field_list = model._meta.get_fields()
        for item in field_list:
            f.write("\n")
            print(item)
            f.write(str(item))

f.close()