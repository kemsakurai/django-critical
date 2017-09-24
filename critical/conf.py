# -*- coding: utf-8 -*-
from appconf import AppConf


class CriticalConf(AppConf):
    PHANTOMJS_PATH = 'phantomjs'
    PENTHOUSE_PATH = 'penthouse.js'
    ENCODING = 'utf-8'

    class Meta:
        prefix = 'critical'
