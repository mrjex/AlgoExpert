# This script does 2 things:
#   1) Runs all implemented functionality in "/Executionary Code"
#   2) Directs the corresponding output to "/Test Outputs" in .txt files


rm -r "Test Outputs/"* # Delete the prior results


declare -A commandsMap=( ["py"]="python" ["js"]="node" ["csproj"]="dotnet run --project")


# Generates the new comparative numerical values (actual vs expect) in the .txt files,
# serving the same purpose as algorithmic test cases
recursiveSearch() {
    for name in  "${1}"/*
    do
        if [ -d "${name}" ] # If current element is a folder (that contains files), then recursively iterate through its elements 
        then

        CURRENT_RECURSIVE_DEPTH=${3}
        ((CURRENT_RECURSIVE_DEPTH++))

        # Divide the tests for each distinct data-structure folder that is a child to "/Executionary Code" directory
        if [ $CURRENT_RECURSIVE_DEPTH == 1 ]
        then
            OUTPUT_DIR=${name##*/} # Splits the string by '/' and takes the last element (the current parent folder in this case)

            echo "CREATE DIR: '${OUTPUT_DIR}'" # For debugging purposes (not necessary)
            mkdir "Test Outputs/${OUTPUT_DIR}"
        fi

        recursiveSearch "${name}" "${OUTPUT_DIR}" "${CURRENT_RECURSIVE_DEPTH}"

        else
            FILE_EXTENSION=${name##*.}

            # Only execute files with script-extensions
            if [[ "$name" == *.py ]] || [[ "$name" == *.js ]] || [[ "$name" == *.csproj ]]
            then
                FILE_PATH=\"${name}\" # Add double quotes to command to explicitly tell compiler that white spaces in the path to the .py file is compilable
                MY_COMMAND="${commandsMap[$FILE_EXTENSION]} ${FILE_PATH}"

                FILE_NAME=${name##*/}
                printf "\n\n #####################   ${FILE_NAME}   ##################### \n\n\n" >> "Test Outputs/${OUTPUT_DIR}/${OUTPUT_DIR,,}.txt"

                echo $MY_COMMAND # For debugging purposes (not necessary)
                eval $MY_COMMAND >> "Test Outputs/${OUTPUT_DIR}/${OUTPUT_DIR,,}.txt"
            fi
        fi
    done
}


START="./Executionary Code" # Start folder
CURRENT_RECURSIVE_DEPTH=0 # Initial recursive folder value
recursiveSearch "${START}" "NULL" $CURRENT_RECURSIVE_DEPTH