# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions and classes
# with structured error handling
# Change Log: (Who, When, What)
#   A.Acklen,5/20/2024,Created Script
#
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#Processing ----------------------------------------#
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
        Read File In
        Write File Out

    ChangeLog: (Who, When, What)
    A.Acklen,5.21.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads in the data from a json file

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

        :return: List of data from the json file
        """
        # Extract the data from the file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


#-- Presentation (Input/Output) --#
class IO:
    """
    A collection of presentation layer functions that manage user input and output
        Error Messages
        Menu Output
        User Selection Input
        Add New Student Data
        View Student Data Summary

    ChangeLog: (Who, When, What)
    A.Acklen,5.21.2024,Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error message to the user

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

         :return: None
         """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

        :return: None
         """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

         :return: string with the users choice
         """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    def output_student_courses(student_data: list):
        """ This function displays the students in the list

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

         :return: string with the users choice
         """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        AAcklen,5.21.2024,Created function

         :return: string with the users choice
         """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

#Beginning of the main body of this script


students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
# Present and Process the data
while (True):
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()
    # Input user data
    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue
    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        IO.output_student_courses(student_data=students)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        break  # out of the loop


#End of the main body of this script
