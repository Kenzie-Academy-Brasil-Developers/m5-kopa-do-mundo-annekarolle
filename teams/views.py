from django.forms import model_to_dict
from django.shortcuts import render
from teams.models import Team
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


class TeamsViews(APIView):
    def post(self, request):
        team_data = request.data

        team = Team.objects.create(
            name=team_data['name'],
            titles=team_data['titles'],
            top_scorer=team_data['top_scorer'],
            fifa_code=team_data['fifa_code'],
            founded_at=team_data['founded_at'],
        )

        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()

        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
        
        return Response(teams_dict)     
   
      
class TeamViewById(APIView):

    def get(self, request, team_id):         
            try:
                team = Team.objects.get(pk=team_id)
                
            except Team.DoesNotExist:
                return Response({"message": "Team not found"}, 404)

            return Response(model_to_dict(team), 200) 


    def delete(self, request, team_id):           
            try:
                team = Team.objects.get(pk=team_id)
                team.delete()
            except Team.DoesNotExist:
                return Response({"message": "Team not found"}, 404)

            return Response(status=204) 


    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)           
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)      

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()
        
        return Response(model_to_dict(team), 200) 

 
    
    
        