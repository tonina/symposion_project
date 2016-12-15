#! usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200, verbose_name=u'Адреса')
