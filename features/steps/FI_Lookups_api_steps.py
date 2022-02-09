from behave import *
import requests
from steps.utils.common import request_headers


@given("the user initiate the API requirements to get the FI Dept data")
def step_impl(context):
    context.url = "https://uat-api.halcyonportal.com/halcyonhub/v1/consumer/fi/departments"


@when("the user perform GET operation to get that data")
def step_impl(context):
    context.response = requests.get(url=context.url, headers=request_headers)


@then("the user should get the status code as {exp_code}")
def step_impl(context, exp_code):
    assert context.response.status_code == int(exp_code), "Actulal status code is "+str(context.response.status_code)+". Expected code "+exp_code


@then("the deparments are listed as below")
def dept_list(context):
    for i, row in enumerate(context.table):
        actual = context.response.json()['responseData'][i]['name']
        assert row['Dept'] == actual, "Actual Dept Data is "+actual+". Expected Dept data is "+row['Dept']


@given("the user initiate the API requirements to get the FI Roles data")
def roles_data(context):
    context.url = "https://uat-api.halcyonportal.com/halcyonhub/v1/consumer/fi/roles"


@then("the Roles are listed as below")
def roles_list(context):
    for i, row in enumerate(context.table):
        actual = context.response.json()['responseData'][i]['roleName']
        assert row['Roles'] == actual, "Actual Dept Data is "+actual+". Expected Dept data is "+row['Roles']
