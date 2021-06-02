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

[Apache TomEE](http://tomee.apache.org/) is a distribution of Tomcat bundled with OpenJPA and the other necessary components to make it a Java EE 6 compliant Web Profile implementation.  Apache TomEE 1.0.0 and later include OpenJPA 2.2.x.  TomEE works in [Eclipse using the Tomcat adapter](http://www.youtube.com/watch?v=Lr8pxEACVRI) and you can simply deploy a web archive that contains a persistence unit without the need to include OpenJPA in the webapp.  Unlike putting OpenJPA in Tomcat, TomEE supports full container managed EntityManagers and JTA persistence units.

<a name="Integration-IntegratingwithApacheGeronimo:"></a>

## Integrating with Apache Geronimo:

[Apache Geronimo](http://geronimo.apache.org/)
 V2.0.2 through 2.1.3 include OpenJPA 1.0.x and you can simply deploy an
enterprise archive, web archive, or EJB-JAR that contains a persistence
unit.
Apache Geronimo V2.1.4 includes OpenJPA 1.2.x and you can simply deploy an
enterprise archive, web archive, or EJB-JAR that contains a persistence
unit.

<a name="Integration-IntegratingwithGlassFish:"></a>

## Integrating with GlassFish:

Since [GlassFish](http://glassfish.dev.java.net)
 implements the Java Persistence API 1.0 SPI, it is very easy to use
OpenJPA in Glassfish. See [Sahoo's blog](http://weblogs.java.net/blog/ss141213/archive/2006/07/using_openjpa_a.html)
 for further details.

<a name="Integration-IntegratingwithSunJavaSystemApplicationServer9.x:"></a>

## Integrating with Sun Java System Application Server 9.x:

Since Sun Java System Application Server is based on code from the [GlassFish project](http://glassfish.dev.java.net)
, the instructions to use OpenJPA in GlassFish and Sun Java System
Application Server remain the same. 

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
