Title: OpenJPA 2.0.0 Milestone 3


<a name="OpenJPA2.0.0Milestone3-OpenJPA2.0.0Milestone3"></a>

# OpenJPA 2.0.0 Milestone 3

The Apache OpenJPA community is proud to provide a Milestone 3 distribution
of OpenJPA 2.0.  This distribution is based on the 20090922 Proposed Final
Draft 2 of the JSR-317 JPA 2.0 specification.  Included are many
enhancements, fixes, and new functionality; giving developers early access
to many key features of JPA 2.0.  Some of the key features included in this
distribution:

* [JSR-317 JPA 2.0](http://jcp.org/en/jsr/detail?id=317)
 support based on the Proposed Final Draft 2 (20090922) of the APIs and
schemas.
* [JSR-303 Bean Validation](http://jcp.org/en/jsr/detail?id=303)
 support based on the 1.0.CR5 level of the APIs and schema.
* No Bean Validation API or provider is included with OpenJPA, but either
the [Hibernate RI v4.0.0 CR1 ](https://validator.hibernate.org/.html)
 or [Agimatec Validation v0.9.3](http://code.google.com/p/agimatec-validation/)
 can be used.
* Many documentation updates and automatic setting of compatibility options
based on persistence version.
* Support for the Criteria and Metamodel API, which can be used together to
create and execute strongly-typed programmatic queries.
* Metamodel source file generation.
* Support for cascading detach using cascade-detach as specified in the
orm.xml.
* Assertion that relationships in MappedSuperclass are unidirectional.
* Support for the TypedQuery and Tuple interfaces.
* Support for naming of unique constraints.
* Lob, Temporal, and Enumeration can now be specified on element
collections.
* JPQL now supports multiple constructors in the query projection list.
* Support for the shared-cache-mode element in the persistence.xml.
* Support for Cacheable annotation and CacheStoreMode/CacheRetriveMode
properties.
* Support for JDBC date, time, and timestamp literals within JPQL and
Criteria queries.
* Significant improvements to OpenJPA's subquery processing.
* Performance enhancements to class reflection utility.
* OpenJPA now includes the ability to use a pluggable encryption provider.
* New example which showcases the use of embeddables.
* [Improved test coverage](openjpa:jpa-2.0-test-coverage.html)
 for many database platforms and separation of database support into
verified and compatible categories.
* Many more...	

This early access distribution is based upon the contributions provided in
development iterations 8 through 12, as defined in the [JPA 2.0 Roadmap](http://cwiki.apache.org/confluence/display/openjpa/JPA+2.0+Roadmap)
.  The [JPA 2.0 Roadmap](jpa-2.0-roadmap.html)
 contains a complete list of features and feature summaries, including what
is on deck for future iterations.

<a name="OpenJPA2.0.0Milestone3-Legal"></a>

## Legal

Apache OpenJPA was developed by The Apache Software Foundation [http://www.apache.org/](http://www.apache.org/)
 and is licensed under [Apache License 2.0|http://www.apache.org/licenses/LICENSE-2.0]
.
Copyright (C) 2006-2009 Apache Software Foundation.
Apache and the Apache feather logo are trademarks of Apache Software
Foundation.

Apache OpenJPA is bundled with the schemas from the JPA specifications, by
Sun Microsystems and licensed under the CDDL 1.0. The source code is
available at: https://glassfish.dev.java.net/source/browse/glassfish/

Please review the [LICENSE](http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa-2.0.0-M3/LICENSE.txt)
 and [NOTICE|http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa-2.0.0-M3/NOTICE.txt]
 files in svn, source or binary distributions for more details.

{note}
This is an implementation of an early-draft specification developed under
the Java Community Process (JCP). The code is untested and presumed not to
be a compatible implementation of the JSR-317 Java Persistence API, Version
2.0 specification.  We encourage you to migrate to an implementation of the
JSR-317 Java Persistence API, Version 2.0 specification that has been
tested and verified to be compatible as soon as such an implementation is
available, and we encourage you to retain this notice in any implementation
of JSR-317 Java Persistence API, Version 2.0 specification that you
distribute.
{note}


<a name="OpenJPA2.0.0Milestone3-Downloads"></a>

## Downloads

Use the links below to download the artifacts or source for Apache OpenJPA
2.0.0 Milestone 3.  It is always good practice to [verify the integrity](downloads##verifying-releases.html)
 of the distribution files.

For information on obtaining OpenJPA artifacts for use within Maven or ANT
builds, see the [Obtaining](obtaining.html)
 page.	For information on building OpenJPA from source, see the [Building](building.html)
 page.


<a name="OpenJPA2.0.0Milestone3-BinaryAssemblies"></a>

### Binary Assemblies

<table>
<tr><th> Description </th><th> Download </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Milestone 3 </td><td class="border"> <a href="http://www.apache.org/dyn/closer.cgi/openjpa/2.0.0-m3/apache-openjpa-2.0.0-m3-binary.zip.html">apache-openjpa-2.0.0-M3-binary.zip</a>
 </td><td class="border"> <a href="http://www.apache.org/dyn/closer.cgi/openjpa/2.0.0-M3/apache-openjpa-2.0.0-M3-binary.zip.asc">PGP</a>
 </td></tr>
</table>


<a name="OpenJPA2.0.0Milestone3-SourceAssemblies"></a>

### Source Assemblies

<table>
<tr><th> Description </th><th> Download </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Milestone 3 Source Code </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa/downloads/apache-openjpa-2.0.0-M3-source.zip">apache-openjpa-2.0.0-M3-source.zip</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa/downloads/apache-openjpa-2.0.0-M3-source.zip.asc">PGP</a>
 </td></tr>
<tr><td class="border"> Geronimo JPA 2.0 PFD2 source code </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0-PFD2/geronimo-jpa_2.0_spec-1.0-PFD2-sources.jar">geronimo-jpa_2.0_spec-1.0-PFD2-sources.jar</a>
 </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0-PFD2/geronimo-jpa_2.0_spec-1.0-PFD2-sources.jar.asc">PGP</a>
 </td></tr>
<tr><td class="border"> Geronimo Validation 1.0 Early Access Spec source code </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0-CR5/geronimo-validation_1.0_spec-1.0-CR5-sources.jar">geronimo-validation_1.0_spec-1.0-CR5-sources.jar</a>
 </td><td class="border"> <a href="https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0-CR5/geronimo-validation_1.0_spec-1.0-CR5-sources.jar.asc">PGP</a>
 </td></tr>
</table>


<a name="OpenJPA2.0.0Milestone3-OtherResources"></a>

## Other Resources

<a name="OpenJPA2.0.0Milestone3-Documentation"></a>

### Documentation

* [Release Notes](http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa-2.0.0-M3/RELEASE-NOTES.html)
* [HTML Manual](http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa-2.0.0-M3/docs/manual/)

<a name="OpenJPA2.0.0Milestone3-QuickStart"></a>

### Quick Start

* [OpenJPA Examples](quick-start.html)

<a name="OpenJPA2.0.0Milestone3-Support"></a>

### Support

* [Reporting bugs and general help](found-a-bug.html)

<a name="OpenJPA2.0.0Milestone3-MavenArtifacts"></a>

### Maven Artifacts

* [OpenJPA 2.0.0 Milestone 3 JAR](http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa-2.0.0-M3/apache-openjpa-2.0.0-M3.jar)
* [OpenJPA 2.0.0 Milestone 3 JAR w/ depends](http://openjpa.apache.org/builds/2.0.0-M3/apache-openjpa-2.0.0-M3/apache-openjpa-2.0.0-M3.jar)
* [Geronimo JPA 2.0 PFD2 Spec artifacts](https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0-PFD2/)
* [Geronimo Validation 1.0 CR5 Spec artifacts](https://repository.apache.org/content/repositories/releases/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0-CR5/)

<a name="OpenJPA2.0.0Milestone3-SVNSourceBranches"></a>

### SVN Source Branches

* [OpenJPA 2.0.0 Milestone 3](https://svn.apache.org/repos/asf/openjpa/tags/2.0.0-M3/)
* [Geronimo JPA 2.0 PFD2 Spec](https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_2.0_spec-1.0-PFD2/)
* [Geronimo Validation 1.0 CR5 Spec](https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-validation_1.0_spec-1.0-CR5/)
  
  

  
  

