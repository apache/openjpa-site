Title: OpenJPA 2.4.x


<a name="OpenJPA-2.4.3-OpenJPA-2.4.3"></a>

# OpenJPA 2.4.3

The Apache OpenJPA community is proud to announce the release of Apache
OpenJPA 2.4.3.
This distribution is based on the final [JSR 317 Java Persistence API,
Version 2.0](http://jcp.org/en/jsr/detail?id=317) specification and
passes the JPA 2.0 TCK, while remaining backwards
compatible with the prior 1.2.x releases based on the Java Persistence API
(JPA 1.0) part of Java Community Process JSR-220 (Enterprise JavaBeans
3.0).

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org).

<a name="OpenJPA-2.4.3"></a>

# Changes in OpenJPA 2.4.3

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2646'>OPENJPA-2646</a>] -         Sporadic NullPointerException occurs under heavy load when QuerySQLCache is enabled.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2689'>OPENJPA-2689</a>] -         Calling setFixedCHAR on newer Oracle JDBC drivers fails with an IllegalAccessException
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2690'>OPENJPA-2690</a>] -         Update OSGi Import-Package to support Oracle CLOB/BLOB
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2691'>OPENJPA-2691</a>] -         OracleDictionary should use non Deprecated method of empty_lob
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2698'>OPENJPA-2698</a>] -         Query cache incorrectly handles parameters for BETWEEN expressions
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2725'>OPENJPA-2725</a>] -         fix ConcurrentModificationException during unrefed dependents cleanup
</li>
</ul>
        
<h2>        New Feature
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2598'>OPENJPA-2598</a>] -         Support SQL server Offset Fetch syntax for pagination
</li>
</ul>
        
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2581'>OPENJPA-2581</a>] -         openjpa-maven-plugin: drop and create schema regardless of the current database state
</li>
</ul>
                                                                    
<h2>        Dependency upgrade
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2730'>OPENJPA-2730</a>] -         Update to XBean Asm 6 Shaded 4.8
</li>
</ul>

<a name="OpenJPA-2.4.2"></a>

# Changes in OpenJPA 2.4.2

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2245'>OPENJPA-2245</a>] -         NotSerializableException when using a remote QueryCache and the Criteria API
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2631'>OPENJPA-2631</a>] -         ClassCastException occurs when an equals comparison query is executed on an entity with an @EmbeddedId that contains more than one field.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2632'>OPENJPA-2632</a>] -         select new not working if result class is not in same classloader
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2636'>OPENJPA-2636</a>] -         Custom plugins (e.g. JDBCListener, DBDictionary) can cause Classloader leaks.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2640'>OPENJPA-2640</a>] -         Cannot use custom DBDictionary with Maven plugin
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2650'>OPENJPA-2650</a>] -         When SchemaFactory and useSchemaName=false is set, a schema name is incorrectly used.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2651'>OPENJPA-2651</a>] -         IDs of entities are incorrectly assigned when @SqlResultSetMapping is used with inheritance and a ManyToOne relationship.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2672'>OPENJPA-2672</a>] -         ConfigurationImpl.loadGlobals() has java.util.ConcurrentModificationException vulnerability
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2674'>OPENJPA-2674</a>] -         JarFile is not closed
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2675'>OPENJPA-2675</a>] -         Missing check for null parameter in equals()
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2676'>OPENJPA-2676</a>] -         openjpa relies on default locale
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2684'>OPENJPA-2684</a>] -         Persistence entities not recognized in Wildfly 10 if in a JAR
</li>
</ul>
                        
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2660'>OPENJPA-2660</a>] -         Resolve Maven warnings
</li>
</ul>

<a name="OpenJPA-2.4.1"></a>

