# magicnumber

A program to calculate "Magic Numbers" inside a range of integers.

> A magic number is a number that has a perfect square root. This square root is also a prime number.

The main dataset used on test (datasets/datasets_huge.json) has 100K entries with A/B pairs ranging from 0 to 100K as well. The program is able to handle this dataset in less than one second (0.3s on Intel i7). This also include the time to load and parse the dataset.

For this project we are using:

- Python 3: A high-level scripting programming language.
- Pytest: Testing framework for Python.
- Coverage: Used to gauge the effectiveness of tests.
- Flake8: For style guide enforcement and lint checks.
- Tox: A virtualenv management and test command line tool.
- Docker: Container software to isolate the aplication.


## Source code

The source code can be found on GitHub:

```bash
git clone https://github.com/yoshiodeveloper/magicnumber.git
```


## Running with Docker

Build the image.

```bash
docker build -t yoshiodeveloper/magicnumber .
```

Now you can run the *CLI* of magicnumber module (bin/calcmagicnumber.py) passing the array as double quoted string. This array must be a valid JSON.

```bash
docker run -t --rm yoshiodeveloper/magicnumber -s "[[1,3], [50, 10982]]"
```

You can pass a filename with a dataset to be loaded. The dataset format must be a valid JSON as well.

```bash
docker run -t --rm yoshiodeveloper/magicnumber -f dataset.json
```

You can also pass the dataset using *pipes*. Use the parameter "-i" on docker.

```bash
cat dataset.json | docker run -i --rm yoshiodeveloper/magicnumber
```

If you want to use the program directly inside the docker, use "-it" and "--entrypoint sh". After that you will be inside the docker container on "/magicnumber" directory.

```bash
docker run -it --rm --entrypoint sh yoshiodeveloper/magicnumber
```

The project will be on "/magicnumber". You don't need to set PYTHONPATH or use the virtualenv there.

Some examples inside the docker container:
```bash
pytest  # to run the tests

python bin/calcmagicnumber.py -s "[[1,3], [50, 10982]]"
python bin/calcmagicnumber.py -f datasets/dataset_huge.json
```


## For development

Install "Python 3", "pip" and "virtualenv" in your system.

Creates a virtualenv to isolate the Python libs for this project:

```bash
virtualenv -p python3 magicnumbervenv
```

Activate it:

```bash
source magicnumbervenv/bin/activate
```

Install the dependencies with pip:

```bash
pip install -r requirements.txt
```

Set the PYTHONPATH.

```bash
export PYTHONPATH=$PYTHONPATH:/home/user/magicnumber
```

> Note: The PYTHONPATH must be set with the project directory. Do not use "/home/user/magicnumber/magicnumber" as this one is the source.

Now you enviroment is ready. You can run the /bin scripts or the tests (see above).

If you want to leave the virtualenv run "deactivate".

```bash
deactivate
```


# Running tests

If you want to run the tests you can use tox or pytest, both are already installed as dependency inside the virtualenv.

**tox**

Run tox with the Python version that you have (ex: py36, py37, py38). Basically tox will call pytest as well and you need virtualenv activated, but you don't need to set up the PYTHONPATH.

```bash
tox -e py38  # or py36, py37
```

**Pytest**

To run Pytest
The virtualenv must be activated and PYTHONPATH must be set. You can also run tests using docker (see above).

```bash
pytest
```

You can also run using tox. Just specify the Python version that you have (ex: py36, py37, py38). Basically tox will call pytest as well.

```bash
tox -e py38
```


## Project files

**/bin**: Scripts/programs to be executed on shell.

**/datasets**: Datasets used on tests.
 
**/magicnumber**: The module/source of the application.
 
**/tests**: Pytest test scripts.
 
 
## Contact

If you found a bug, typo or bad coding you can contribute. Send a pull request or contact geanyoshio@gmail.com.
