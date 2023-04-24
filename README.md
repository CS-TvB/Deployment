# Deployment

in this assignment i had to make a continuous deployment pipeline to my server. first i had to make an account on digital ocean to create a droplet. 
afther wich i could do a apt --update and install all the necessities like flask, gunicorn, python, pip etc. 

# for me the most challaging part of this assignments where the secrets and keys in github.

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


To create a deploy key in GitHub, you need to follow these steps:

1. Generate a new SSH key pair. You can use the ssh-keygen command on your local machine to generate a new key pair. 
2. Make sure to specify a name for your key pair that makes it clear that it's a deploy key.
3. Add the public key to your repository as a deploy key. To do this, go to your repository on GitHub, click on the "Settings" tab, 
   and then click on "Deploy keys" in the sidebar. Click on "Add deploy key", and then paste the public key you generated in step 1 into the "Key" field. 
4. Give your deploy key a name that describes what it's used for.
5. Add the private key to your deployment server. You'll need to copy the private key you generated in step 1 to your deployment server. 
6. Make sure to keep the private key secure and not share it with anyone else.
7. Configure your deployment script to use the private key. You'll need to modify your deployment script to use the private key you copied to your deployment server. 
8. The exact steps to do this will depend on your deployment script and server setup.

By following these steps, you can create a deploy key in GitHub that allows your deployment server to access your repository securely.

Afther i made a server settup in digital ocean, a communication with github, and a working flask script i had to test it. for this purpose i used pytest. i stuggled alot to make my own pytest but it turns out that github has alot of default settups for this. you might already reconized this first half of the python-app.yml file.

overal i struggled alot with this assignment but its actualy not that hard once you know what to do and how to do it.....
