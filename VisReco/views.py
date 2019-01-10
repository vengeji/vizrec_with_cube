# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from dr.partial_order import execute
from ml.timer import venloji_timer
import json


# Create your views here.
def index(request):
    # with venloji_timer('Whole'):
    #     context = execute('', 'localhost',
    #                       '3306',
    #                       'root',
    #                       'root',
    #                       'test',
    #                       'crime',
    #                       "SELECT * FROM crime",
    #                       'ID',
    #                       "Case Number",
    #                       'Date',
    #                       'Block',
    #                       'IUCR',
    #                       "Primary Type",
    #                       'Description',
    #                       "Location Description",
    #                       'Arrest',
    #                       'Domestic',
    #                       'Beat',
    #                       'District',
    #                       'Ward',
    #                       "Community Area",
    #                       "FBI Code",
    #                       'Latitude',
    #                       'Longitude',
    #                       'Location',
    #                       'int(20)',
    #                       'varchar(255)',
    #                       'datetime',
    #                       'varchar(255)',
    #                       'varchar(255)',
    #                       'varchar(255)',
    #                       'varchar(255)',
    #                       'varchar(255)',
    #                       'int(11)',
    #                       'int(11)',
    #                       'varchar(11)',
    #                       'varchar(11)',
    #                       'varchar(11)',
    #                       'varchar(11)',
    #                       'varchar(255)',
    #                       'float',
    #                       'float',
    #                       'varchar(255)')
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
