Title: JPA 2.0 Tasks



<a name="Task List"></a>

## OpenJPA 2.0 Tasks

<a name="JPA2.0Tasks-JPA2.0SpecFeatures"></a>

### JPA 2.0 Spec Features

<table>
<tr><th> Status </th><th> JIRA(s) </th><th> Effort </th><th> Summary </th><th> Area </th><th> JPA 2.0 Spec
Reference(s) </th></tr>
  
  
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1358">OPENJPA-1358</a>
 </td><td class="border"> Low </td><td class="border"> Added find method that accepts properties (no lock mode) </td><td class="border"> EM </td><td class="border">
3.1.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1358">OPENJPA-1358</a>
 </td><td class="border"> Low </td><td class="border"> New refresh method that accepts properties (no lock mode) </td><td class="border"> EM </td><td class="border">
3.1.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1358">OPENJPA-1358</a>
 </td><td class="border"> Low </td><td class="border"> Verify cache mode properties support on find, refresh and Query </td><td class="border">
Cache </td><td class="border"> 3.7.2 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1306">OPENJPA-1306</a>
 </td><td class="border"> Medium </td><td class="border"> Added new javax.persistence.lock.scope property </td><td class="border"> Locking </td><td class="border">
3.4.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1253">OPENJPA-1253</a>
 </td><td class="border"> Medium </td><td class="border"> Review @JoinColumn elements for behavioral changes </td><td class="border"> Mapping </td><td class="border">
11.1.21 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1306">OPENJPA-1306</a>
 </td><td class="border"> Medium </td><td class="border"> Review clarifications to locking modes </td><td class="border"> Locking </td><td class="border"> 3.4.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> </td><td class="border"> Low </td><td class="border"> Review chapter on deployment and
bootstrapping contracts for updates. </td><td class="border"> General </td><td class="border"> Ch 9 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1270">OPENJPA-1270</a>
 </td><td class="border"> Low </td><td class="border"> Assert that relationships defined in a mapped superclass must be
unidirectional. </td><td class="border"> General </td><td class="border"> 2.11.2 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> Spec updated </td><td class="border"> TBD</td><td class="border"> New JPQL reserved
identifiers. </td><td class="border"> JPQL </td><td class="border"> 4.4.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1069">OPENJPA-1069</a>
 </td><td class="border"> Low </td><td class="border"> Review @OrderBy for behavioral changes </td><td class="border"> Mapping </td><td class="border"> 11.1.38 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1274">OPENJPA-1274</a>
 </td><td class="border"> Low </td><td class="border"> Test CascadeType.DETACH via orm.xml </td><td class="border"> Testing </td><td class="border"> 12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> Routine JPQL BNF update</td><td class="border"> Low </td><td class="border"> Updated
single_valued_path_expression definition </td><td class="border"> JPQL </td><td class="border"> 4.4.4 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> Routine JPQL BNF update </td><td class="border"> Low </td><td class="border"> New JPQL
reserved identifiers should not be used as result variables </td><td class="border"> JPQL </td><td class="border"> 4.4.1
</td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1272">OPENJPA-1272</a>
 </td><td class="border"> Low </td><td class="border"> attribute-override and association-override available from
element-collection XML schema type </td><td class="border"> Mapping </td><td class="border"> 12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1271">OPENJPA-1271</a>
 </td><td class="border"> Medium </td><td class="border"> Support for CacheRetrieveMode and CacheStoreMode properties. </td><td class="border">
Cache </td><td class="border"> 3.7.2 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1264">OPENJPA-1264</a>
 </td><td class="border"> Low </td><td class="border"> Cacheable attribute added to entity element in orm.xml </td><td class="border"> Cache </td><td class="border">
12.2.3.3, 12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1264">OPENJPA-1264</a>
 </td><td class="border"> Medium </td><td class="border"> Cacheable annotation </td><td class="border"> Cache </td><td class="border"> 3.7, 11.1.7 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1266">OPENJPA-1266</a>
</td><td class="border"> Low </td><td class="border"> Support for JDBC escape sequence for date/time literals (6/19 rev)
</td><td class="border"> JPQL </td><td class="border"> 4.6.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1240">OPENJPA-1240</a>
 </td><td class="border"> Low </td><td class="border"> Allow Lob, Temporal, Enumerated annotations to be applied to
element collections annotations and in XML. </td><td class="border"> Mapping </td><td class="border"> 11.1.16, 11.1.24,
11.1.47 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1264">OPENJPA-1264</a>
 </td><td class="border"> Low </td><td class="border"> Cache mode elements added to persistence.xml </td><td class="border"> Cache </td><td class="border"> 3.7.1,
