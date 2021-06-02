Title: Build and Runtime Dependencies


<a name="OpenJPABuildandRuntimeDependencies"></a>


<a name="BuildandRuntimeDependencies-Javaversions"></a>

## Java versions

* OpenJPA trunk (i.e. OpenJPA 3.1.x currently) require JDK 1.8 or later.
* OpenJPA 2.1.x..2.4.x branches require JDK 1.6 or later.
* OpenJPA 2.0.x branch requires JDK 1.6 or 1.5. Note that some functionality that requires JDK 1.6 will not be available if you choose to build with JDK 1.5.
* Building javadoc from 2.0.x branch or newer requires JDK 1.6.
* OpenJPA 1.3.x, 1.2.x and 1.1.x branches require JDK 1.5.
* OpenJPA 1.0.x branch requires JDK 1.5 or 1.4.


<a name="BuildandRuntimeDependencies-Mavenversions"></a>

## Maven versions
* 2.4.x and 3.x branches require Maven 3.3 or later
* 2.2.x, 2.2.1.x, 2.1.x and 2.0.x branches require Maven 2.2.1.
* 1.3.x, 1.2.x, 1.1.x and 1.0.x branches require Maven 2.0.9.


<a name="BuildandRuntimeDependencies-RuntimeDependencies"></a>

## Runtime Dependencies

The binary release download of OpenJPA
_apache-openjpa-&lt;version&gt;-binary.zip_ includes all of the code needed to
run in a stand-alone Java SE JVM or within a Java EE application server.

<a name="BuildandRuntimeDependencies-OpenJPA1.0.x-1.2.xReleases"></a>

### OpenJPA 1.0.x - 1.2.x Releases

The binary download includes the following required OpenJPA core artifact:

* openjpa-&lt;version&gt;.jar

and the following required runtime dependencies under the lib/ directory:

* commons-collections-3.2.jar
* commons-lang-2.1.jar
* commons-pool-1.3.jar
* serp-1.13.1.jar

The following artifacts under lib/ are only required for Java SE
environments, as a Java EE application server should provide an
implementation:

* geronimo-jpa_3.0_spec-1.0.jar
* geronimo-jta_1.1_spec-1.1.jar

