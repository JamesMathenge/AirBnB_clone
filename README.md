# 0x00. AirBnB clone - The console

![Picture](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230818%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230818T162857Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7b3c8bcf3fb94063eabc55f4b4b4dac7c6bc36479b9915b37a2f81e01bc917f8)

# Background Context

## Welcome to the AirBnB clone project!

### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

## Table of contents

* [0x01 Authors] (#0x01 Authors)
* [0x02 Introduction] (#0x02 Introduction)
* [0x03 Environment] (#0x03 Environment)
* [0x04 Installation] (#0x04 Installation)
* [0x05 Testing] (#0x05 Testing)
* [0x06 Usage] (#0x06 Usage)

### 0x01 Authors
These are the team members who helped to build and edit the [AirBnB] Clone project.

#### 0x02 Introduction

Our  team will build a clone of [AirBnB] (https://www.airbnb.com/).

This console is a command interpreter tat manages abstractions between the objects and how they are stored.

The console will perform the following:
* Create a new object
* Retriving an object from a file.
* Do various required operations on objects
* Destroy an object when required to.


### storage
In the 'Filestorage', all the classes are handled by the 'storage' engine.

## 0x03 Environment
We are using the Ubuntu.
 
## 0x04 Installation
''bash
git clone https://github.com/aysuarex/AirBnB_clone.git
'''

change the 'AirBnB' directory and run the command:
'''bash
 ./console.py
'''

### Execution
In interactive mode

'''bash
$./console.py
(hbnb) help

Documented command (type: help <topic>):
========================================

EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
=======
0x00. AirBnB clone - The console
>>>>>>> 392fabc4174bd979ca6369a127bdc9d3c95b9f36
