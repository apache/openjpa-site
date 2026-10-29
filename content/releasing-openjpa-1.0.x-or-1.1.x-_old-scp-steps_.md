Title: Releasing OpenJPA 1.0.x or 1.1.x (Old SCP Steps)


<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-MakinganOpenJPA1.0.xor1.1.xRelease"></a>

# Making an OpenJPA 1.0.x or 1.1.x Release

These instructions guide the release manager through the steps of making an
official OpenJPA release.

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-Prerequisites"></a>

## Prerequisites

1. You should read the [OpenJPA Release Policy](openjpa-release-policy.html)
 to decide on the name of the new release, based on the content.
1. You should read the Apache [Release FAQ](http://www.apache.org/dev/release.html)
1. You must have shell access to people.apache.org
1. You must have the following utilities installed on your local machine and
available in your path:
    * [JDK 1.4 / 1.5](http://java.sun.com/)
    * [ssh](http://www.openssh.com/)
    * [Maven 2](http://maven.apache.org/)
    * [gnupg](http://www.gnupg.org/)
1. For Windows users, install [Cygwin](http://cygwin.com/)
 in addition to the above utilities
    * Make sure the Net/openssh and Utils/gnupg packages are installed that
come with Cygwin installation. 
    * Optional: [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/)

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-Tasksthatneedtobeperformedforeachrelease"></a>

## Tasks that need to be performed for each release

{info}In the examples below, it is assumed that the release name will be
**1.0.1**, and that the current checked-in version name is **1.0.1-SNAPSHOT**
and stored in the branch named *1.0.x*.{info}
  
  
  
  
{code:none}
svn copy -m "OpenJPA Release 1.0.1 branch" \
  https://svn.apache.org/repos/asf/openjpa/branches/1.0.x \
  https://svn.apache.org/repos/asf/openjpa/branches/1.0.1

    || Monday, 12:02 | Check out a clean branch from which to build the
release: \\
    {code:none}
    svn checkout https://svn.apache.org/repos/asf/openjpa/branches/1.0.1
    cd 1.0.1

{note}Make sure there is no space characters in the path to the build root subdirectory, i.e. "c:\OpenJPA 1.0.1 Release\build". See "[#Space Character in Build Root Path](#space-character-in-build-root-path.html)
"{note} ||
  
  
{code:none}
perl -pi -e
"s;<version>1.0.1-SNAPSHOT</version>;<version>1.0.1</version>;g" \
    pom.xml */pom.xml */*/pom.xml

    Update the {{<scm.dir>}} property in the top level pom.xml to the 1.0.1
release. \
    Update the {{<developer>}} element in the top level pom.xml if new
committers are added or removed. This applies to the 1.0.x branch only. ||
    || Monday, 12:10 | Verify that LICENSE.txt contains up to date licenses for
any dependencies which are included in our distribution.\\ Any jars or
source code which is included with the OpenJPA distribution that is not
covered by the Apache license must be noted in LICENSE.txt. Two examples of
this are the persistence and orm dtds (licensed under the CDDL) and Serp.
If any new non Apache dependencies have been introduced they will have to
be covered here as well. If any discrepancies are found update LICENSE.txt
and commit the changes. \\ ||
    || Monday, 12:15 | Update BUILDING.txt, CHANGES.txt and RELEASE-NOTES.html
\\
    * BUILDING.txt should be included in the source tarball and contains
instructions on how to build OpenJPA. Prior to shipping a release we should
ensure that those instructions are accurate.
    * CHANGES.txt contains a text representation of all the changes which have
been made since the preceding release. Most of the contents of this file
can be generated through JIRA's release notes mechanism [here|http://issues.apache.org/jira/secure/ConfigureReleaseNote.jspa?projectId=12310351]
    * RELEASE-NOTES.html contains general information on the OpenJPA project as
well as an html version of the changes since the preceding version. The
html change log may also be generated via JIRA.\\
    ||
    || Monday, 12:20 | Commit the POM changes \\
    {code:none}
    svn commit -m "Updated to version 1.0.1 for the release"

  
  
{code:none}
mvn clean install -Dtest=false

    || Monday, 12:23 | Now build the release locally, which will build and
test, run the Apache [Release Audit Tool|http://mojo.codehaus.org/rat-maven-plugin/]
 to verify license headers, generate the javadoc and docbook PDF and HTML,
run through the JPA TCK, build the source and binariy assemblies in
*target/site/downloads/*, and sign the release files. \\
    {code:none}
    export MAVEN_OPTS=-Xmx1000m
    mvn --batch-mode deploy site \
       
-Ptck-profile,examples-profile,license-verify-profile,javadoc-profile,docbook-profile,sign-release
\
        -Djava14.jar=${JAVA_HOME}/../../1.4/Classes/classes.jar \
        -Dtck.zip=${HOME}/.m2/privaterepos/jpa-1_0b-tck.zip

  
  
  
  
  
  
{note} The *examples-profile* has problem running automatically in this
maven build task. You will need to run the examples manually. Run the maven
command without the *examples-profile*, then perform the following steps
to run the example:

    mkdir openjpa-integration\examples\target\examples
    unzip target\site\downloads\apache-openjpa-1.0.1-binary.zip -d
openjpa-integration\examples\target\examples
    cd
openjpa-integration\examples\target\examples\apache-openjpa-1.0.1\examples\hellojpa
    ant
    cd ..\relations
    ant
    cd ..\reversemapping
    ant

{note} ||
  
  
{code:none}
gpg --multifile --verify target/site/downloads/*.asc

    || Monday, 13:01 | Upload the release candidate to [http://openjpa.apache.org/builds/1.0.1/downloads/]
: \\
    {code:none}
    mvn site:deploy

Bear in mind that uploads to
*people.apache.org/www/openjpa.apache.org/builds/* are not visible at [http://openjpa.apache.org/builds](http://openjpa.apache.org/builds)
 until after the hourly synchronization has taken place, as described at [http://www.apache.org/dev/project-site.html]
.
{warning}||
<table>
<tr><th> Monday, 15:00 </td><td> Start a vote for the release on the [mailto:dev@openjpa.apache.org](mailto:dev@openjpa.apache.org.html)
 mailing list. Votes made by committers and members of the OpenJPA project
are considered binding for this vote. For an example of the mail, see [this archived 1.0.0 vote</td><td>http://www.nabble.com/-VOTE--Approve-OpenJPA-1.0.0-release-%284th-attempt%29-p12305349.html]
 </th></tr>
<tr><th> Tuesday, Wednesday </td><td> While waiting for the vote to complete, perform
whatever manual review and testing on the release you deem appropriate. </th></tr>
  
  
  
  
{code:none}
ssh people.apache.org
cp -r /www/openjpa.apache.org/builds/1.0.1/downloads/*
/www/www.apache.org/dist/openjpa/1.0.1
chgrp -R openjpa /www/www.apache.org/dist/openjpa/1.0.1
chmod -R g+w /www/www.apache.org/dist/openjpa/1.0.1

    The OpenJPA binary release will be available via the link [http://www.apache.org/dyn/closer.cgi/openjpa/1.0.1/apache-openjpa-1.0.1-binary.zip]
 after 24 hours, as per the [Apache mirroring information|http://apache.org/dev/mirrors.html]
.
    {warning}||
    || Thursday, 15:15 | Now that the release is locked down, convert the
writeable 1.0.1 branch to a (du jure) read-only tag: \\
    {code:none}
    svn mv -m "OpenJPA Release 1.0.1 tag" \
      https://svn.apache.org/repos/asf/openjpa/branches/1.0.1 \
      https://svn.apache.org/repos/asf/openjpa/tags/1.0.1

  
  
{code:none}
svn checkout https://svn.apache.org/repos/asf/openjpa/branches/1.0.x
cd 1.0.x
perl -pi -e
"s;<version>1.0.1-SNAPSHOT</version>;<version>1.0.2-SNAPSHOT</version>;g" \
    pom.xml */pom.xml */*/pom.xml
svn commit -m "Updating version in branch to 1.0.2-SNAPSHOT"

    || Thursday, 15:20 | Update the [http://cwiki.apache.org/openjpa/downloads.html]
 page with links to the download mirrors, using the existing entries as
templates. {note}All artifacts (*apache-openjpa-1.0.1-binary.zip* and
*apache-openjpa-1.0.1-source.zip*) *must* link to the mirrors, but
signatures (*apache-openjpa-1.0.1-binary.zip.asc* and
*apache-openjpa-1.0.1-source.zip.asc*) *must not* link to mirrors.{note}||
    || Thursday, 15:30 | The documentation on the server-side must manually be
extracted on *people.apache.org*, and the links at [http://openjpa.apache.org/documentation.html]
 need to be updated with the new versions and the "latest" documentation
symbolic links need to be updated: \\
    {code:none}
    cd /www/openjpa.apache.org/builds/1.0.1/
    unzip downloads/apache-openjpa-1.0.1-binary.zip
    rm /www/openjpa.apache.org/docs/latest
    ln -fvs ../builds/1.0.1/apache-openjpa-1.0.1/docs/
/www/openjpa.apache.org/docs/latest

  
  
  
  
  
  
  
  
  
  
<table>
<tr></tr>
  
  
{code:none}
svn co
http://svn.apache.org/repos/asf/maven/plugins/trunk/maven-stage-plugin/ \
    /tmp/maven-stage-plugin
mvn -f /tmp/maven-stage-plugin/pom.xml clean install
for i in $(find openjpa-* -name m2-repository | egrep -v
"openjpa-project|openjpa-integration|openjpa-examples"); do
    cd $i
    mvn stage:copy -Dsource=file://. \
   
-Dtarget=scp://people.apache.org:/www/people.apache.org/repo/m2-ibiblio-rsync-repository
\
    -Dversion=1.0.1
    cd -
done

    This process requires Maven 2.0.5. It is currently quite delicate and
error-prone. Once the *maven-stage-plugin* is released, it should be
possible to make it more automated.
    {warning}
    {info}
    Window/Cygwin user: See [#Merging local repository to remote repository in Cygwin/Windows]
    {info}
    {info}
    Linux users: You may need to change the '-Dsource=' option to read
'-Dsource=file:{}'. The file://{} syntax may result in errors creating the
wagon file with errors like: "Repository path
/openjpa-jdbc-5/target/site/m2-repository does not exist, and cannot be
created."
    {info}
    || Thursday, 16:00 | Update the [JIRA versions | https://issues.apache.org/jira/secure/project/ManageVersions.jspa?pid=12310351]
 page to mark the version as "released", and set the date to the date that
the release was approved. You may also need to make a new release entry for
the subsequent release.||
    || Friday, 16:00 | After the mirrors have had time to update (24 hours to
be on the safe side), make a [news announcement|http://cwiki.apache.org/confluence/pages/createblogpost.action?spaceKey=openjpa]
 on the OpenJPA wiki. {note}Once the news item is made, it won't show up on
the [front page|http://cwiki.apache.org/openjpa/]
 unless you make some minor edit to the containing page (e.g., adding a
newline somewhere).{note} ||
    || Friday, 16:05 | Make an announcement about the release on the [mailto:users@openjpa.apache.org]
 list (and, for major releases, on the [mailto:announce@apache.org]
 list as per [the Apache Announcement Mailing Lists page|http://www.apache.org/foundation/mailinglists.html#foundation-announce]
). The announcement might look something like [this|http://www.nabble.com/-ANNOUNCE--Apache-OpenJPA-1.0.0-released-p12397604.html]
. ||
    || Friday, 16:10 | Make an announcement for the [freshmeat.net OpenJPA project|http://freshmeat.net/projects/openjpa/]
 (optional) ||
    || Friday, 17:00 | Have a beer and enjoy your weekend while the world's
grateful programmers revel in yet another high-quality release of Apache
OpenJPA! ||
    
    h2. One time setup
    
    These setup steps only need to be performed on a particular machine once.
    {info}Developers using Linux workstations can skip over the references to
PuTTY and Cygwin
    {info}
    
    h3. Create and install a SSH key
    
    || 1 | Install PuTTY ||
    || 2a | Use ssh-keygen to create a SSH key.
    {info} See [Authenticating By Public Key (OpenSSH)|http://www.networknewz.com/networknewz-10-20030707AuthenticatingbyPublicKeyOpenSSH.html]
 for a good description on why and how to perform this task.
    {info} ||
    || 2b | In Windows platform, use PuttyGen to create a SSH key (see Putty
help for details). 
    {info}
    * Use "*SSH-2 DSA*" key type and *1024*-bit key size.
    * Copy the content of the "Public key for pasting...." and save it to a
file named {{authorized_keys}} for later use.
    * The private key saved by PuTTYGen can only be used in Putty
configuration.	
    {info} ||
    || 3 | {{pscp}} your SSH public key {{authorized_keys}} saved in last step
to {{\~/authorized_keys}} ||
    || 4 | Use PuTTY to login to people.apache.org ||
    || 5 | Create a {{\~\.ssh}} folder and change its file mode to 700.
    || 6 | Move or append {{\~/authorized_keys}} to {{\~/.ssh/authorized_keys}}
and change its file mode to 600.
    {info}
    * Each public key in the {{authorized_keys}} spans only one line.
    ** For example: "{{ssh-dss AAAAB3NzaC1kc3MAAA ..... agBmmfZ9uAbSqA==
dsa-key-20071107}}"
    * '#' in the first column is a comment line.
    {info} ||
    || 7 | Configure putty to use your private key and save the session 
    {info}
    Specify your private key in the "Connection -> SSH -> Auth" category in
Putty configuration.
    {info}
    ||
    
    h3. Create a PGP key
    
    || 1 | Install cgywin, including *Utils/gnupg* and *Net/openssh* packages, or install gpg from {{[http://www.gnupg.org/(en)/download/index.html]
}} ||
    || 2 | Generate a key-pair with {{$ gpg \--gen-key}} using default key kind
("DSA and Elgamal") and ELG-E keys size (2048).
    {info}
    * The generated keys are stored in $HOME/.gnupg or %HOME%\Application
Data\gnupg subdirectory.
    * Save the content in this subdirectory to a safe media. This contains your
private key used to sign all the OpenJPA release materials.
    {info} ||
    || 3 | Backup your cygwin home directory to another media ||
    || 4 | Add your public key to {{[https://svn.apache.org/repos/asf/openjpa/site/docs/KEYS]
}} and {{/www/www.apache.org/dist/openjpa/KEYS}}. See the commands describe
at the beginning of this KEYS file to perform this task. The gpg key-pair
is used to sign the published artifacts for the OpenJPA releases. ||
    || 5 | Following the instructions in [http://people.apache.org/~henkp/trust/]
 and ask someone in the OpenJPA project to sign your public key. ||
    || 6 | Submit your public key to a key server. E.g. [http://pgp.surfnet.nl:11371/]
 or [http://pgp.mit.edu/]
||
    
    h3. Update Maven settings for our servers
    
    || 1 | Create a settings.xml under .m2 (in your Document and Settings
folder in Windows) ||
    | | {code:xml|title=settings.xml|borderStyle=solid}
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
*$PATH_TO_PRIVATE_KEY* is the path to the private key generated for ssh.
E.g. /home/yourLocalUserId/.ssh/id_dsa.
{info} |

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-ExposeacopyofknownhoststoMaven"></a>

### Expose a copy of known hosts to Maven

<table>
<tr><th> 1 </td><td> From cygwin, ssh to people.apache.org, save the public key if
prompted, and exit </th></tr>
<tr><td> </td><td> cygwin will save the known hosts to your *\~/.ssh* folder, but the
script cannot access it there (from Windows) </td></tr>
<tr><th> 2 </td><td> From cygwin (not Windows) create another *.ssh* folder at (?) </th></tr>
<tr><th> 3 </td><td> Copy the *known_hosts* file to the new *.ssh* folder </th></tr>
</table>

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-Troubleshooting"></a>

## Troubleshooting

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-SpaceCharacterinBuildRootPath"></a>

### Space Character in Build Root Path

<table>
<tr><th> Description </td><td> If there are spaces in the path to the build root
subdirectory, the maven task uses to generate the revision number for the
org.apache.openjpa.revision.properties yields incorrect data. For example:
</tr>
<DIV class="code panel" style="border-style: solid;border-width: 1px;"><DIV class="codeHeader panelHeader" style="border-bottom-width: 1px;border-bottom-style: solid;"><B>org.apache.openjpa.revision.properties|borderStyle=solid</B></DIV><DIV class="codeContent panelContent">
    revision.number=Type 'svnversion --help' for usage.
    openjpa.version=1.0.1

<table>
<tr><th> Solution </td><td> Rename the path and remove all spaces. </th></tr>
</table>

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-MerginglocalrepositorytoremoterepositoryinCygwin/Windows"></a>

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

    find "c:/OpenJPA.1.0.1.Release/1.0.1" -name m2-repository -not -path "*openjpa-project*" \
        -exec mvn -f "c:/tmp/maven-stage-plugin/pom.xml" stage:copy \
        -Dsource=file://{} \
        -Dtarget=scp://allee8285@people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository \
        -Dversion=1.0.1 \;


<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-Cygwin/WindowsFilePath"></a>

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

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-"Toomanyunapprovedlicenses:""></a>

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
 ||
</table>

<a name="ReleasingOpenJPA1.0.xor1.1.x(OldSCPSteps)-Resources"></a>

## Resources

* Apache Apache [Release FAQ](http://www.apache.org/dev/release.html)
* [Signing Releases](http://apache.org/dev/release-signing.html)
* [Wendy's notes on Release Signing](http://wiki.wsmoak.net/cgi-bin/wiki.pl?ReleaseSigning)
* Apache [Mirroring Guidelines](http://apache.org/dev/mirrors.html)
* Struts [Release Instructions](http://cwiki.apache.org/WW/creating-and-signing-a-distribution.html)
 (upon which these instructions are based)
