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
                      'websales2005_season1',
                      "SELECT * FROM sales",
                      'price',
                      'itemname',
                      'itemdesc',
                      'category',
                      "solddate",
                      'quantity',
                      'double',
                      'varchar',
                      'varchar(255)',
                      'varchar(255)',
                      'date',
                      'int')

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
