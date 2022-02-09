
# =============> Behave Hooks methods <================


def before_scenario(context, scenario):
    print("********Started the execution*********")
    print(scenario.name)


def after_scenario(context, scenario):
    print(scenario.name)
    print("*********Ending the execution*********")
