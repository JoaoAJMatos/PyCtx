# PyCTX

__PyCTX__ is a Python tool built by and for University students who suffer from the restrictions imposed by their teachers when it comes to developing projects.

PyCTX comes with a set of utilities useful for developing C/C++ projects.

The two main scripts (`start.sh` and `start.ps1`) can be used to interact with the project utilities.

## Running

To start the project on __Linux__ or __MacOS__, run the following command:

```bash
sudo ./start.sh
```

To start the project on __Windows__, run the following command in a __PowerShell__ terminal with __Administrator__ privileges:

```powershell
.\start.ps1
```

## Utilities

##### Build Single File Project:

Used to build a single file project from a given multi-file project. This is needed because of compatibility issues with the anti-copyrighting system used by our University.

This tool indexes all the files in the project and places their contents correctly in a single __C__ file. This file can then be compiled and the resulting binary can be ran normally.

<br>

##### Build CodeBlocks Project: 

Used to convert a multi-file project into a __CodeBlocks__ project. This is useful since it is the __IDE__ most of my colleagues use at school, and is where our code will be ran by the teachers.

<br>

##### Update Project:

Used to update the project with the latest remote changes from the __GitHub__ repository. 

## Features

- [x] Single File Project Builder
- [x] Codeblocks Project Builder
- [x] GitHub Repo Interactions


## Notice

The _project utilities_ are dependent on a set of third party programs, all of which are installed automatically on startup if they are not already installed on the system.

These are:
- [Python](https://www.python.org/)
- [Chocolatey](https://chocolatey.org/) (on __Windows__)
- [Brew](https://brew.sh/) (on __MacOS__)

The last two are package managers that help us install __Python__.

To run the script you must have __Internet access__, since both the package managers and __Python__ are downloaded from the Internet. All the programs installed __can be automatically removed__ by the user if they wish to do so.

<br>

###### [Back to top](#project-utilities)
[//]: # (End of README.md)