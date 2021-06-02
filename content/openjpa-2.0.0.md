Title: OpenJPA 2.0.0

<a name="OpenJPA2.0.0-OpenJPA2.0.0"></a>


# OpenJPA 2.0.0

The Apache OpenJPA community is proud to announce the release of Apache
OpenJPA 2.0.0.	This distribution is based on the final [JSR 317 Java Persistence API, Version 2.0](http://jcp.org/en/jsr/detail?id=317)
 specification and passes the JPA 2.0 TCK, while remaining backwards
compatible with prior releases based on the Java Persistence API (JPA 1.0)
part of Java Community Process JSR-220 (Enterprise JavaBeans 3.0). 
Included are many enhancements, fixes, and new functionality; giving
developers access to all the new features of JPA 2.0, including:

* Access Types - expanded to allow specification on a per-persistent type
basis or on individual attributes.
* Embeddables - expanded to include collections of embeddables, nested
embeddables, and embeddables containing relationships to other entities.
* Enhanced Map Collections - expanded to support ElementCollection and new
annotations for MapKeyColumn, MapKeyClass and MapKeyJoinColumn
* Derived Identities - enables the ID of an entity to be derived from
another entity, which provides for parent-to-dependent relationships
* Query API - methods to get typed query parameters and results, supported
and in-effect hints and lock mode getter/setter
* Locking - official support for Pessimistic locking (included in prior
OpenJPA releases) along with LockModeType properties and hint
* JPQL Updates -
    * Embeddables support for path expressions to nested Embeddables and
Embeddables with relationships
    * Enhanced Map Collection support for ElementCollection and new query
expressions for KEY, ENTRY, VALUE
    * Support for CASE and TYPE expressions along with IN expressions for
Collection parameters
    * Support for native date/time/timestamp literals
    * Support for INDEX expressions on an OrderColumn 
* L2 Cache -
    * Provides cache operations such as entity eviction and cache mode
behaviors to use, bypass or refresh items
    * Per-entity annotation to specify whether an entity should be cached
* Bean Validation - supports using a JSR 303 implementation for entity
validation for persist and remove operations
* Metamodel API - 
    * Provides API to dynamically retrieve metamodel information for a
persistence unit
    * Used with Criteria API to generate and execute type safe queries
    * Supports dynamic or static generation of the metamodel
* Criteria API -
    * Provides programmatic construction of queries using an object based
query graph
    * Operates on Metamodel objects to provide compile-time type safety
enforcement
* EntityManagerFactory API - updated for new L2 Cache, Properties, Criteria
and Metamodel APIs
* EntityManager API - updated for new Query and Query Result APIs, Hints,
Properties, LockModeType, and Detach
* OSGi - support for the Persistence Unit Service Specification 1.0 in the
OSGi Service Platform Release 4 Enterprise Version 4.2 specifications has
been provided by integration with the Apache Aries JPA module
* And many more...  

This distribution is based upon the contributions provided in all of the
development iterations for 2.0, as defined in the [OpenJPA 2.0 Roadmap](jpa-2.0-roadmap.html)
.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org)
.

  
  

----

<a name="OpenJPA2.0.0-Downloads"></a>

## Downloads

Use the links below to download the artifacts or source for Apache OpenJPA
2.0.0.	It is always good practice to [verify the integrity](downloads.html##verifying-releases)
 of the distribution files.

For information on obtaining OpenJPA artifacts for use within Maven or ANT
builds, see the [Obtaining](obtaining.html)
 page.	For information on building OpenJPA from source, see the [Building](building.html)
 page.


<table>
<tr><th> Description </th><th> Download </th><th> Checksums </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Binary </td><td class="border"> [apache-openjpa-2.0.0-binary.zip](http://archive.apache.org/dist/openjpa/2.0.0/apache-openjpa-2.0.0-binary.zip)
 </td><td class="border"> [MD5</td><td class="border">http://archive.apache.org/dist/openjpa/2.0.0/apache-openjpa-2.0.0-binary.zip.md5]
 </td><td class="border"> [PGP</td><td class="border">http://archive.apache.org/dist/openjpa/2.0.0/apache-openjpa-2.0.0-binary.zip.asc]
 </td></tr>
<tr><td class="border"> OpenJPA 2.0.0 Source Code </td><td class="border"> [apache-openjpa-2.0.0-source.zip](-http://archive.apache.org/dist/openjpa/2.0.0/apache-openjpa-2.0.0-source.zip.html)
 </td><td class="border"> [MD5</td><td class="border">http://archive.apache.org/dist/openjpa/2.0.0/apache-openjpa-2.0.0-source.zip.md5]
 </td><td class="border"> [PGP</td><td class="border">http://archive.apache.org/dist/openjpa/2.0.0/apache-openjpa-2.0.0-source.zip.asc]
 </td></tr>
</table>

  
  

----

<a name="OpenJPA2.0.0-OtherResources"></a>

## Other Resources

<a name="OpenJPA2.0.0-Documentation"></a>

### Documentation

* [Release Notes](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/RELEASE-NOTES.html)
* [User Guide (HTML)](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/docs/manual/)
* [User Guide (PDF)](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/docs/manual/manual.pdf)
* [Java API Docs](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/docs/javadoc/)

<a name="OpenJPA2.0.0-QuickStart"></a>

### Quick Start

* [OpenJPA Examples](quick-start.html)

<a name="OpenJPA2.0.0-Support"></a>

### Support

* [Reporting bugs and general help](found-a-bug.html)

<a name="OpenJPA2.0.0-MavenArtifacts"></a>

### Maven Artifacts

* [OpenJPA 2.0.0 JAR](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/openjpa-2.0.0.jar)
* [OpenJPA 2.0.0 JAR w/ depends](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/openjpa-all-2.0.0.jar)
* [Geronimo JPA 2.0 Spec API artifacts](https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0/)
* [Geronimo Bean Validation 1.0 Spec API artifacts](https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0/)

<a name="OpenJPA2.0.0-SVNSourceBranches"></a>

### SVN Source Branches

* [OpenJPA 2.0.0 ](https://svn.apache.org/repos/asf/openjpa/tags/2.0.0/)
* [Geronimo JPA 2.0 Spec API](https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_2.0_spec-1.0/)
* [Geronimo Bean Validation 1.0 Spec API](https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-validation_1.0_spec-1.0/)
  
  

  
  

----

<a name="OpenJPA2.0.0-Legal"></a>

## Legal

Apache OpenJPA was developed by [The Apache Software Foundation](http://www.apache.org/)
 and is licensed under [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
.
Copyright 2006,2010 The Apache Software Foundation.

Apache OpenJPA is bundled with the schemas from the JPA specifications, by
Sun Microsystems and licensed under the CDDL 1.0. The source code is
available at: <https://glassfish.dev.java.net/source/browse/glassfish/>

Please review the [LICENSE](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/LICENSE.txt)
 and [NOTICE](http://openjpa.apache.org/builds/2.0.0/apache-openjpa-2.0.0/NOTICE.txt)
 files in svn, source or binary distributions for more details.
----
  
  
