import django.conf
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(django.conf.settings.AUTH_USER_MODEL)]
    operations = [migrations.CreateModel(
        name="Ticket",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=160)),
            ("description", models.TextField()),
            ("status", models.CharField(choices=[("open", "Open"), ("in_progress", "In progress"), ("resolved", "Resolved")], default="open", max_length=20)),
            ("priority", models.CharField(choices=[("low", "Low"), ("normal", "Normal"), ("high", "High")], default="normal", max_length=10)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("updated_at", models.DateTimeField(auto_now=True)),
            ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="created_tickets", to=django.conf.settings.AUTH_USER_MODEL)),
        ],
        options={"ordering": ["-created_at"]},
    )]
