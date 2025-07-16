#!/usr/bin/env python3


from snowflake.snowpark import Session

# connection parameter
# just account name and user/pwd
connection_parameters = {
  "account": "LJRCPTB-BGB86487",
  "user": "CHOBBS",
  "password": "eyJraWQiOiIyOTAzNzM3MTk0NzE3MTkwIiwiYWxnIjoiRVMyNTYifQ.eyJwIjoiMTczMDc2MjI4OjE3MzA3NjM1NiIsImlzcyI6IlNGOjEwNDkiLCJleHAiOjE3NTUyNzcxNDh9.c4x7OLVsCzpXEE4WWoXyCFhFRKwvAK6364QjMRvc4XTas-9h_u_oDiHzE43lBhe5dsVlDMGLEujYgxpB7Ns8Iw",
  "role": "ACCOUNTADMIN",  
  "warehouse": "DEMO", 
  "database": "SNOWFLAKE_SAMPLE_DATA",  
  "schema": "TPCDS_SF100TCL" 
}  

session = Session.builder.configs(connection_parameters).create()

# print connection params
print("The Parameter :",connection_parameters)

# creating a session object
session = Session.builder.configs(connection_parameters).create()

# print values from session object to test
print("\n\t Current Account Name: ",session.get_current_account())
print("\t Current Database Name: ",session.get_current_database())
print("\t Current Schema Name: ",session.get_current_schema())
print("\t Current Role Name: ",session.get_current_role())
print("\t Current Warehouse Name: ",session.get_current_warehouse())
print("\t Fully Qualified Schema Name: ",session.get_fully_qualified_current_schema(),"\n")

print("Session Object Type:", type(session))
# closing the session
session.close()
