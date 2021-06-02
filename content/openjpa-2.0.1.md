Title: OpenJPA 2.0.1

<a name="OpenJPA2.0.1-OpenJPA2.0.1"></a>

# OpenJPA 2.0.1

The Apache OpenJPA community is proud to announce the maintenance release
of Apache OpenJPA 2.0.1.  As with the prior 2.0.0 release, this
distribution is based on the final [JSR 317 Java Persistence API, Version 2.0](http://jcp.org/en/jsr/detail?id=317)
 specification and passes the JPA 2.0 TCK, while remaining backwards
compatible with the prior 1.2.x releases based on the Java Persistence API
(JPA 1.0) part of Java Community Process JSR-220 (Enterprise JavaBeans
3.0).  For a list of all the new features of JPA 2.0, please checkout the [OpenJPA 2.0.0](openjpa-2.0.0.html)
 release notes.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org)
.


<a name="OpenJPA2.0.1-ChangesinOpenJPA2.0.1"></a>

# Changes in OpenJPA 2.0.1

<a name="OpenJPA2.0.1-Sub-task"></a>

### Sub-task

* [OPENJPA-1635](https://issues.apache.org/jira/browse/OPENJPA-1635)
 Reduce lock contention in MetaDataRepository.processRegisteredClasses
* [OPENJPA-1638](https://issues.apache.org/jira/browse/OPENJPA-1638)
 Add test variation to TestNamedQueryLockMode

<a name="OpenJPA2.0.1-Bug"></a>

### Bug

* [OPENJPA-1424](https://issues.apache.org/jira/browse/OPENJPA-1424)
   Out of bounds exception using fetch plan
* [OPENJPA-1641](https://issues.apache.org/jira/browse/OPENJPA-1641)
 SybaseDictionary should try both JDBC column names and Sybase specific
column names
* [OPENJPA-1668](https://issues.apache.org/jira/browse/OPENJPA-1668)
 User's ''DBDictionary.sequenceSQL' setting not being honored on zOS 
* [OPENJPA-1678](https://issues.apache.org/jira/browse/OPENJPA-1678)
 SQL Parameter values may contain sensitive information and should not be
logged by default.
* [OPENJPA-1679](https://issues.apache.org/jira/browse/OPENJPA-1679)
 Index name too long for DB2 zOS when schema is present
* [OPENJPA-1690](https://issues.apache.org/jira/browse/OPENJPA-1690)
 DistinctResultList is not Serializable
* [OPENJPA-1704](https://issues.apache.org/jira/browse/OPENJPA-1704)
 PCEnhancer incorrectly generates readExternal 
* [OPENJPA-1713](https://issues.apache.org/jira/browse/OPENJPA-1713)
 OutOfMemory caused by EntityManagerImpl.push/popFetchPlan processing
* [OPENJPA-1714](https://issues.apache.org/jira/browse/OPENJPA-1714)
 Consider openjpa.Optimistic setting when calculating the default lock
mode to apply to a named query
* [OPENJPA-1715](https://issues.apache.org/jira/browse/OPENJPA-1715)
 OpenJPA generates wrong SQL if a result variable that references an
aggregate expression is used in ORDER BY clause
* [OPENJPA-1719](https://issues.apache.org/jira/browse/OPENJPA-1719)
 Prepared SQL cache ordering problem with subqueries. 
* [OPENJPA-1722](https://issues.apache.org/jira/browse/OPENJPA-1722)
 Problem serializing DistinctResultList when EntityManager is closed
* [OPENJPA-1737](https://issues.apache.org/jira/browse/OPENJPA-1737)
 The openjpa-2.0.0.jar does not have its MANIFEST.MF has the first entry
* [OPENJPA-1742](https://issues.apache.org/jira/browse/OPENJPA-1742)
 Recover if connectionFactory on EntityManagerFactory is invalid but cf
on EntityManager is valid. 
* [OPENJPA-1749](https://issues.apache.org/jira/browse/OPENJPA-1749)
 Throw exception if using datacache / synchronize mappings and specifying
datasource name at EM creation.
* [OPENJPA-1753](https://issues.apache.org/jira/browse/OPENJPA-1753)
 TestMixedLockManagerLockPermutation: Timing issue determines the
pass/no-pass of the test case

<a name="OpenJPA2.0.1-Improvement"></a>

### Improvement

* [OPENJPA-1637](https://issues.apache.org/jira/browse/OPENJPA-1637)
 Upgrade to latest Geronimo Specs for JPA2 and Bean Validation
* [OPENJPA-1673](https://issues.apache.org/jira/browse/OPENJPA-1673)
 Update MetaDataRepository docs
* [OPENJPA-1712](https://issues.apache.org/jira/browse/OPENJPA-1712)
 Upgrade builds to use Apache hosted Nexus repo
* [OPENJPA-1735](https://issues.apache.org/jira/browse/OPENJPA-1735)
 Mark commons-logging as provided in the build to remove transient maven
dependency
* [OPENJPA-1771](https://issues.apache.org/jira/browse/OPENJPA-1771)
 Upgrade to latest Apache BVAL for testing and apache-rat plugin