3.7.2, 8.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1228">OPENJPA-1228</a>
</td><td class="border"> Low </td><td class="border"> Default value change of exclude-unlisted-classes element </td><td class="border"> General
</td><td class="border"> 8.2.1.6.1 (7/23) </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1251">OPENJPA-1251</a>
 </td><td class="border"> Low </td><td class="border"> EntityManagerFactory getProperties returns Map of <String, Object>
</td><td class="border"> EMF </td><td class="border"> 7.4 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1251">OPENJPA-1251</a>
 </td><td class="border"> Medium </td><td class="border"> Added setProperty method </td><td class="border"> EM </td><td class="border"> 3.1.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1013">OPENJPA-1013</a>
 </td><td class="border"> High </td><td class="border"> Build strictly-typed Criteria API </td><td class="border"> Criteria </td><td class="border"> Ch 6 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1014">OPENJPA-1014</a>
 </td><td class="border"> High </td><td class="border"> Build weakly-typed Criteria API </td><td class="border"> Criteria </td><td class="border"> Ch 6 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1180">OPENJPA-1180</a>
 </td><td class="border"> High </td><td class="border"> Added getParameters, getParameterValue, getParameter methods to
Query interface </td><td class="border"> Typed Parameters </td><td class="border"> 3.8.1, 3.8.5 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1009">OPENJPA-1009</a>
 </td><td class="border"> High </td><td class="border"> Populate canonical meta-model for strictly typed Criteria Query
building </td><td class="border"> Metamodel </td><td class="border"> Ch 5 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1010">OPENJPA-1010</a>
 </td><td class="border"> High </td><td class="border"> Instantiate meta-model classes for JPA 2.0 from source code
annotations </td><td class="border"> Metamodel </td><td class="border"> Ch 5 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1008">OPENJPA-1008</a>
 </td><td class="border"> High </td><td class="border"> Generate meta-model for JPA 2.0 </td><td class="border"> Metamodel </td><td class="border"> Ch 5 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1235">OPENJPA-1235</a>
 </td><td class="border"> Low </td><td class="border"> Optional name element to UniqueConstraint annotation and
corresponding XML type. </td><td class="border"> Mapping </td><td class="border"> 11.1.49, 12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1107">OPENJPA-1107</a>
 </td><td class="border"> Medium </td><td class="border"> Provide TraversableResolver for use with Bean Validation
Factory </td><td class="border"> Spec API </td><td class="border"> 3.6.1.2 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1013">OPENJPA-1013</a>
 </td><td class="border"> Low </td><td class="border"> Modified getQueryBuilder to return updated criteria query builder
</td><td class="border"> EMF, Criteria </td><td class="border"> 7.4 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1010">OPENJPA-1010</a>
 </td><td class="border"> Low </td><td class="border"> New getMetamodel method </td><td class="border"> EMF, Metamodel </td><td class="border"> 7.4 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1191">OPENJPA-1191</a>
 </td><td class="border"> High </td><td class="border"> Implement Typed Query interface </td><td class="border"> Typed Query </td><td class="border"> 3.8.1, 3.8.5 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1191">OPENJPA-1191</a>
 </td><td class="border"> High </td><td class="border"> Implement Tuple interface </td><td class="border"> Typed Query </td><td class="border"> 3.8.1, 3.8.5 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1068">OPENJPA-1068</a>
 </td><td class="border"> High </td><td class="border"> Support Bean Validation: Entity validation upon lifecycle events.
</td><td class="border"> Bean Validation </td><td class="border"> 3.6, 3.2.9 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1082">OPENJPA-1082</a>
 </td><td class="border"> Low </td><td class="border"> Validation target groups via persistence.xml or createEMF
properties Map </td><td class="border"> Bean Validation </td><td class="border"> 3.6.1.2, 8.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1013">OPENJPA-1013</a>
 </td><td class="border"> Low </td><td class="border"> Modified createQuery to accept updated criteria query definition </td><td class="border">
EM, Criteria </td><td class="border"> 3.1.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1013">OPENJPA-1013</a>
 </td><td class="border"> Low </td><td class="border"> Modified getQueryBuilder to return updated criteria query builder
</td><td class="border"> EM, Criteria </td><td class="border"> 3.1.1. </td></tr>
  
  
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-995">OPENJPA-995</a>
 </td><td class="border"> High </td><td class="border"> Migrate existing Criteria Query implementation as OpenJPA
extension </td><td class="border"> Criteria </td><td class="border"> Ch 6 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1069">OPENJPA-1069</a>
 </td><td class="border"> Medium </td><td class="border"> OrderBy annotation applied to an element collection of basic
type doesn't require property or field name </td><td class="border"> Mapping </td><td class="border"> 11.1.38 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1055">OPENJPA-1055</a>
 </td><td class="border"> Medium </td><td class="border"> Added MapKeyEnumerated and MapKeyTemporal annotations and XML.
