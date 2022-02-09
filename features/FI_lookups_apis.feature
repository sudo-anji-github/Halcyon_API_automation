Feature: Financial Institute Lookups API's coverage


  @test1
  Scenario: Get the List of FI page departments
    Given the user initiate the API requirements to get the FI Dept data
    When the user perform GET operation to get that data
    Then the user should get the status code as 200
    And the deparments are listed as below
    | Dept         |
    | Headquarters |
    | Product      |
    | Operations   |
    | Sales        |
    | Tech         |

  @test2
  Scenario: Get the List of FI page Roles
    Given the user initiate the API requirements to get the FI Roles data
    When the user perform GET operation to get that data
    Then the user should get the status code as 200
    And the Roles are listed as below
    | Roles                |
    | Relationship Manager |
    | Operations Manager   |
    | Admin                |
