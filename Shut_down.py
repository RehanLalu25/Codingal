def shutdown(user_input):
    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "No":
        print("Abort shutdown")
    else:
        print("Sorry")
choice = input("Do you want to shut down the system? (Yes/No): ")
shutdown(choice)
