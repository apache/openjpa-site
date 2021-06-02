Title: Release Setup

<a name="Release-Setup"></a>


These setup steps only need to be performed on a particular machine once.
 
<table class="info"><tr>
  <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
  <td>Developers using Linux workstations can skip over the references to Cygwin.  If using Windows, install cygwin, including <b>Utils/gnupg</b> and <b>Net/openssh</b> packages.<br/><br/>
  See <a href="http://www.gnupg.org/gph/en/manual.html">GNU Privacy Handbook</a> for a quick start on the basic concepts.
</tr></table>

<a name="ReleaseSetup-CreateandinstallaSSHkey"></a>

## Create and install a SSH key

1. Open a shell window.	If using Windows, open a cygwin window.
1. Use ssh-keygen to create an SSH key.

   <span class="note"> ssh-keygen dsa key type only accept 1024 bits; use rsa / 4096 bits instead.</span>

        $ ssh-keygen -t rsa -b 4096

   Program defaults should be fine. No passphrase is required for the ssh key generation. The keys will be saved in ~/.ssh/id_rsa (private) and ~/.ssh/id_rsa.pub (public).
    
<table class="info"><tr>
      <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
      <td>

See [Authenticating By Public Key(OpenSSH)](http://www.networknewz.com/networknewz-10-20030707AuthenticatingbyPublicKeyOpenSSH.html) for a good description on why and how to perform this task.

</tr></table>
    
1. scp your SSH public key ~/.ssh/id_rsa.pub created in last step to ~/id_rsa.pub on people.apache.org.
    
        $ cd ~/.ssh
        $ scp id_rsa.pub <your userid>@people.apache.org:id_rsa.pub 
    
    You will be prompted for your password.

1. Use ssh to login to people.apache.org 

        $ cd ~
        $ ssh <your userid>@people.apache.org

    At this point, you will still be prompted for your password.

1. Create a ~/.ssh folder in your home directory on people.apache.org and change its file mode to 700.

        $ mkdir ~/.ssh
        $ chmod 700 ~/.ssh

1. Move or append ~/id_rsa.pub to ~/.ssh/authorized_keys and change its file mode to 600.  

        $ mv ~/id_rsa.pub ~/.ssh/authorized_keys
         or
        $ cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
        $ chmod 600 ~/.ssh/authorized_keys

<table class="info"><tr>
    <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
    <td>
    
   * Each public key in the **`authorized_keys`**<a name="ReleaseSetup-CreateandinstallaSSHkey"></a>
 spans only one line. For example:
             
          "ssh-dss AAAAB3NzaC1kc3MAAA ..... agBmmfZ9uAbSqA== dsa-key-20071107"
            
   * '#' in the first column is a comment line.

</tr></table>

1. Exit out of this ssh session.

1. Start a new ssh session.  No login should be required this time due to the private ssh key on your local box matching up with the public ssh key in your home directory (~/.ssh).

        $ ssh <your userid>@people.apache.org

<table class="info"><tr>
      <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
      <td>If you are still prompted for a password, then you have not set up the ssh keys properly.	Review the steps above and ensure that all of the steps were followed properly.  Or, maybe the instructions are still not quite right and they still need some adjusting.  In that case, please update the instructions accordingly.  :-)

</tr></table>

<a name="ReleaseSetup-CreateaGPGkey"></a>

## Create a GPG key

1. Open a shell window.	If using Windows, open a cygwin window.

