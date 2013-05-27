##########################################################
#Working                                                 #
##########################################################
import paramiko
import os

#Create Paramiko Object
ssh = paramiko.SSHClient()
privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
print privatekeyfile
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('staging-anz.aws.cottonon.com',username='ubuntu', password=mykey)
##########################################################
#stdin, stdout, stderr 
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('dir')
print "output", ssh_stdout.read() #Reading output of the executed command