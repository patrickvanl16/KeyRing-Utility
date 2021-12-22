# Simple KeyRing password setter / remover.

For more information about KeyRing: https://pypi.org/project/keyring/

## Setup:

To make use of this script please install the dependency as follows:

`pip install keyring`

## Usage

You can activate this script through the following command: ``python KeyRingUtil.py`` 

When executed succesfully you will get the following options:

``[1] - New service
[2] - Remove service``

### [1] - New service
This option will enable you to create a new service easily though the command line.

You will be asked to provide a servicename, username and verify the password twice, like so:

``Service name: <Your input>``

``Username: <Your input>``

``Password: <Your input>``

``Verify password: <Your input>``

KeyRing will insert the new service if it doesn't exist yet.

#### IMPORTANT: It is important to carefully write down the services and usernames associated with it. This script cannot get all your services! So if you forget you will have to find your own way to remove it / get it back.

#### [2] - Remove service

Removing a service works similarly to creating one. Simply execute the script and select option 2.

The script will ask you to provide the name of the service to delete and the username associated with it.

``Service to delete: <Your input>``

``Username associated with service: <Your input>``

You will have to verify like this:

``Are you sure? This action cannot be undone. (Type Y or N): <Your Input>``

If the data that was provided is correct then KeyRing will remove it. If not you will get an error message.