Title: OpenJPA 3.0.x


<a name="OpenJPA-3.0.0"></a>

# OpenJPA 3.0.x

The Apache OpenJPA community is currently working on Apache OpenJPA 3.0.0.

This distribution is based on the final [JSR 338 Java Persistence API,
Version 2.2](http://jcp.org/en/jsr/detail?id=338) specification.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org).

<a name="OpenJPA-2.4.3"></a>

# Changes in OpenJPA 3.0.0


<h2>        Sub-task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2663'>OPENJPA-2663</a>] -         cleanup ConcreteClassGenerator and move to ASM
</li>
</ul>
        
<h2>        Bug
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2300'>OPENJPA-2300</a>] -         AnnotationProcessor shows warnings when executed on Java 7 sources
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2646'>OPENJPA-2646</a>] -         Sporadic NullPointerException occurs under heavy load when QuerySQLCache is enabled.
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2658'>OPENJPA-2658</a>] -         TestQueryTimeout test is broken
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
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2592'>OPENJPA-2592</a>] -         JPA 2.1 stored procedure support
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2598'>OPENJPA-2598</a>] -         Support SQL server Offset Fetch syntax for pagination
</li>
</ul>
        
<h2>        Improvement
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2660'>OPENJPA-2660</a>] -         Resolve Maven warnings
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2669'>OPENJPA-2669</a>] -         Add apache karaf feature for openjpa and adapt OSGi imports
</li>
</ul>
            
<h2>        Task
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2641'>OPENJPA-2641</a>] -         update build pom
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2652'>OPENJPA-2652</a>] -         Prepare SVN for OpenJPA-3.0 development
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2653'>OPENJPA-2653</a>] -         Upgrade documentation page for 3.0.0 work
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2654'>OPENJPA-2654</a>] -         merge over the work done in branches/openjpa_jpa-2.1/ to trunk
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2655'>OPENJPA-2655</a>] -         verify signature of geronimo-jpa-2.1-spec with the RI jars
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2659'>OPENJPA-2659</a>] -         upgrade to apache-parent-18
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2664'>OPENJPA-2664</a>] -         migrate from commons-lang to commons-lang3
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2666'>OPENJPA-2666</a>] -         Fix Java9 compatibility
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2667'>OPENJPA-2667</a>] -         Upgrade BVAL to 1.1
</li>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2677'>OPENJPA-2677</a>] -         upgrade to BVAL-1.1.2
</li>
</ul>
                                                        
<h2>        Dependency upgrade
</h2>
<ul>
<li>[<a href='https://issues.apache.org/jira/browse/OPENJPA-2730'>OPENJPA-2730</a>] -         Update to XBean Asm 6 Shaded 4.8
</li>
</ul>