# Changes in OpenJPA 2.4.1

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2341'>OPENJPA-2341</a>] -         OpenJPA ignores custom field strategies globally defined in persistence.xml
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2517'>OPENJPA-2517</a>] -         Incorrect the time unit of query timeout value.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2539'>OPENJPA-2539</a>] -         JPQL interpret wrongly for inner join table (without mapped relation)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2582'>OPENJPA-2582</a>] -         openjpa bundle module leaks jest dependencies
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2586'>OPENJPA-2586</a>] -         Incorrect relationship data returned when QueryCache and FetchPlans are used.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2596'>OPENJPA-2596</a>] -         schema-delta generation (sqlAction=refresh) drops columns if they have an alternative typeName
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2597'>OPENJPA-2597</a>] -         HsqlDictionary considers NUMERIC/DECIMAL as a fixedSizeTypeNameSet
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2600'>OPENJPA-2600</a>] -         finally remove NullSafeConcurrentHashMap and SizedConcurrentHashMap
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2601'>OPENJPA-2601</a>] -         &#39;hint&#39; element in orm:xml is ignored
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2603'>OPENJPA-2603</a>] -         Merging an unmanaged entity multiple (3) times leads to an exception.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2605'>OPENJPA-2605</a>] -         DelegatingConnection.unwrap() doesn&#39;t adhere to java.sql.Wrapper.unwrap() contract
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2609'>OPENJPA-2609</a>] -         Sporadic ClassCastException occurs under heavy load when QuerySQLCache is enabled.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2616'>OPENJPA-2616</a>] -         Update Commons Collections to 3.2.2
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2617'>OPENJPA-2617</a>] -         blacklist org.codehaus.groovy.runtime.,org.apache.commons.collections.functors.,org.apache.xalan in our custom ObjectInputStreams
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2626'>OPENJPA-2626</a>] -         isEnhanced doesn&#39;t support java 8 bytecode
</li>
</ul>

<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2602'>OPENJPA-2602</a>] -         OracleDictionary uses reflection way too often
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2607'>OPENJPA-2607</a>] -         Import range for javax.transaction is to small
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2623'>OPENJPA-2623</a>] -         Switch to Java5 mojo annotations
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2627'>OPENJPA-2627</a>] -         Create an option to disable column type checking errors during schema validation.
</li>
</ul>

<h2>        Test
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2595'>OPENJPA-2595</a>] -         upgrade test framework from junit-3 to junit 4
</li>
</ul>



<a name="OpenJPA-2.4.0"></a>

# Changes in OpenJPA 2.4.0


