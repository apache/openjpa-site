Title: OpenJPA 2.1.0

<a name="OpenJPA2.1.0-OpenJPA2.1.0"></a>

# OpenJPA 2.1.0

The Apache OpenJPA community is proud to announce the release of Apache
OpenJPA 2.1.0.	As with the prior 2.0.1 release, this distribution is based
on the final [JSR 317 Java Persistence API, Version 2.0](http://jcp.org/en/jsr/detail?id=317)
 specification and passes the JPA 2.0 TCK, while remaining backwards
compatible with the prior 1.2.x releases based on the Java Persistence API
(JPA 1.0) part of Java Community Process JSR-220 (Enterprise JavaBeans
3.0).  For a list of all the new features of JPA 2.0, please checkout the [OpenJPA 2.0.1](openjpa-2.0.1.html)
 release notes.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org)
.

<a name="OpenJPA2.1.0-ChangesinOpenJPA2.1.0"></a>

# Changes in OpenJPA 2.1.0

<a name="OpenJPA2.1.0-Sub-task"></a>

### Sub-task

* OPENJPA-1214 - RelationFieldStrategy behaviour
* OPENJPA-1247 - WriteBehindCallback sleepTime interval of one EMF
datacache adversely impacting other EMF datacache
* OPENJPA-1311 - StoreCacheImpl
* OPENJPA-1312 - SelectImpl
* OPENJPA-1313 - RowManagerImpl
* OPENJPA-1314 - QueryResultCacheImpl
* OPENJPA-1316 - GeneratorImpl
* OPENJPA-1317 - FetchPlanImpl
* OPENJPA-1318 - org.apache.openjpa.persistence.ExtentImpl
* OPENJPA-1320 - BrokerImpl
* OPENJPA-1348 - Embeddable data not persisted when using WriteBehind
cache flush operation
* OPENJPA-1635 - Reduce lock contention in
MetaDataRepository.processRegisteredClasses
* OPENJPA-1638 - Add test variation to TestNamedQueryLockMode
* OPENJPA-1730 - Bundle Apache Commons DBCP in our binary distribution
* OPENJPA-1731 - Document and provide samples on how to use
commons-dbcp
* OPENJPA-1764 - Automatically enable connection pooling in unmanaged
environments
* OPENJPA-1821 - Upgrade to Commons DBCP 1.4
* OPENJPA-1826 - Can we have a new type for ignoring values?

<a name="OpenJPA2.1.0-Bug"></a>

