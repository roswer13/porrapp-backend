from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import User, Competition, Team, Match


# Create a seed view to load data.
class SeedView(APIView):

    def post(self, request):

        # Create user admin if not exists.
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create_superuser(email='admin@example.com', password='root1234')

        # Create demo user if not exists.
        if not User.objects.filter(email='user@example.com').exists():
            User.objects.create_user(
                email='user@example.com', password='root1234', name='Demo User'
            )

        # Reset model data.
        Competition.objects.all().delete()
        Team.objects.all().delete()
        Match.objects.all().delete()

        # Create demo competitions.
        competition = Competition.objects.create(name='Competition 1', year=2025, host_country='Location A')

        for i in range(1, 5):
            Team.objects.create(name=f'Team {i}', competition=competition)


        for i in range(1, 5):
            Match.objects.create(
                competition=competition,
                home_team=Team.objects.get(name=f'Team {i}'),
                away_team=Team.objects.get(name=f'Team {(i % 4) + 1}'),
                stage='Group Stage',
                date='2025-06-0{}'.format(i),
            )

        return Response({"message": "Datos de prueba cargados"}, status=201)
