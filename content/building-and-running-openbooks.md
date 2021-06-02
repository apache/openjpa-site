Title: Building and Running OpenBooks

<a name="BuildingandRunningOpenBooks-InstructionstodownloadandrunOpenBooksDemo"></a>

## Instructions to download and run OpenBooks Demo

OpenBooks comes with

* complete source code
* build scripts to demonstrate how to build a typical OpenJPA application and package it for JSE or JEE environment
* scripts to run OpenBooks in on your local database installation.


Follow the simple instructions below to build and run OpenBooks:

<a name="BuildingandRunningOpenBooks-DownloadInstructions"></a>

## Download Instructions

OpenBooks can be checked out from OpenJPA repository.

 *$ svn co* [https://svn.apache.org/repos/asf/openjpa/trunk/openjpa-examples/openbooks](https://svn.apache.org/repos/asf/openjpa/trunk/openjpa-examples/openbooks).

will check out the source code and build scripts of OpenBooks in current
directory.

OpenBooks requires following software environment to run:

* Java Runtime version 6.0 or higher
* OpenJPA Libraries version 2.0 or higher
* Ant version 1.6 or higher
* Any JDBC complaint database supported by OpenJPA (embedded Derby is the default).



<a name="BuildingandRunningOpenBooks-Configurebuildandrunenvironment"></a>

## Configure build and run environment

OpenBooks builds with Ant. The Ant build script is somewhat involved
because OpenBooks can be built and packaged either as a JSE (Swing based)
application or a JEE Web Application. By default, OpenBooks is built as a
JSE application.

OpenBooks can be built in JSE and JEE mode -- and to keep things simple the
common build steps are available in main build script *build.xml* while
JSE and JEE specific packaging steps are described in separate
*build.jse.xml* and *build.jee.xml*, respectively. Furthermore, for
JEE, the deployment step is further refined for each application server.
See *build.jee.was.xml* and *build.jee.liberty.xml* for build and
installation steps for WebSphere Application Server and the Liberty Profile
for WAS, respectively.

Before you run a build, configure the build environment by editing
*openjpa-examples/openbooks/build.properties*. Essentially, you need to

*   Point *openjpa.lib* variable to the local directory where OpenJPA class
library(ies) reside. Notice that the variable points to a directory and not
a *\*.jar* file. All *\*.jar* files found under the directory are
included in compilation classpath. OpenJPA version 2.0, however, is also
available with all its runtime dependencies (such as JPA specification API,
Apache Commons Collections and others) packaged together in a _single_
library (lib).

_Note:_ Access to the OpenJPA class libraries is easier if you have a
Maven repository (.m2) available on your system.&nbsp; In this case, all
that is required is to update the *openjpa.version* variable to point at
the proper OpenJPA SNAPSHOT version.

*   Ideally, a JPA-compliant application _should_ not require
provider-specific library during compilation. OpenBooks persistent domain
model and application logic also does not use any OpenJPA specific
features, but OpenJPA libraries are still used during compilation because
bytecode for persistent entities are _enhanced_ as a post-compilation step.
This bytecode enhancement is not essential but an important step for using
OpenJPA.

The next step is to configure runtime configuration descriptors and
environment variables.

*   JSE
    *  Edit *persistence.xml* located in *openjpa-examples/openbooks/src/main/resources/META-INF* directory. Modify the *javax.persistence.jdbc.driver* and *javax.persistence.jdbc.url* property to suit your local database and its driver.
    *  Edit *openjpa-examples/openbooks/run.properties* to specify location
of OpenJPA class libraries and JDBC Driver used in runtime classpath.  Here
again, the use of the *openjpa.version* variable with a Maven repository
makes the library and jdbc driver configuration easy.

* JEE
    * You may already have a JTA data source configured and registered in
JNDI. Of course, then the appropriate configuration is to be edited
accordingly in the *<jta-data-source>* and *<non-jta-data-source>*
clauses. See *persistence.jee.was.xml* for WebSphere environment, or * persistence.jee.liberty.xml* for the Liberty Profile. 
    * OpenJPA library and JDBC drivers are configured in JEE server and hence
variables in this file are irrelevant.
    * More information on the build and installation of the OpenBooks example
for application servers can be found in the [WebSphere Application Server](#BuildingandRunningOpenBooks-WebSphereApplicationServer)
 and [Liberty Profile](#BuildingandRunningOpenBooks-LibertyProfileinWebSphereApplicationServerv8.5)
 deployment sections.



Both *build.properties* and *run.properties* files are commented
in-place on what is to be edited.


<a name="BuildingandRunningOpenBooks-BuildOpenBooksfromsource"></a>

## Build OpenBooks from source

Once you have configured the environment, simply issue (from the
*openjpa-examples/openbooks* directory):

 *$ ant*

or

 *$ ant \-Dbuild.mode=jee*

The default target of the ant script will

* generate metamodel classes (required for Criteria API)
* compile the source code
* enhance the persistence domain model
* package the application based on the build.mode as a Swing-based application or a Web Application Archive.
* copy the deployable artifacts to *target* and *target/openbooks* directories relative to the current directory.


<a name="BuildingandRunningOpenBooks-DeployOpenBooksinanApplicationServer"></a>

## Deploy OpenBooks in an Application Server

Deployment techniques and configuration vary across JEE compliant
application servers. Hence, OpenBooks does not provide an uber-deployment
script for all application server. Instead, application server specific
steps are encoded in separate build scripts for each application server.
Using generic build as described in the previous section, the
*target/openbooks.war* web archive needs to be deployed manually.


<a name="BuildingandRunningOpenBooks-WebSphereApplicationServer"></a>

### WebSphere Application Server

For WebSphere Application Server, automated build scripts are available in
*build.jee.was.xml*. WebSphere deployment needs to be triggered by
*ws_ant* utility as follows

 *$ ws_ant \-Dbuild.mode=jee \-Dappserver=was \-Dwas.home=<WAS_HOME\>*

where *<WAS_HOME\>* denotes the root directory where WAS V7 with JPA 2.0
feature pack has been installed (at a minimum). Yes, OpenBooks requires
features defined by the JPA 2.0 specification, thus the use of the WAS V7
JPA 2.0 feature pack is a minimum requirement. Further information on this
feature pack is available [here](http://www-01.ibm.com/support/docview.wss?rs=180&uid=swg27018836)
 or [WebSphere in general](http://www-01.ibm.com/software/websphere/).

The WebSphere specific build will configure appropriate JTA data sources
using a python script (found under *openbooks/scripts/* directory before
deploying OpenBooks as a web application. The script assumes a single
server instance. If multiple profiles exist, the script will use the first
server profile.


<a name="BuildingandRunningOpenBooks-LibertyProfileinWebSphereApplicationServerv8.5"></a>

### Liberty Profile in WebSphere Application Server v8.5

For the Liberty Profile in WebSphere Application Server v8.5, automated
build scripts are available in *build.jee.liberty.xml*. Liberty Profile
deployment is very easy and needs to be triggered by *ant* as follows

 *$ ant \-Dbuild.mode=jee \-Dappserver=liberty \-Dliberty.home=<WAS_HOME\>/wlp \-Dliberty.server=<server name\>*

where \<WAS_HOME\> denotes the root directory where WAS v8.5 has been
installed, and <server name> is the name of your Liberty Profile server. 
Instead of specifying these two variables, *liberty.home* and
*liberty.server*, you could modify the build variables in the
*build.jee.liberty.xml* file.  

By specifying *liberty.home* and *liberty.server*, the ant script will
attempt to "deploy" the resulting openbooks.war application to the
designated Liberty server.  Additional configuration of your Liberty server
may be required before OpenBooks will work.  For example, you will need to
specify the *jpa-2.0* and *jdbc-4.0* features in your server.xml.  You
will also need to define the JTA datasources used by the OpenBooks
application via your server.xml file.  Examples of a derby configuration
can be found in the *openbooks/scripts/liberty* directory.

Additional information on the Liberty Profile can be found [here](http://www.wasdev.net/)
.  General WebSphere information can be found [here](http://www-01.ibm.com/software/websphere/).

<a name="BuildingandRunningOpenBooks-RunOpenBooks"></a>

## Run OpenBooks

If you have built OpenBooks for JSE, then go to the
*openjpa-examples/openbooks/target/openbooks* directory.

Invoke the Ant script to run OpenBooks

*$ ant \-f run.xml*

If you have built OpenBooks for JEE, a Web Application Archive
*openbooks.war* will be created in *openjpa-examples/openbooks/target*
directory. You need to deploy *openbooks.war* to a JEE Application
Server. Once deployed, you can point a browser to Application Server URL

 *http:// < app server host >:<port>/openbooks/*

For example,

 [http://localhost:9080/openbooks/](http://localhost:9080/openbooks/)

to access OpenBooks as a web application.


<a name="BuildingandRunningOpenBooks-PopulateOpenBooksDatabase"></a>

## Populate OpenBooks Database

OpenBooks checks for existing data at first connection to the database. If
the database is empty, the schema is defined and populated with initial
data. However, you can explicitly populate the database in JSE build.

_Note:_ By default, the OpenBooks example uses and populates an Embedded
Derby instance on "first touch".  So, no further configuration or loading
is required for the default configuration.

Edit *load.properties* to specify load parameters such as number of Books
etc. OpenBooks uses this data to populate a database with some sample data.
This example file has some typical values. If you are satisfied with it,
you can leave them as it is. Then invoke the Ant script

 *$ ant \-f run.xml load*
