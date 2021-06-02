Title: JPA 2.1 Tasks


<a name="Task List"></a>

## OpenJPA 2.1 Tasks

 <table class="note"><tr>
  <td valign="top"> <IMG src="images/warning.gif" width="16" height="16" border="0">
  <td>Under Construction...  This is just an initial cut...  We will need these tasks further broken down into
manageable two week iteration chunks of work...  And, I have probably forgotten some new features or minor update...  We will also need to create corresponding JIRAs to get the 
code integrated...
<br><br>But, this will give us an idea of the amount of work ahead of us...  	
 </tr></table>

<a name="JPA2.1Tasks-GeneralTasks"></a>

### General (Preliminary) Tasks

<table>
<tr><th> Status </th><th> JIRA </th><th> Summary </th></tr>
<tr><td class="border"> <font color="red">Done</font> </td><td class="border"> Not Needed
 </td><td class="border"> Need to cut an OpenJPA 2.3.0 release and associated service stream</td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Upgrade to <a href="https://wikis.oracle.com/display/GlassFish/Java+EE+7+Maven+Coordinates">JPA 2.1 interfaces</a> in trunk</td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Evaluate <a href="https://svn.apache.org/repos/asf/openjpa/sandboxes/21">Pinaki's 2.1 sandbox</a> and merge with trunk (post 2.3.0 release)</td></tr>
<tr><td class="border"> <font color="red">Done</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-2459">OPENJPA-2459</a>
 </td><td class="border"> Upgrade trunk to Java 7 for build and test</td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Prep for JPA 2.1 TCK <a href="http://openjpa.apache.org/running-the-sun-tck-for-jpa.html">(Existing JPA 2.0 TCK instructions)</a> </td></tr>

<!--
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1103">OPENJPA-1103</a>
 </td><td class="border"> Remove early-access disclaimer from the NOTICE files once the spec is
released </td></tr>
-->
</table>

<a name="JPA2.1Tasks-JPA2.1SpecFeatures"></a>

### JPA 2.1 Spec Features

<table>
<tr><th> Status </th><th> JIRA(s) </th><th> Effort </th><th> Summary </th><th> Area </th><th> JPA 2.1 Spec
Reference(s) </th></tr>
  
  
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> Add ON condition to JPQL query.  
<br><br>Will require BNF change (see jpql.jjt). Can ripple across the codebase. </td><td class="border"> JPQL </td><td class="border">
4.4.5.2, 4.14 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> Downcast relation paths with TREAT operator in JPQL queries.  Will require BNF change. The BNF changes will be non-trivial as TREAT can appear as a path component e.g. p.TREAT(p.items as Book).pageCount.  
<br><br>JPQLEpressionBuilder will require change to process the treated path. The downstream changes on building the appropriate expression will not be a heavy task as the current kernel expressions support the notion of implicit types.
 </td><td class="border"> JPQL </td><td class="border">
4.4, 4.4.4.1, 4.4.5, 4.4.9, 4.6.16, 4.14 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Low </td><td class="border"> Use database function or user-defined function with FUNCTION operator in JPQL queries The support for this feature exists. The task is mainly to parse (JPQLEpressionBuilder) and connect to the appropriate kernel expression.
 </td><td class="border"> JPQL </td><td class="border">
4.6.17.3, 4.14 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Low </td><td class="border"> Object construction in mapping results from native SQL query The support for this feature exists in ResultShape object. 
 </td><td class="border"> Query </td><td class="border">
3.10.16.2.2, 3.10.16.3, 12.3 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Add ON condition to Criteria Query The on() function is to be added to each derivation of Join separately because of generic signature of the method.
 </td><td class="border"> Criteria </td><td class="border">
4.4.5.2, 6.3.17, 6.3.20, 6.3.21, 6.3.22, 6.3.23, 6.5.3 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Add TREAT operator in Criteria query Each derivation of Path interface will require a downcast construct e.g. a class like PathImpl$Treated because the return type of the classes that implement path has generic type signature in OpenJPA implementation. A downcast (or treated) path must have a different generic signature for compile-time type checking.
 </td><td class="border"> Criteria </td><td class="border">
6.3.1, 6.5.7 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Delete via Criteria query. The design challenge for this task is to reuse the existing code for query portion of existing implementation.
 </td><td class="border"> Criteria </td><td class="border">
6.3.1, 6.3.6, 6.5.15 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Update via Criteria query. Same comment as the above task. The good news is that the refactoring has been done.
 </td><td class="border"> Criteria </td><td class="border">
6.3.1, 6.3.5, 6.5.15 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Very High </td><td class="border"> Invoke Stored Procedure. The basic support for CallableStatement exists in OpenJPA. However, this feature is going to impact several aspects of current query execution model. A stored procedure can result into multiple types of result sets while the current execution model assumes that a query returns a single type of result. It is unclear at this point how best to handle such multiplicity. Also parameter processing (always a rather weak/heuristic aspect of OpenJPA) requires extension. 
 </td><td class="border"> Query </td><td class="border">
