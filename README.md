
## TOY ROBOT
### What is this repository for? ###

* The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.


### Prerequisites ###

* Git - Download & Install Git. OSX and Linux machines typically have this already installed.
* Python3.8
* Pip


### Cloning The GitHub Repository ###

```bash
# SSH
>>  git clone git@github.com:alvinsel/toy-robot.git
# HTTPS
>> git clone https://github.com/alvinsel/toy-robot.git
```
### Running Robot in command line ###
```bash
>>  python run.py
```

### Running Robot in using text files ###
```bash
>>  python3 file_reader -f <file_name>
>>  python3 file_reader.py -f sample/example.txt
```
### Valid Commands ###
```bash
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```
### Code Formatting ###
```bash
>> pip install black
>> black -l 79 .
```

### Running the test ###
```bash
>> pip install -r requirements.txt
>> pytest tests/
```

### Running the test with coverage ###
This will write the coverage report to htmlcov/index.html that you can check on your browser
```bash
>> pip install -r requirements.txt
>> coverage run --omit="*tests*" -m pytest ./tests/
>>coverage html
```
