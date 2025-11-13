# main.py
"""
Menu-driven program to calculate CSA, TSA and Volume for:
 Cylinder, Cone, Cube, Cuboid, Sphere
Uses the shape.py module.
"""

from shape import cylinder, cone, cube, cuboid, sphere  # importing all classes from shape module


# ---------- Function to take positive numeric input ----------
def get_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))                 # take input and convert to float
            if value <= 0:                               # check for positive value
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:                               # handle non-numeric inputs
            print("Invalid input. Enter a numeric value.")


# ---------- Menu for Cylinder ----------
def cylinder_menu():
    print("\nCylinder selected.")
    r = get_positive_number("Enter radius (r): ")        # get radius
    h = get_positive_number("Enter height (h): ")        # get height
    print("-----------------------------------------------------------")
    cyl = cylinder(r, h)                                 # create Cylinder object
    operation_menu(cyl)                                  # pass object to operation menu


# ---------- Menu for Cone ----------
def cone_menu():
    print("\nCone selected.")
    r = get_positive_number("Enter radius (r): ")        # get radius
    h = get_positive_number("Enter height (h): ")        # get height
    print("-----------------------------------------------------------")
    cone_obj = cone(r, h)                                # create Cone object
    operation_menu(cone_obj)                             # pass to operation menu


# ---------- Menu for Cube ----------
def cube_menu():
    print("\nCube selected.")
    a = get_positive_number("Enter side length (a): ")   # get side length
    print("-----------------------------------------------------------")
    cube_obj = cube(a)                                   # create Cube object
    operation_menu(cube_obj)


# ---------- Menu for Cuboid ----------
def cuboid_menu():
    print("\nCuboid selected.")
    l = get_positive_number("Enter length (l): ")        # get length
    b = get_positive_number("Enter breadth (b): ")       # get breadth
    h = get_positive_number("Enter height (h): ")        # get height
    print("-----------------------------------------------------------")
    cuboid_obj = cuboid(l, b, h)                         # create Cuboid object
    operation_menu(cuboid_obj)


# ---------- Menu for Sphere ----------
def sphere_menu():
    print("\nSphere selected.")
    r = get_positive_number("Enter radius (r): ")        # get radius
    print("-----------------------------------------------------------")
    sphere_obj = sphere(r)                               # create Sphere object
    operation_menu(sphere_obj)


# ---------- Submenu for operations ----------
def operation_menu(obj):
    """
    obj is expected to have csa(), tsa(), and either volume() or vol() methods.
    """
    while True:
        print("\nChoose operation:")
        print("1. Curved Surface Area (CSA)")
        print("2. Total Surface Area (TSA)")
        print("3. Volume")
        print("4. Back to main menu")
        print("-----------------------------------------------------------")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":                                # calculate CSA
            try:
                result = obj.csa()
                print(f"CSA = {result:.4f}")
                print("-----------------------------------------------------------")
            except Exception as e:
                print("Error calculating CSA:", e)

        elif choice == "2":                              # calculate TSA
            try:
                result = obj.tsa()
                print(f"TSA = {result:.4f}")
                print("-----------------------------------------------------------")
            except Exception as e:
                print("Error calculating TSA:", e)

        elif choice == "3":                              # calculate Volume
            try:
                # check which method exists (volume or vol)
                if hasattr(obj, "volume"):
                    result = obj.volume()
                elif hasattr(obj, "vol"):
                    result = obj.vol()
                else:
                    raise AttributeError("No volume() or vol() method found.")
                print(f"Volume = {result:.4f}")
                print("-----------------------------------------------------------")
            except Exception as e:
                print("Error calculating Volume:", e)

        elif choice == "4":                              # return to main menu
            return
        else:
            print("Invalid choice. Enter 1-4.")


# ---------- Main menu ----------
def main():
    while True:
        print("\n=== Figures Menu ===")
        print("1. Cylinder")
        print("2. Cone")
        print("3. Cube")
        print("4. Cuboid")
        print("5. Sphere")
        print("6. Exit")
        print("-----------------------------------------------------------")
        choice = input("Select a figure (1-6): ").strip()

        if choice == "1":
            cylinder_menu()                              # call cylinder submenu
        elif choice == "2":
            cone_menu()                                  # call cone submenu
        elif choice == "3":
            cube_menu()                                  # call cube submenu
        elif choice == "4":
            cuboid_menu()                                # call cuboid submenu
        elif choice == "5":
            sphere_menu()                                # call sphere submenu
        elif choice == "6":
            print("Exiting. Goodbye!")                   # exit program
            break
        else:
            print("Invalid selection. Please choose 1-6.")  # invalid option handling


# ---------- Program Entry Point ----------
if __name__ == "__main__":
    main()                                               # run the main function
