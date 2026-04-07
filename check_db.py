import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refactor.settings')
django.setup()

from myapp.models import Activity
from django.db import connection

# Afficher les colonnes
cursor = connection.cursor()
cursor.execute("PRAGMA table_info(myapp_activity)")
columns = cursor.fetchall()
print("=" * 50)
print("Colonnes de la table Activity:")
print("=" * 50)
for col in columns:
    print(f"  {col[1]}: {col[2]}")

# Afficher le nombre de lignes et un exemple
count = Activity.objects.count()
print(f"\nNombre total d'activités: {count}")
if count > 0:
    a = Activity.objects.first()
    print(f"\nPremière activité:")
    print(f"  act_id: {a.act_id}")
    print(f"  act_name: {a.act_name}")
    print(f"  act_power: {a.act_power}")
    print(f"  act_normal_power: {a.act_normal_power}")
    print(f"  display_powers: {a.display_powers}")
