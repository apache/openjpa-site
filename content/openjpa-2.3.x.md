Title: OpenJPA 2.3.0


<a name="OpenJPA-2.3.0-OpenJPA-2.3.0"></a>

# OpenJPA 2.3.0

The Apache OpenJPA community is proud to announce the release of Apache
OpenJPA 2.3.0.
This distribution is based on the final [JSR 317 Java Persistence API,
Version 2.0](http://jcp.org/en/jsr/detail?id=317) specification and
passes the JPA 2.0 TCK, while remaining backwards
compatible with the prior 1.2.x releases based on the Java Persistence API
(JPA 1.0) part of Java Community Process JSR-220 (Enterprise JavaBeans
3.0).

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org)
.
<a name="OpenJPA2.3.0-ChangesinOpenJPA2.3.0"></a>

# Changes in OpenJPA 2.3.0

<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2168'>OPENJPA-2168</a>] -         Do not go through LifeCycleEventManager overhead if the Entity has declared to be excluded
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2481'>OPENJPA-2481</a>] -         Do release of JIRA&#39;s 2.3.0 version
</li>
</ul>

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-696'>OPENJPA-696</a>] -         Cache TransactionSynchronizationRegistry per EMF (vs JVM)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1794'>OPENJPA-1794</a>] -         Result of aggregate function MAX is 0 on empty table (instead of NULL).
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1819'>OPENJPA-1819</a>] -         ORDER BY will append additional column to the SELECT clause which may potentialy cause ORA-00979 error
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1901'>OPENJPA-1901</a>] -         QueryCacheStoreQuery$CachedObjectId that is not Serializable
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1979'>OPENJPA-1979</a>] -         Regression for non-standard joins with constant column values
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1993'>OPENJPA-1993</a>] -         Deadlock Potential with ORM XML Processing
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2018'>OPENJPA-2018</a>] -         Cannot bind String[] to ParameterExpression for path.in(parameter)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2067'>OPENJPA-2067</a>] -         A &#39;length&#39; of &#39;-1&#39; passed to PreparedStatement.setBinaryStream can cause an exception on some, but not all, JDBC drivers.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2072'>OPENJPA-2072</a>] -         InvalidStateException deleting an instance with a timestamp in its primary key
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2094'>OPENJPA-2094</a>] -         Metadata processing needs to support jar:file URLs that address Jar directories
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2095'>OPENJPA-2095</a>] -         Unhandled exception thrown from within an Externalizer method causes incorrect/incomplete SQL to be generated/executed.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2102'>OPENJPA-2102</a>] -         URLs which contains spaces are not properly handled by OpenJPA.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2110'>OPENJPA-2110</a>] -         Abstract entity causes standard openjpa collection proxies to be injected even if custom collections are used.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2118'>OPENJPA-2118</a>] -         Prepared SQL query does not handle collection-valued parameter where collection is empty
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2123'>OPENJPA-2123</a>] -         Minor performance improvements for Connection and ResultSet processing
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2131'>OPENJPA-2131</a>] -         Missing IN or OUT parameter exception with OracleDictionary
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2132'>OPENJPA-2132</a>] -         Traversal of a OneToMany relationship returns an empty list when InheritanceType.JOINED or SINGLE_TABLE is used.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2133'>OPENJPA-2133</a>] -         OpenJPA doesn&#39;t find custom mappings with an applicable class loader
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2136'>OPENJPA-2136</a>] -         NPE when using LiteAutoDetach
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2140'>OPENJPA-2140</a>] -         Locking tests issue many warnings about the use of a duplicate pu name
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2142'>OPENJPA-2142</a>] -         Merge of a new object does not handle Entity Id field
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2145'>OPENJPA-2145</a>] -         Missing ASM depending jar in binary zip
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2146'>OPENJPA-2146</a>] -         StateManager for Embeddable may throw Exception while initializing
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2149'>OPENJPA-2149</a>] -         Criteria.function adds wrong casts to parameters making it unsuable
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2153'>OPENJPA-2153</a>] -         NoSuchMethodException of DBCPDriverDataSource.newInstance()
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2154'>OPENJPA-2154</a>] -         test-dynamic-enhancer profile failed for module more than one level deep
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2156'>OPENJPA-2156</a>] -         Fix bug in org.apache.openjpa.persistence.util.SourceCode to correctly generate imports.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2158'>OPENJPA-2158</a>] -         LiteAutoDetach + DetachProxyFields=false can lead to Broker concurrency exceptions
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2161'>OPENJPA-2161</a>] -         Make some members of StateManagerImpl protected to allow for greater extensability
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2163'>OPENJPA-2163</a>] -         Lifecycle event callback occurs more often than expect
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2170'>OPENJPA-2170</a>] -         Multiple INSERT of the same row in batch update manager
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2172'>OPENJPA-2172</a>] -         openjpa-all jar is missing slf4j runtime dependency
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2174'>OPENJPA-2174</a>] -         Result set mapping was not looked up when retrieving column data from a NamedNativeQuery
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2178'>OPENJPA-2178</a>] -         PostgresDictionary
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2180'>OPENJPA-2180</a>] -         OpenJPA build broken in java7 / jdk-1.7
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2187'>OPENJPA-2187</a>] -         metamodel generation with default package creates invalid class
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2191'>OPENJPA-2191</a>] -         QueryCache don&#39;t allow for misconfigurations
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2196'>OPENJPA-2196</a>] -         Create Sequence Postgres 9.1
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2197'>OPENJPA-2197</a>] -         MethodComparator in AnnotationPersistenceMetaDataParser should also compare parameters
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2199'>OPENJPA-2199</a>] -         Constraint violation exception when removing relationship using (orphanRemoval = true)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2204'>OPENJPA-2204</a>] -         NPE in JDBCStoreManager with Trace turned on
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2221'>OPENJPA-2221</a>] -         Use of AbstractValueHandler map() causes exception on find()
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2227'>OPENJPA-2227</a>] -         OpenJPA doesn&#39;t find custom SequenceGenerators
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2228'>OPENJPA-2228</a>] -         QuerySQLCache broken for Entities with @EmbeddedId
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2229'>OPENJPA-2229</a>] -         Persistence entities not recognized when deploying on JBoss AS 7.1
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2230'>OPENJPA-2230</a>] -         Event Listener detection didn&#39;t work with MappedSuperClasses or Entity heirarchies
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2234'>OPENJPA-2234</a>] -         EntityManager instance creation needs TX activity
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2235'>OPENJPA-2235</a>] -         &quot;READ_UNCOMMITTED&quot; setting for the fetch plan isolation level is ignored in DB2Dictionary
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2236'>OPENJPA-2236</a>] -         Trace of connection info can cause class transform/enhancement to fail
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2238'>OPENJPA-2238</a>] -         IllegalAccessError when trying to proxy a default scoped Class
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2240'>OPENJPA-2240</a>] -         JVMVRFY012 when using openjpa together with hyperjaxb3
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2244'>OPENJPA-2244</a>] -         Nested classpath ignored in mapping tool ant task
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2245'>OPENJPA-2245</a>] -         NotSerializableException when using a remote QueryCache and the Criteria API
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2247'>OPENJPA-2247</a>] -         JoinColumn annotation is ignored when mapping a unidirectional owned OneToOne that is in a SecondaryTable
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2253'>OPENJPA-2253</a>] -         Memory leak in Audit feature
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2255'>OPENJPA-2255</a>] -         Couldn&#39;t load the referencedColumn definition when create the JoinTable
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2257'>OPENJPA-2257</a>] -         Concurreny in org.apache.openjpa.persistence.EntityManagerImpl.getProperties leads to NullPointer and ConcurrentModificationException
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2260'>OPENJPA-2260</a>] -         Parenthesis-augmented parameters are improperly processed at EM level
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2261'>OPENJPA-2261</a>] -         Query SQL Cache issue with NULL parameters
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2267'>OPENJPA-2267</a>] -         native query select with null result causes NullPointerException
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2269'>OPENJPA-2269</a>] -         Duplicate key exception in sequence table on multithreaded initialization
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2271'>OPENJPA-2271</a>] -         Old &lt;ciManagement/&gt; info on root POM
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2282'>OPENJPA-2282</a>] -         ESCAPE &#39;\&#39; is appended to the like clause unexpectedly
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2284'>OPENJPA-2284</a>] -         NPE occurs when &lt;cascade-persist/&gt; is added to a &lt;persistence-unit-defaults&gt; in an orm.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2288'>OPENJPA-2288</a>] -         MetaDataRepository should be able to filter classes from other app ClassLoaders in JEE Env
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2289'>OPENJPA-2289</a>] -         Additional SQL alias generated for query with subquery causes incorrect # of rows returned - Oracle only
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2298'>OPENJPA-2298</a>] -         VerifyError/Stack underflow due to extra &#39;return&#39; statements generated by PCEnhancer.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2304'>OPENJPA-2304</a>] -         Thread deadlock in CriteriaBuilder
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2305'>OPENJPA-2305</a>] -         Canonical MetaModel class generation should not use inhertence
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2318'>OPENJPA-2318</a>] -         Left outer join is not generated when specifien using Criteria API
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2320'>OPENJPA-2320</a>] -         CriteriaBuilder predicate construction deadlocks in multi-core VM due to static initializer
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2321'>OPENJPA-2321</a>] -         Synchronizing logging output stream causes deadlock when used some JDK LogManger derivative
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2325'>OPENJPA-2325</a>] -         MappedSuperClass without an @Id causes wrong identity type for the inherited types
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2326'>OPENJPA-2326</a>] -         Updates in TCK execution configuration
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2328'>OPENJPA-2328</a>] -         NPE caused by one too many calls on the iterator inside the library.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2330'>OPENJPA-2330</a>] -         Stackoverflow due to endless recursive calls
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2334'>OPENJPA-2334</a>] -         OpenJPA must support processing puRoot &amp; jar-file URLs as jar-formatted InputStreams
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2335'>OPENJPA-2335</a>] -         Constrained foreign key column value setting needs to be flexible
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2336'>OPENJPA-2336</a>] -         Relax Join column name comparison based on database dictionary schema case setting
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2343'>OPENJPA-2343</a>] -         Version field returns null when explicity projected from a JOIN in SELECT clause
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2355'>OPENJPA-2355</a>] -         CONCAT() function must support more than two arguments
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2357'>OPENJPA-2357</a>] -         @..ToMany(optional=false) throws InvalidStateException: [...] the metadata for this field specifies that nulls are illegal.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2369'>OPENJPA-2369</a>] -         duplicate call to getUnloadedInternal function
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2374'>OPENJPA-2374</a>] -         Avoid OID creation in BrokerImpl.isDetached when lookup is not required.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2377'>OPENJPA-2377</a>] -         Metamodel.managedType returns wrong result for Embeddable
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2378'>OPENJPA-2378</a>] -         TestHandlerStrategy.testIssue_OPENJPA2328 failed with Oracle
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2384'>OPENJPA-2384</a>] -         Rendering criteria query to JPQL-like string ignores multiple GROUP BY clauses
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2390'>OPENJPA-2390</a>] -         HSQLDB SELECT NEXT VALUE FOR Sequence will skip 1 sequence value if allocation size is 1
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2391'>OPENJPA-2391</a>] -         HSQLDB v2.2.9
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2400'>OPENJPA-2400</a>] -         Support MariaDB
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2405'>OPENJPA-2405</a>] -         EntityManager.merge does not work for entity that is managed by another EntityManager
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2409'>OPENJPA-2409</a>] -         allow the openjpa-maven-plugin to use a persistence.xml from resources and not only from files
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2414'>OPENJPA-2414</a>] -         FinderCache does not consider active Fetch Groups/FetchPlan added Fields
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2418'>OPENJPA-2418</a>] -         Cannot build 2.2.x due to NullPointerException in maven-checkstyle-plugin
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2421'>OPENJPA-2421</a>] -         Slices: Can&#39;t setting up FinderTargetPolicy
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2423'>OPENJPA-2423</a>] -         Isolation level is not working properly on DB2 for JPQL queries with nested sub-queries.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2425'>OPENJPA-2425</a>] -         SELECT fields with @ExternalValues defined returns datastore values instead of unmapped fields
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2432'>OPENJPA-2432</a>] -         MySQL dictionary can&#39;t be found from a valid connection
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2435'>OPENJPA-2435</a>] -         Version field in a projection always returned as an Integer.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2437'>OPENJPA-2437</a>] -         transactional listeners added too late to observe begin event
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2440'>OPENJPA-2440</a>] -         foreign key drop leaks jdbc connections
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2443'>OPENJPA-2443</a>] -         InvalidStateException while merging a new Entity with a GeneratedValue id
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2444'>OPENJPA-2444</a>] -         ReverseMappingTool creates orm.xml files in the current working directory
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2480'>OPENJPA-2480</a>] -         Update the website with 2.3.0 release information
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2585'>OPENJPA-2585</a>] -         Update the website with 2.4.0 release information
</li>
</ul>

