# sensyne-assignment
## Setup
1. At first clone the project repo via [repo](https://github.com/shaonsani/sensyne-assignment-demo.git) link.
2. Then go to the project root directory where manage.py located.
3. Make sure your device has docker installed or please install docker via this link [docker installation](https://docs.docker.com/engine/install/).

## Build and run project
```
make start
```
This will pull neccessary images and create all kind of initial migrations files for you and you will get a running development Django server which runs on localhost and port 8000.

## Run test cases
```
make test
```
This make will run all the test cases for you using pytest.
Now you are ready to go to test api's via postman collections.

## License
[MIT](https://choosealicense.com/licenses/mit/)
