Title: Apache Nexus Release Process 1.2.x-2.x


<a name="apache-nexus-release-process-(1.2.x-2.1.x)"></a>


# Release Steps for OpenJPA 1.2.x - 2.x

We're starting to move our builds over to using the Apache Nexus repository (repository.apache.org) for releasing SNAPSHOT and release artifacts.
More details on releasing artifacts and using Nexus can be found on the Maven website at - <http://maven.apache.org/developers/release/apache-release.html>
https://svn.apache.org/repos/infra/websites/production/openjpa/content/builds
  1. Environment setup for releasing artifacts (same for SNAPSHOTs and releases)
    1. Increase the default Java heap available to Maven (required for Java SE 6)
    
            export MAVEN_OPTS="-Xmx1024m -XX:MaxPermSize=512m"
        
    2. Use the latest Sun 1.6.0 JDK (1.5.0 for 1.2.x and 1.3.x)
    3. Use Maven 2.2.1 or later (2.2.1 is required for release signing fixes)
    4. Make sure the [Release Setup](http://openjpa.apache.org/release-setup.html) steps have been performed.
    5. To verify:

            [root@vega workspace]# mvn -v
            Apache Maven 2.2.1 (r801777; 2009-08-06 14:16:01-0500)
            Java version: 1.6.0_43
            Java home: /opt/java/sun/jdk6_43/jre
            Default locale: en_US, platform encoding: UTF-8
            OS name: "linux" version: "2.6.18-348.3.1.el5xen" arch: "amd64" Family: "unix"
            [root@vega workspace]#
        
  2. Prepare the source for release: 
    1. Cleanup JIRA so the Fix Version in issues resolved since the last release includes this release version correctly.  Also, transition any Resolved issues to the Closed state.
    2. Update the text files in a working copy of the openjpa-project subdir -
        1. Update the CHANGES.txt based on the Text release reports from JIRA.
            1. Choose the release from the "Versions" tab in the [releases page](https://issues.apache.org/jira/browse/OPENJPA/fixforversion/)
            2. Click "Release Notes" link in upper right.
        2. Update the RELEASE-NOTES.html based on the HTML release reports from JIRA.
        3. Review and update README.txt, CHANGES.txt, BUILDING.txt and NOTICE if needed.
        4. Change Copyright to correct years:
            * openjpa-project/src/doc/manual/manual.xml
            * openjpa-project/CHANGES.txt
            * openjpa-project/RELEASE.NOTES.html
        5. Commit any changes back to svn - 
        
                $ svn commit -m "Updating files for release."

    1. Stage any Roadmap or Release landing pages on the wiki.
    2. Verify the source has the required headers before trying to release.
      
            $ mvn apache-rat:check

    1. Perform a full build with tests
    
            $ mvn clean install -Papache-release,docbook-profile,test-derby,bval

    1. Run the JPA 1.0 TCK (for 1.x) and JPA 2.0 TCK (for 2.x) to verify the latest code passes.
    1. Perform a full build and deploy the SNAPSHOT artifacts
    
            $ mvn clean deploy -Papache-release,docbook-profile,test-derby,bval -DskipTests

         <div class="note">
If you run into the following exception during the build:

            [ERROR] BUILD ERROR
            [INFO] ------------------------------------------------------------------------
            [INFO] Error retrieving previous build number for artifact 'org.apache.openjpa:openjpa-parent:pom':
                      repository metadata for: 'snapshot org.apache.openjpa:openjpa-parent:2.2.2-SNAPSHOT' could not 
                      be retrieved from repository: apache.snapshots.https due to an error: 
                      Error transferring file: RSA premaster secret error
            Illegal key size or default parameters

        You may need to install the [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html).
        Simply extract and replace the jar files into $JAVE_HOME/jre/lib/security.
        </div>
        
    1. Inspect the files in your local target directories to ensure:
        * All jars and zips include:	LICENSE and NOTICE files
        * The NOTICE files cover all third-party included files (like XSD schemas)
        * The LICENSE files include any third-party licenses (like XSD schemas)
        * The openjpa and openjpa-all jars include the right packages.
        * The openjpa source and release distribution files have the right content.
        * All jars/zips/poms have .asc (PGP signature) and md5 files
    
  3. For new major releases (like 2.0.0 to 2.1.0)
    1. Create a sub-branch from which to make the release. Releasing from a branch will allow any cosmetic changes that need to be made for the release to be approved to be done without preventing other more disruptive advances in the trunk from potentially causing problems with the release. It also provides a future maintenance branch (like 2.0.x.)  A branch can be made by running:
    
            $ mvn release:branch -DbranchName=2.0.x -Dusername=svn.user -Dpassword=svn.password

  4. Checkout a clean copy of the trunk/branch to release using command line svn.
    1. Do not use Eclipse to do the checkout. The extra dot (.) files created by Eclipse throws off the rat:check processing and will get included in the source distribution.
     
            $ svn checkout https://svn.apache.org/repos/asf/openjpa/branches/2.0.x/ 2.0.1-rc1/

        <span class="note">Make sure you use https:// protocol because the following release:prepare step requires update to the svn repository.</span>
 
  5. \(Optional\) Do a dry run of the release:prepare step.
    1. The dry run will not commit any changes back to SVN and gives you the opportunity to verify that the release process will complete as expected.  You will be prompted for the following information :
        1. Release version - take the default - (default 2.0.1) 
        2. SCM release tag - *DO NOT TAKE THE DEFAULT* - (default openjpa-parent-2.0.1): : 2.0.1
        3. New development version - take the default - (default 2.0.2-SNAPSHOT) 
        4. _optional_ if you have not specified a GPG passphrase in settings.xml you will be prompted for it. 
        
                    $ mvn -Papache-release release:prepare -DdryRun=true
        
        <div class="note">
     If you cancel a release:prepare before it updates the pom.xml versions,
then use the *release:clean* goal to just remove the extra files that were
created. If that doesn't help, try running *mvn clean*.</div>

    2. Verify that the release process completed as expected
        1. The release plugin will create pom.xml.tag files which contain the changes that would have been committed to SVN. The only differences between pom.xml.tag and it's corresponding pom.xml file should be the version number.
        2. If other formatting changes have been made you should review the changes and then commit them -
        
                 $ svn commit -m "fixing formatting for release"

        3. Assuming the .tag files look OK you may proceed and do any other validation you feel necessary. The following list may be helpful 
            1. Check release.properties and make sure that the scm properties have the right version. Sometimes the scm location can be the previous version not the next version. *
            2. verify signatures [Verifying release signatures](#verifySig)

    3. Once any failures or required updates have been committed to svn, rollback the release prepare files -
    
            $ mvn -Papache-release release:rollback

  6. Prepare the release
    1. Run the "release:prepare" step for real this time.  You'll be prompted for the same version information and optionally your GPG passphrase again.
      
            $ mvn release:prepare -Papache-release,docbook-profile,test-derbymem,bval -DskipTests \
                  -DpreparationGoals="clean install" \
                  -Dusername=svn.user -Dpassword=svn.password

         <div class="note">
Different arguments and steps are required as there are problems with the maven-jar-plugin and maven-release-plugin when using the test-jar goal.  See <a href="http://jira.codehaus.org/browse/MJAR-68">http://jira.codehaus.org/browse/MJAR-68</a> and <a href = "http://jira.codehaus.org/browse/MRELEASE-285">,http://jira.codehaus.org/browse/MRELEASE-285</a>.

            $ mvn release:prepare -Papache-release,docbook-profile,test-derbymem,bval -DskipTests \
                  -DpreparationGoals="clean install" -Dusername=allee8285 -Dpassword=xxxxxxxx
              ... Build failed....
            $ mvn install -DskipTests
            $ mvn release:prepare -Papache-release,docbook-profile,test-derbymem,bval -DskipTests \
                  -DpreparationGoals="clean install" -Dusername=allee8285 -Dpassword=xxxxxxxx

        </div>

  7. Backup (zip or tar) your local release candidate directory in case you need to rollback the release after the next step is performed.

        cd ..
        tar -czf 2.0.1-rc1-preRelease.tar.gz 2.0.1-rc1/
        cd 2.0.1-rc1

  8. Perform the release
    1. This step will create a maven staging repository and site for use in testing and voting. You will be prompted for your repository.apache.org and people.apache.org password several times if you have not added server profiles to your settings.xml.	See [Release Setup](http://openjpa.apache.org/release-setup.html) for more information.
     
            $ mvn release:perform -Papache-release -Duser.name=<your-apache-uid>

    2. The maven-release-plugin is configured with goals "deploy site site-deploy" and will deploy the site files to a staging-site directory on people.apache.org.
    
  9. Verify the release artifacts
    1. Verify the HTML links in staging-site/index.html are correct
        1. Login to people.apache.org
        2. Edit public_html/openjpa/\[release\]/staging-site/index.html and updates the followings:

                <a href="downloads/">Downloads</a>
                  to
                <a href="apache-openjpa/downloads/">Downloads</a>
    
                <a href="docs/index.html">docs/index.html</a>
                  to
                <a href="apache-openjpa/docs/index.html">docs/index.html</a>

    2. Login to [Nexus](https://repository.apache.org/index.html)
    3. Verify the staged artifacts in the nexus repo
        1. Build Promotion --> Staging Repositories
        2. Select/check org.apache.openjpa-xxx
        3. In Browser tab, navigate through the artifact tree and make sure that all javadoc, sources, tests, jars, ... have .asc (GPG signature) and .md5 files. See [http://people.apache.org/~henkp/repo/faq.html](http://people.apache.org/~henkp/repo/faq.html) and <http://www.apache.org/dev/release-signing.html>.
    4. Close the nexus staging repo
        1. Select/check org.apache.openjpa-xxx and select Close.

  10. Put the release candidate up for a vote
    1. Create a VOTE email thread on dev@openjpa to record votes as replies, like -
                
                To: dev@
                Subject: [VOTE] Apache OpenJPA 2.0.1 Release Candidate
                I've created a 2.0.1 release candidate, with the following artifacts up for a vote:
                SVN source tag (rXXXXXX):
                https://svn.apache.org/repos/asf/openjpa/tags/2.0.1/
                        
                Maven staging repo:
                https://repository.apache.org/content/repositories/orgapacheopenjpa-XXX/
                
                Source release:
                https://repository.apache.org/content/repositories/orgapacheopenjpa-XXX/\
                      org/apache/openjpa/openjpa-parent/2.0.1/openjpa-parent-2.0.1-source-release.zip
                
                Javadoc staging site:
                http://people.apache.org/~dwoods/openjpa/2.0.1/staging-site/apidocs/
                
                PGP release keys (signed using D018E6B1):
                https://svn.apache.org/repos/asf/openjpa/KEYS
                
                
                Vote will be open for 72 hours.
                
                [ ] +1  approve
                [ ] +0  no opinion
                [ ] -1  disapprove (and reason why)

    2. Create a DISCUSS email thread on dev@ for any vote questions, like -
    
                To: dev@
                Subject: [DISCUSS] Apache OpenJPA 2.0.1 Release Candidate
                
                Discussion thread for vote on 2.0.1 release candidate, with SVN source tag
                (rXXXXXX).
                
                For more information on the release process, checkout -
                http://www.apache.org/dev/release.html
                http://incubator.apache.org/guides/releasemanagement.html
                
                Some of the things to check before voting are:
                - does "mvn apache-rat:check" pass on the source
                - can you build the contents of source-release.zip and svn tag
                - do all of the staged jars/zips contain the required LICENSE and NOTICE
                files
                - are all of the staged jars signed and the signature verifiable
                - is the signing key in the project's KEYS file and on a public server
                - does the release pass the TCK

    3. Perform a review of the release and cast your vote. See the following for more details on Apache releases -
        1. [http://www.apache.org/dev/release.html](http://www.apache.org/dev/release.html)
        1. [http://incubator.apache.org/guides/releasemanagement.html](http://incubator.apache.org/guides/releasemanagement.html)
    4. A -1 vote does not necessarily mean that the vote must be redone, however it is usually a good idea to rollback the release if a -1 vote is received. See - [Recovering from a vetoed release](#recoverFromVetoRelease)
    5. After the vote has been open for at least 72 hours, has at least three +1 PMC votes and no -1 votes, then post the results to the vote thread by -
        1. Reply to the initial email and prepend to the original subject -
 
                [RESULTS]
        
        2. Include a list of everyone who voted +1, 0 or -1.

  11. Finalizing a release
    1. Release the staged nexus artifacts -
        1. [https://repository.apache.org/index.html](https://repository.apache.org/index.html)
        2. Build Promotion --> Staging Repositories
        3. Select/check org.apache.openjpa-xxx and select Release.
        
    2. Copy documentation contents (RELEASE.NOTES, javadoc and manual) from the staged site over to the
    <http://openjpa.apache.org/builds>/${RELEASE} site. The content of this site is located on
    <https://svn.apache.org/repos/infra/websites/production/openjpa/content/builds>.
        1. Assume the following environment variable definitions (you need to adjust to your configuration):
        
                # Release designation
                export RELEASE=2.2.2
                # Location where the release candidate is built
                export RCDIR=/root/tc/WASX/workspace/${RELEASE}-rc2
                # OpenJPA svn user id
                export ojUser=allee8285
                # Temporary location where the "builds" contents are collected
                export RELBUILDS=/tmp/${RELEASE}.builds
                
        2. Prepare the "check out" environment for artifact collection
        
        		$ rm -rf ${RELBUILDS}
        		$ svn co https://svn.apache.org/repos/infra/websites/production/openjpa/content/builds ${RELBUILDS} --depth empty
        		
        		$ mkdir ${RELBUILDS}/${RELEASE}
        		$ mkdir ${RELBUILDS}/${RELEASE}/apache-openjpa
        
        3. Collect RELEASE.NOTES.html, manual style sheet and images,
        
        		$ cd ${RELBUILDS}/${RELEASE}
        		$ cp ${RCDIR}/openjpa-project/RELEASE-NOTES.html apache-openjpa
        		$ cp -r ${RCDIR}/openjpa-project/src/doc/manual/css apache-openjpa/docs
        		$ cp -r ${RCDIR}/openjpa-project/src/doc/manual/img apache-openjpa/docs
        
        4. Collect manual and javadoc
        
        		$ scp -r ${ojUser}@people.apache.org:~/public_html/openjpa/${RELEASE}/staging-site/apache-openjpa/docs apache-openjpa
        		$ scp -r ${ojUser}@people.apache.org:~/public_html/openjpa/${RELEASE}/staging-site/apidocs apidocs
        
        5. Commit content to svn repository.  (The commit will take a l-o-n-g time due to the many, many file updates...  May have to break it into several individual commits.)
        
        		$ cd ${RELBUILDS}
        		$ svn add ${RELEASE}
        		$ svn commit -m "Commit ${RELEASE} RELEASE-NOTES, javadoc and manual to http://openjpa.apache.org/builds"
        		
        6. Verify that /www/openjpa.apache.org/builds/${RELEASE}/docs/manual is populated correctly by comparing it to a previous release.

    3. Copy the distribution artifacts over to the distribution area.  This step is what will eventually populate the download mirrors.

        1. checkout the distribution directory

                $ svn co https://dist.apache.org/repos/dist/release/openjpa/ openjpa-dist
                $ cd openjpa-dist

        2. create the release folder

                $ mkdir ${RELEASE}
                $ cd ${RELEASE}
            
        3. update the assemblies in the distribution directory. For this, we'll just wget copies of the released assemblies with their signatures and hashes from the Apache repo:
        
                $ wget --no-check-certificate https://repository.apache.org/content/repositories/releases/\
                      org/apache/openjpa/apache-openjpa/${RELEASE}/apache-openjpa-${RELEASE}-source.zip
                $ wget --no-check-certificate https://repository.apache.org/content/repositories/releases/\
                      org/apache/openjpa/apache-openjpa/${RELEASE}/apache-openjpa-${RELEASE}-binary.zip

            Along with the corresponding .asc, .md5, and .sha1 files for both ZIP files above.

        4. commit

                $ cd ..
                $ svn add ${RELEASE}
                $ svn commit -m "Copying ${RELEASE} artifacts to the distribution directory"
        
        4. remove any previous maintenance versions, i.e. if you're publishing 2.0.1 you would remove 2.0.0.  Verify that the release being removed is in the distribution archives before removing.

                $ svn rm <any older release artifact (if present)>
                $ svn commit -m "Cleaning up older releases"

    4. Update the [JIRA Releases](https://issues.apache.org/jira/plugins/servlet/project-config/OPENJPA/versions) page to mark the version as "released", and set the date to the date that the release was approved. 
    (You may need to make a new release entry for the next release.)

    5. If the release contains the OpenBooks sample, check and update the "openjpa.version" property to the correct release in:

            openjpa-examples/openbooks/build.properties
            openjpa-examples/openbooks/run.properties
    
  12. Update wiki pages
    1. After the distribution and build files have been mirrored out to the external sites (takes about an hour):
        1. Update the [Documentation](http://openjpa.apache.org/documentation.html) wiki page:
         
   			* Update the new SNAPSHOT manual and javadoc links
   			* Add a newly created release entry 
   			* Update SNAPSHOT documentation source URL in <https://svn.apache.org/repos/asf/openjpa/site/trunk/content/.htaccess>. For example:

                    From
                      Redirect Permanent /builds/apache-openjpa-2.2.2-SNAPSHOT/docs   http://ci.apache.org/projects/openjpa/2.2.x
                    to        
                      Redirect Permanent /builds/apache-openjpa-2.2.3-SNAPSHOT/docs   http://ci.apache.org/projects/openjpa/2.2.x        

        2. If new branch is created, one will need to submit requests to infrastructure team to create or update the buildbot process for the new branch. See [BuildBot Doc Build](http://openjpa.apache.org/buildbot.tips.n.techniques.html) for doc build tips, see the [Jenkins wiki](http://wiki.apache.org/general/Jenkins?action=show&redirect=Hudson) for information on the Jenkins build process.  Also, reference the following JIRAs for learning further about the process.

            * Example [doc builds JIRA](https://issues.apache.org/jira/browse/INFRA-7738)
            * Example [Jenkins build JIRA](https://issues.apache.org/jira/browse/INFRA-7739) 

        3. Update the [Downloads](http://openjpa.apache.org/downloads.html) wiki page:
         
            * Add the newly ${RELEASE} binary and source links to the dynamic distributed servers
            * Add the newly ${RELEASE} RELEASE-NOTES.html link.
            * Update previous release links to the corresponding entry in //archive.apache.org/dist/openjpa/*  
        	
        4. Update the [Nightly Downloads](http://openjpa.apache.org/downloads-nightly.html) wiki page:
        
        	* Update the binary and source links in the "Pre-packaged binaries for SNAPSHOT releases" section 
        	to the new SNAPSHOT.  
    
    3. Push all the Wiki page changes to the openjpa.apache.org site using CMS "Publish Site" function.

    2. Make an announcement on the OpenJPA wiki. 
        1. Just do normal CMS update on the [OpenJPA main index page](http://openjpa.staging.apache.org/index.html).  Copy and paste from previous release announcements.

13. Announcing the release
    1. After the Maven mirrors have had time to update (24 hours to be on the safe side) and the wiki updates have 
    been exported and mirrored to the external website, then it's time to announce the release. Make an announcement about 
    the release on the dev@, user@ and [mailto:announce@apache.org] list as per 
    [the Apache Announcement Mailing Lists page](http://www.apache.org/foundation/mailinglists.html#foundation-announce).

        <div class="note">
Make sure you send the announcement to announce@apache.org from your
user@apache.org. This can be achieved using gmail by setting the "From"
field to user@apache.org instead of user@gmail.com when sending the
announcement.
</div>
    
<a name="recoverFromVetoRelease"></a>
 
# Recovering from a vetoed release
1. Reply to the initial vote email and prepend to the original subject -

        [CANCELED]

2. Rollback the version upgrades in trunk by either -
    1. Restore the 2.0.1-rc1.tar.gz and run
    
            $ mvn -Papache-release release:rollback

    2. Manually revert the versions in trunk to the prior version and commit

3. Delete the svn tag created by the release:perform step -

            $ svn del https://svn.apache.org/repos/asf/openjpa/tags/2.0.1 -m "rollback release attempt"
   
4. Drop the nexus staging repo
    1. [https://repository.apache.org/index.html](https://repository.apache.org/index.html)
    2. Enterprise --> Staging
    3. Staging tab --> Name column --> org.apache.openjpa
    4. Right click on the closed staging repo (org.apache.openjpa-XXX) and select Drop.
        
5. Remove the staged site

        $ ssh ${user.name}@people.apache.org 
        $ cd ~/public_html/openjpa
        $ rm -fr ${project.version}

6. Make the required updates that caused the vote to be canceled
7. Spin another release candidate!


<a name="verifySig"></a>

# Verifying release signatures

On unix platforms the following command can be executed -

    for file in `find . -type f -iname '*.asc'`
    do
        gpg --verify ${file} 
    done

    
You'll need to look at the output to ensure it contains only good
signatures -

    gpg: Good signature from ...
    gpg: Signature made ...
  
  