<table class="info"><tr>
  <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
  <td>

  * The generated keys are stored in:
    * *nix - $HOME/.gnupg
    * Windows XP - %HOME%\Application Data\gnupg
    * Windows 7 - C:\ProgramData\GNU\etc\gnupg

  * "gpg --version" shows the GnuPG's home location.
  * Follow the latest steps and guides on the ASF website at [http://www.apache.org/dev/openpgp.html#generate-key](http://www.apache.org/dev/openpgp.html#generate-key) as you need to disable using SHA1 and new keys should be 4096 bits. 
  * Append the following text to gpg.conf.
  
        personal-digest-preferences SHA512
        cert-digest-algo SHA512
        default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 \
            ZLIB BZIP2 ZIP Uncompressed

    * If you are using an existing gpg certificate, update your current certificate with the above preference using:
    
            leealber@jpadev:~/.gnupg$ gpg --edit-key Albert Lee
            Secret key is available.
            
            pub  1024D/8007117F  created: 2007-11-05  expires: never       usage: SC  
    	        	     trust: ultimate	  validity: ultimate
            sub  2048g/8D910F8A  created: 2007-11-05  expires: never       usage: E   
            [ultimate] (1). Albert Lee (CODE SIGNING KEY) <allee8285@apache.org>
    
            Invalid command  (try "help")
    
            Command> showpref
            [ultimate] (1). Albert Lee (CODE SIGNING KEY) <allee8285@apache.org>
                 Cipher: AES256, AES192, AES, CAST5, 3DES
                 Digest: SHA512, SHA384, SHA256, SHA224, SHA1
                 Compression: ZLIB, BZIP2, ZIP, Uncompressed
                 Features: MDC, Keyserver no-modify
   
            Command> setpref SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB \
                BZIP2 ZIP Uncompressed
            Set preference list to:
                 Cipher: AES256, AES192, AES, CAST5, 3DES
                 Digest: SHA512, SHA384, SHA256, SHA224, SHA1
                 Compression: ZLIB, BZIP2, ZIP, Uncompressed
                 Features: MDC, Keyserver no-modify
            Really update the preferences? (y/N) y
    
            pub  1024D/8007117F  created: 2007-11-05  expires: never       usage: SC  
    	        	     trust: ultimate	  validity: ultimate
            sub  2048g/8D910F8A  created: 2007-11-05  expires: never       usage: E   
            [ultimate] (1). Albert Lee (CODE SIGNING KEY) <allee8285@apache.org>
    
            Command>

</tr></table>

1. Generate a key-pair with gpg, using default key kind ("DSA and Elgamal") and ELG-E keys size (2048).

        $ gpg --gen-key

    The program's default values should be fine.  For the "Real Name" enter your full name (ie. Stan Programmer).  For the "e-mail address" enter your apache address (ie. sprogrammer@apache.org).  You will also be required to enter a "passphrase" for the GPG key generation.  Keep track of this as you will need this for the Release processing.
    
<table class="info"><tr>
    <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
    <td>Save the content in this subdirectory to a safe media. This contains your private key used to sign all the release materials.
    </tr></table>
    
1. Backup your cygwin home directory to another media
1. Append your public key to [https://svn.apache.org/repos/asf/openjpa/KEYS](https://svn.apache.org/repos/asf/openjpa/KEYS)
 and <http://www.apache.org/dist/openjpa/KEYS>. See the commands describe at the beginning of this KEYS file to perform this task. The gpg key-pair is used to sign the published artifacts for the releases.
 
        $ ( gpg --list-sigs <Real Name> && gpg --armor --export <Real Name> ) >> KEYS

<table class="info"><tr>
      <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
      <td>

    * The <https://svn.apache.org/repos/asf/openjpa/KEYS> file is updated via normal svn commit procedures.

            svn co https://svn.apache.org/repos/asf/openjpa --depth empty
            cd openjpa
            svn up KEYS
            ( gpg --list-sigs <Real Name> && gpg --armor --export <Real Name> ) >> KEYS
            svn commit KEYS --message "update gpg public key for ME."

    * The one under www.apache.org/dist/ has to be manually updated. 

            scp KEYS yourid@people.apache.org:/www/www.apache.org/dist/openjpa/KEYS
        
</tr></table>
    
1. Submit your public key to a key server. E.g. <http://pgp.surfnet.nl:11371/> or <http://pgp.mit.edu/>

1. Following the instructions in <http://people.apache.org/~henkp/trust/> and ask multiple (at least 3) current Apache committers to sign your public key.
    
## Update Maven settings for our servers
    
1. Create a settings.xml under .m2

        <settings xmlns="http://maven.apache.org/POM/4.0.0"
    	      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	      xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
              http://maven.apache.org/xsd/settings-1.0.0.xsd">
          <servers>
            <!-- SCP settings for people.apache.org -->
            <server>
    	      <id>people.apache.org</id>
    	      <username>$USERNAME</username>
    	      <privateKey>$PATH_TO_PRIVATE_KEY</privateKey>
    	      <passphrase>$SSH_PASSPHRASE</passphrase>
    	      <directoryPermissions>775</directoryPermissions>
    	      <filePermissions>644</filePermissions>
    	      <!-- following is only for Windows only
    	        <configuration>
    	          <sshExecutable>plink</sshExecutable>
    	          <scpExecutable>pscp</scpExecutable>
    	          <scpArgs>-2Bp</scpArgs>
    	          <sshArgs>-2</sshArgs>
    	        </configuration>
    	      -->
            </server>
            <!-- ASF Nexus settings -->
            <server>
    	      <id>apache.snapshots.https</id>
    	      <username>$USERNAME</username>
    	      <password>$APACHE_LDAP_PWD</password>
            </server>
            <server>
    	      <id>apache.releases.https</id>
    	      <username>$USERNAME</username>
    	      <password>$APACHE_LDAP_PWD</password>
            </server>
          </servers> 
          <profiles>
    	    <profile>
    	      <id>apache-release</id>
    	      <properties>
    		    <site.deploy.user.name>$USERNAME</site.deploy.user.name>
    		    <gpg.passphrase>$GPG_PASSPHRASE</gpg.passphrase>
    	      </properties>
    	    </profile>
    	    <profile>
    	      <id>gpg-passphrase</id>
    	      <properties>
    		    <gpg.passphrase>$GPG_PASSPHRASE</gpg.passphrase>
    	      </properties>
    	    </profile>
          </profiles>
        </settings>

<table class="info"><tr>
  <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
  <td>

  * __$USERNAME__ is the remote username on people.apache.org, not your local userid.
  * __$PATH_TO_PRIVATE_KEY__ is the path to the private key generated for ssh. E.g. /home/yourLocalUserId/.ssh/id_rsa.  For Windows' cygwin users, you will need to enter the full cygwin path: /cygdrive/c/cygwin/home/yourLocalUserId/.ssh/id_rsa.
  * __$SSH_PASSPHRASE__ for the supplied __$PATH_TO_PRIVATE_KEY__.  If you don't use this in your settings.xml file, then you will be prompted for it during the Release processing.
  * __$GPG_PASSPHRASE__ is pass phase for the GPG key.
  * __$APACHE_LDAP_PWD__ is your Apache LDAP password, which is shared between SVN and password login for  people.apache.org.

</tr></table>
