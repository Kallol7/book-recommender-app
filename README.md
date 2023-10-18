# book-recommender-app
## What it is?
1. A Django project.
2. Recommends other books based on the contents of the chosen book.
3. Whenever "Update" button is clicked recommendation list is updated.
   Constraints: A book field won't get updated with new recommendations 
   until five hours have passed after the it last update. It stores the latest
   recommendations inside database. 
   Note: "Update" button is not related with actual recommendation in "Recommend". So you can
   ignore it.
4. The contents are not published. Dummy files added for completeness.
5. Uses Latent Dirichlet Allocation (topic modelling technique) for recommendation.

## Instructions:
0. First follow the instructions from 1 to 6 in "Instructions.md" file.
1. After development server starts, click on "Clean" button, it will promt you to log in. 
2. - You need need to log in using the following credential (log in as staff member):
      ```
        Username: staff
        Password: staffssdram
      ```
   - Also, you can use this superuser account:
      ```
        User: admin
        Password: admin
      ```
3. It will run the script to clean the text files. It takes some time. Thats why only staff members (and Admin) can access it after Logging In.
4. Click on "Update". Again, only staff member can access it. But you are already Logged In. So, you won't be asked to Log In again.
5. Log Out by clicking "Log Out". You need to log out to check the functionality of "Recommend" button. Either "Sign Up" and Log back in or use an existing user account (doesn't have staff permission): 
      ```
        Username: user@user.com 
        Password: user
      ```
6. "Update" button is not related with actual recommendation in "Recommend". So you can ignore it.
7. "Recommend" loads the data from csv file that was created after running "Clean". So, "Clean" first whenever new books are added inside "json_dummy" folder.
