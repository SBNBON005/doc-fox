## Description
A program that takes in a file with commands and then displays its resulting rover location to console.

### Commands
- M - Move one space forward in the direction it is facing.
- R - rotate 90 degrees to the right
- L - rotate 90 degrees to the left

### Assumptions
- Rover should not go beyond the zone's boundary
- horizontal axis constraints [0, 9]
- Vertical axis constraints [0, 9]
- Rover will not move if commands go beyond the zone's defined boundaries.


## Prerequisites

Install `Docker`

Clone `git clone git@github.com:SBNBON005/rover-navigation.git`

## Build

```
$ cd /path/to/doc-fox/directory
$ docker build -t doc-fox:latest .
```

Example Output
```
Sending build context to Docker daemon   7.68kB
Step 1/5 : FROM python:3.6
 ---> 55fb8aca33df
Step 2/5 : RUN mkdir /app
 ---> Using cache
 ---> cf6cbb0178ab
Step 3/5 : COPY . /app
 ---> 9139ee38da4f
Step 4/5 : WORKDIR /app
 ---> Running in 429966ec5f99
Removing intermediate container 429966ec5f99
 ---> aa5fc51f38ae
Step 5/5 : CMD ["python", "rover.py"]
 ---> Running in a40823481fd0
Removing intermediate container a40823481fd0
 ---> 7fb3c151fa18
Successfully built 7fb3c151fa18
Successfully tagged doc-fox:latest

```

## Run
```
$  docker run --rm --name doc-fox doc-fox:latest

3 3 S
```

## Testing
To run the unittest (You'll need to have python >= 3.6 installed on your machine)

```
$ python3 test_rover.py
```
