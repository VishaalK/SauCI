./cloud_sql_proxy -instances="strong-matrix-237304:us-central1:test-mysql-instance"=tcp:5432

# tutorial: https://cloud.google.com/python/django/kubernetes-engine

# create the database
# gcloud sql databases create builds --instance=strong-matrix-237304:us-central1:test-mysql-instance

# create the user
# gcloud sql users create [USER_NAME] --instance=[INSTANCE_NAME] --password=[PASSWORD]

# set up environment variables
# export DATABASE_USER=<your-database-user>
# export DATABASE_PASSWORD=<your-database-password>