<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2120'>OPENJPA-2120</a>] -         Add new option to eliminate reflection calls from enhancer generated IdClass PC copy operations
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2134'>OPENJPA-2134</a>] -         Do not close Connections when ConnectionRetainMode is set to &quot;always&quot;
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2137'>OPENJPA-2137</a>] -         Make some members of StateManagerImpl protected to allow for greater extensibility
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2143'>OPENJPA-2143</a>] -         Reduce lock contention on LifecycleEventManager
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2151'>OPENJPA-2151</a>] -         Improve the performance of StateManagerImpl.initialize
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2152'>OPENJPA-2152</a>] -         Don&#39;t process query hints when LockModeType == NONE
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2159'>OPENJPA-2159</a>] -         Add support for no rounding of Date
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2162'>OPENJPA-2162</a>] -         Avoid delimited identifier processing if it&#39;s not required by application
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2164'>OPENJPA-2164</a>] -         Don&#39;t setPCState if field requested is already loaded
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2167'>OPENJPA-2167</a>] -         Misc changes to improve flush() path performance
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2171'>OPENJPA-2171</a>] -         asm should be optional
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2189'>OPENJPA-2189</a>] -         Update OpenBooks example to build, install, and execute in the WAS Liberty Profile
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2208'>OPENJPA-2208</a>] -         Add additional Java 2 Security doPriv function
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2209'>OPENJPA-2209</a>] -         MetaDataRepository preload configuration should be more inclusive
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2220'>OPENJPA-2220</a>] -         Persistent field fetching statistic tool
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2231'>OPENJPA-2231</a>] -         jest  TokenReplacedStream use Reader instead of Inputstream
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2264'>OPENJPA-2264</a>] -         Upcast PreparedStatementManagerImpl.logSQLWarnings to take a Statement rather than a PreparedStatement
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2275'>OPENJPA-2275</a>] -         Extending SchemaTool
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2292'>OPENJPA-2292</a>] -         Reduce object allocations
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2293'>OPENJPA-2293</a>] -         Reduce LifecycleEventManager
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2324'>OPENJPA-2324</a>] -         Option to express literal in query string directly into generate SQL
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2332'>OPENJPA-2332</a>] -         Update message when unable to resolve datasource configuration
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2342'>OPENJPA-2342</a>] -         Consider modifying PCEnhancer.run to use serp.bytecode.BCClass.getDeclaredInterfaceNames instead of getDeclaredInterfaceTypes.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2346'>OPENJPA-2346</a>] -         Optimize MetaDataRepository.getMetaDataInternal
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2347'>OPENJPA-2347</a>] -         Make StateManagerImpl more extensible
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2348'>OPENJPA-2348</a>] -         Cache calculated hashCode in OpenJPAId
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2353'>OPENJPA-2353</a>] -         Reduce object allocations
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2354'>OPENJPA-2354</a>] -         Removed synchronized from enhancer added pcReplaceStateManager method
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2368'>OPENJPA-2368</a>] -         Move www.apache.org/openjpa/ns/orm to openjpa.apache.org/ns/orm
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2410'>OPENJPA-2410</a>] -         Build time detection of System.out/err.print(ln) in source files
</li>
</ul>

<h2>        New Feature
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2283'>OPENJPA-2283</a>] -         Upgrade to ASM 4 dependency
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2295'>OPENJPA-2295</a>] -         speed up query metadata lookup
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2366'>OPENJPA-2366</a>] -         provide option to exclude schema name from generated @Table annotation for generated entities
</li>
</ul>

<h2>        Question
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1532'>OPENJPA-1532</a>] -         Should the &lt;shared-cache-mode&gt; element in a persistence unit definition automatically turn on the data cache?
</li>
</ul>

<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2388'>OPENJPA-2388</a>] -         support new xbean asm4 shade
</li>
</ul>

<h2>        Test
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2169'>OPENJPA-2169</a>] -         TestOracleXmlColumn test failed using Oracle 11.2 driver
</li>
</ul>


