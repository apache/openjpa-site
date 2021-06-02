Title: OpenJPA 2.0.0 Early Access 2


<a name="OpenJPA2.0.0EarlyAccess2-OpenJPA2.0.0EarlyAccess2"></a>

# OpenJPA 2.0.0 Early Access 2

The Apache OpenJPA community is proud to provide an early access
distribution of OpenJPA 2.0.  This distribution is based on the 03/13/2009
draft of the JPA 2.0/JSR-317 specification.  Included are many
enhancements, fixes, and new functionality; giving developers early access
to many key features of JPA 2.0.  Some of the key features included in this
distribution:

* JPA 2.0 API and persistence and orm schemas
* Support for nested embeddables and relationships within embeddables
* Support for collections of embeddables and basic types
* A programmatic query construction API based upon the 10/2008 revision of
the JSR-317 specification
* A standardized Level 2 cache interface
* Enhanced map collection support
* Support for standard javax.persistence configuration properties
* A new prepared query cache for the caching of the SQL underlying JPQL and
find queries 
* Support for derived identities
* The ability to specify an order column on ordered collections
* Significant enhancements to JPQL
* Automatic orphan removal
* Support for individual entity detachment, including the ability to
cascade
* Methods to retrieve active and all supported properties on the entity
manager and entity manager factory
* New lock modes, including pessimistic locking on a per entity manager and
query method level
* Support for query and lock timeout hints on a per entity manager and
query method level
* Specification of explicit persistent access type on persistent classes
and attributes
* Many more...	

