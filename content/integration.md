Title: Integration

<a name="How to integrate OpenJPA with various containers and application servers"> </a>

<a name="Integration-RuntimeDependencies"></a>

## Runtime Dependencies

The binary release download of OpenJPA includes all of the code needed to
run in a stand-alone Java SE JVM or within a Java EE application server.

See [Build and Runtime Dependencies](build-and-runtime-dependencies.html)
 for details on the required Java levels and runtime artifacts.


<a name="Integrating-IntegrationwithApacheTomEE"></a>

## Integration with Apache TomEE

[Apache TomEE](http://tomee.apache.org/) is a distribution of Tomcat bundled with OpenJPA and the other necessary components to make it a Java EE 6-8 and Jakarta EE 9+ compliant Web Profile implementation.  Apache TomEE 1.0.0 and later include OpenJPA 2.2.x.  TomEE works in [Eclipse using the Tomcat adapter](http://www.youtube.com/watch?v=Lr8pxEACVRI) and you can simply deploy a web archive that contains a persistence unit without the need to include OpenJPA in the webapp.  Unlike putting OpenJPA in Tomcat, TomEE supports full container managed EntityManagers and JTA persistence units.

<a name="Integration-IntegratingwithGlassFish:"></a>

## Integrating with GlassFish:

Since [GlassFish](http://glassfish.dev.java.net)
 implements the Jakarta Persistence API, you must [add openjpa-VERSION.jar and xbean-asm9-shaded-VERSION.jar to its libs](https://glassfish.org/docs/latest/reference-manual.html#add-library) and define explicitly in persistence.xml file that your provider is org.apache.openjpa.persistence.PersistenceProviderImpl.

 
<a name="Integration-IntegratingwithSunJavaSystemApplicationServer9.x:"></a>

## Integrating with Sun Java System Application Server 9.x:

Since Sun Java System Application Server is based on code from the [GlassFish project](http://glassfish.dev.java.net)
, the instructions to use OpenJPA in GlassFish and Sun Java System Application Server remain the same. 

<a name="Integration-IntegratingwithOpenLibertyServer:"></a>

## Integrating with OpenLiberty Server

If you want to integrate OpenJPA on your application using OpenLiberty maven plugin, add the following configuration to the pom.xml:


    <plugins>
    ...
    <plugin>
        <groupId>io.openliberty.tools</groupId>
        <artifactId>liberty-maven-plugin</artifactId>
        <version>${openliberty.maven.version}</version>
        <configuration>
            <copyDependencies>
                <dependencyGroup>
                    <location>jdbc</location>
                    <dependency>
                        <groupId>org.postgresql</groupId>
                        <artifactId>postgresql</artifactId>
                        <version>${postgresql.version}</version>
                    </dependency>
                </dependencyGroup>
                <dependencyGroup>
                    <location>lib/global</location>
                    <dependency>
                        <groupId>org.apache.openjpa</groupId>
                        <artifactId>openjpa</artifactId>
                        <version>${openjpa.version}</version>
                    </dependency>
                    <dependency>
                        <groupId>org.apache.xbean</groupId>
                        <artifactId>xbean-asm9-shaded</artifactId>
                        <version>4.31</version>
                    </dependency>
                </dependencyGroup>
            </copyDependencies>
        </configuration>
    </plugin>
    </plugins>

Remember to configure the database jdbc in src/main/liberty/config/server.xml:


    <server description="openjpa-liberty-server">
        <featureManager>
            <feature>webProfile-10.0</feature>
        </featureManager>

        <basicRegistry id="basic" realm="BasicRealm">
        </basicRegistry>

        <httpEndpoint id="defaultHttpEndpoint" httpPort="9080" httpsPort="9443" />

        <!-- Automatically expand WAR files and EAR files -->
        <applicationManager autoExpand="true" />

        <!-- Configures the application on a specified context root -->
        <webApplication contextRoot="/APP-WEB-ROOT" location="APP-NAME-1.0.0-SNAPSHOT.war" />

        <library id="postgresql-jdbclib">
            <fileset dir="jdbc" includes="postgresql*.jar" />
        </library>

        <dataSource jndiName="jdbc/your-datasource">
            <jdbcDriver libraryRef="postgresql-jdbclib" />
            <properties.postgresql serverName="DATABASE_HOST" databaseName="DATABASE_NAME" user="DATABASE_USER"
                password="DATABASE_PASSWORD" />
        </dataSource>
        <!-- Default SSL configuration enables trust for default certificates from the Java runtime -->
        <ssl id="defaultSSLConfig" trustDefaultCerts="true" />
    </server>


As occurs with Glassfish, as the default JPA provider of OpenLiberty is not OpenJPA, you must define OpenJPA as the provider in persistence.xml:


    <persistence version="3.0" xmlns="https://jakarta.ee/xml/ns/persistence"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="https://jakarta.ee/xml/ns/persistence https://jakarta.ee/xml/ns/persistence/persistence_3_0.xsd">
        <persistence-unit name="YOUR-PERSISTENCE-UNIT-NAME" transaction-type="JTA">
            <provider>org.apache.openjpa.persistence.PersistenceProviderImpl</provider>
            <jta-data-source>jdbc/your-datasource</jta-data-source>
            <properties>
                <property name="openjpa.jdbc.SynchronizeMappings" value="buildSchema(ForeignKeys=true)" />
            </properties>
        </persistence-unit>
    </persistence>

After that, you may run ```mvn -Pyour-liberty-profile liberty:dev```.

<a name="Integration-IntegratingwithIBMWebSphereApplicationServer:"></a>

## Integrating with IBM WebSphere Application Server:

See [IBM WebSphere Developer Technical Journal: Leveraging OpenJPA with WebSphere Application Server V6.1](http://www-128.ibm.com/developerworks/websphere/techjournal/0612_barcia/0612_barcia.html).

Also, WebSphere Application Server V6.1 can download and install the [EJB3 Feature Pack](http://www-01.ibm.com/support/docview.wss?rs=177&uid=swg21287579)
, which includes OpenJPA 1.0.x.

[WebSphere Application Server V7.0](http://www.ibm.com/developerworks/downloads/ws/was/)
 includes OpenJPA 1.2.x and you can simply deploy an enterprise archive, web archive, or EJB-JAR that contains a persistence unit.  

The [WebSphere Application Server V7 Feature Pack for OSGi Applications and Java Persistence API 2.0](http://www-01.ibm.com/software/webservers/appserv/was/featurepacks/osgi/)
 includes OpenJPA 2.0 and provides the use of the JPA 2.0 programming model
within Java EE5 and OSGi applications.

<a name="Integration-IntegratingwithIBMWebSphereApplicationServerCommunityEdition:"></a>

## Integrating with IBM WebSphere Application Server Community Edition:

[WebSphere Application Server Community Edition](http://www.ibm.com/developerworks/websphere/zones/was/wasce.html)
 V2.0.0.2 through 2.1.1.1 include OpenJPA 1.0.x and you can simply deploy
an enterprise archive, web archive, or EJB-JAR that contains a persistence unit.

WebSphere Application Server Community Edition V2.1.x releases after
V2.1.1.1 will include OpenJPA 1.2.x and you can simply deploy an enterprise
archive, web archive, or EJB-JAR that contains a persistence unit.


## Integrating with JOnAS Application Server V 4.X (J2EE 1.4 / EJB2.1 Container):

OpenJPA can successfully be integrated with the JOnAS 4.x Application
server family. I succeeded in configuring OpenJPA to use managed JTA
transactions of JOnAS, which means that you can use OpenJPA in parallel to
EJB 2.1 CMP/BMP  Entity Beans within the SAME container managed
transactions of your JOnAS Application Server. See [Hans Prueller's blog entry](http://hanzz.zapto.org/index.php?option=com_content&task=view&id=105&Itemid=31)
 for further details.

<a name="Integration-IntegratingwithBEAWeblogicServer10:"></a>

## Integrating with BEA Weblogic Server 10:

[BEA WebLogic Server 10](http://www.bea.com/framework.jsp?CNT=index.htm&FP=/content/products/weblogic/)
 includes OpenJPA. To use OpenJPA in a WebLogic Server environment, you can
simply deploy an enterprise archive, web archive, or EJB-JAR that contains
a persistence unit. The default persistence provider in WebLogic Server is
OpenJPA + Kodo, so you can either leave the <provider> element out of your
persistence.xml file, or set it to
org.apache.openjpa.persistence.PersistenceProviderImpl.

[BEA Kodo](http://www.bea.com/framework.jsp?CNT=index.htm&FP=/content/products/weblogic/kodo/)
 is built on top of OpenJPA, and so includes the OpenJPA jars.

<a name="Integration-IntegratingwithSpring:"></a>

## Integrating with Spring:

It is not necessary to configure a Spring loadTimeWeaver when using OpenJPA
build time enhancement. The following warning message will be logged by
OpenJPA when creating an EntityManagerFactory but it can be safely ignored.

> WARN   \[main\] while registering a ClassTransformer with PersistenceUnitInfo: name 'PuName', root URL \[file:/.../\]. The error has been consumed. To see it, set your openjpa.Runtime log level to TRACE. Load-time class transformation will not be available.

Please see the [Spring documentation](http://static.springframework.org/spring/docs/2.0.x/reference/orm.html#orm-jpa-setup-lcemfb)
 for more information.
