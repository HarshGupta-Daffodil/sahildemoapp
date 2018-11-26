# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sample_app.skill.models import Skill
from sample_app.serializers import SkillDetailsSerializer
from rest_framework import generics


class SkillList(generics.ListCreateAPIView):
    """
    list all Skills
    """
    queryset = Skill.objects.all()
    serializer_class = SkillDetailsSerializer


class GetSkill(generics.RetrieveAPIView):
    """
    retive the skill based on id
    """
    queryset = Skill.objects
    serializer_class = SkillDetailsSerializer


class DeleteSkill(generics.DestroyAPIView):
    """
    Delete skill based on id
    """
    queryset = Skill.objects
    serializer_class = SkillDetailsSerializer


class UpdateSkill(generics.UpdateAPIView):
    """
    Update skill based on id
    """
    queryset = Skill.objects
    serializer_class = SkillDetailsSerializer


class CreateSkill(generics.ListCreateAPIView):
    """
    Create a new skill
    """
    queryset = Skill.objects
    serializer_class = SkillDetailsSerializer




