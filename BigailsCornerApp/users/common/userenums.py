from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender (models.TextChoices) :
    MALE    =   'MALE', _('Male')
    FEMALE  =   'FEMALE', _('Female')
    OTHER   =   'OTHER', _('Other')
    UNKNOWN =   'UNKNOWN', _('Unknown')

class EmpType (models.TextChoices) :
    ADMIN     =   'ADMIN', _('Administrator')
    MANAGER   =   'MANAGER', _('Manager')
    CASHIER   =   'CASHIER', _('Cashier')
    ATTENDANT = 'ATTENDANT', _('Attendant')
    UNKNOWN   =   'UNKNOWN', _('Unknown')


class Role (models.TextChoices) :
    ADMINISTRATOR   =   'ADMINISTRATOR', _('Administrator')
    STOREMANAGER    =   'STOREMANAGER', _('StoreManager')
    CASHIER         =   'CASHIER', _('Cashier')
    SALESATTENDANT  =   'SALESATTENDANT', _('SalesAttendant')
    UNKNOWN         =   'UNKNOWN', _('Unknown')


class LogEvent (models.TextChoices) :
    LOGIN  = 'LOGIN', _('Login')
    LOGOUT = 'LOGOUT', _('Logout')

class CustomerType (models.TextChoices) :
    GUEST  = 'GUEST', _('Guest Customer')
    STANDARD = 'STANDARD', _('Standard Customer')
