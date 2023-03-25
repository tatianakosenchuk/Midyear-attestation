
import functions
from logger import logging
import csv
import exception
from os import path
from logger import logging

def ID_check(ID,data):
    for row in data:
        if row[2] == ID:
            return row


def Seach_date_check(date,data):
    for row in data:
        if row[0] == date:
            return row
        