### Bug
* OPENJPA-398 - ConcurrentModificationException at
org.apache.openjpa.kernel.BrokerImpl
* OPENJPA-526 - Insert text more than 4K bytes to Clob column causes
SQLException: Exhausted Resultset
* OPENJPA-641 - ConcurrentModificationException with self-referring
entity-class when not running the enhancer
* OPENJPA-1372 - Generating identifiers by using sequence table may
fail during sequence table initialization
* OPENJPA-1424 - Out of bounds exception using fetch plan
* OPENJPA-1454 - InstrumentationFactory crashes the tomcat
WebappClassLoader by injecting org.apache.openjpa classes into the
SystemClassLoader
* OPENJPA-1501 - EntityManager.find may return multiple instances of
Entities with String identities if id value has trailing spaces.
* OPENJPA-1508 - ArrayIndexOutOfBoundsException being thrown from
ClassMetaData.getExtraFieldDataIndex()
* OPENJPA-1550 - When batchLimit=-1 or >1 and an exception is caused,
the params and failedObject are missing from the resultant exception.
* OPENJPA-1582 - @OrderColumn(updatable=false) may have the order
column field updated
* OPENJPA-1584 - PreparedQuery gives wrong result if query has subquery
and parameters are used in both main select and subselect
* OPENJPA-1609 - PessimisticLockException instead of
LockTimeoutException thrown on DB2V9 for ZOS
* OPENJPA-1613 - Exception thrown when enhancing a (property access)
class that has an abstract @MappedSuperclass with no annotated properties
* OPENJPA-1626 - ParseException when specified name of QueryCache
* OPENJPA-1627 - ORderBy with @ElementJoinColumn and EmbeddedId uses
wrong columns in SQL
* OPENJPA-1634 - Loading JAXB meta data when using MetaDataRepository
preloading isn't thead safe.
* OPENJPA-1641 - SybaseDictionary should try both JDBC column names and
Sybase specific column names
* OPENJPA-1644 - Null field values after calling EntityManager.remove()
* OPENJPA-1646 - DataCacheManager initialization still isn't thread
safe.
* OPENJPA-1648 - Slice thread pool breaks down under high concurrency
* OPENJPA-1662 - Type support has regressed in OpenJPA 2.0
* OPENJPA-1665 - Problems when using auto incrementing colums that
start at zero
* OPENJPA-1667 - Incorrect column type for LOB streaming in MySQL
* OPENJPA-1668 - User's ''DBDictionary.sequenceSQL' setting not being
honored on zOS
* OPENJPA-1670 - PCRegistry memory leak when using MetaDataRepository
preloading.
* OPENJPA-1676 - PCClassFileTransformer.transform causing NPE when
class name is null
* OPENJPA-1678 - SQL Parameter values may contain sensitive information
and should not be logged by default.
* OPENJPA-1682 - TestSimpleXmlEntity.testId failed with invalid DB2
create table SQL statement
* OPENJPA-1683 - Why string encoding of OpenJPA Identity instances for
LongId differes from other built-in identity types?
* OPENJPA-1685 - Comma delimited validation groups defined in
persistence.xml do not handle whitespace
* OPENJPA-1689 - The mapping tool does not remove user created
sequences on PostgreSQL
* OPENJPA-1690 - DistinctResultList is not Serializable
* OPENJPA-1691 - Oracle XMLType column failed to insert/update when xml
contains more than 4000 characters
* OPENJPA-1692 - Add post creation callback to BrokerFactory
* OPENJPA-1695 - OutOfMemoryError from
CacheMarshallerImpl.setInputUrlFromResourceLocation.
* OPENJPA-1696 - Type discriminator for polymorphic queries limited to
Single Table inheritance
* OPENJPA-1697 - A EnumValueHandler strategy along with XmlType
annotation incorrectly mapped to XmlType in create table DDL
* OPENJPA-1701 - Calling em.refresh(...) causes a WARNING message to be
logged
* OPENJPA-1704 - PCEnhancer incorrectly generates readExternal
* OPENJPA-1713 - OutOfMemory caused by
EntityManagerImpl.push/popFetchPlan processing
* OPENJPA-1715 - OpenJPA generates wrong SQL if a result variable that
references an aggregate expression is used in ORDER BY clause
* OPENJPA-1719 - Prepared SQL cache ordering problem with subqueries.
* OPENJPA-1722 - Problem serializing DistinctResultList when
EntityManager is closed
* OPENJPA-1726 - Clean up OpenJPA test case failures for PostgreSQL
* OPENJPA-1727 - QueryCache TIMESTAMP eviction policy doesn't evict a
timed out query if it returns zero results.
* OPENJPA-1736 - Mappings with foreign keys as identity fields
sometimes not resolved correctly
* OPENJPA-1737 - The openjpa-2.0.0.jar does not have its MANIFEST.MF
has the first entry
* OPENJPA-1738 - Prepared SQL query does not handle collection-valued
parameter of persistence-capable objects
* OPENJPA-1740 - Type expression for entites using Joined table
strategy is not working properly
* OPENJPA-1742 - Recover if connectionFactory on EntityManagerFactory
is invalid but cf on EntityManager is valid.
* OPENJPA-1743 - Tool configuration does not support EMF anchors
* OPENJPA-1749 - Throw exception if using datacache / synchronize
mappings and specifying datasource name at EM creation.
* OPENJPA-1751 - New openbooks and image-gallery samples are not in the
binary assembly
* OPENJPA-1752 - TestPessimisticLocks JUNIT test produced inconsistent
behavior with various backends
* OPENJPA-1753 - TestMixedLockManagerLockPermutation: Timing issue
determines the pass/no-pass of the test case
* OPENJPA-1757 - Em.refresh(..) not refreshing from the DB when
shared-cache-mode is set to ALL
* OPENJPA-1765 - TableGenerator doesn't properly utilize all keys when
under heavy stress.
* OPENJPA-1769 - Broker getObjectId(...) doesn't return a proper object
id for an Entity that is detached and has no DetachedStateManager
* OPENJPA-1770 - Inconsistent behaviour when fetching an Entity that
has a null embeddable and the DataCache is enabled
* OPENJPA-1784 - Map value updates not flushed
* OPENJPA-1788 - Problem in Firebird 2.1 with sequence creation
* OPENJPA-1790 - java.lang.VerifyError thrown when trying to commit
entity.
* OPENJPA-1793 - @EmbeddedId class having only one field java.sql.Data
* OPENJPA-1800 - Duplicate column created for sybase
* OPENJPA-1801 - CacheStatistics misses are improperly calculated.
* OPENJPA-1804 - NPE in MappingInfo.java line 1514
* OPENJPA-1809 - Refresh of versioned entity locked with pessimistic
locking throws incorrect exception
* OPENJPA-1810 - ClassCastException when using QueryCache and Criteria
API
* OPENJPA-1811 - Dynamic load of enhancer agent on Mac OS X fails
* OPENJPA-1814 - JPQL fails with Group By and Having
aggregate_expression IN (subquery)
* OPENJPA-1818 - SQL-Syntax errors with h2
* OPENJPA-1819 - ORDER BY will append additional column to the SELECT
clause which may potentialy cause ORA-00979 error
* OPENJPA-1828 - Query with expression IN
(collection_valued_input_parameter) should report syntax error, correct
usange is IN collection_valued_input_parameter
* OPENJPA-1830 - Deserialization of EMF causes connectionPassword to be
overwritten with Value.INVISIBLE
* OPENJPA-1831 - DataSourceFactory manipulates queryTimeout which is
already in milliseconds
* OPENJPA-1832 - Numeric is not a fixed size type for Sybase
* OPENJPA-1835 - dummy is not a valid column name for Sybase
* OPENJPA-1838 - Sybase can create Foriegn Keys
* OPENJPA-1839 - TestXMLCustomerOrder failed against Oracle with
"ORA-01461: can bind a LONG value only for insert into a LONG column"
* OPENJPA-1840 - QueryTimeoutException not thrown with Sybase
* OPENJPA-1853 - iSeries DB2 problem with using
@GeneratedValue(strategy=GenerationType.IDENTITY)
* OPENJPA-1856 - Executing bulk updates should evict stale data from
the DataCache
* OPENJPA-1857 - Wrong exception is thrown when JoinColumn annotation
is not incorrectly specified
* OPENJPA-1866 -
org.apache.openjpa.persistence.AnnotationPersistenceMetaDataSerializer
missing break on Switch
* OPENJPA-1867 - ClassCastException when using DataCache
* OPENJPA-1870 - Blob types override column definition from @Column
annotation with MySQL
* OPENJPA-1874 - Handle Oracle specific XML column type with @Lob
annotation
* OPENJPA-1877 - Treat Oracle XMLType columns as XML
* OPENJPA-1881 - Create "completion" message for the Enhancement
processing
* OPENJPA-1882 - NPE in DataCacheStoreManager when all types aren't
cached
* OPENJPA-1886 - Query trace may contain sensitive information and
should not be logged by default.
* OPENJPA-1890 - NPE is thrown when an Embeddable object is set more
than once to a managed entity
* OPENJPA-1892 - NullPointerException thrown by the BrokerImpl.find()
if requesting an entity which is marked by the @Cacheable(false) annotation
* OPENJPA-1893 - Missing join clause in query with collection-table
with two join-columns
* OPENJPA-1894 - Performance Improvement for SelectImpl
* OPENJPA-1896 - OpenJPA cannot store POJOs if a corresponding record
already exists
* OPENJPA-1897 - Sybase reserved words may not be used as column names
* OPENJPA-1898 - TestQueryMultiThreaded fails with OOME "unable to
create new native thread"
* OPENJPA-1900 - ClassCastException when serializing an entity if
DetachedStateField=true
* OPENJPA-1902 - SQLServer reserved words may not be used as
identifiers
* OPENJPA-1904 - OptimisticLockException during
refresh(*,PESSIMISTIC_*) with eagar fetch on relationship fields
* OPENJPA-1905 - jar-file validation should be deferred until after
OpenJPA is confirmed to be the application's chosen provider
* OPENJPA-1906 - Issue info / warning message when connection retain
mode is always
* OPENJPA-1909 - enhance unit tests with the correct persistence.xml
* OPENJPA-1910 - openjpa uses application ClassLoader for resolving
BrokerFactory (revisited)
* OPENJPA-1911 - InvalidStateException is thrown when merge an entity
with derived identiy
* OPENJPA-1918 - MetaDataRepository.preload() ignores class loader
returned by PersistenceUnitInfo.getClassLoader()
* OPENJPA-1923 - Allow flexible (non-standard) syntax for
collection-valued parameters in IN() expresseion of JPQL query
* OPENJPA-1935 - Informix lock exceptions are not mapped properly by
OpenJPA
* OPENJPA-1938 - Typo of time data type in SQLServerdictionary for
MSSQL 2008