3.1.1, 3.10.17, 10.4.3, 10.4.4, 12.2, 12.2.2.9, 12.2.3.20, 12.3 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Low </td><td class="border"> Bulk update of the members of an embeddable collection.
 </td><td class="border"> Query </td><td class="border">
3.10.16.1 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Context Dependency Injection via Entity Listeners
 </td><td class="border"> Listeners </td><td class="border">
3.5.1, 9.1 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Create EntityManager with SynchronizationType.UNSYNCHRONIZED. Unsynchorized context requires to be explicitly joined to a JTA transaction, as opposed to SYNCHRONIZED contexts that are automatically joined to a JTA transaction if available.
<br><br>If an unsynchronized context is not joined to a transaction, queries with pessimistic locks, bulk update or delete queries will throw the TransactionRequiredException.
<br><br>The context propgation rules differ and certain restrictions apply when the context is unsynchronized.
<br><br>A new method of EntityManager affirms if a context has joined a transaction.
<br><br>It is recommended that a non-JTA datasource be specified for use by the persistence provider for a persistence context of type SynchronizationType.UNSYNCHRONIZED that has not been joined to a JTA transaction in order to alleviate the risk of integrating uncommitted changes into the persistence context in the event that the transaction is later rolled back.
<br><br>Container implications as well...
 </td><td class="border"> Transactions </td><td class="border">
3.3, 3.3.1, 7.2.1, 7.4, 7.6.1, 7.6.2, 7.6.3, 7.6.4.1 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> Type conversion of basic attributes. The basic support for conversion exists as Externalizer. But the new conversion facility covers a wider type of properties that can be externalized. Also specification to convert the data type can be attached to the class definition. Such a feature is not available in OpenJPA.
 </td><td class="border"> EM </td><td class="border">
3.8 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Medium </td><td class="border"> Conversion facility.
<br><br>Parsing @Converter annotation or XML descriptor.
<br><br>Type conversion of embeddable attributes.
<br><br>Type conversion of collection members.
<br><br>Type conversion of key/value of Map type persistent property.
<br><br>Accept converter specification at a class level declaration.
 </td><td class="border"> EM </td><td class="border">
11.1.10, 11.1.11, 12.3 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> Low </td><td class="border"> Support adding named query via EntityManagerFactory.addNamedQuery() method
 </td><td class="border"> EMF </td><td class="border">
3.10.14, 7.4 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> Entity Graph for query and find operations. Though OpenJPA has extensive support for fetch plans, the EntityGraph specification uses a rather different (and perhaps incomplete) way to define these subgraphs. It will be some work to translate the specification's way of defining these subgraphs to equivalent OpenJPA constructs.
<br><br>The path navigation includes key field of a Map-type attribute. No equivalent exists in OpenJPA.
<br><br>javax.persistence.loadgraph is similar to named fetch group concept. 
 </td><td class="border"> Query </td><td class="border">
3.1.1, 3.2.7, 3.7, 7.4, 10.3, 12.2.3.17, 12.3 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> Support Schema Generation via Persistence bootstrap. Schema can be generated at startup both JSE and JEE environment. The schema can be generated both from entity mapping metadata and/or DDL scripts. A new set of properties javax.persistence.schema-generation.* can be passed via the Map argument while creating EntityManagerFactory.
<br><br>The support exists in OpenJPA, but not as extensive as per the specification. Moreover the specified javax.persistence.schema-generation.* actions are to be mapped to the existing SchemaTool features.
 </td><td class="border"> Tools </td><td class="border">
8.2.1, 8.2.1.19, 9.2.1, 9.4, 9.4.1, 9.5.1, 9.7, 11.1.6, 11.1.19, 11.1.20, 11.1.23, 11.1.26, 11.2 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> New mapping annotations @Index, @ForeignKey are supported. Synonymous annotations are defined in OpenJPA.
 </td><td class="border"> Query </td><td class="border">
2.13, 11.1.2, 11.1.8, 11.1.19, 11.1.23, 11.1.25, 11.1.26, 11.1.27, 11.1.35, 11.1.36, 11.1.44, 11.1.45, 11.2, 11.2.4 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> The version of persistence.xml is upgraded to 2.1. OpenJPA selects many default configurations based on the version of persistence.xml. These decisions points are to be checked for the new version.
 </td><td class="border"> Parser </td><td class="border">
8.3, 12.3 </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-????">OPENJPA-????</a>
 </td><td class="border"> High </td><td class="border"> Unwrap Cache, EntityManager etc. The EntityManager in the container had a derivation that supported unwrapping. That derivation may now be integrated with OpenJPA implementation. 
 </td><td class="border"> EM </td><td class="border">
3.1.1, 7.9.1, 7.10 </td></tr>

</table>