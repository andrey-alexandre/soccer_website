import django_tables2 as tables
from .models import Matches

class MatchesTable(tables.Table):
    class Meta:
        model = Matches
        template_name = "django_tables2/bootstrap4.html"  # Use um template para estilização (opcional)
        attrs = {"class": "table table-striped"} 