# AlertMe

AlertMe is a web application aimed at delivering automated emergency notifications.

## Installation

### Installing dependencies
Use [pipenv](https://pipenv.readthedocs.io/en/latest/) to install dependencies and to create a virtual environment for AlertMe.

__You can install pipenv with the following:__

###### *_If Python 3 is the only version of Python installed on your machine_*
```bash
pip install pipenv
```
or

###### *_If Python 2 and Python 3 are installed on your machine_*
```bash
pip3 install pipenv
```
__Now that pipenv is installed, open your terminal/command prompt and navigate to the root of the project folder:__

```bash
cd cruzhacks2019
```

**Install dependencies:**
```bash
pipenv install
```
### Creating virtual environment for AlertMe

If the last command was successful, then pipenv should have done two things: 1. install dependencies from the Pipfile 
and 2. create a virtual environment. 

__To use the virtual environment that was created by pipenv, use the following command:__
```bash
pipenv shell
```


## Usage

Now that the dependencies have been installed and we have a working virtual environement,
we can run the Django server to get the project running locally.

_**Make sure you are inside the virtual environment prior to following the next steps**_

__Navigate to the root of the django project:__
```bash
cd cruzhacks2019/cruzhacks2019
```

##### _**If you run `ls`, you should be able to see a file called `manage.py`.**_

__Run the Django server__:

###### *_If Python 3 is the only version of Python installed on your machine_*
```bash
python manage.py runserver
```
###### *_If Python 2 and Python 3 are installed on your machine_*
```bash
python3 manage.py runserver
```
You're all set! Open your browser and navigate to 127.0.0.1:8000 to view the project locally. Please open an issue should you
come across any problems.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
