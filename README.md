For full operation, check fabfile.py

## To make yourself able to push and deploy

1. Add your key to git-receive
`fab add_upload_key:chpapa,keyfile=id_rsa.pub`

2. Add deployment target
`git remote add skygeario git@chima-facebook.skygeario.com:chima-fb`

3. Change your code

4. To deploy
`git push skygear master -f`

