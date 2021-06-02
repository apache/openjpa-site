Title: Obtaining

<a name="Obtaining"></a>


OpenJPA official releases can be downloaded at the [Downloads](downloads.html)
 page.

Released binaries can also by accessed from Maven pom.xml files by pointing
them to the repository at
<http://people.apache.org/repo/m2-incubating-repository>. An example pom.xml
that will use the 0.9.0-incubating release is as follows:


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
    	    <id>central</id>
    	    <url>http://www.ibiblio.org/maven2</url>
    	</repository>
    	<repository>
    	    <id>apache-snapshots</id>    	   
            <url>http://people.apache.org/repo/m2-incubating-repository</url>
    	</repository>
        </repositories>
        <dependencies>
    	<dependency>
    	    <groupId>org.apache.openjpa</groupId>
    	    <artifactId>openjpa-all</artifactId>
    	    <version>0.9.6-incubating</version>
    	</dependency>
        </dependencies>
    </project>



Also, there is a snapshot repository set up for maven located at <http://people.apache.org/repo/m2-snapshot-repository/org/apache/openjpa/>
 where development snapshot jars will be stored. Maven projects can be
configured to depend on the openjpa snapshots by setting up their pom.xml
as follows:

----
> **Update Version**
>
>In the example below replace 0.9.8-SNAPSHOT with the version you wish to
use. Ex. 1.2.0, or 1.3.0-SNAPSHOT
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
    	    <id>central</id>
    	    <url>http://www.ibiblio.org/maven2</url>
    	</repository>
    	<repository>
    	    <id>apache-snapshots</id>
    	    <url>http://people.apache.org/repo/m2-snapshot-repository</url>
    	</repository>
        </repositories>
        <dependencies>
    	<dependency>
    	    <groupId>org.apache.openjpa</groupId>
    	    <artifactId>openjpa-all</artifactId>
    	    <version>0.9.8-incubating-SNAPSHOT</version>
    	</dependency>
        </dependencies>
    </project>

