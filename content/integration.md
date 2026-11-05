Title: Integration

<a name="How to integrate OpenJPA with various containers and application servers"> </a>

<a name="Integration-RuntimeDependencies"></a>

## Runtime Dependencies

The binary release download of OpenJPA includes all of the code needed to
run in a stand-alone Java SE JVM or within a Java EE application server.

## Standalone usage

It is preferred, though, to use maven or gradle artifacts builds to use it.

In a standalone environment, please add org.apache.openjpa:openjpa-persistence-jdbc:VERSION as a dependency of your project. With only this dependency, you will *not* have access to Jakarta Validation API.

## Application environments usage

As a Jakarta Persistence provider, OpenJPA may also be used in Jakarta WebProfile and Jakarta EE environments, such as:

* [Apache TomEE](https://tomee.apache.org)
* [Eclipse Glassfish](https://glasfish.org)
* [IBM OpenLIberty](https://openliberty.io)
* [Redhat WilFly](https://www.wildfly.org/)
* [VMWare Tanzu Spring](https://spring.io)

Please check in each server documentation if OpenJPA is already embedded or if it is necessary to add the needed libraries. If you need them, please note you should add org.apache.openjpa:openjpa and org.apache.xbean:xbean-asm9-shaded artifacts to the corresponding global libraries. Check the server documentation how to do that.

## OSGi

You may use OpenJPA also in OSGi environments, such as:

* [Apache Karaf](https://karaf.apache.org)
* [Apache Felix](https://felix.apache.org)

As with application servers, please check the project documentation about integration instructions.
