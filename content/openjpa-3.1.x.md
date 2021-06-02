Title: OpenJPA 3.1.X

# OpenJPA 3.1.x

The Apache OpenJPA community is currently mainly working on Apache OpenJPA 3.1.x.

This distribution is based on the final [JSR 338 Java Persistence API, Version 2.2](http://jcp.org/en/jsr/detail?id=338) specification.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org).

# Changes in OpenJPA 3.1.2


<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2807'>OPENJPA-2807</a>] -         javax.persistence.Index#columnList should strip spaces
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2810'>OPENJPA-2810</a>] -         Major version is returned instead of minor
</li>
</ul>

<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2790'>OPENJPA-2790</a>] -         Convert build from SVN to GIT
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2798'>OPENJPA-2798</a>] -         OpenJPA need to be more Java11 friendly
</li>
</ul>

<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2809'>OPENJPA-2809</a>] -         Add openjpa-junit5 helper to enhance entities at test run
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2811'>OPENJPA-2811</a>] -         Upgrade to ASM 8
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2812'>OPENJPA-2812</a>] -         Enable to force snake_case for column names
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2813'>OPENJPA-2813</a>] -         Implement basic support of PersistenceProvidergenerateSchema
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2815'>OPENJPA-2815</a>] -         Basic jakarta bundle
</li>
</ul>


# Changes in OpenJPA 3.1.1


<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2713'>OPENJPA-2713</a>] -         [JPA-2.2] add support for Java8 Date/Time types
</li>
</ul>

<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2743'>OPENJPA-2743</a>] -         AttributeConverter fails to enhance
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2799'>OPENJPA-2799</a>] -         Karaf features contains mistake on the commons-collections4 location
</li>
</ul>

<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2801'>OPENJPA-2801</a>] -         Kubernetes TCPRemoteCommitProvider
</li>
</ul>

<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2803'>OPENJPA-2803</a>] -         DBCP2 should be optional in OSGi
</li>
</ul>

# Changes in OpenJPA 3.1.0


<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2710'>OPENJPA-2710</a>] -         Create and update to geronimo-jpa_2.2_spec
</li>
</ul>
        
<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-1993'>OPENJPA-1993</a>] -         Deadlock Potential with ORM XML Processing
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2555'>OPENJPA-2555</a>] -         Timestamp precision from manual schema not respected
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2567'>OPENJPA-2567</a>] -         TINY/MEDIUM/LONG TEXT fields for MySQL and MariaDB are not supported
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2673'>OPENJPA-2673</a>] -         Table is not created in openjpa 3.0.0-SNAPSHOT and OSGi
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2704'>OPENJPA-2704</a>] -         The openjpa.jdbc.Schema no longer overrides orm.xml default
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2733'>OPENJPA-2733</a>] -         Subquery parameters are incorrectly assigned
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2742'>OPENJPA-2742</a>] -         SchemaTool fails with MySQL
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2746'>OPENJPA-2746</a>] -         OpenJPA Karaf feature is not complete
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2756'>OPENJPA-2756</a>] -         PostgreSQL requires escaping of search strings in all versions
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2757'>OPENJPA-2757</a>] -         upgrade to xbean-asm7 to support Java11
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2761'>OPENJPA-2761</a>] -         problem inserting more than 4000 charcters in oracle XMLTYPE column
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2764'>OPENJPA-2764</a>] -         Map path expression tests behave random
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2768'>OPENJPA-2768</a>] -         XMLStore SAXParser doesn&#39;t distinguish between element and extent
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2770'>OPENJPA-2770</a>] -         false boolean literal doesn&#39;t work
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2771'>OPENJPA-2771</a>] -         It seems like h2 &#39;unlimited&#39; is not &quot;LIMIT 0&quot; but rather &quot;LIMIT -1&quot;
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2772'>OPENJPA-2772</a>] -         list of h2 reserved words is incomplete
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2777'>OPENJPA-2777</a>] -         Indices specified using javax.persistence.Index annotation are not being created
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2780'>OPENJPA-2780</a>] -         ReverseMappingTool does not generate @Enumerated annotation
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2781'>OPENJPA-2781</a>] -         OpenJPA need internet connection to read the persistence.xml
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2785'>OPENJPA-2785</a>] -         Queries invoked by Spring data that have parameters fail
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2791'>OPENJPA-2791</a>] -         Parsing persistence.xml throws premature end of file error
</li>
</ul>
                
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2745'>OPENJPA-2745</a>] -         Clean up try-catch implementation for DB2Dictionary
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2747'>OPENJPA-2747</a>] -         Upgrade to JPA 2.2 and use javax.persistence-api spec
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2748'>OPENJPA-2748</a>] -         commons-collections should be updated to most recent version
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2750'>OPENJPA-2750</a>] -         commons-dbcp need to be updated to most recent version
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2751'>OPENJPA-2751</a>] -         Code clean-up should be performed
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2752'>OPENJPA-2752</a>] -         More libraries can be updated
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2753'>OPENJPA-2753</a>] -         Create profiles to start various databases via Docker
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2755'>OPENJPA-2755</a>] -         support MySQL DATETIME and TIMESTAMP fractions (milliseconds, nanos)
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2773'>OPENJPA-2773</a>] -         set minIdle to &gt; 0 in DBCPDriverDataSource
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2775'>OPENJPA-2775</a>] -         hsqldb doesn&#39;t support NullTable to retrieve meta information
</li>
</ul>
            
<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2744'>OPENJPA-2744</a>] -         commons-pool should be updated to most recent version
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2754'>OPENJPA-2754</a>] -         update to latest dbcp and verify moving from maxActive to maxTotal
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2758'>OPENJPA-2758</a>] -         JPA 2.2 compliance
</li>
</ul>
                                                        
<h2>        Dependency upgrade
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2784'>OPENJPA-2784</a>] -         update docs before our release
</li>
</ul>