This early access distribution is based upon the contributions provided in
development iterations through iteration 7, as defined in the [JPA 2.0 Roadmap](http://cwiki.apache.org/confluence/display/openjpa/JPA+2.0+Roadmap)
.  The [JPA 2.0 Roadmap](jpa-2.0-roadmap)
 contains a complete list of features and feature summaries, including what
is on deck for future iterations.

<a name="OpenJPA2.0.0EarlyAccess2-Legal"></a>

## Legal

Apache OpenJPA was developed by The Apache Software Foundation [http://www.apache.org/](http://www.apache.org/)
 and is licensed under [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
.
Copyright &copy; 2006-2009 Apache Software Foundation.
Apache and the Apache feather logo are trademarks of Apache Software
Foundation.

Apache OpenJPA is bundled with the schemas from the JPA specification, by
Sun Microsystems and licensed under the CDDL 1.0. The source code is
available at: <https://glassfish.dev.java.net/source/browse/glassfish/>

Please review the [LICENSE](https://svn.apache.org/repos/asf/openjpa/branches/2.0.0-EA2/LICENSE.txt)
 and [NOTICE](https://svn.apache.org/repos/asf/openjpa/branches/2.0.0-EA2/NOTICE.txt)
 files in svn, source or binary distributions for more details.

<table class="note"><tr>
  <td valign="top"> <IMG src="images/warning.gif" width="16" height="16" border="0">
  <td> This is an implementation of an early-draft specification developed under
the Java Community Process (JCP) and is *made available for testing and
evaluation purposes only*. The code is not compatible with any
specification of the JCP.
</tr></table>


<a name="OpenJPA2.0.0EarlyAccess2-Downloads"></a>

## Downloads

Use the links below to download the artifacts or source for Apache OpenJPA
2.0.0 Early Access 2.  It is always good practice to [verify the integrity](downloads##verifying-releases.html)
 of the distribution files.

For information on obtaining OpenJPA artifacts for use within Maven or ANT
builds, see the [Obtaining](obtaining.html)
 page.	For information on building OpenJPA from source, see the [Building]
 page.


<a name="OpenJPA2.0.0EarlyAccess2-BinaryAssemblies"></a>

### Binary Assemblies

<table>
<tr><th> Description </th><th> Download </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Early Access 2 runtime </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-ea2-snapshot/downloads/apache-openjpa-2.0.0-ea2-snapshot-binary.zip.html">apache-openjpa-2.0.0-EA2-SNAPSHOT-binary.zip</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/apache-openjpa-2.0.0-EA2-SNAPSHOT-binary.zip.MD5">MD5</a>
 </td></tr>
</table>


<a name="OpenJPA2.0.0EarlyAccess2-SourceAssemblies"></a>

### Source Assemblies

<table>
<tr><th> Description </th><th> Download </th><th> Signatures </th></tr>
<tr><td class="border"> OpenJPA 2.0.0 Early Access 2 source code </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/apache-openjpa-2.0.0-EA2-SNAPSHOT-source.zip">apache-openjpa-2.0.0-EA2-SNAPSHOT-source.zip</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/apache-openjpa-2.0.0-EA2-SNAPSHOT-source.zip.MD5">MD5</a>
 </td></tr>
<tr><td class="border"> Geronimo JPA 2.0 Early Access Spec source code </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/geronimo-jpa_2.0_spec-1.0-EA2-SNAPSHOT-sources.jar">geronimo-jpa_2.0_spec-1.0-EA2-SNAPSHOT-sources.jar</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/geronimo-jpa_2.0_spec-1.0-EA2-SNAPSHOT-sources.jar.MD5">MD5</a>
 </td></tr>
<tr><td class="border"> Geronimo Validation 1.0 Early Access Spec source code </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/geronimo-validation_1.0_spec-1.0-EA-SNAPSHOT-sources.jar">geronimo-validation_1.0_spec-1.0-EA-SNAPSHOT-sources.jar</a>
 </td><td class="border"> <a href="http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/downloads/geronimo-validation_1.0_spec-1.0-EA-SNAPSHOT-sources.jar.MD5">MD5</a>
 </td></tr>
</table>


<a name="OpenJPA2.0.0EarlyAccess2-OtherResources"></a>

## Other Resources

<a name="OpenJPA2.0.0EarlyAccess2-Documentation"></a>

### Documentation

* [HTML Manual](http://openjpa.apache.org/builds/2.0.0-EA2-SNAPSHOT/docs/manual/)

<a name="OpenJPA2.0.0EarlyAccess2-QuickStart"></a>

### Quick Start

* [OpenJPA Examples](quick-start.html)

<a name="OpenJPA2.0.0EarlyAccess2-Support"></a>

### Support

* [Reporting bugs and general help](found-a-bug.html)

<a name="OpenJPA2.0.0EarlyAccess2-MavenArtifacts"></a>

### Maven Artifacts

* [OpenJPA 2.0.0 Early Access 2 aggregate jar](http://people.apache.org/repo/m2-snapshot-repository/org/apache/openjpa/openjpa/2.0.0-EA2-SNAPSHOT/)
* [Geronimo JPA 2.0 Early Access Spec](http://people.apache.org/repo/m2-snapshot-repository/org/apache/geronimo/specs/geronimo-jpa_2.0_spec/1.0-EA2-SNAPSHOT/)
* [Geronimo Validation 1.0 Early Access Spec](http://people.apache.org/repo/m2-snapshot-repository/org/apache/geronimo/specs/geronimo-validation_1.0_spec/1.0-EA-SNAPSHOT/)

<a name="OpenJPA2.0.0EarlyAccess2-SVNSourceBranches"></a>

### SVN Source Branches

* [OpenJPA 2.0.0 Early Access](https://svn.apache.org/repos/asf/openjpa/branches/2.0.0-EA2/)
* [Geronimo JPA 2.0 Early Access Spec](https://svn.apache.org/repos/asf/geronimo/specs/branches/geronimo-jpa_2.0_spec-1.0-EA2/)
* [Geronimo Validation 1.0 Early Access Spec](https://svn.apache.org/repos/asf/geronimo/specs/branches/geronimo-validation_1.0_spec-1.0-EA/)
  
  

  
  

