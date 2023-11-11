#imports
from modules import module
import os
from dotenv import load_dotenv
import argparse

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Pull requests Data Bootcamp' )
    help_message ='Choose the lab of choice.' 
    parser.add_argument('-l', '--lab', help=help_message, type=str)
    args = parser.parse_args()
    return args

#Token
load_dotenv('./.env')
TOKEN = os.environ.get("API_TOKEN")
#Endpoints
API_TOKEN = TOKEN #API TOKEN (REMEMBER: do not push these to your repo)
USERNAME = "aaguiare"#USERNAME
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ih-datapt-mad/'
REPO = "dataptmad0923_labs/"#LAB_REPOSITORY
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'
#Column names
field_list1 = ['number',
               'title',
               'state',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']

field_list2 = ['student_name',
               'number',
               'lab_name',
               'state',
               'lab_status',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']
field_sort1 = ['lab_status',
               'lab_name',
               'student_name']
field_name1 = ['Student Name',
               'PR Number',
               'Lab Name',
               'PR Status',
               'Lab Status',
               'PR Created at',
               'PR Updated at',
               'PR Closed at',
               'PR URL',
               'base repository',
               'base',
               'head repository',
               'compare',
               'Pushed at']

#Execution
if "_name_" == '_main_':
    DF_PULLS = module.get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = module.df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    if argument_parser().lab:
        DF_STATUS = module.filter_dataframe(DF_STATUS,argument_parser().lab)
      
    DF_CSV = module.create_csv(DF_STATUS, field_sort1, field_name1)
        