Title: Releasing OpenJPA 1.2.x (Old SCP Steps)

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-ReleasingOpenJPA"></a>

# Releasing OpenJPA
These instructions guide the release manager through the steps of making an
official OpenJPA release.

_Work in progress. Times are just guesses and some information may be
missing._

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-Prerequisites"></a>

## Prerequisites

// TODO MDD Still may need some work...

1. You should read the [OpenJPA Release Policy](openjpa-release-policy.html)
 to decide on the name of the new release, based on the content.
1. You should read the Apache [Release FAQ](http://www.apache.org/dev/release.html)
1. You must have shell access to people.apache.org
1. You must have the following utilities installed on your local machine and
available in your path:
1. * Java SE 5.0 (for 1.2.x and 1.3.x) or Java SE 6 (for 2.0.x) (prefer Sun
JDK over IBM JDK)
1. * [Maven 2](http://maven.apache.org/)
 (at least version 2.0.10)
1. * [ssh](http://www.openssh.com/)
 (cygwin covers this on Windows)
1. * [gnupg](http://www.gnupg.org/)
 (cygwin covers this on Windows)
1. For Windows users, install [Cygwin](http://cygwin.com/)
 in addition to the above utilities
1. * Make sure the Net/openssh and Utils/gnupg packages are installed that
come with Cygwin installation. 

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-Tasksthatneedtobeperformedforeachrelease"></a>

## Tasks that need to be performed for each release

_The example below uses 1.2.x as the new branch and 1.2.0 as the new
release._

  
  
* Cleanup JIRA so the Fix Version in issues resolved since the last release
includes this release version correctly.
* Update the files in openjpa-project -
** Update the CHANGES.txt and RELEASE_NOTES.html based on the Text and HTML
release reports from JIRA.
** Review and update BUILDING.txt if needed.
* Stage any Roadmap or Release landing pages on the wiki.
* Use "mvn rat:check" to verify the source has the required headers before
trying to release.
* Perform a full build (IANAL + tests) and TCK runs before trying to
release.
  
  
* set MAVEN_OPTS=-Xmx1024m -XX:MaxPermSize=256m (especially for Java SE 6)
* Use Sun JDK (if possible)
** If using IBM JDK, then also set the system property test.jvm.arguments
to -Xdump:none (Avoids OOM heap dumps on selected tests.  These extra files
throw off the rat:check processing.)  For example,
{code:none}
mvn -Dtest.jvm.arguments="-Xdump:none" ...

    * On Windows, use a cygwin window (vs a standard DOS prompt window) for the
Release processing.||
    || Monday, 12:01 \\ | ??? For new major releases (like 2.0.0) create a
sub-branch off of the parent branch from which to make the release.
Releasing from a branch will allow any cosmetic changes that need to be
made for the release to be approved to be done without preventing other
more disruptive advances in the trunk from potentially causing problems
with the release. A branch can be made by running: \\
    {code:none}
    $ mvn release:branch -DbranchName=1.2.x

  
  
* Do not use Eclipse to do the checkout.  The extra dot (.) files created
by Eclipse throws off the rat:check processing. 
{code:none} $ svn checkout
https://svn.apache.org/repos/asf/openjpa/branches/1.2.x 1.2.x
$ cd 1.2.x {code}||
  
  
<table>
<tr></tr>
  
  
{code:none} $ svn commit -m "updating text files for 1.2.0 release"

    || Monday, 12:11 \\ | Do a dry run of the release plugin. The dry run will
not commit any changes back to SVN and gives you the opportunity to verify
that the release process will complete as expected. You will be prompted
for the following information :
    # The new release number (default 1.2.0) 
    # The SCM tag (default apache-openjpa-1.2.0) *this should be changed to
just 1.2.0
    # The new development version (default 1.2.1) 
    # _optional_ if you have not specified a GPG passphrase in settings.xml you
will be prompted for it. 
    {code:none}$ mvn -Prelease,docbook-profile release:prepare -DdryRun=true  
        <snip>
     [INFO]
 [release:prepare]
     [INFO]
 Verifying that there are no local modifications...
     [INFO]
 Executing: svn --non-interactive status
     [INFO]
 Working directory: /home/mikedd/workspaces/temp/jpadev/branches/1.0.x
     [INFO]
 Checking dependencies and plugins for snapshots ...
        What is the release version for "OpenJPA"?
(org.apache.openjpa:openjpa-parent) 1.2.0: : 
        What is SCM release tag or label for "OpenJPA"?
(org.apache.openjpa:openjpa-parent) openjpa-parent-1.2.0: : 1.2.0
        What is the new development version for "OpenJPA"?
(org.apache.openjpa:openjpa-parent) 1.2.1-SNAPSHOT: : 
        {code} ||
    || Monday, 12:30 \\ | Validate that the release process completed as
expected. The release plugin will create pom.xml.tag files which contain
the changes that would have been committed to SVN. The only differences
between pom.xml.tag and it's corresponding pom.xml file should be the
version number. If other formatting changes have been made you should
rollback the release and commit the changes manually.
    {code:none}$ mvn -Prelease,docbook-profile release:rollback 
    # make changes
    $ svn commit -m "fixing formatting for 1.2.0 release" {code} ||
    || Monday, 12:31 \\ | Assuming the .tag files look OK you may proceed and
do any other validation you feel necessary. The following list may be
helpful 
    * verify signatures [Verifying release signatures]
    * run examples. [Running OpenJPA Examples]
    * if you have access to the TCK, run it [Running the TCK]
|| 
    || Monday, 12:52 \\ | Prepare the release. You'll be prompted for the
version information and optionally your GPG passphrase again.
    {code:none} $ mvn -Dmaven.test.execute=false -Prelease release:prepare
{code}
    For the 2.0.x code, different steps are required as there are problems with
the maven-jar-plugin and maven-release-plugin when using the test-jar goal.
 See [http://jira.codehaus.org/browse/MJAR-68]
  and [http://jira.codehaus.org/browse/MRELEASE-285]
.
    {code:none} $ mvn -DskipTests=true -Prelease release:prepare
-DpreparationGoals="clean install"
     $ mvn clean install -Dtest=false -DfailIfNoTests=false
-Dmaven.test.execute=false 
     $ mvn -DskipTests=true -Prelease release:prepare -DpreparationGoals="clean
install" {code} ||
    || Monday, 13:12 \\ | Check release.properties and make sure that the scm
properties have the right version. Sometimes the scm location can be the
previous version not the next version. For example if the new version is
1.2.2 you shouldn't see 1.2.1 in the file. \\
    {note}Backup (zip or tar) your local directory in case you need to rollback
the release.{note} ||
    || Monday, 13:15 \\ | Perform the release. This step will create a maven
repository for use in testing on
people.apache.org:/home/userName/public_html/openjpa/newVersion. You will
may be prompted for your people.apache.org password several times if you
have not added a ssh key to .authorized_keys. [#One time setup#people.apache.org]
. 
    {code:none}$ mvn -Prelease,docbook-profile release:perform {code} 
    For the 2.0.x code, you'll need additional parameters, due to the test-jar
issues.
    {code:none}$ mvn -Prelease,docbook-profile,test-derby release:perform
{code} 
    {info} If your local OS userid doesn't match your Apache userid, then
you'll have to set -Duser.name=<your_apache_id> on the cmdline and/or
update your release profile in settings.xml {info} ||
    || Monday, 13:40 \\ | Create and upload the site. This step also uploads
data to people.apache.org. 
    For 1.x releases:
    {code:none} 
    $ cd target/checkout
    $ mvn -Prelease,docbook-profile site site:deploy {code} 
    {warning} *For 2.x releases*, this step is not needed, as the
maven-release-plugin is configured with goals "deploy site site:deploy"
{warning} ||
    || Monday, 13:41 \\ | Unzip the binary archive the staging site directory
    {code:none}
    # ssh to people.apache.org 
    $ cd ~/public_html/openjpa/${pom.version}/staging-site
    $ unzip -qq
apache-openjpa/downloads/apache-openjpa-${pom.version}-binary.zip 

Verify that the HTML links in staging-site/index.html are correct (usually
only the downloads and docs links need to be updated to be prefixed with
apache-openjpa/)
  
  
See [http://people.apache.org/~henkp/repo/faq.html](http://people.apache.org/~henkp/repo/faq.html)
 and [http://www.apache.org/dev/release-signing.html#openpgp-ascii-detach-sig]
 {note}
  
  
  
  
  
  
{code:none} $ mvn stage:copy
-Dsource="http://people.apache.org/~mikedd/openjpa/1.2.0/staging-repo" \
 
-Dtarget="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"
\
  -Dversion=1.2.0 \
  -DtargetRepositoryId=apache.releases

    After the stage plugin completes it's a good idea to check the permissions
on the file system. 

$ ssh people.apache.org
$ cd
/www/people.apache.org/repo/m2-ibiblio-rsync-repository/org/apache/openjpa/
$ ls -l openjpa-examples/1.2.0

1. if you see something like the following you probably need to change the
permissions.
1. *-rw-r--r--*	1 mikedd  apcvs  59162 Jul 23 09:34
openjpa-examples-1.2.0-javadoc.jar

$ for file in `find
/www/people.apache.org/repo/m2-ibiblio-rsync-repository/org/apache/openjpa/
-type d -iname '1.2.0'`\
  do \
  chmod -R g+w ${file} \ 
  done

$ ls -l openjpa-examples/1.2.0

1. Now it should look something like this
1. *-rw-rw--r--*  1 mikedd  apcvs  59162 Jul 23 09:34
openjpa-examples-1.2.0-javadoc.jar

    || Thursday, 14:00 \\ | Copy build artifacts to the openjpa/builds location
on people.apache.org. 
    {code:none}# ssh to people.apache.org
    $ cp -r ~/public_html/openjpa/1.2.0/staging-site/
/www/openjpa.apache.org/builds/1.2.0
    $ chmod -R g+w /www/openjpa.apache.org/builds/1.2.0
    # verify that /www/openjpa.apache.org/builds/1.2.0/docs/manual is populated
correctly by comparing it to a previous release. 
    $ rm /www/openjpa.apache.org/docs/latest
    $ ln -fvs ../builds/1.2.0/apache-openjpa/docs/
/www/openjpa.apache.org/docs/latest {code} ||
    || Thursday, 14:10 \\ | Copy the distribution files to dist on
people.apache.org. 
    {code:none} 
    # ssh to people.apache.org
    
    # verify that md5 and sha1 files were generated for the download artifacts
    ls /www/openjpa.apache.org/builds/1.2.0/apache-openjpa/downloads/*.md5
    ls /www/openjpa.apache.org/builds/1.2.0/apache-openjpa/downloads/*.sha1
    
    # if no md5 and sha1 files are present, generate them. 
    # Alternatively you can copy the artifacts from the staging-repo directory
the checksums are generated there.
    for file in `ls . ` 
    do 
    md5 -q ${file} > ${file}.md5
    sha1 -q ${file} > ${file}.sha1
    done
    
    mkdir /www/www.apache.org/dist/openjpa/1.2.0
    cp -r /www/openjpa.apache.org/builds/1.2.0/apache-openjpa/downloads/*
/www/www.apache.org/dist/openjpa/1.2.0
    chgrp -R openjpa /www/www.apache.org/dist/openjpa/1.2.0
    chmod -R g+w /www/www.apache.org/dist/openjpa/1.2.0
    
    # remove the previous version from /dist. Ie if you're publishing 1.2.1 you
would remove 1.2.0.
    # For this example we wouldn't remove anything, but for the next release
(1.2.1) we'd do the following : 
    $ rm -Rf /www/openjpa.apache.org/dist/openjpa/1.2.0

<table>
<tr><th> Thursday, 14:15 </td><td> Update the [JIRA versions ](-https://issues.apache.org/jira/secure/project/manageversions.jspa?pid=12310351.html)
 page to mark the version as "released", and set the date to the date that
the release was approved. You may also need to make a new release entry for
the subsequent release.</th></tr>
<tr><th> Friday, 14:15 </td><td> After the mirrors have had time to update (24 hours to
be on the safe side) update the [Downloads](downloads.html)
 and [Documentation]
 pages with the new release </th></tr>
<tr><th> Friday, 14:15 </td><td> Make a [news announcement](http://cwiki.apache.org/confluence/pages/createblogpost.action?spaceKey=openjpa)
 on the OpenJPA wiki. {info}Once the news item is made, it won't show up on
the [front page</td><td>http://cwiki.apache.org/openjpa/]
 unless you make some minor edit to the containing page (e.g., adding a
newline somewhere).{info} </th></tr>
<tr><th> Friday, 14:15 </td><td> Make an announcement about the release on the [mailto:users@openjpa.apache.org](mailto:users@openjpa.apache.org.html)
 list (and, for major releases, on the [mailto:announce@apache.org]
 list as per [the Apache Announcement Mailing Lists page</td><td>http://www.apache.org/foundation/mailinglists.html#foundation-announce]
). The announcement might look something like [this</td><td>http://www.nabble.com/-ANNOUNCE--Apache-OpenJPA-1.0.0-released-p12397604.html]
. </th></tr>
<tr><th> Friday, 14:20 </td><td> Make an announcement for the [freshmeat.net OpenJPA project](http://freshmeat.net/projects/openjpa/)
 (optional) </th></tr>
<tr><th> Friday, 14:30 </td><td> Have a beer and enjoy your weekend while the world's
grateful programmers revel in yet another high-quality release of Apache
OpenJPA! </th></tr>
</table>

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-Onetimesetup"></a>

## One time setup

These setup steps only need to be performed on a particular machine once.
{info}Developers using Linux workstations can skip over the references to
Cygwin.  If using Windows, install cygwin, including *Utils/gnupg* and
*Net/openssh* packages.
{info}

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-CreateandinstallaSSHkey"></a>

### Create and install a SSH key

<table>
<tr><th> 1 </td><td> Open a shell window.  If using Windows, open a cygwin window.  </th></tr>
<tr><th> 2 </td><td> Use ssh-keygen to create an SSH key.
</tr>
{note}Follow the latest steps and guides on the ASF website at [http://www.apache.org/dev/openpgp.html#generate-key](http://www.apache.org/dev/openpgp.html#generate-key)
 as you need to disable using SHA1 and new keys should be 4096 bits.{note}
{code:none}
$ ssh-keygen -t dsa

    * Program defaults should be fine.  No passphrase is required for the ssh
key generation.  The keys will be saved in ~/.ssh/id_dsa (private) and
~/.ssh/id_dsa.pub (public).
    {info} See [Authenticating By Public Key (OpenSSH)|http://www.networknewz.com/networknewz-10-20030707AuthenticatingbyPublicKeyOpenSSH.html]
 for a good description on why and how to perform this task.
    {info} ||
    || 3 | {{scp}} your SSH public key ~/.ssh/id_dsa.pub created in last step
to ~/id_dsa.pub on people.apache.org.
    {code:none} 
    $ cd ~/.ssh
    $ scp id_dsa.pub <your userid>@people.apache.org:id_dsa.pub 
    $ You will be prompted for your password.

<table>
<tr><th> 4 </td><td> Use ssh to login to people.apache.org 
</tr>
{code:none}
$ cd ~
$ ssh <your userid>@people.apache.org

    * At this point, you will still be prompted for your password. ||
    || 5 | Create a ~/.ssh folder in your home directory on people.apache.org
and change its file mode to 700.
    {code:none}
    $ mkdir ~/.ssh
    $ chmod 700 ~/.ssh

<table>
<tr><th> 6 </td><td> Move or append ~/id_dsa.pub to ~/.ssh/authorized_keys and change its
file mode to 600.
</tr>
{code:none}
$ mv ~/id_dsa.pub ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/authorized_keys

    {info}
    * Each public key in the {{authorized_keys}} spans only one line.
    ** For example: "{{ssh-dss AAAAB3NzaC1kc3MAAA ..... agBmmfZ9uAbSqA==
dsa-key-20071107}}"
    * '#' in the first column is a comment line.
    {info} ||
    || 7 | Exit out of this ssh session.  ||
    || 8 | Start a new ssh session.  No login should be required this time due
to the private ssh key on your local box matching up with the public ssh
key in your home directory (~/.ssh).
    {code:none}
    $ ssh <your userid>@people.apache.org

{info}
If you are still prompted for a password, then you have not set up the ssh
keys properly.	Review the steps above and ensure that all of the steps
were followed properly.  Or, maybe the instructions are still not quite
right and they still need some adjusting.  In that case, please update the
instructions accordingly.  :-)
{info}
<table>
<tr></tr>
</table>

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-CreateaGPGkey"></a>

### Create a GPG key

<table>
<tr><th> 1 </td><td> Open a shell window.  If using Windows, open a cygwin window. </th></tr>
<tr><th> 2 </td><td> Generate a key-pair with gpg, using default key kind ("DSA and
Elgamal") and ELG-E keys size (2048).
</tr>
{code:none}
$ gpg --gen-key

    * The program's default values should be fine.	For the "Real Name" enter
your full name (ie. Stan Programmer).  For the "e-mail address" enter your
apache address (ie. sprogrammer@apache.org).  You will also be required to
enter a "passphrase" for the GPG key generation.  Keep track of this as you
will need this for the Release processing.
    {info}
    * The generated keys are stored in $HOME/.gnupg or %HOME%\Application
Data\gnupg subdirectory.
    * Save the content in this subdirectory to a safe media. This contains your
private key used to sign all the OpenJPA release materials.
    {info} ||
    || 3 | Backup your cygwin home directory to another media ||
    || 4 | Add your public key to {{[https://svn.apache.org/repos/asf/openjpa/site/docs/KEYS]
}} and {{http://www.apache.org/dist/openjpa/KEYS}}. See the commands
describe at the beginning of this KEYS file to perform this task. The gpg
key-pair is used to sign the published artifacts for the OpenJPA releases. 
    {code:none}
    $ gpg --list-sigs <Real Name> && gpg --armor -- export <Real Name>

{info}The {{[https://svn.apache.org/repos/asf/openjpa/site/docs/KEYS](https://svn.apache.org/repos/asf/openjpa/site/docs/KEYS)
}} file is updated via normal svn commit procedures.  How the
*http://www.apache.org/dist/openjpa/KEYS* file gets updated is still a
mystery to me...
{info} ||
<table>
<tr><th> 5 </td><td> Following the instructions in [http://people.apache.org/~henkp/trust/](http://people.apache.org/~henkp/trust/)
 and ask someone in the OpenJPA project to sign your public key. </th></tr>
<tr><th> 6 </td><td> Submit your public key to a key server. E.g. [http://pgp.surfnet.nl:11371/](http://pgp.surfnet.nl:11371/)
 or [http://pgp.mit.edu/]
</th></tr>
</table>

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-UpdateMavensettingsforourservers"></a>

### Update Maven settings for our servers

<table>
<tr><th> 1 </td><td> Create a settings.xml under .m2 (in your Document and Settings
folder in Windows) </th></tr>
<tr><td> </td><td> {code:xml</td><td>title=settings.xml</td><td>borderStyle=solid}
</tr>
<settings xmlns="http://maven.apache.org/POM/4.0.0"
	  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/settings-1.0.0.xsd">
    <servers>
       <server>
	  <id>people.apache.org</id>
	  <username>$USERNAME</username>
	  <privateKey>$PATH_TO_PRIVATE_KEY</privateKey>
	  <directoryPermissions>775</directoryPermissions>
	  <filePermissions>644</filePermissions>
       </server>
    </servers>	  
</settings>

    {info}
    * {{$USERNAME}} is the remote username on people.apache.org, not your local
userid.
    * {{$PATH_TO_PRIVATE_KEY}} is the path to the private key generated for
ssh. E.g. /home/yourLocalUserId/.ssh/id_dsa.  For Windows' cygwin users,
you will need to enter the full cygwin path: 
/cygdrive/c/cygwin/home/yourLocalUserId/.ssh/id_dsa.
    * You can also enter a PGP passphrase stanza:  <passphrase>..</passphrase>.
 If you don't use this in your settings.xml file, then you will be prompted
for it during the Release processing.
    {info} |
    
    h3. Expose a copy of known hosts to Maven
    {info}
    Is this step even necessary?  Due to the question mark below without an
explanation of the new location for this alternate .ssh folder, I never
performed these steps.	And, the release process still seemed to work okay
for me...  The next person to use these instructions can verify whether any
tricks had to be played with the .ssh folders...
    {info}
    
    || 1 | From cygwin, ssh to people.apache.org, save the public key if
prompted, and exit ||
    | | cygwin will save the known hosts to your {{\~/.ssh}} folder, but the
script cannot access it there (from Windows) |
    || 2 | From cygwin (not Windows) create another {{.ssh}} folder at (?) ||
    || 3 | Copy the {{known_hosts}} file to the new {{.ssh}} folder ||
    
    h2. Troubleshooting
    
    h3. Space Character in Build Root Path
    
    || Description | If there are spaces in the path to the build root
subdirectory, the maven task uses to generate the revision number for the
org.apache.openjpa.revision.properties yields incorrect data. For example:
    {code:title=org.apache.openjpa.revision.properties|borderStyle=solid}
    revision.number=Type 'svnversion --help' for usage.
    openjpa.version=1.0.1

<table>
<tr><th> Solution </td><td> Rename the path and remove all spaces. </th></tr>
</table>

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-MerginglocalrepositorytoremoterepositoryinCygwin/Windows"></a>

### Merging local repository to remote repository in Cygwin/Windows

<table>
<tr><th> Description </td><td> The "maven-stage-plugin" is very sensitive to the
parameters being passed to it, i.e. the source and target URL properties.
When this plugin is used under Cygwin, make sure the following practices
are used:
</tr>
  
  
Problem symptom:

    $ find . -name m2-repository -not -path "*openjpa-project*" \
        -exec mvn -f "c:/tmp/maven-stage-plugin/pom.xml" stage:copy \
        -Dsource=file://{}
-Dtarget=scp://allee8285@people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository
\
        -Dversion=1.0.1 \;
    [INFO]
 Scanning for projects...
    [INFO]
 Searching repository for plugin with prefix: 'stage'.
    ........
    [INFO]
 Downloading file from the source repository:
    [INFO]
 ------------------------------------------------------------------------
    [ERROR]
 BUILD ERROR
    [INFO]
 ------------------------------------------------------------------------
    [INFO]
 Error copying repository from
file://./openjpa-all/target/site/m2-repository to \
          
scp://allee8285@people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository

* Quote and use the drive name in the path.
Problem symptom:

    $ find /cygdrive/c/OpenJPA.1.0.1.Release/1.0.1 -name m2-repository -not
-path "*openjpa-project*" \
        -exec mvn -f /cygwin/c/tmp/maven-stage-plugin/pom.xml stage:copy \
        -Dsource=file://{}
-Dtarget=scp://allee8285@people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository
\
        -Dversion=1.0.1 \;
    [INFO]
 Scanning for projects...
    [INFO]
 Searching repository for plugin with prefix: 'stage'.
    ........
    [INFO]
 Downloading file from the source repository:
    [INFO]
 ------------------------------------------------------------------------
    [ERROR]
 BUILD ERROR
    [INFO]
 ------------------------------------------------------------------------
    [INFO]
 Error copying repository from
file:///cygdrive/c/OpenJPA.1.0.1.Release/1.0.1/openjpa-all/target/site/m2-repository
to
          
scp://allee8285@people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository
    
    Embedded error: Could not read from file:
c:\cygdrive\c\OpenJPA.1.0.1.Release\1.0.1\openjpa-all\target\site\m2-repository
    \cygdrive\c\OpenJPA.1.0.1.Release\1.0.1\openjpa-all\target\site\m2-repository
(Access is denied.)

* Specify the people.apache.org user id in the target property.
Problem symptom:

    $ find "c:/OpenJPA.1.0.1.Release/1.0.1" -name m2-repository -not -path
"*openjpa-project*" \
       -exec mvn -f "c:/tmp/maven-stage-plugin/pom.xml" stage:copy 
       -Dsource=file://{}
-Dtarget=scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository
\
       -Dversion=1.0.1 \;
    [INFO]
 Scanning for projects...
    [INFO]
 Searching repository for plugin with prefix: 'stage'.
    [INFO]

----------------------------------------------------------------------------
    ........
    [INFO]
 Downloading file from the source repository:
/org/apache/openjpa/openjpa/maven-metadata.xml.sha1
    [INFO]
 Downloading metadata from the target repository.
    Password:: *********
    ........
    Password:: *********
    [INFO]
 ------------------------------------------------------------------------
    [ERROR]
 BUILD ERROR
    [INFO]
 ------------------------------------------------------------------------
    [INFO]
 Error copying repository from
file://c:/OpenJPA.1.0.1.Release/1.0.1/openjpa-all/target/site/m2-repository
to \
          
scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository

<table>
<tr><th> Solution </td><td> As recommended in the descriptions.
</tr>
{note}For example:

    find "c:/OpenJPA.1.0.1.Release/1.0.1" -name m2-repository -not -path
"*openjpa-project*" \
        -exec mvn -f "c:/tmp/maven-stage-plugin/pom.xml" stage:copy \
        -Dsource=file://{} \
       
-Dtarget=scp://allee8285@people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository
\
        -Dversion=1.0.1 \;


<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-Cygwin/WindowsFilePath"></a>

### Cygwin/Windows File Path

<table>
<tr><th> Description </td><td> For Cygwin/Windows user: file and folder path names using
drive identifier (e.g. *C:\OpenJPA Release\1.0.1\* ) in commands can be
expressed as */cygwin/c/OpenJPA Release/1.0.1/*. This form of path name
specification may have inconsistent and undesirable behaviors.</th></tr>
<tr><th> Solution </td><td> Consistently use the following naming conventions:
</tr>
* Continue to use the Windows form of path name, e.g. *C:\a\b\c*
* Use *'/'* instead of *'\'* character as file separator, e.g.
*C:/a/b/c*
* Quote all path name using *'"'* character, e.g. "*C:/a/b/c*"
* Avoid using space characters in path name, e.g.
"*C:/OpenJPA.Release/1.0.1*"
 ||
</table>

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-"Toomanyunapprovedlicenses:""></a>

### "Too many unapproved licenses:"

<table>
<tr><th> Description </td><td> Encounter the "Too many unapproved licenses:" message
while running the "license-verify-profile" profile in "{{mvn deploy
site...}}" step. This is caused by extra artifacts in the build tree that
the license verification plugin does not recognized. Examples of these
artifacts are:
</tr>
1. Eclipse control files, .classpath, .project
1. User created log files ||
<tr><th> Solution </td><td> Avoid the followings:
</tr>
1. Don't use Eclipse's svn plugin to "Check out" files to a Eclipse project.
Simply use the svn command, as described in the release instructions.
1. Don't create, directly or indirectly, any files under the release build
tree.
1. Don't use the IBM JDK.  By default, the IBM JDK will create heap dumps
when hitting the OOM condition in some of our tests.  These extra files
throw off the rat:check processing.  If you must use the IBM JDK, then also
set MAVEN_OPTS=-Xdump:none.
 ||
</table>

<a name="ReleasingOpenJPA1.2.x(OldSCPSteps)-Resources"></a>

## Resources

* Apache Apache [Release FAQ](http://www.apache.org/dev/release.html)
* [Signing Releases](http://apache.org/dev/release-signing.html)
* [Wendy's notes on Release Signing](http://wiki.wsmoak.net/cgi-bin/wiki.pl?ReleaseSigning)
* Apache [Mirroring Guidelines](http://apache.org/dev/mirrors.html)
* Struts [Release Instructions](http://cwiki.apache.org/WW/creating-and-signing-a-distribution.html)
 (upon which these instructions are based)
