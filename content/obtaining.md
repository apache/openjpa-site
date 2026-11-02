Title: Obtaining

<a name="Obtaining"></a>


OpenJPA official releases can be downloaded at the [Downloads](downloads.html)
 page.

Released binaries can also by accessed from Maven Central Repositories adding the
 following to the dependencies section on your pom.xml:


    <dependency>
        <groupId>org.apache.openjpa</groupId>
        <artifactId>openjpa-all</artifactId>
        <version>4.2.0</version>
    </dependency>
 
 

If you wish to use a STAGING version, you must point your pom.xml
to the repository at <https://repository.apache.org/content/groups/staging/>. 
An example pom.xml that will use the 4.2.1 release is as follows:


    <?xml version="1.0" encoding="UTF-8"?>
    <project>
        <modelVersion>4.0.0</modelVersion>
        <groupId>some-project</groupId>
        <artifactId>some-project</artifactId>
        <packaging>jar</packaging>
        <name>My Project</name>
        <version>1.0.0</version>
        <repositories>
    	<repository>
    	    <id>apache-staging</id>    	   
            <url>https://repository.apache.org/content/groups/staging/</url>
    	</repository>
        </repositories>
        <dependencies>
    	<dependency>
    	    <groupId>org.apache.openjpa</groupId>
    	    <artifactId>openjpa-all</artifactId>
    	    <version>4.2.1</version>
    	</dependency>
        </dependencies>
    </project>



Also, there is a snapshot repository set up for maven located at <https://repository.apache.org/content/repositories/snapshots/>
 where development snapshot jars will be stored. Maven projects can be
configured to depend on the openjpa snapshots by setting up their pom.xml
as follows:

----
> **Update Version**
>
>In the example below replace 4.1.1-SNAPSHOT with the version you wish to
use. Ex. 4.2.0
----

    <?xml version="1.0" encoding="UTF-8"?>
    <project>
        <modelVersion>4.0.0</modelVersion>
        <groupId>some-project</groupId>
        <artifactId>some-project</artifactId>
        <packaging>jar</packaging>
        <name>My Project</name>
        <version>1.0.0</version>
        <repositories>
    	<repository>
    	    <id>apache-snapshots</id>
    	    <url>https://repository.apache.org/content/repositories/snapshots/</url>
    	</repository>
        </repositories>
        <dependencies>
    	<dependency>
    	    <groupId>org.apache.openjpa</groupId>
    	    <artifactId>openjpa-all</artifactId>
    	    <version>4.2.1-SNAPSHOT</version>
    	</dependency>
        </dependencies>
    </project>

