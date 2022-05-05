import adal

# Located in App Registrations from Azure Portal
tenant_id = "c62b5b8d-4235-4aed-8119-c6716db47e1c"

# Located in App Registrations from Azure Portal
resource_app_id_url = "sql-weu-uc-sree54-test-01.database.windows.net"
service_principal_id = "a494ca25-7abf-4482-a906-355c62361291"
service_principal_secret = "Y3kjWzSdGxRdLadgxt7WZuv7_fd0vQm-jH"

# Authority
authority = "https://login.windows.net/" + tenant_id

context = adal.AuthenticationContext(authority)
token = context.acquire_token_with_client_credentials(resource_app_id_url, service_principal_id, service_principal_secret)
access_token = token["accessToken"]


jdbc_df = spark.read \
        .format("com.microsoft.sqlserver.jdbc.spark") \
        .option("url", url) \
        .option("dbtable", dbtable) \
        .option("accessToken", access_token) \
        .option("encrypt", "true") \
        .option("hostNameInCertificate", "*.database.windows.net") \
        .load()