<a name="OpenJPA2.1.0-Improvement"></a>

### Improvement
* OPENJPA-6 - OpenJPA doesn't meaningfully implement JDBC3, JDBC4
methods in its delegates
* OPENJPA-735 - Provide dictionary support for SolidDB
* OPENJPA-1364 - Upgrade to latest commons-lang for required OSGi
metadata
* OPENJPA-1378 - Provide LRU option for L2 data cache
* OPENJPA-1563 - Better parameter validation on StoreCache.pinAll()
method
* OPENJPA-1612 - Mapping an unsupported type
* OPENJPA-1637 - Upgrade to latest Geronimo Specs for JPA2 and Bean
Validation
* OPENJPA-1643 - Use container-managed data sources as Slice
* OPENJPA-1649 - Refactor property processing for distributed Slice
configuration
* OPENJPA-1673 - Update MetaDataRepository docs
* OPENJPA-1699 - Streaming Lob support in DB2
* OPENJPA-1700 - Use FindBugs to reduce coding errors
* OPENJPA-1707 - A warning message should be logged when a down level
enhanced Entity is encountered.
* OPENJPA-1708 - Excessive Info message on locking row in optimistic
transaction
* OPENJPA-1712 - Upgrade builds to use Apache hosted Nexus repo
* OPENJPA-1717 - CacheStatistics should not be collected by default in
FinderCache
* OPENJPA-1723 - Improve the scalability of PreparedQueryCacheImpl
* OPENJPA-1724 - Allow MappingTool to generate DDL SQL files in a
different encoding than the local JVM
* OPENJPA-1729 - Simplified connection pooling
* OPENJPA-1732 - LogFactory adapter for SLF4J
* OPENJPA-1733 - Not meaningful message on bean validation valicator
configuration - "null" resaon
* OPENJPA-1734 - Support the DynamicEnhnacer on IBM JDK
* OPENJPA-1735 - Mark commons-logging as provided in the build to
remove transient maven dependency
* OPENJPA-1739 - Add pluggable instrumentation and instrumentation
provider capabilities to OpenJPA
* OPENJPA-1754 - Include Bean Validation API and Implementation in
openjpa-all and binary distribution
* OPENJPA-1761 - Upgrade Commons Pool from 1.5.3 to 1.5.4
* OPENJPA-1763 - Remove the requirement to configure
openjpa.RemoteCommitProvider when using the DataCache
* OPENJPA-1771 - Upgrade to latest Apache BVAL for testing and
apache-rat plugin
* OPENJPA-1776 - Allow slice distribution policy to delay the decision
to select the target slice
* OPENJPA-1791 - Remove test-base and testsupport artifacts dependency
for *-test.jar creation
* OPENJPA-1807 - Improved lifecycle tracing of EntityManager and
EntityManagerFactory
* OPENJPA-1833 - Add build date/time, branch version/revision and
copyright to docs
* OPENJPA-1836 - Update nightly-upload build script to use
key/passphrase
* OPENJPA-1841 - Allow DBDictionary to optimize IS NOT NULL SQL for
specific data types.
* OPENJPA-1844 - Create a JConsole plugin to display DataCache
statistics and help tune the cache
* OPENJPA-1847 - Use a single connection when generating schema
* OPENJPA-1855 - OpenJPA shouldn't silently ignore an invalid
javax.persistence.xxxx configuration property
* OPENJPA-1858 - Cache a reference to MetaDataRepository in BrokerImpl
* OPENJPA-1861 - Update maven plugins used in builds to support Maven
3.0
* OPENJPA-1863 - update HSQL dictionary for HSQLDB 2.0
* OPENJPA-1865 - Makes inefficient use of keySet iterator instead of
entrySet iterator
* OPENJPA-1868 - Miscellaneous FindBugs suggested performance
improvements
* OPENJPA-1871 - Makes inefficient use of keySet iterator instead of
entrySet iterator
* OPENJPA-1872 - Optimize CacheMap read performance
* OPENJPA-1885 - Improve persistAll to avoid redundant checked on each
instance
* OPENJPA-1888 - Add generics to the Kernel
* OPENJPA-1889 - Relax query binding parameter type-checking for enum
types
* OPENJPA-1895 - Minor reflection performance improvement.
* OPENJPA-1917 - Cache column alias in SelectImpl

