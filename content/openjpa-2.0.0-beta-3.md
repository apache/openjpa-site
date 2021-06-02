Title: OpenJPA 2.0.0 Beta 3

<a name="OpenJPA2.0.0Beta3-OpenJPA2.0.0Beta3"></a>

# OpenJPA 2.0.0 Beta 3

The Apache OpenJPA community is proud to release a Beta 3 distribution of
OpenJPA 2.0.0.	This distribution is based on the final [JSR 317 Java Persistence API, Version 2.0](http://jcp.org/en/jsr/detail?id=317)
 specification and passes the JPA 2.0 TCK.  Included are many enhancements,
fixes, and new functionality; giving developers access to all the new
features of JPA 2.0, including:

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
    * Currently limited to persistent state and relationships
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
* And many more...  

This distribution is based upon the contributions provided since the Beta 2
release, as defined in the [OpenJPA 2.0 Roadmap](jpa-2.0-roadmap.html)
, which contains a complete list of included features, including what is on
deck for future iterations.

  
  

----

<a name="OpenJPA2.0.0Beta3-Downloads"></a>

## Downloads

Use the links below to download the artifacts or source for Apache OpenJPA
2.0.0 Beta 3.  It is always good practice to [verify the integrity](downloads.html#verifying-releases)
 of the distribution files.

For information on obtaining OpenJPA artifacts for use within Maven or ANT
builds, see the [Obtaining](obtaining.html)
 page.	For information on building OpenJPA from source, see the [Building](building.html)
 page.


<a name="OpenJPA2.0.0Beta3-BinaryAssemblies"></a>

### Binary Assemblies

<table>
<tr><th> Description </th><th> Download </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Beta 3 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa/downloads/apache-openjpa-2.0.0-beta3-binary.zip.html">apache-openjpa-2.0.0-beta3-binary.zip</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa/downloads/apache-openjpa-2.0.0-beta3-binary.zip.asc">PGP</a>
 </td></tr>
</table>


<a name="OpenJPA2.0.0Beta3-SourceAssemblies"></a>

### Source Assemblies

<table>
<tr><th> Description </th><th> Download </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Beta 3 Source Code </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa/downloads/apache-openjpa-2.0.0-beta3-source.zip">apache-openjpa-2.0.0-beta3-source.zip</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa/downloads/apache-openjpa-2.0.0-beta3-source.zip.asc">PGP</a>
 </td></tr>
<tr><td class="border"> Geronimo JPA 2.0 Spec API v1.0 source code </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0/geronimo-jpa_2.0_spec-1.0-sources.jar">geronimo-jpa_2.0_spec-1.0-sources.jar</a>
 </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0/geronimo-jpa_2.0_spec-1.0-sources.jar.asc">PGP</a>
 </td></tr>
<tr><td class="border"> Geronimo Bean Validation 1.0 Spec API v1.0 source code </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0/geronimo-validation_1.0_spec-1.0-sources.jar">geronimo-validation_1.0_spec-1.0-sources.jar</a>
 </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0/geronimo-validation_1.0_spec-1.0-sources.jar.asc">PGP</a>
 </td></tr>
</table>

  
  

----

<a name="OpenJPA2.0.0Beta3-OtherResources"></a>

## Other Resources

<a name="OpenJPA2.0.0Beta3-Documentation"></a>

### Documentation

* [Release Notes](http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa-2.0.0-beta3/RELEASE-NOTES.html)
* [HTML Manual](http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa-2.0.0-beta3/docs/manual/)

<a name="OpenJPA2.0.0Beta3-QuickStart"></a>

### Quick Start

* [OpenJPA Examples](quick-start.html)

<a name="OpenJPA2.0.0Beta3-Support"></a>

### Support

* [Reporting bugs and general help](found-a-bug.html)

<a name="OpenJPA2.0.0Beta3-MavenArtifacts"></a>

### Maven Artifacts

* [OpenJPA 2.0.0 Beta 3 JAR](http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa-2.0.0-beta3/openjpa-2.0.0-beta3.jar)
* [OpenJPA 2.0.0 Beta 3 JAR w/ depends](http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa-2.0.0-beta3/openjpa-all-2.0.0-beta3.jar)
* [Geronimo JPA 2.0 Spec API artifacts](https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0/)
* [Geronimo Bean Validation 1.0 Spec API artifacts](https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0/)

<a name="OpenJPA2.0.0Beta3-SVNSourceBranches"></a>

### SVN Source Branches

* [OpenJPA 2.0.0 Beta 3](https://svn.apache.org/repos/asf/openjpa/tags/2.0.0-beta3/)
* [Geronimo JPA 2.0 Spec API](https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_2.0_spec-1.0/)
* [Geronimo Bean Validation 1.0 Spec API](https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-validation_1.0_spec-1.0/)
  
  

  
  

----

<a name="OpenJPA2.0.0Beta3-Legal"></a>

## Legal

Apache OpenJPA was developed by [The Apache Software Foundation](http://www.apache.org/)
 and is licensed under [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
.
Copyright 2006,2010 The Apache Software Foundation.
Apache, the Apache feather logo and OpenJPA are trademarks of Apache
Software Foundation.

Apache OpenJPA is bundled with the schemas from the JPA specifications, by
Sun Microsystems and licensed under the CDDL 1.0. The source code is
available at: <https://glassfish.dev.java.net/source/browse/glassfish/>

Please review the [LICENSE](http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa-2.0.0-beta3/LICENSE.txt)
 and [NOTICE](http://openjpa.apache.org/builds/2.0.0-beta3/apache-openjpa-2.0.0-beta3/NOTICE.txt)
 files in svn, source or binary distributions for more details.
----
  
  
