# SDE-intern
Visitor Application

This Application Basically consisting of three modules

> 1.Check IN 
> 2.Check OUT
> 3.Host






Check-In


* Of course, the Organisation have a limited and designated host whose ID when created backend will automatically update it on software

* Now when a new visitor come, he/she must click the check in button 

* Now user must fill his own credential and he need to select the host whom he wishes to visit from the dropdown list

* Check in time will be automatically fetched from the system

* now he/she click on submit, python will save its data to sql data base and send the data to the specified host through email and generate a unique visit ID which will be noted by user for the checkout purpose




Check-Out


* Now when user click on check out button, system will ask him to enter visit ID/ mobile number 

* System will validate the visit ID and if found then it will successfully record the time and send the user a thank you note

Host

* Host part is so simple
* Every host will have a user ID and password, where he can check all the visit request for a day


