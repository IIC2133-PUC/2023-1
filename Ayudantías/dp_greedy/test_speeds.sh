# bin/bash

# Compare times of naive, iterative and dp executables

scripts=("./dp" "./iterative" "./naive" )

for script in ${scripts[@]}
do
    echo "Running $script"
    time $script
done

echo "Done"
