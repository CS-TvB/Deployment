# Deployment.

In this assignment i had to make a continuous deployment pipeline to my server. First i had to make an account on digital ocean to create a droplet. 
Afther wich i could do a apt --update and install all the necessities like flask, gunicorn, python, pip etc. Then i had to write a simple flask script in python and link that to github.
Everytime i made some changes in my flask script it had to be pushed to github, github had to run a simple pytest on it and if and only if the tests pass it would log into the digital ocean droplet and pull the new files. There also had to be a service running on the server to keep the Flask application running at all times.

# For me the most challaging part of this assignments where the understanding of secrets and keys in github and the services in the server.

If you find the correct stackoverflow threads or articles that help you trough it step by step its actualy not difficult (if you get it working..) i know that there is tons of documentation but most of the time i find that information very raw and hard to understand. here are the steps that i took to make it work. 

To set up a secret in GitHub, follow these steps:
1. Navigate to the repository where you want to add the secret.
2. Click on the "Settings" tab.
3. Click on "Secrets" in the sidebar.
4. Click on "New repository secret".
5. Enter a name for your secret, and then enter the value of your secret.
6. Click "Add secret" to save your secret.
7. Once you have added a secret to your repository, you can use it in your workflows or actions. 
8. To access the value of your secret in a workflow or action, you can use the ${{ secrets.SECRET_NAME }} syntax.

TAKE A NOTE: i dint knew that once you made a secret and open it later the secret apears to be empty... that is because it is empty for security reasons. 

# To create a deploy key in GitHub, you need to follow these steps:

1. Open the terminal app on your computer. 
2. Connect to your droplet with the following command ssh root@<ip>
3. Enter your password.
4. Enter the following command, substituting Thomas@example.com with your email address:
               -  root@abuntu-server# ssh-keygen -t rsa -b 4096 -C "Thomas@example.com"
5. Press Enter to accept the default file location.
6. Enter a secure passphrase. (i dont believe this is necessary)
7. Press Enter. 
8. Enter this command to display the contents of your public key:
               -  root@abuntu-server# cat .ssh/id_rsa.pub (i first tried this with nano but you get it al on 1 single line so the coppy paste is horrendous, USE CAT)
9. Copy the contents of your key to your clipboard (we will need it later).
10. Go to your github reposetory, and click on settings.
11. Select ssh and GPG keys
12. Click new SSH key
13. Enter a title in the field
14. Paste your public key into the Key field
15. Click Add SSH key

# Check this realy helpfull article on how to run a Flask application as a service with systemd.

https://blog.miguelgrinberg.com/post/running-a-flask-application-as-a-service-with-systemd

# Settup the test.

Afther i made a server settup in digital ocean, a communication with github, and a working flask script i had to test it. for this purpose i used pytest. I stuggled alot to make my own pytest but it turns out that github has alot of default settups for this. You might already reconized this first half of the python-app.yml file.