</td><td class="border"> Mapping </td><td class="border"> 11.1.30, 11.1.33, 12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-937">OPENJPA-937</a>
 </td><td class="border"> Medium </td><td class="border"> Allow use of AssociationOverrides with mapped superclass
relationships. </td><td class="border"> Mapping </td><td class="border"> 11.1.2 </td></tr>
  
  
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-926">OPENJPA-926</a>
 </td><td class="border"> Medium </td><td class="border"> Support persistent access types including @Access annotation
and AccessType enum and XML </td><td class="border"> General </td><td class="border"> 2.3, 11.1.1, 12.2.1.4, 12.2.2.4,
12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1034">OPENJPA-1034</a>
 </td><td class="border"> Low </td><td class="border"> Remove contiguous and base elements from OrderColumn annotation </td><td class="border">
Mapping </td><td class="border"> 11.1.39 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1032">OPENJPA-1032</a>
 </td><td class="border"> Low </td><td class="border"> Removal and revert behavior of getNamedParameters and
getPositionalParameters </td><td class="border"> Query </td><td class="border"> 3.8.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1013">OPENJPA-1013</a>
 </td><td class="border"> Low </td><td class="border"> Added getMetamodel method </td><td class="border"> EM, Metamodel </td><td class="border"> 3.1.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-773">OPENJPA-773</a>
 </td><td class="border"> Low </td><td class="border"> Renamed clear method to detach </td><td class="border"> EM </td><td class="border"> 3.1.1 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-773">OPENJPA-773</a>
 </td><td class="border"> Low </td><td class="border"> Changed target-entity attribute to target-class in
element-collection </td><td class="border"> Mapping </td><td class="border"> 12.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-773">OPENJPA-773</a>
 </td><td class="border"> Low </td><td class="border"> Update pessimistic lock mode names </td><td class="border"> Locking </td><td class="border"> 3.4.4 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-878">OPENJPA-878</a>
 </td><td class="border"> Low </td><td class="border"> Timeouts are in milliseconds. </td><td class="border"> Query, Locking </td><td class="border"> 3.8.8, 3.4.4.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-773">OPENJPA-773</a>
 </td><td class="border"> Low </td><td class="border"> Renamed cascade CLEAR to DETACH </td><td class="border"> EM </td><td class="border"> 3.1.1, 3.2.6 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1077">OPENJPA-1077</a>
 </td><td class="border"> Low </td><td class="border"> Validation-mode element support added to persistence.xml and to
createEMF properties Map </td><td class="border"> Bean Validation </td><td class="border"> 3.6.1.1, 8.3 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1102">OPENJPA-1102</a>
 </td><td class="border"> Low </td><td class="border"> Support application/container provided ValidatorFactory </td><td class="border"> Bean
Validation </td><td class="border"> 3.6.2 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1076">OPENJPA-1076</a>
 </td><td class="border"> Medium </td><td class="border"> PersistenceProviderResolver interface and
PersistenceProviderResolverHolder class </td><td class="border"> Spec API </td><td class="border"> 9.3 </td></tr>
</table>



[Task list for JSR-317 10/31/2008 public draft](jsr-317-20081031-public-draft-tasks.html)



<a name="JPA2.0Tasks-OtherImprovements"></a>

### Other Improvements

<table>
<tr><th> Status </th><th> JIRA </th><th> Summary </th></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1011">OPENJPA-1011</a>
 </td><td class="border"> Instantiate meta-model classes for JPA 2.0 from XML descriptors </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-766">OPENJPA-766</a>
 </td><td class="border"> Tests that currently fail should be committed to the repository </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-5">OPENJPA-5</a>
 </td><td class="border"> Allow compilation with JDK 6 </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1114">OPENJPA-1114</a>
 </td><td class="border"> Bean Validation APIs should be an optional runtime dependency </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1113">OPENJPA-1113</a>
 </td><td class="border"> Reflection class performance improvement </td></tr>
</table>


<a name="JPA2.0Tasks-GeneralTasks"></a>

### General Tasks

<table>
<tr><th> Status </th><th> JIRA </th><th> Summary </th></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-837">OPENJPA-837</a>
 </td><td class="border"> OpenJPA does not fully support database catalogs </td></tr>
<tr><td class="border"> <font color="red">Not Started</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-910">OPENJPA-910</a>
 </td><td class="border"> Allow multiple keys for the same property to be specified at different
levels </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-773">OPENJPA-773</a>
 </td><td class="border"> Upgrade to JPA 2 - umbrella task - includes updating spec API </td></tr>
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-757">OPENJPA-757</a>
 </td><td class="border"> Map existing OpenJPA extensions to new features of JPA 2.0 </td></tr>
  
  
<tr><td class="border"> <font color="green">Complete</font> </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1103">OPENJPA-1103</a>
 </td><td class="border"> Remove early-access disclaimer from the NOTICE files once the spec is
released </td></tr>
</table>

  
  