<a name="OpenJPA2.1.0-NewFeature"></a>

### New Feature
* OPENJPA-1231 - Bean Validation sample
* OPENJPA-1663 - Add a policy interface for targeting queries to subset
of slices
* OPENJPA-1664 - Add a policy interface for targeting finder to a
subset of slices
* OPENJPA-1681 - Produce JPA Bean Validation example and corresponding
documentation
* OPENJPA-1759 - Add support for DATETIME2 with MS SQLServer
* OPENJPA-1773 - New OpenTrader example
* OPENJPA-1864 - MaxDB support

<a name="OpenJPA2.1.0-Task"></a>

### Task
* OPENJPA-1786 - Upgrade to latest JPA 2.0 TCK
* OPENJPA-1792 - Drop JDK5 support starting with OpenJPA 2.1

<a name="OpenJPA2.1.0-Test"></a>

### Test
* OPENJPA-33 - Need Query Engine test bucket
* OPENJPA-1639 - Simple openjpa-xmlstore tests
* OPENJPA-1660 - Add support to test with Apache Bean Validation
provider
* OPENJPA-1842 - CachedEntityStatistics depends on @GeneratedValue
which is not supported in Oracle by default
* OPENJPA-1848 - Update openjpa-integration-daytrader to perform user
tasks
* OPENJPA-1849 - testExternalValues failed with ORA-01438 Oracle
exception
* OPENJPA-1862 - Fix 2 test cases that cause failures on DB2 9.7
