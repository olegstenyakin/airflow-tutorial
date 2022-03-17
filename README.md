### Airflow local installation

https://airflow.apache.org/docs/apache-airflow/stable/start/local.html

Airflow needs a home. '~/airflow' is the default, but you can put it
somewhere else if you prefer (optional)
```console
$ mkdir airflow
$ export AIRFLOW_HOME=~/airflow
```

Install Airflow using the constraints file
```console
$ AIRFLOW_VERSION=2.2.4
$ PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
$ CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
```

Ensure pip, setuptools, and wheel are up to date
```console
python3 -m pip install --upgrade pip setuptools wheel
```

Install
```console
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

The Standalone command will initialise the database, make a user,
and start all components for you.
```console
airflow standalone
```

Visit localhost:8080 in the browser and use the admin account details
shown on the terminal to login.
Enable the example_bash_operator dag in the home page

### Activate and run the DAG