The following artifact under lib/ is optional, as you should include the
JDBC driver artifacts required by your database provider and [supported](http://openjpa.apache.org/builds/1.2.2/apache-openjpa-1.2.2/docs/manual/supported_databases.html#d0e32625)
 by OpenJPA:

* derby-10.2.2.0.jar


<a name="BuildandRuntimeDependencies-OpenJPA1.3.0SNAPSHOTBranch"></a>

### OpenJPA 1.3.0 SNAPSHOT Branch

The binary download includes the following required OpenJPA core artifact:

* openjpa-&lt;version&gt;.jar

and the following required runtime dependencies under the lib/ directory:

* commons-collections-3.2.1.jar
* commons-lang-2.1.jar
* commons-pool-1.5.3.jar
* serp-1.13.1.jar

The following artifacts under lib/ are only required for Java SE
environments, as a Java EE application server should provide an
implementation:

* geronimo-jms_1.1_spec-1.1.1.jar
* geronimo-jpa_1.0_spec-1.1.2.jar
* geronimo-jta_1.1_spec-1.1.1.jar

The following artifact under lib/ is optional, as you should include the
JDBC driver artifacts required by your database provider and [supported](http://openjpa.apache.org/builds/1.2.2/apache-openjpa-1.2.2/docs/manual/supported_databases.html#d0e32625)
 by OpenJPA:

* derby-10.2.2.0.jar

The binary download also contains an artifact which includes the OpenJPA
core code plus all of the runtime dependencies for Java SE environments:

* openjpa-all-&lt;version&gt;.jar

which in turn includes classes from the following packages:

* commons-collections-3.2.1.jar
* commons-lang-2.1.jar
* commons-logging-1.0.4.jar
* commons-pool-1.5.3.jar
* geronimo-jms_1.1_spec-1.1.1.jar
* geronimo-jpa_1.0_spec-1.1.2.jar
* geronimo-jta_1.1_spec-1.1.1.jar
* serp-1.13.1.jar


<a name="BuildandRuntimeDependencies-OpenJPA2.0.xReleases"></a>

### OpenJPA 2.0.x Releases

The binary download includes the following required OpenJPA core artifact:

* openjpa-&lt;version&gt;.jar

and the following required runtime dependencies under the lib/ directory:

* commons-collections-3.2.1.jar
* commons-lang-2.1.jar
* commons-pool-1.5.3.jar
* serp-1.13.1.jar

The following artifacts under lib/ are only required for Java SE
environments, as a Java EE application server should provide an
implementation:

* geronimo-jms_1.1_spec-1.1.1.jar
* geronimo-jpa_2.0_spec-1.0.jar
* geronimo-jta_1.1_spec-1.1.1.jar

The following artifact under lib/ is optional, as you should include the
JDBC driver artifacts required by your database provider and [supported](http://openjpa.apache.org/builds/2.0.1/apache-openjpa-2.0.1/docs/manual/dbsupport.html#d0e36152)
 by OpenJPA:

* derby-10.5.3.0_1.jar

The binary download also contains an artifact which includes the OpenJPA
core code plus all of the runtime dependencies for Java SE environments:

* openjpa-all-&lt;version&gt;.jar

which in turn includes classes from the following packages:

* commons-collections-3.2.1.jar
* commons-lang-2.1.jar
* commons-logging-1.0.4.jar
* commons-pool-1.5.3.jar
* geronimo-jms_1.1_spec-1.1.1.jar
* geronimo-jpa_2.0_spec-1.0.jar
* geronimo-jta_1.1_spec-1.1.1.jar
* serp-1.13.1.jar


<a name="BuildandRuntimeDependencies-OpenJPA2.1.xReleasesandOpenJPA2.2.0SNAPSHOTBranch"></a>

### OpenJPA 2.1.x Releases and OpenJPA 2.2.0 SNAPSHOT Branch

The binary download includes the following required OpenJPA core artifact:

* openjpa-&lt;version&gt;.jar

and the following required runtime dependencies under the lib/ directory:

* commons-collections-3.2.1.jar
* commons-lang-2.4.jar
* commons-pool-1.5.4.jar
* serp-1.13.1.jar

The following artifacts under lib/ are only required for Java SE
environments, as a Java EE application server should provide an
implementation:

* geronimo-jms_1.1_spec-1.1.1.jar
* geronimo-jpa_2.0_spec-1.1.jar
* geronimo-jta_1.1_spec-1.1.1.jar

The following artifact under lib/ is optional, as you should include the
JDBC driver artifacts required by your database provider and [supported](http://openjpa.apache.org/builds/2.1.1/apache-openjpa/docs/dbsupport.html)
 by OpenJPA:

* derby-10.5.3.0_1.jar

The following artifacts under lib/ are optional and can be used for bean
validation:

* commons-beanutils-1.8.3.jar
* org.apache.bval.bundle-0.2-incubating.jar

The binary download also contains an artifact which includes the OpenJPA
core code plus all of the runtime dependencies for Java SE environments:

* openjpa-all-&lt;version&gt;.jar

which in turn includes classes from the following packages:

* commons-beanutils-1.8.3.jar
* commons-collections-3.2.1.jar
* commons-lang-2.4.jar
* commons-logging-1.0.4.jar
* commons-pool-1.5.4.jar
* geronimo-jms_1.1_spec-1.1.1.jar
* geronimo-jpa_2.0_spec-1.1.jar
* geronimo-jta_1.1_spec-1.1.1.jar
* org.apache.bval.bundle-0.2-incubating.jar
* serp-1.13.1.jar


  
  
