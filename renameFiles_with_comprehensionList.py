filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [filename.replace("hpp", "h") if filename[-3:] == "hpp" else filename for filename in filenames]  



print(new_filenames) 

