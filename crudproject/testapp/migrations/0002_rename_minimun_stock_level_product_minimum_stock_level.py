from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="minimun_stock_level",
            new_name="minimum_stock_level",
        ),
    ]
