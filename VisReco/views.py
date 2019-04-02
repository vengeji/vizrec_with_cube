# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from pr.partial_order import execute
from ml.timer import venloji_timer
import json


# Create your views here.
def index(request):
    with venloji_timer('Whole'):
        context = execute('', 'localhost',
                          '3306',
                          'root',
                          'root',
                          'test',
                          'elec',
                          "SELECT * FROM elec WHERE date BETWEEN '2015-01-01' AND '2016-08-25'",
                          'city',
                          'date',
                          'electricity(kWh)',
                          'varchar(255)',
                          'date',
                          'float'
                          )

    return render(request, 'index.html', context={'charts': context, 'chartsjs': json.dumps(context)})


def crime(request):
    context = execute('', 'localhost',
                      '3306',
                      'root',
                      'root',
                      'test',
                      'crime1',
                      "SELECT * FROM crime1",
                      'ID',
                      "Case Number",
                      'Date',
                      'Block',
                      'IUCR',
                      "Primary Type",
                      'Description',
                      "Location Description",
                      'Arrest',
                      'Domestic',
                      'Beat',
                      'District',
                      'Ward',
                      "Community Area",
                      "FBI Code",
                      'Latitude',
                      'Longitude',
                      'Location',
                      'varchar(20)',
                      'varchar(255)',
                      'datetime',
                      'varchar(255)',
                      'varchar(255)',
                      'varchar(255)',
                      'varchar(255)',
                      'varchar(255)',
                      'int(11)',
                      'int(11)',
                      'varchar(11)',
                      'varchar(11)',
                      'varchar(11)',
                      'varchar(11)',
                      'varchar(255)',
                      'float',
                      'float',
                      'varchar(255)')

    return render(request, 'crime.html', context={'charts': context, 'chartsjs': json.dumps(context)})


def story(request):
    with venloji_timer('Whole'):
        context = execute('', 'localhost',
                          '3306',
                          'root',
                          'root',
                          'test',
                          'story',
                          "SELECT * FROM story",
                          'film',
                          'genre',
                          'leadstudio',
                          'audiencescore',
                          'profitability',
                          'tomatoes',
                          'gross',
                          'year',
                          'varchar(255)',
                          'varchar(255)',
                          'varchar(255)',
                          'int(11)',
                          'float',
                          'int(11)',
                          'float',
                          'varchar(255)',
                          )

    return render(request, 'story.html', context={'charts': context, 'chartsjs': json.dumps(context)})


def titan(request):
    with venloji_timer('Whole'):
        context = execute('', 'localhost',
                          '3306',
                          'root',
                          'root',
                          'test',
                          'titanic',
                          "SELECT * FROM titanic",
                          'PassengerId',
                          'TicketNumber',
                          'Cabin',
                          'Pclass',
                          'Sex',
                          'Embarked',
                          'Survived',
                          'age',
                          'age_bucket',
                          'fare',
                          'varchar(255)',
                          'varchar(255)',
                          'varchar(255)',
                          'varchar(255)',
                          'varchar(255)',
                          'varchar(255)',
                          'varchar(255)',
                          'int(11)',
                          'varchar(255)',
                          'float',
                          )

    return render(request, 'titan.html', context={'charts': context, 'chartsjs': json.dumps(context)})
