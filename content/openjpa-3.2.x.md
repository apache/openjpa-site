Title: OpenJPA 3.2.X

# OpenJPA 3.2.x

This distribution is based on the final [JSR 338 Java Persistence API, Version 2.2](http://jcp.org/en/jsr/detail?id=338) specification.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org).

# Changes in OpenJPA 3.2.2

<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2713'>OPENJPA-2713</a>] -         [JPA-2.2] add support for Java8 Date/Time types
</li>
</ul>
                            
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2900'>OPENJPA-2900</a>] -         javax.xml.bind must be relocated to jakarta namespace
</li>
</ul>


# Changes in OpenJPA 3.2.1

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2614'>OPENJPA-2614</a>] -         First rollback after application start does not work under certain circumstances
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2876'>OPENJPA-2876</a>] -         running &#39;refresh&#39; schema action creates wrong SQL output
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2877'>OPENJPA-2877</a>] -         [JPA-2.1] implement AttributeConverter 
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2882'>OPENJPA-2882</a>] -         Exception passing javax.persistence.* String values to createEntityManager(Map)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2883'>OPENJPA-2883</a>] -         UseTriggersForAutoAssign in Oracle seems to be broken
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2889'>OPENJPA-2889</a>] -         commons-pool2 bundle version defined in karaf features repository is not aligned with the actual version used by openjpa
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2891'>OPENJPA-2891</a>] -         @Generated annotation cannot be disabled for static metamodel
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2896'>OPENJPA-2896</a>] -         Automatic module name is not set for bundles
</li>
</ul>
                
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2875'>OPENJPA-2875</a>] -         JPA Provider must filter out other JPA Providers
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2881'>OPENJPA-2881</a>] -         runtime exception in org.apache.openjpa.lib.meta.XMLMetaDataParser.parseNewResource
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2893'>OPENJPA-2893</a>] -         H2 2.x is not working with OpenJPA
</li>
</ul>
            
<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2884'>OPENJPA-2884</a>] -         javax.annotation.processing shouldn&#39;t be relocated in jakarta shade
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2885'>OPENJPA-2885</a>] -         Make openjpa-junit5 support jakarta namespace
</li>
</ul>


# Changes in OpenJPA 3.2.0

<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1594'>OPENJPA-1594</a>] -         Tests not handling new QueryTimeOut and LockTimeOut exceptions correctly
</li>
</ul>
            
