# cal_tracker

Simple program for tracking calories throughout the day.

## Project Startup

### Running Locally
In order to run locally, you need to install the requirements first using `pip install -r requirements.txt`.

Start your local postgres instance and edit the connection string in `models/adapters/postgres_adapter.py` on line 8 to reflect your local postgres instance. (TODO: ENV variable controlled connection string)

Start the Flask application using `flask --app base run`.

### Running with Docker
Install docker and simply run `docker-compose up --build`. The prompt should show two instances `db` and `web` up and running. 

Hot-reloading is enabled, and the base directory is loaded into the docker instance. Any changes you make and save should reload the docker instance. 

#### Flush and Debugging
Right now, `print()` and other console statements in the project will get *buffered* and will not show up in the docker prompt until a reload happens (then it'll flush all the print statements at once).

To change this behavior you can do 1 of 3 things:

1. Call an explicit `flush` after every print
```
import sys
print("Hello World")
sys.stdout.flush()
```
2. Unbuffer the entire app via `PYTHONUNBUFFERED` env var by setting `PYTHONBUFFERED: 1` inside of `docker-compose.yml` in the `environment` section of `web`.
3. We can also run python with the `-u` flag in the docker by adding it to the `CMD` in our `Dockerfile`
