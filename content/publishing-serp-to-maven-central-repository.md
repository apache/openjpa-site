Title: Publishing Serp to Maven Central Repository


<a name="PublishingSerptoMavenCentralRepository-PublishingSerptoMavenCentralRepository"></a>


# Publishing Serp to Maven Central Repository

<a name="PublishingSerptoMavenCentralRepository-SerpProject"></a>

## Serp Project
Serp is used by OpenJPA for the bytecode enhancement processing.  It is
maintained as a [SourceForge project](http://sourceforge.net/projects/serp)
.  Serp has been a very solid third-party dependent software project. 
OpenJPA has had a dependency on Serp v1.13.1 for a long time.  Recently, a
problem was discovered [JIRA OPENJPA-2240](http://issues.apache.org/jira/browse/OPENJPA-2240) which
required an update to Serp.  Eventually, it was determined that this
problem was resolved in the 1.14.1 version of Serp.  Unfortunately, the
last version of Serp that was published to Maven Central was version
1.13.1.  This page discusses how to get an updated Serp release into the
Maven Central repository.

SourceForge Serp:  <https://sourceforge.net/projects/serp/> <br/>
Serp homepage:	<http://serp.sourceforge.net> <br/>
Serp sourcecode:  <http://serp.cvs.sourceforge.net/serp> <br/>


<a name="PublishingSerptoMavenCentralRepository-MavenInstructions"></a>

## Maven Instructions
The easiest way to get the updated artifacts for Serp 1.14.1 into Maven
Central was to follow the instructions on <a href="https://docs.sonatype.org/display/Repository/Uploading+3rd-party+Artifacts+to+The+Central+Repository">this page</a>. 
You will need a GPG utility and signature (instructions on that page). 
You will also need a login for Sonatype's Nexus server (instructions also
on that page).

<table class="note"><tr>
  <td valign="top"> <IMG src="images/warning.gif" width="16" height="16" border="0">
  <td> <B>Update to the Sonatype documentation...</B><BR>The above referenced wiki page 
is no longer in service.  I talked with Joel Orlina (jorlina@sonatype.com) and he pointed 
me at this <a href="http://central.sonatype.org/pages/producers.html">updated documentation</a>.  
We should attempt to follow these updated, simpler instructions for publishing Serp
to Maven Central.  But, for historical reference, Sonatype also has the 
<a href="https://web.archive.org/web/20140903200507/https://docs.sonatype.org/display/Repository/Uploading+3rd-party+Artifacts+to+The+Central+Repository">original wiki page in archive</a>.

</tr></table>

Since this exercise shouldn't be a common occurrence, I just went the
manual route and signed each of the artifacts that were built into my local
repository:

    > gpg -ab serp-1.14.1-javadoc.jar
    > gpg -ab serp-1.14.1.jar
    > gpg -ab serp-1.14.1-sources.jar
    > gpg -ab serp-1.14.1.pom


And, then I created a bundle:

    > jar -cvf serp-1.14.1-bundle.jar serp-*


The bundle contained:

    Archive:  serp-1.14.1-bundle.jar
      Length     Date   Time    Name
     --------    ----   ----    ----
    	0  09-04-12 15:23   META-INF/
           62  09-04-12 15:23   META-INF/MANIFEST.MF
       962397  09-04-12 15:21   serp-1.14.1-javadoc.jar
          499  09-04-12 15:22   serp-1.14.1-javadoc.jar.asc
       140576  09-04-12 15:21   serp-1.14.1-sources.jar
          499  09-04-12 15:21   serp-1.14.1-sources.jar.asc
       206638  09-04-12 15:21   serp-1.14.1.jar
          499  09-04-12 15:22   serp-1.14.1.jar.asc
         5508  09-04-12 15:21   serp-1.14.1.pom
          499  09-04-12 15:23   serp-1.14.1.pom.asc
     --------		    -------
      1317177		    10 files


This bundle is what I uploaded to the Sonatype Staging repository as
outlined on that [original wiki page](https://web.archive.org/web/20140903200507/https://docs.sonatype.org/display/Repository/Uploading+3rd-party+Artifacts+to+The+Central+Repository)
.

<table class="note"><tr>
  <td valign="top"> <IMG src="images/warning.gif" width="16" height="16" border="0">
  <td> <B>Not documented..</B><BR>One process point that was not documented on that
<a href="https://web.archive.org/web/20140903200507/https://docs.sonatype.org/display/Repository/Uploading+3rd-party+Artifacts+to+The+Central+Repository">original wiki page</a>
was the need for a JIRA to be created against the OSSRH project (Open
Source Project Repository Hosting).  This JIRA should include the Central
Repository staging URL that is provided after you upload the bundle. 
Here's an <a href="https://issues.sonatype.org/browse/OSSRH-4247">example JIRA</a>
 that worked for me.  If all else fails, contact Joel Orlina,
jorlina@sonatype.com.
</tr></table>

<a name="PublishingSerptoMavenCentralRepository-SerpCodeUpdates"></a>

## Serp Code Updates
In order to create the -javadoc and -sources jar files, I had to make a
couple of minor updates to the existing pom file for serp 1.14.1.  I
committed these changes to HEAD (1.14.2 snapshot) for future reference:

        <plugin>
    	  <artifactId>maven-source-plugin</artifactId>
    	  <executions>
    	    <execution>
    		<id>attach-sources</id>
    		<goals>
    		    <goal>jar</goal>
    		</goals>
    	    </execution>
    	  </executions>
        </plugin>
        
        <plugin>
    	  <artifactId>maven-javadoc-plugin</artifactId>
    	  <executions>
    	    <execution>
    		<id>attach-javadoc</id>
    		<goals>
    	      <goal>jar</goal>
    		</goals>
    	    </execution>
    	  </executions>
        </plugin>


If we continue to require changes to Serp, we may want to do more extensive
changes in the maven processing to make it easier to deploy the artifacts. 
Several of the deployment locations in the pom.xml no longer exist.  I made
a couple of updates, but the permissions don't show up right, so the
deployment step is still manual.

Another idea would be to consume Serp into OpenJPA as an Apache
sub-project...	That might be the best long-term solution.  But, I will
leave that for another day.
