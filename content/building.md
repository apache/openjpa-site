Title: Building


<a name="Building"></a>


<a name="Building-Contents"></a>

# Contents

* [Building OpenJPA](#Building-BuildingOpenJPA)

    * [Maven](#Building-Maven)
   
        * [Command Line Builds](#Building-CommandLineBuilds)
        * [Executing various Maven build tasks](#Building-ExecutingvariousMavenbuildtasks)
      
            * [Running just the "TestPersistence" test case](#Building-RunningjusttheTestPersistencetestcase)
            * [Running tests with Java 2 security enabled](#Building-RunningtestswithJava2securityenabled)
            * [Building and running only the examples included in the distribution](#Building-Buildingandrunningonlytheexamplesincludedinthedistribution)
            * [Building just the javadoc](#Building-Buildingjustthejavadoc)
            * [Building just the docbook documentation](#Building-Buildingjustthedocbookdocumentation)
            * [Building with JDK 1.4 module verification (only for versions of OpenJPA prior to svn revision 640685)](#Building-BuildingwithJDK1.4moduleverification(onlyforversionsofOpenJPApriortosvnrevision640685))
            
    * [Eclipse with Command-line Maven utilities](#Building-EclipsewithCommand-lineMavenutilities)
    * [Eclipse with M2Eclipse plugin](#Building-EclipsewithM2Eclipseplugin)
    * [Common 2.x Build Problems](#Building-Common2.xBuildProblems)
    
        * [Wrong Maven Level](#Building-WrongMavenLevel)
        * [Wrong Java Level](#Building-WrongJavaLevel)
        * [Missing License Headers](#Building-MissingLicenseHeaders)
        * [Checkstyle failed due to System.out/err.print](#Building-CheckstyleFailure)

<a name="Building-BuildingOpenJPA"></a>

# Building OpenJPA

See [Build and Runtime Dependencies](build-and-runtime-dependencies.html)
 for details on the required Java levels.

<a name="Building-Maven"></a>

## Maven

<a name="Building-CommandLineBuilds"></a>

### Command Line Builds

These instructions describe how to check out the current OpenJPA source
code (from the Subversion source code management repository) and build it
(using the Apache Maven 2 build tool). They are written for use from the
console, and are known to work on Linux, Mac OSX and Windows.

1. Ensure that you have Java installed and in your path by running: `java
-fullversion`
1. Set following maven options to avoid out of memory error:


    set MAVEN_OPTS="-XX:MaxPermSize=128m -Xms512m -Xmx1024m"

1. Install the build tool, Apache Maven 2.2.1 or later, from
<http://maven.apache.org/>. If it is installed correctly, typing *mvn -v*
from the console will result in text like `Apache Maven 2.2.1 (r801777;
2009-08-06 21:16:01+0200)`
1. Install Subversion v1.4.x or newer from <http://subversion.apache.org/>.
If it is installed correctly, typing the following command should output
help information: **svn help** or **svn --version**
1. Create a new directory you want to do your work in, then change to that
directory from the console.
1. Check out the sources by running: `svn co`
<https://svn.apache.org/repos/asf/openjpa/trunk> `openjpa-trunk`. It will
check out the sources to the openjpa-trunk directory. More information on
checking out the OpenJPA sources can be found on the [Source Code](source-code.html)
 page.
1. Change to the openjpa-trunk directory, which has already been created in
the previous step.
1. Build OpenJPA by running: `mvn package` or better `mvn install`. The
first time you run the build, many dependencies are automatically resolved
and downloaded. **It is common for dependency downloading to fail the first
time, which will fail the build.** If any of these dependency downloads
fail, just re-run the command. You may also add the following to your
`~/.m2/setting.xml` file (see <http://maven.apache.org/guides/mini/guide-mirror-settings.html>)

        <settings>
            <mirrors>
                <mirror>
                    <id>repo.mergere.com</id>
                    <url>http://repo.mergere.com/maven2</url>
                    <mirrorOf>central</mirrorOf>
                </mirror>
            </mirrors>
        </settings>

 If any tests fail, and you want to ignore the failures, instead run:

    mvn package -DfailIfNoTests=false

      or

    mvn package -DskipTests


An example session is as follows:


    $ cd /tmp/
    
    $ java -version
    
    java version "1.6.0"
    Java(TM) SE Runtime Environment (build 1.6.0-b105)
    Java HotSpot(TM) Client VM (build 1.6.0-b105, mixed mode, sharing)
    
    $ mvn -v
    
    Apache Maven 2.2.1 (r801777; 2009-08-06 21:16:01+0200)
    Java version: 1.6.0
    Java home: /alt/sun160/jre
    Default locale: en_US, platform encoding: UTF-8
    OS name: "linux" version: "2.6.18-1.2798.fc6" arch: "i386" Family: "unix"
    
    $ svn --version
    
    svn, version 1.4.3 (r23084)
       compiled Jan 18 2007, 07:47:40
    
    $ svn co https://svn.apache.org/repos/asf/openjpa/trunk/
    
    A  trunk/openjpa-lib
    A  trunk/openjpa-lib/src
    A  trunk/openjpa-lib/src/test
    A  trunk/openjpa-lib/src/test/java
    A  trunk/openjpa-lib/src/test/java/org
    A  trunk/openjpa-lib/src/test/java/org/apache
    A  trunk/openjpa-lib/src/test/java/org/apache/openjpa
    A  trunk/openjpa-lib/src/test/java/org/apache/openjpa/lib
    A  trunk/openjpa-lib/src/test/java/org/apache/openjpa/lib/test
    A  trunk/openjpa-lib/src/test/java/org/apache/openjpa/lib/test/AbstractTestCase.java
    
     ...
    
    A  trunk/openjpa-persistence/pom.xml
    Checked out revision 1065345.
    
    $ cd trunk/
    
    $ mvn compile
    
    [INFO] Scanning for projects...
    [INFO] Reactor build order: 
    [INFO]   OpenJPA Parent POM
    [INFO]   OpenJPA Utilities Library
    [INFO]   OpenJPA Kernel
    [INFO]   OpenJPA JDBC
    [INFO]   OpenJPA Persistence
    [INFO]   OpenJPA Persistence JDBC
    [INFO]   OpenJPA Persistence Locking Tests
    [INFO]   OpenJPA XML Store
    [INFO]   OpenJPA Slice
    [INFO]   OpenJPA JEST
    [INFO]   OpenJPA Aggregate Jar
    [INFO]   OpenJPA Aggregate Jar with Dependencies
    [INFO]   OpenJPA Project Docs and Assemblies
    [INFO]   OpenJPA Examples
    [INFO]   OpenJPA Examples - Simple
    [INFO]   OpenJPA Examples - image-gallery
    [INFO]   OpenJPA Examples - OpenBooks
    [INFO]   OpenJPA Integration Tests
    [INFO]   OpenJPA Integration Tests - Daytrader
    [INFO]   OpenJPA Integration Tests - Examples
    [INFO]   OpenJPA Integration Tests - SLF4JLogFactory
    [INFO]   OpenJPA Integration Tests - JPA TCK
    [INFO]   OpenJPA Integration Tests - Bean Validation
    [INFO]   OpenJPA Integration Tests - JMX Platform MBeans
    [INFO] ------------------------------------------------------------------------
    [INFO] Building OpenJPA Parent POM
    [INFO]    task-segment: [compile]
    [INFO] ------------------------------------------------------------------------
    
     ...
    
    [INFO]
    [INFO] ------------------------------------------------------------------------
    [INFO] Reactor Summary:
    [INFO] ------------------------------------------------------------------------
    [INFO] OpenJPA Parent POM .................................... SUCCESS [1:23.143s]
    [INFO] OpenJPA Utilities Library ............................. SUCCESS [13.749s]
    [INFO] OpenJPA Kernel ........................................ SUCCESS [19.251s]
    [INFO] OpenJPA JDBC .......................................... SUCCESS [14.351s]
    [INFO] OpenJPA Persistence ................................... SUCCESS [10.254s]
    [INFO] OpenJPA Persistence JDBC .............................. SUCCESS [46.774s]
    [INFO] OpenJPA Persistence Locking Tests ..................... SUCCESS [15.183s]
    [INFO] OpenJPA XML Store ..................................... SUCCESS [11.788s]
    [INFO] OpenJPA Slice ......................................... SUCCESS [4.437s]
    [INFO] OpenJPA JEST .......................................... SUCCESS [4.854s]
    [INFO] OpenJPA Aggregate Jar ................................. SUCCESS [10.729s]
    [INFO] OpenJPA Aggregate Jar with Dependencies ............... SUCCESS [6.761s]
    [INFO] OpenJPA Project Docs and Assemblies ................... SUCCESS [1:41.937s]
    [INFO] OpenJPA Examples ...................................... SUCCESS [0.663s]
    [INFO] OpenJPA Examples - Simple ............................. SUCCESS [1.475s]
    [INFO] OpenJPA Examples - image-gallery ...................... SUCCESS [3.920s]
    [INFO] OpenJPA Examples - OpenBooks .......................... SUCCESS [12.961s]
    [INFO] OpenJPA Integration Tests ............................. SUCCESS [0.381s]
    [INFO] OpenJPA Integration Tests - Daytrader ................. SUCCESS [7.565s]
    [INFO] OpenJPA Integration Tests - Examples .................. SUCCESS [0.269s]
    [INFO] OpenJPA Integration Tests - SLF4JLogFactory ........... SUCCESS [1.977s]
    [INFO] OpenJPA Integration Tests - JPA TCK ................... SUCCESS [0.248s]
    [INFO] OpenJPA Integration Tests - Bean Validation ........... SUCCESS [3.213s]
    [INFO] OpenJPA Integration Tests - JMX Platform MBeans ....... SUCCESS [7.729s]
    [INFO] ------------------------------------------------------------------------
    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESSFUL
    [INFO] ------------------------------------------------------------------------
    [INFO] Total time: 6 minutes 26 seconds
    [INFO] Finished at: Sun Jan 30 19:43:50 CET 2011
    [INFO] Final Memory: 92M/158M
    [INFO] ------------------------------------------------------------------------
    
    
    $ mvn package -DskipTests
    
    [INFO] Scanning for projects...
    
    ...
    
    [INFO] Building zip:/tmp/trunk/openjpa-project/target/site/downloads/apache-openjpa-2.2.0-SNAPSHOT-binary.zip
    
    ... 
    
    $ ls -lh openjpa-project/target/site/downloads/
    
    total 40M
    -rw-r--r-- 1 milosz milosz 15M Jan 30 19:41 apache-openjpa-2.2.0-SNAPSHOT-binary.zip
    -rw-r--r-- 1 milosz milosz 25M Jan 30 19:43 apache-openjpa-2.2.0-SNAPSHOT-source.zip
    

<a name="Building-ExecutingvariousMavenbuildtasks"></a>

### Executing various Maven build tasks

<a name="Building-RunningjusttheTestPersistencetestcase"></a>

##### Running just the "TestPersistence" test case


    mvn test -Dtest=TestPersistence


<a name="Building-RunningtestswithJava2securityenabled"></a>

##### Running tests with Java 2 security enabled


    mvn test -Penable-security


<a name="Building-Buildingandrunningonlytheexamplesincludedinthedistribution"></a>

##### Building and running only the examples included in the distribution


    mvn -DskipTests -Pexamples-profile integration-test


<a name="Building-Buildingjustthejavadoc"></a>

##### Building just the javadoc

First install the jars:


    mvn install -DskipTests


Then build the javadoc:


    mvn package -DskipTests -Pjavadoc-profile


The javadoc will be output to *target/site/apidocs/index.html*.

<a name="Building-Buildingjustthedocbookdocumentation"></a>

##### Building just the docbook documentation


    set MAVEN_OPTS=-Xmx512m
    mvn -f openjpa-project/pom.xml process-resources -Pdocbook-profile


The manual HTML will be output to `openjpa-project/target/manual/manual.html`.

<a name="Building-BuildingwithJDK1.4moduleverification(onlyforversionsofOpenJPApriortosvnrevision640685)"></a>

##### Building with JDK 1.4 module verification (only for versions of OpenJPA prior to svn revision 640685)


    mvn compile -Djava14.jar=C:\Program Files\Java\j2re1.4.2_07\lib\rt.jar compile


Specifying the "java14.jar" system property will cause the
JDK-1.4-dependent modules to be compiled with the value as the
bootclasspath to the compiler. This can be useful to ensure that
modifications and additions do not violate the JDK version restriction of
the module. Since the runtime jar location is platform, version, and
installation dependent, the exact location of the runtime jar will vary,
which is why it needs to be manually specified.

<a name="Building-EclipsewithCommand-lineMavenutilities"></a>

## Eclipse with Command-line Maven utilities

1. Checkout the source as described above
1. Build the source using Maven as described above
1. Create the Eclipse Metadata -
     
        mvn eclipse:eclipse
    1. If this is the first project in your workspace to use maven artifacts you need to create a classpath variable named M2_REPO which contains the full path to your local repository. The eclipse plugin can do this for you with the following command
    
            mvn eclipse:configure-workspace -Declipse.workspace=${path to your workspace} 

1. Start Eclipse (3.2 - 3.4 SR2 are known to work) and create a new
workspace
1. Import the OpenJPA projects, by:

    * Select File --> Import... --> General - Existing Projects into Workspace --> Next
    * Select root directory = <svn checkout location above>
    * Deselect the openjpa-examples project
    * Press Finish
    
1. A few fixups will be required to remove the errors that exist in the
imported projects...

    * openjpa-kernel -> Properties -> Java Build Path -> Source -> Add Folders
    
        * add target/generated-sources/javacc
        
    * openjpa-jdbc -> Properties -> Java Build Path -> Libraries -> JRE System Library -> Edit
    
        * change this to a Java 6 JRE to remove these errors (see below if you can not use Java SE 6)
        
    * openjpa-persistence -> Properties -> Java Build Path -> Libraries -> JRE System Library -> Edit
    
        * change this to a Java 6 JRE to remove these errors (see below if you
can not use Java SE 6)

    * openjpa-persistence-jdbc -> Properties -> Java Build Path -> Libraries
-> JRE System Library -> Edit

        * change this to a Java 6 JRE to remove these errors (see below if you
can not use Java SE 6)

    * openjpa-examples.  Open up src/main/java and select ReverseMapping
folder.  Right mouse click.

        * Select Build Path -> Exclude
        
1. For each imported project, you'll need to edit the build properties to
remove an incorrect dependency:

    * Project --> Properties --> Java Build Path --> Source
    * Remove openjpa-project from the list of source folders

For Java SE 5 users building from the 2.0.x branch, you will need to
exclude some Java SE 6 specific classes by performing the following steps
for the source:

1. Open the Properties for openjpa-persistence
1. Select Java Build Path --> Source
1. Edit the openjpa-persistence/src/main/java --> Excluded setting to
include the following:

        org/apache/openjpa/persistence/meta/AnnotationProcessor6.java
        org/apache/openjpa/persistence/meta/CompileTimeLogger.java
        org/apache/openjpa/persistence/meta/SourceAnnotationHandler.java


<a name="Building-EclipsewithM2Eclipseplugin"></a>

## Eclipse with M2Eclipse plugin

1. Checkout the source as described above
1. Build the source using Maven as described above
1. Start Eclipse (3.5 Galileo is recommended) and create a new workspace
1. Good references for this M2Eclipse plugin (need to install the plugin
into your Eclipse environment)

    * <http://m2eclipse.codehaus.org/>
    * <http://docs.codehaus.org/display/M2ECLIPSE/Home>
    * <http://www.theserverside.com/tt/articles/article.tss?l=Introductiontom2eclipse>
    
1. Import the OpenJPA projects, by:

    * Select File --> Import... --> General -> Maven Projects --> Next
    * Select root directory = <svn checkout location above>
    * All of the pom.xml files should be pre-selected for the svn checkout
location
    * You can affect the naming convention used for the generated Eclipse projects (one for each Maven module).  Click on Advanced and fill in the Name Template field.  I prefer "TRUNK-\[artifactId\](artifactid\.html)
" since it helps with workspace organization, but it's your choice.
    * Press Finish
    * **Note:**  You may get a popup internal error at the end of this Import
processing.  Not sure what the problem is, but it doesn't seem to affect
the usage.

1. A few fixups will be required to remove the errors that exist in the
imported projects...

    * openjpa-kernel -> Properties -> Java Build Path -> Source -> Add Folders
        * add target/generated-sources/javacc
    * openjpa-jdbc -> Properties -> Java Build Path -> Libraries -> JRE System
Library -> Edit
        * change this to a Java 6 JRE to remove these errors (see below if you
can not use Java SE 6)
    * openjpa-persistence -> Properties -> Java Build Path -> Libraries -> JRE
System Library -> Edit
        * change this to a Java 6 JRE to remove these errors (see below if you
can not use Java SE 6)
    * openjpa-persistence-jdbc -> Properties -> Java Build Path -> Libraries
-> JRE System Library -> Edit
        * change this to a Java 6 JRE to remove these errors (see below if you
can not use Java SE 6)
    * openjpa-examples.  Open up src/main/java and select ReverseMapping
folder.  Right mouse click.
        * Select Build Path -> Exclude

For Java SE 5 users building from the 2.0.x branch, you will need to
exclude some Java SE 6 specific classes by performing the following steps
for the source:

1. Open the Properties for BR20-openjpa-persistence (or whatever your naming
convention is)
1. Select Java Build Path --> Source
1. Edit the openjpa-persistence/src/main/java --> Excluded setting to
include the following:

        org/apache/openjpa/persistence/meta/AnnotationProcessor6.java
        org/apache/openjpa/persistence/meta/CompileTimeLogger.java
        org/apache/openjpa/persistence/meta/SourceAnnotationHandler.java

<a name="Building-Common2.xBuildProblems"></a>

## Common 2.x Build Problems

<a name="Building-CheckstyleFailure"></a>

### Checkstyle failure due to System.out.print or System.err.print
Changes were added to build so that the build will fail if there are any calls to System.out/err.print(ln). 
This was done to force people to use the proper logging facilities. If there is an honest reason that
you need to have System.out/err.print in your code, you can use the following comments to turn the 
checkstyle scanner off, then back on again.

    // START - ALLOW PRINT STATEMENTS
    System.err.println("This needs to be here!");
    // STOP - ALLOW PRINT STATEMENTS

<a name="Building-WrongMavenLevel"></a>

### Wrong Maven Level

Example Maven output -

    [INFO] [enforcer:enforce {execution: default}]
    [WARNING] Rule 0: org.apache.maven.plugins.enforcer.RequireMavenVersion failed with message:
    Detected Maven Version: 2.0.10 is not in the allowed range [2.2.1,).
    [INFO] ------------------------------------------------------------------------
    [ERROR] BUILD ERROR
    [INFO] ------------------------------------------------------------------------
    [INFO] Some Enforcer rules have failed. Look above for specific messages explaining why the rule failed.

Solution - Upgrade to Maven 2.2.1 or later

<a name="Building-WrongJavaLevel"></a>

### Wrong Java Level
    
Example Maven output -

    [INFO] [enforcer:enforce {execution: default}]
    [WARNING] Rule 1: org.apache.maven.plugins.enforcer.RequireJavaVersion failed with message:
    Detected JDK Version: 1.5.0-19 is not in the allowed range [1.6,).
    [INFO] ------------------------------------------------------------------------
    [ERROR] BUILD ERROR
    [INFO] ------------------------------------------------------------------------
    [INFO] Some Enforcer rules have failed. Look above for specific messages explaining why the rule failed.

Solution - Upgrade to latest Sun JDK 1.6.0 or IBM 6 SDK

Note - OpenJDK and Java SE 7 are not supported at this time.

<a name="Building-MissingLicenseHeaders"></a>

### Missing License Headers

Example Maven output -

    . . .
    [INFO] ------------------------------------------------------------------------
    [INFO] Building OpenJPA Parent POM
    [INFO]    task-segment: [clean, install]
    [INFO] ------------------------------------------------------------------------
    . . .
    [INFO] [enforcer:enforce {execution: default}]
    [INFO] [source:test-jar {execution: attach-sources}]
    [INFO] [ianal:verify-legal-files {execution: default}]
    [INFO] [apache-rat:check {execution: default}]
    [INFO] Exclude: **/javax.persistence.spi.PersistenceProvider
    [INFO] Exclude: **/javax.annotation.processing.Processor
    [INFO] Exclude: **/*.rsrc
    [INFO] Exclude: **/org.apache.openjpa.revision.properties
    [INFO] Exclude: scripts/*.list
    [INFO] Exclude: scripts/*.options
    [INFO] Exclude: scripts/*.dict
    [INFO] Exclude: **/.*/**
    [INFO] Exclude: **/target/**/*
    [INFO] Exclude: **/dependency-reduced-pom.xml
    [INFO] Exclude: **/*.log
    [INFO] Exclude: **/maven-eclipse.xml
    [INFO] Exclude: **/rat.txt
    [INFO] Exclude: **/internal-repository/**
    [INFO] ------------------------------------------------------------------------
    [ERROR] BUILD FAILURE
    [INFO] ------------------------------------------------------------------------
    [INFO] Too many unapproved licenses: 1
    [INFO] ------------------------------------------------------------------------

For the module that failed to build (which in the case above is the root
pom.xml) open the target/rat.txt file and search for any "????"
occurrences, like -

    . . .
    *****************************************************
      Files with Apache License headers will be marked AL
      Binary files (which do not require AL headers) will be marked B
      Compressed archives will be marked A
      Notices, licenses etc will be marked N
      N	LICENSE.txt
      N	NOTICE.txt
      AL	openjpa/pom.xml
      AL	openjpa/src/main/appended-resources/META-INF/LICENSE.vm
      AL	openjpa/src/main/appended-resources/META-INF/NOTICE.vm
     !????? OPENJPA-1621.patch
    . . .

Solution - either add the missing Apache License v2.0 license header, remove the file
from your local working directory (if it is a temporary file that should
not be added to svn), or ask on the dev@openjpa list if the file can be
added to the exclude list for the apache-rat checks.