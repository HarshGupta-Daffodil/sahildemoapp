# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import skill
from .serializer import SkillDetailsSerializer


class SkillList(generics.ListCreateAPIView):
    """
    list all Skills
    """
    queryset = skill.objects.all()
    serializer_class = SkillDetailsSerializer


class GetSkill(generics.RetrieveAPIView):
    """
    retive the skill based on id
    """
    queryset = skill.objects
    serializer_class = SkillDetailsSerializer


class DeleteSkill(generics.DestroyAPIView):
    """
    Delete skill based on id
    """
    queryset = skill.objects
    serializer_class = SkillDetailsSerializer


class UpdateSkill(generics.UpdateAPIView):
    """
    Update skill based on id
    """
    queryset = skill.objects
    serializer_class = SkillDetailsSerializer


class CreateSkill(generics.ListCreateAPIView):
    """
    Create a new skill
    """
    queryset = skill.objects
    serializer_class = SkillDetailsSerializer




