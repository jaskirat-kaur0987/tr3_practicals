from project import Project
from operator import attrgetter

# constants
CONSTANT = "- (L)oad project\n-(S)ave project\n-(D)isplay project\n-(F)ilter project by date\n-(A)dd new project\n-(" \
           "U)pdate project\n-(Q)uit "
PROJECT_FILE = 'projects.texts'


def load_project(project_file):
    """Read file of project details, return a list of project."""
    projects = []
    # Open the file for reading
    in_file = open(PROJECT_FILE, 'r')

    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()

    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging

        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split('\t')

        # Construct a ProgrammingLanguage object using the elements
        # priority should be an int
        # estimate should be a float
        # completion should be an int

        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))

        # Add the project to the list
        projects.append(project)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return projects


def main():
    print(CONSTANT)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            PROJECT_FILE = input("File name to load from:")
            projects = load_project(PROJECT_FILE)
        elif menu_choice == 's':
            user_saved_file = input("File name to save to:")
            out_file = open(user_saved_file, 'w')
            for project in project:
                print(repr(project), file=out_file)
            out_file.close()
        elif menu_choice == 'D':
            projects.sort(key=attrgetter('priority'))
            for project in projects:
                print(project)
        elif menu_choice == 'F':
            print("Filter by date")
        elif menu_choice == 'A':
            name = input("Name:")
            start_date = input("Start date (dd/mm/yyyy):")
            priority = int(input("Priority:"))
            cost_estimate = float(input("Cost estimate:"))
            completion_percentage = int("Completion percentage:")
            new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(new_project)
            print(new_project, "added to file.")
        elif menu_choice == 'U':
            project_to_update = input("Choose a project to update: ")
        else:
            print("Thank you for using custom-built project management software")


if __name__ == '__main__':
    main()
