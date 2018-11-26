from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Api_view.skill.models import *
from .serializer import SkillDetailsSerializer


class SkillView(APIView):

    def get(self, request):
        """
        To list all the skills
        """
        skills = Skill.objects.all()
        response = {
            'Details': SkillDetailsSerializer(
                skills,
                many=True
            ).data
        }
        return Response(response)

    def post(self, request):
        """
        Create a new entry
        """
        data = request.data
        Skill.objects.update_or_create(**data)
        return Response(
                data=request.data
                )


class UpdateSkill(APIView):

    def get(self, request, pk):
        """
        Reterive skill based on id
        """
        skills = Skill.objects.get(pk=pk)
        if skills:
            response = {
                'payment_methods': SkillDetailsSerializer(
                    skills,
                ).data
            }
        else:
            response = {
                "data": "entry not exist"
            }
        return Response(response)

    def delete(self, request, pk):
        """
        Delete a particular entry based on id
        """
        skills = Skill.objects.get(pk=pk)
        skills.delete()
        return Response(
            data=' Entry deleted',
            )

    def put(self, request, pk):
        """
        update a particular entry based in id
        """
        skills = Skill.objects.get(pk=pk)
        serializer = SkillDetailsSerializer(skills, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(
            data='Entry Updated',

        )