<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1303'>OPENJPA-1303</a>] -         Reserved words are not mapped correctly in table definition
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2182'>OPENJPA-2182</a>] -         DB dictionaries do not properly process reserved words for column names
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2648'>OPENJPA-2648</a>] -         hsqldb @Id long create table as interger instead of bigint
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2731'>OPENJPA-2731</a>] -         Problems with Boolean Representation with Postgres
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2788'>OPENJPA-2788</a>] -         Anonymous parameters are not being picked when adding via CriteriaBuilder
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2789'>OPENJPA-2789</a>] -         JDBC connection not closed when running named query in explicitly opened connection
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2795'>OPENJPA-2795</a>] -         generate foreign key indexes for Oracle
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2821'>OPENJPA-2821</a>] -         Subclassing enhancer must use AsmAdapter
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2828'>OPENJPA-2828</a>] -         org.apache.openjpa.kernel.conf.Specification.equals() : returns true even if different
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2829'>OPENJPA-2829</a>] -         javax script execution does not ignore empty lines
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2830'>OPENJPA-2830</a>] -         javax.persistence.sql-load-script-source does not support &quot;;&quot; in strings
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2832'>OPENJPA-2832</a>] -         DROP COLUMN does not use delimiters and always add double quotes
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2834'>OPENJPA-2834</a>] -         Performance issue while deploying in Wildfly EAP with OpenJPA-3.1.1
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2842'>OPENJPA-2842</a>] -         openjpa.Log=log4j vs log4j2 - reintroduce log4j support and add explicit log4j2 support
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2843'>OPENJPA-2843</a>] -         try to get rid of com.ibm dependency
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2846'>OPENJPA-2846</a>] -         Enhancement does not work with JDK 16
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2849'>OPENJPA-2849</a>] -         select(max) etc of LocalDate, LocalDateTime etc leads to ClassCastException
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2850'>OPENJPA-2850</a>] -         [MSSQL] BLOB column type is not supported
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2851'>OPENJPA-2851</a>] -         argument CURRENT_DATE cannot handle java.time.LocalDateTime entity fields
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2854'>OPENJPA-2854</a>] -         fix OffsetTime handling for PostgreSQL
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2855'>OPENJPA-2855</a>] -         primary keys do no respect naming rules 
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2856'>OPENJPA-2856</a>] -         [MariaDB] improve TIME handling
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2857'>OPENJPA-2857</a>] -         [MariaDB] locking in some cases gets handled via sqlState 70100
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2858'>OPENJPA-2858</a>] -         update dbcp2 to 2.8.0
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2859'>OPENJPA-2859</a>] -         [HSQLDB] HSQLDictionary wrongly maps double to NUMERIC without precision
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2860'>OPENJPA-2860</a>] -         [Postgres] use setQueryTimeout for PostgreSQL &gt;= 10
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2861'>OPENJPA-2861</a>] -         select sum(CASE x WHEN x THEN 1 ELSE 0 ) returns String instead of Long.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2862'>OPENJPA-2862</a>] -         select SUM doesn&#39;t return spec defined types
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2863'>OPENJPA-2863</a>] -         java.time.LocalDateTime in Oracle gets rounded to just 3 digits
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2864'>OPENJPA-2864</a>] -         respect the Columns precision when persisting a java.sql.Timestamp value
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2865'>OPENJPA-2865</a>] -         [Oracle] use native java.time JDBC features
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2866'>OPENJPA-2866</a>] -         [Oracle] add GenerationType#IDENTITY support for Oracle
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2871'>OPENJPA-2871</a>] -         upgrade to xbean-4.20 to remove transitive ASM dependency
</li>
</ul>
            
<h2>        New Feature
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2816'>OPENJPA-2816</a>] -         Add HerdDB DBDictionary
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2873'>OPENJPA-2873</a>] -         Add ProductDerivation for persistence_2_2.xsd
</li>
</ul>
    
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-84'>OPENJPA-84</a>] -         Escape sql reserved words in column names
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2665'>OPENJPA-2665</a>] -         refactore code to use more Java7 features.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2765'>OPENJPA-2765</a>] -         Fix documentation of JPA spec compliance
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2820'>OPENJPA-2820</a>] -         Track when a DBIdentifier is already delimited in order to save memory allocations and cpu
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2822'>OPENJPA-2822</a>] -         enhancer can rely on at least java8
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2823'>OPENJPA-2823</a>] -         treat jakarta.* as spec class in enhancer
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2852'>OPENJPA-2852</a>] -         Maven Plugin should be marked thread safe
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2853'>OPENJPA-2853</a>] -         [MSSQL Server] support sendTimeAsDatetime handling
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2867'>OPENJPA-2867</a>] -         generate list of reserved Words via unit test
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2868'>OPENJPA-2868</a>] -         update reserved column names list for various of our DBDictionaries
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2870'>OPENJPA-2870</a>] -         update specification-version to 2.2
</li>
</ul>
            
<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2819'>OPENJPA-2819</a>] -         Add simple GitHub Actions validation for Pull Requests
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2824'>OPENJPA-2824</a>] -         When @OpenJPASupport (junit5 extension) is used, ensure to not do auto enhancement more than once
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2831'>OPENJPA-2831</a>] -         Import commons-collections4 classes instead of the dependency in openjpa-lib
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2833'>OPENJPA-2833</a>] -         Upgrade to ASM 9
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2835'>OPENJPA-2835</a>] -         update to xbean-asm9 for Java16 support
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2838'>OPENJPA-2838</a>] -         Add a JUL LogFactory
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2840'>OPENJPA-2840</a>] -         Enable a light SPI for asm support in kernel module
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2869'>OPENJPA-2869</a>] -         Specification-Version still in v2
</li>
</ul>
