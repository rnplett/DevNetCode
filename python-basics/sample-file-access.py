# This line opens the file and creates an object called my_file_object that holds the reference to the file
my_file_object = open("my-file.txt", "r")

# read() reads in the entire file.  In this line of code, we read in the contents of the file and print it to the screen.
print (my_file_object.read())