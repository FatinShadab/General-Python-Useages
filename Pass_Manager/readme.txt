The project is divided into 3 parts,
--------------------------------------->

    i) pydb -- A script to do crud operation(+ reset, format) in a json file which is used as a demo DB.
        * The master key is stored in md5 hash
        * Every other passwords/data is encoded and secured in json file

    ii) Manager -- A script to execute the functions of pydb(which is a custom python db with json as a storage)

    iii) main(passManagerUi) -- A made by pyqt5 to use the project

*** When run for the 1st time, the json database storage file will generate automatically.
------------------------------------------.