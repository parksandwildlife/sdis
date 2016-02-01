# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pythia.fields
import pythia.projects.models
import django.utils.timezone
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('effective_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_to', models.DateTimeField(null=True, blank=True)),
                ('type', models.PositiveSmallIntegerField(default=0, help_text="The project type determines the approval and documentation requirements during the project's life span. Choose wisely - you will not be able to change the project type later.", verbose_name='Project type', choices=[(0, 'Science project'), (1, 'Core function project'), (2, 'Collaboration project'), (3, 'Student project')])),
                ('status', django_fsm.FSMField(default='new', max_length=50, verbose_name='Project Status', choices=[('new', 'New project, pending concept plan approval'), ('pending', 'Pending project plan approval'), ('active', 'Approved and active'), ('updating', 'Update requested'), ('closure requested', 'Closure pending approval of closure form'), ('closing', 'Closure pending final update'), ('final update', 'Final update requested'), ('completed', 'Completed and closed'), ('terminated', 'Terminated and closed'), ('suspended', 'Suspended')])),
                ('year', models.PositiveIntegerField(default=pythia.projects.models.get_current_year, help_text='The project year with four digits, e.g. 2014', verbose_name='Project year')),
                ('number', models.PositiveIntegerField(default=pythia.projects.models.get_project_number, help_text='The running project number within the project year.', verbose_name='Project number')),
                ('position', models.IntegerField(default=1000, help_text='The primary ordering instance. If left to default, ordering happends by project year and number (newest first).', null=True, blank=True)),
                ('title', pythia.fields.Html2TextField(help_text='The project title with formatting if required.', verbose_name='Project title')),
                ('image', models.ImageField(help_text='Upload an image which represents the meaning, or shows a nice detail, or the team of the project.', null=True, upload_to=pythia.projects.models.projects_upload_to, blank=True)),
                ('tagline', pythia.fields.Html2TextField(help_text='Sell the project in one sentence to a wide audience.', null=True, blank=True)),
                ('comments', pythia.fields.Html2TextField(help_text='Any additional comments on the project.', null=True, blank=True)),
                ('start_date', models.DateField(help_text='The project start date, update the initial estimate later. Use format YYYY-MM-DD, e.g. 2014-12-31.', null=True, blank=True)),
                ('end_date', models.DateField(help_text='The project end date, update the initial estimate later. Use format YYYY-MM-DD, e.g. 2014-12-31.', null=True, blank=True)),
                ('team_list_plain', models.TextField(help_text='Team member names in order of membership rank.', verbose_name='Team list', null=True, editable=False, blank=True)),
                ('supervising_scientist_list_plain', models.TextField(help_text='Supervising Scientist names in order of membership rank. NOT the project owner, but all supervising scientists on the team.', verbose_name='Supervising Scientists list', null=True, editable=False, blank=True)),
                ('area_list_dpaw_region', models.TextField(help_text='DPaW Region names.', verbose_name='DPaW Region List', null=True, editable=False, blank=True)),
                ('area_list_dpaw_district', models.TextField(help_text='DPaW Region names.', verbose_name='DPaW Region List', null=True, editable=False, blank=True)),
                ('area_list_ibra_imcra_region', models.TextField(help_text='DPaW Region names.', verbose_name='DPaW Region List', null=True, editable=False, blank=True)),
                ('area_list_nrm_region', models.TextField(help_text='DPaW Region names.', verbose_name='DPaW Region List', null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['position', '-year', '-number'],
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.PositiveSmallIntegerField(help_text='The role this team member fills within this project.', choices=[(1, 'Supervising Scientist'), (2, 'Research Scientist'), (3, 'Technical Officer'), (8, 'External Collaborator'), (6, 'Academic Supervisor'), (7, 'Supervised Student'), (4, 'External Peer'), (5, 'Consulted Peer'), (9, 'Involved Group')])),
                ('time_allocation', models.FloatField(default=0, help_text='Indicative time allocation as a fraction of a Full Time Equivalent (220 person-days). Values between 0 and 1.', null=True, verbose_name='Time allocation (0 to 1 FTE)', blank=True)),
                ('position', models.IntegerField(default=100, help_text='The lowest position number comes first in the team members list. Ignore to keep alphabetical order, increase to shift member towards the end of the list, decrease to promote member to beginning of the list.', null=True, verbose_name='List position', blank=True)),
                ('comments', models.TextField(help_text='Any comments clarifying the project membership.', null=True, blank=True)),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Project Membership',
                'verbose_name_plural': 'Project Memberships',
            },
        ),
        migrations.CreateModel(
            name='ResearchFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('effective_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_to', models.DateTimeField(null=True, blank=True)),
                ('name', pythia.fields.Html2TextField(help_text="The research function's name with formatting if required.", verbose_name='Name')),
                ('description', pythia.fields.Html2TextField(help_text="The research function's description with formatting if required.", null=True, verbose_name='Description', blank=True)),
                ('association', pythia.fields.Html2TextField(help_text="The research function's association with departmental programs.", null=True, verbose_name='Association', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollaborationProject',
            fields=[
                ('project_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='projects.Project')),
                ('name', pythia.fields.Html2TextField(help_text='The collaboration name with formatting if required.', max_length=2000, verbose_name='Collaboration name (with formatting)')),
                ('budget', pythia.fields.Html2TextField(help_text='Specify the total financial and staff time budget.', verbose_name='Total Budget')),
                ('staff_list_plain', models.TextField(help_text='Staff names in order of membership rank. Update by adding DPaW staff as team members.', verbose_name='DPaW Involvement', null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'External Partnership',
                'verbose_name_plural': 'External Partnerships',
            },
            bases=('projects.project',),
        ),
        migrations.CreateModel(
            name='CoreFunctionProject',
            fields=[
                ('project_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Core Function',
                'verbose_name_plural': 'Core Functions',
            },
            bases=('projects.project',),
        ),
        migrations.CreateModel(
            name='ScienceProject',
            fields=[
                ('project_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Science Project',
                'verbose_name_plural': 'Science Projects',
            },
            bases=('projects.project',),
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('project_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='projects.Project')),
                ('level', models.PositiveSmallIntegerField(default=0, help_text='The academic qualification achieved through this project.', null=True, blank=True, choices=[(0, 'PhD'), (1, 'MSc'), (2, 'BSc (Honours)'), (3, 'Yr 4 intern'), (4, '3rd year'), (5, 'Undergraduate project')])),
                ('organisation', models.TextField(help_text='The full name of the academic organisation.', null=True, verbose_name='Academic Organisation', blank=True)),
                ('student_list_plain', models.TextField(help_text='Student names in order of membership rank.', verbose_name='Student list', null=True, editable=False, blank=True)),
                ('academic_list_plain', models.TextField(help_text='Academic supervisors in order of membership rank. Update by adding team members as academic supervisors.', verbose_name='Academic', null=True, editable=False, blank=True)),
                ('academic_list_plain_no_affiliation', models.TextField(help_text='Academic supervisors without their affiliation in order of membership rank. Update by adding team members as academic supervisors.', verbose_name='Academic without affiliation', null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Student Project',
                'verbose_name_plural': 'Student Projects',
            },
            bases=('projects.project',),
        ),
    ]
