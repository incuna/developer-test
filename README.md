# Python Test

The project includes a simple `course_list` view that loads course detail and
course schedule data from a json file (`/data/course_list.json`) then and 
displays the data as a list of courses, each with their schedule.

**The task** is to create a course list view that takes the existing data and 
renders it by day, so each day that has a course scheduled lists all the courses
on that day. If a course has multiple occurrences on the same day (in different
locations) then the course should only be listed once with all occurrences 
included.

The data in the json file should not be altered.


## Quickstart
* `git clone git@github.com:incuna/<project_name>`
* `pip install -r dev_requirements.txt`
* `source env.sh`
