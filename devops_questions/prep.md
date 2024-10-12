# bash:
- check if a file exist:
    test -e file_name && echo TRUE
- Rename all .txt files to .log in a path:
```bash
    ls *.txt | cut -d. -f1 | xargs -i mv {}.txt {}.log
```
- command line args:
    ```bash
    #!/bin/sh
        echo "Script Name: $0"
        echo "First Parameter of the script is $1"
        echo "The second Parameter is $2"
        echo "The complete list of arguments is $@"
        echo "Total Number of Parameters: $#"
        echo "The process ID is $$"
        echo "Exit code for the script: $?"
    ```
- check if a file exist using the if else condition:
    ```bash
    #!/bin/sh

        if [ -f file_name ]
        then
            echo "TRUE"
        fi
    ```

- using the special exit status variable:

    ```bash
    #!/bin/bash

    # execute a command
    cp path/file path2

    #check exit status

    if [ @? -eq 0 ]
    then
        echo "command executed correctly"
    else
        echo "command failed"
    fi
    ```

# GIT: