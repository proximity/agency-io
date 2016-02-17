from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import logging
import sys
from users import utils

class Agency(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Agencies"

class Department(models.Model):
    agency = models.ForeignKey(Agency)
    name   = models.CharField(max_length=100)
    def __str__(self):
        return '%s - %s' % (self.name, self.agency)

class Group(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Person(models.Model):
    # The user is not mandatory, we might just want a person
    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    email                   = models.EmailField(blank=True)
    phone_number            = models.CharField(max_length=15, null=True, blank=True)
    active                  = models.BooleanField(default=True)
    is_guest                = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    # Returns the current status
    def current_status(self):
        try:
            return Status.objects.filter(person_id=self.id).order_by('-timestamp')[0]
        except IndexError:
            return

    # Says if the person is checked in
    @property
    def checked_in(self):
        if hasattr(self.current_status(), 'is_checked_in'):
            return self.current_status().is_checked_in
        else:
            return False

    @property
    def group(self):
        try:
            group = Group.objects.filter(employee=self.id)[0]
            return group.id
        except IndexError:
            return

    # set if the person is checked in
    @checked_in.setter
    def checked_in(self, value):
        if value != self.checked_in:
            status = Status(person=self, is_checked_in=value)
            status.save()

class Status(models.Model):
    person    = models.ForeignKey(Person)
    is_checked_in  = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

class Employee(Person):
    photo                   = models.ImageField('Profile Pic', upload_to=utils.user_directory_path, null=True, blank=True)
    department              = models.ForeignKey(Department, null=True)
    group                   = models.ForeignKey(Group ,null=True)
    job_title               = models.CharField(max_length=255)
    bio                     = models.TextField(null=True, blank=True)
    address                 = models.TextField(null=True, blank=True)
    emergency_contact_name  = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    medical_alert           = models.TextField(null=True, blank=True)
    # Override the is_guest attribute of the parent
    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)
        self._meta.get_field('is_guest').default = False