<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2135'>OPENJPA-2135</a>] -         Deprecate prepareForPooling
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2489'>OPENJPA-2489</a>] -         Delayed collection proxy tests failing with Java 8
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2491'>OPENJPA-2491</a>] -         AssertionFailedError with Java 8 and TestInExpressionParamaterBinding
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2492'>OPENJPA-2492</a>] -         TestConcurrentMap error with Java 8
</li>
</ul>

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1590'>OPENJPA-1590</a>] -         Agent enhancer doesn&#39;t work with Tomcat
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1988'>OPENJPA-1988</a>] -         openjpa does not process persistence unit default &lt;cascade-persist&gt;
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2022'>OPENJPA-2022</a>] -         Reversemappingtooltask with oracle is failing like in OPENJPA-1940 previous bug
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2094'>OPENJPA-2094</a>] -         Metadata processing needs to support jar:file URLs that address Jar directories
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2233'>OPENJPA-2233</a>] -         Failed to invoke pcGetIDOwningClass method on embeddable entity with ID annotation
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2286'>OPENJPA-2286</a>] -         SELECT COUNT with date litteral,used more than once, provokes ArgumentException: Attempt to compare incompatible types class java.util.Date and class org.apache.openjpa.jdbc.sql.Raw
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2287'>OPENJPA-2287</a>] -         OpenJPA makes fields null
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2381'>OPENJPA-2381</a>] -         Update serp to 1.15.1
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2441'>OPENJPA-2441</a>] -         TestNullSafeConcurrentHashMap fails when running on Oracle Java 8
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2442'>OPENJPA-2442</a>] -         java.lang.VerifyError in TestProxyManager when loading a dynamically created custom proxy class on Oracle Java 8
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2443'>OPENJPA-2443</a>] -         InvalidStateException while merging a new Entity with a GeneratedValue id
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2444'>OPENJPA-2444</a>] -         ReverseMappingTool creates orm.xml files in the current working directory
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2456'>OPENJPA-2456</a>] -         Fresh checkout from svn won&#39;t compile tests due to OutOfMemoryError: Java heap space
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2463'>OPENJPA-2463</a>] -         Wrong logging level on message issued by the fix to OPENJPA-2233
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2467'>OPENJPA-2467</a>] -         No setter was found for method like tStart
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2470'>OPENJPA-2470</a>] -         DataCacheManagerImpl infinite loop for checking if classes are cachable
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2472'>OPENJPA-2472</a>] -         Concurrency issue in ClassMetaData.getPkAndNonPersistentManagedFmdIndexes()
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2475'>OPENJPA-2475</a>] -         A query with LEFT FETCH JOIN returns incorrect results.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2476'>OPENJPA-2476</a>] -         OptimisticLockEx due to rounding of a Timestamp (either by OJ, or the DB)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2478'>OPENJPA-2478</a>] -         Erroneous message from the enhancer when a Mapped Superclass contains an @Id.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2482'>OPENJPA-2482</a>] -         java.sql.SQLException when processing a query result
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2494'>OPENJPA-2494</a>] -         A default Schema defined in a PU default (&lt;persistence-unit-defaults&gt;) in an orm.xml file is not being honored.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2502'>OPENJPA-2502</a>] -         NPE in QueryKey.createKey using criteria with QueryCache enabled
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2505'>OPENJPA-2505</a>] -         OpenJPA PersistenceException: LongId cannot be cast to MyEntityClass… @OneToMany in combination with FetchType.EAGER
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2506'>OPENJPA-2506</a>] -         StoreCache interface doesn&#39;t work for many ID types
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2507'>OPENJPA-2507</a>] -         Weird EmptyStackException in CriteriaQueryImpl
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2508'>OPENJPA-2508</a>] -         LEFT JOIN FETCH not honored when data cache is enabled
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2515'>OPENJPA-2515</a>] -         Fix 2.3.x binary downloads
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2525'>OPENJPA-2525</a>] -         Use of JoinColumn(.. referencedColumnName= ..) targets to another joinColumn key exposed as an attribute will cause a ConstrainViolation exception on persist
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2533'>OPENJPA-2533</a>] -         Table name defined in XML mapping file is not used when executing a named query.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2534'>OPENJPA-2534</a>] -         A boolean is not converted correct when using the hint &#39;UseLiteralInSQL&#39;.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2536'>OPENJPA-2536</a>] -         FetchGroup is not returning lazy fields.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2542'>OPENJPA-2542</a>] -         Using custom openjpa.BrokerFactory not working in OSGi due to ClassLoader
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2547'>OPENJPA-2547</a>] -         When two threads attempt to get a Pessimistic Lock, one thread gets a &#39;false&#39; lock.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2551'>OPENJPA-2551</a>] -         Standard SQL boolean mapping impossible
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2557'>OPENJPA-2557</a>] -         FinderCache contains incorrectly cached query with a NULL for a Primary Key.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2571'>OPENJPA-2571</a>] -         Criteria Builder query generates extra alias when using multiselect.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2573'>OPENJPA-2573</a>] -         org.apache.openjpa.persistence.InvalidStateException: Attempt to set column &quot;X to two different values... on trunk/2.4.0
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2576'>OPENJPA-2576</a>] -         fix broken JavaDoc
</li>
</ul>

<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2386'>OPENJPA-2386</a>] -         Support for JAVA 8
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2389'>OPENJPA-2389</a>] -         For entity fields missing @Transient annotations, let us know the classes they are in.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2449'>OPENJPA-2449</a>] -         refresh(PESSIMISTIC_WRITE) generates seperate SQL for the lock
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2450'>OPENJPA-2450</a>] -         Option to disable execution of ALTER SEQUENCE...INCREMENT BY statement for sequences.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2453'>OPENJPA-2453</a>] -         Add support to retain milliseconds of &#39;un-rounded&#39; Date field.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2466'>OPENJPA-2466</a>] -         Modify ReverseMappingTool to write generated classes to a map
</li>
</ul>

<h2>        New Feature
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2511'>OPENJPA-2511</a>] -         provide a minimal shade
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2558'>OPENJPA-2558</a>] -         Implement a way to select the db representation of Boolean values
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2570'>OPENJPA-2570</a>] -         Allow an Informix user the option to disable the &#39;RETAINUPDATELOCKS&#39; SQL.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2575'>OPENJPA-2575</a>] -         wrong context class loader in org.apache.openjpa.enhance.PCClassFileTransformer#transform0
</li>
</ul>

<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2200'>OPENJPA-2200</a>] -         cleanup sources: remove unused imports, remove tabs, etc
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2487'>OPENJPA-2487</a>] -         upgrade openjpa to asm5 to support java 8
</li>
</ul>
