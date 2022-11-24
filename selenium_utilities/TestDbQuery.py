from selenium_utilities import dbManager

dbManager.createDbConnection()
result = dbManager.getMySqlQuery("select tutorial_author from selenium where "
                                 "tutorial_id = 2")
print(result)
