#!/usr/bin/env python
"""
Library to handle requests for stats, process data and produce results in
a proscribed format.
"""
import json
import datetime

class Newsletter(object):
    '''
    Main class to handle requests
    '''
    def __init__(self):
        pass

    def get_current_active_users(self):
        '''
        Get the number of users who are active in the whole system this week
        '''
        pass

    def process_data(self):
        '''
        Process the received data from the API into the various requirements
        for the reporerts
        '''
        pass

    def format_report(self):
        '''
        Use templates to create the newsletter and set it out to be saved as
        PDF or other file
        '''
        pass

    def send_report(self):
        '''
        Connect to the info email address and send out the pdf report to users
        '''
        pass

    def create_newsletter(self):
        '''
        main method to be called to create and distribute the newsletter
        '''
        pass

#Testing area - to be commented out whenever not being used
if __name__ == "__main__":
    NEWSLETTER = Newsletter()
    NEWSLETTER.create_newsletter()
