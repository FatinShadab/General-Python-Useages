-------------------------------------------------------------------------------------|
-------------------------------------------------------------------------------------|
                                BASIC TOP LEVEL OVERVIEW                             |
-------------------------------------------------------------------------------------|
FileOrganizer                                                                        |
|                                                                                    |
|                                                                                    |
+---> take parent folder path --> 1st Task                                           |
    |                                                                                |
    |                                                                                |
    +---> organize flies by catagory and sub-catagory as follows --> 2nd Task        |
        |    |                                                                       |
        |    +---> if contain any folder --> merge all content                       |
        |                                                                            |
        |                                                                            |
        +---> move/write the files according the analyzation result.                 |
                                                                                     |
                                                                                     |
task 2nd :                                                                           |
    if user select delete along the way --> then cut and paste                       |
    if user select keep old way --> then copy paste                                  |
        * check if the drive have enough space, if not abot                          |
    analyze the files while merging                                                  |
                                                                                     |
task 3rd :                                                                           |
    create the catagory folders and sub catagory and copy/cut the files and paste    |
-------------------------------------------------------------------------------------|
-------------------------------------------------------------------------------------|
                            CLASS AND CLASS RESPONSIBILTY                            |
-------------------------------------------------------------------------------------|
1.  CONFIG                  // settings.CONFIG                                       |
    |                                                                                |
    +---> TYPE ---> SINGLETON CLASS                                                  |
    |                                                                                |
    +---> INSTANCE ---> config                                                       |
    |                                                                                |
    +---> TASK ---> 1. provide methods to write and store user settings              |
                |                                                                    |
                +--> 2. provide methods to read user settings                        |
                                                                                     |
2.  PROTOCOL                // protocol.PROTOCOL                                     |
    |                                                                                |
    +---> TYPE ---> SINGLETON CLASS                                                  |
    |                                                                                |
    +---> INSTANCE ---> system                                                       |
    |                                                                                |
    +---> TASK ---> create a organize directory map(dict) according user catagory    |
                    settings                                                         |
                                                                                     |
3.  APP                    // base.APP                                               |
    |                                                                                |
    +---> TYPE ---> SINGLETON CLASS                                                  |
    |                                                                                |
    +---> INSTANCE ---> app                                                          |
    |                                                                                |
    +---> TASK ---> Provide and run the main logic of the app using the help of other|
                    classes.                                                         |
-------------------------------------------------------------------------------------|