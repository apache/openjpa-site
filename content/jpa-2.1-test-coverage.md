Title: JPA 2.1 Test Coverage


<a name="JPA2.1TestCoverage-JPA2.1TestCoverage"></a>

# JPA 2.1 Test Coverage

 <table class="note"><tr>
  <td valign="top"> <IMG src="images/warning.gif" width="16" height="16" border="0">
  <td>Under Construction...  The exact database types and versions still need to be determined for this new JPA 2.0 release...    	
 </tr></table>


Starting with OpenJPA 2.0.0, we have split the [supported databases ](-http://openjpa.apache.org/builds/latest/docs/manual/supported_databases.html.html)
 into verified and compatible categories.  The automated database testing
performed by IBM and regular testing performed by the OpenJPA community in
the lists below are used to determine which databases will be listed as
*verified* instead of just *compatible*.

  
  

<a name="JPA2.1TestCoverage-AutomatedDatabaseCoverage"></a>

### Automated Database Coverage

JUnit results for OpenJPA supported databases being tested nightly by IBM
using Java SE 6 (either IBM SDK or Sun JDK).

  (/) - All tests passed<br/>
  (x) - Number of failing tests

<table>
<tr><th> Database </th><th> JDBC Driver </th><th> M3 (I11 - 20091005) </th><th> Beta (I14 - 20100125)
</th><th> Beta2 (20100224) </th><th> Beta3 (20100323) </th></tr>
<tr><td class="border"> Derby 10.2.2.0 </td><td class="border"> Embedded </td><td class="border"> (/) 2711 </td><td class="border"> (/) 2904 </td><td class="border">  </td><td class="border">	</td></tr>
<tr><td class="border"> Derby 10.5.3.0 </td><td class="border"> Embedded </td><td class="border">  </td><td class="border"> </td><td class="border"> (/) 3004 </td><td class="border"> (/) 3049 </td></tr>
<tr><td class="border"> DB2 9.5.2 </td><td class="border"> JCC 3.50.152 </td><td class="border"> 2 (x) </td><td class="border"> 1 (x) </td><td class="border"> (/) 3004 </td><td class="border"> 1 (x) </td></tr>
<tr><td class="border"> HSQLDB 1.8.0.10 </td><td class="border"> Embedded in-memory </td><td class="border"> 13 (x) </td><td class="border"> 12 (x) </td><td class="border"> 12 (x) </td><td class="border"> 16 (x)
</td></tr>
<tr><td class="border"> MySQL 5.0.67 </td><td class="border"> JDBC 5.1.6 </td><td class="border"> 1 (x) </td><td class="border"> (/) </td><td class="border"> (/) </td><td class="border"> 2 (x) </td></tr>
<tr><td class="border"> MS SQL Server 2005 SP3 (9.00.4035) </td><td class="border"> sqljdbc4 2.0.1803.100 </td><td class="border"> 14 (x) </td><td class="border"> 8
(x) </td><td class="border"> 8 (x) </td><td class="border"> 10 (x) </td></tr>
<tr><td class="border"> MS SQL Server 2008 SP2 (10.0.2531) </td><td class="border"> sqljdbc4 2.0.1803.100 </td><td class="border"> 14 (x) </td><td class="border"> 5
(x) </td><td class="border"> 5 (x) </td><td class="border"> 8 (x) </td></tr>
<tr><td class="border"> Oracle 10g Express (10.2.0.1.0) </td><td class="border"> ojdbc14 10.2.0.1.0XE </td><td class="border"> 5 (x) </td><td class="border"> 3 (x) </td><td class="border">
5 (x) in locking </td><td class="border"> 1 (x) + locking </td></tr>
</table>

  
  

<a name="JPA2.1TestCoverage-ManualDatabaseCoverage"></a>

### Manual Database Coverage

If you regularly test OpenJPA 2.4.x against another DB vendor or level not
listed above and would like to share your results, then feel free to add
them below.  All we ask, is that you provide as much of the details
requested below, so others can make their own decision on whether to use
one of these combinations in their environment.

<table>
<tr><th> Database </th><th> JDBC Driver </th><th> Java </th><th>  SVN Rev </th><th>  Results </th><th> Submitter </th><th>
Notes </th></tr>
<tr><td class="border"> Derby 10.3.3.0 (652961) </td><td class="border"> Embedded </td><td class="border"> Sun 1.6.0_15 </td><td class="border"> r817831 (20090922) </td><td class="border">
2 (x) </td><td class="border"> dwoods </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1322">OPENJPA-1322</a>
 </td></tr>
<tr><td class="border"> Derby 10.4.2.0 (689064) </td><td class="border"> Embedded </td><td class="border"> Sun 1.6.0_15 </td><td class="border"> r817831 (20090922) </td><td class="border">
2 (x) </td><td class="border"> dwoods </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1322">OPENJPA-1322</a>
 </td></tr>
<tr><td class="border"> Derby 10.5.3.0 (802917) </td><td class="border"> Embedded </td><td class="border"> Sun 1.6.0_15 </td><td class="border"> r813659 (20090910) </td><td class="border">
1 (x) </td><td class="border"> dwoods </td><td class="border"> <a href="https://issues.apache.org/jira/browse/OPENJPA-1293">OPENJPA-1293</a>
 </td></tr>
<tr><td class="border"> MS SQL Server 2008 (10.00.1600) </td><td class="border"> jTDS 1.2.5 </td><td class="border"> Sun 1.5.0_11-b03 </td><td class="border"> r895453
(20100103) </td><td class="border"> 4 (x) </td><td class="border"> mtylenda </td><td class="border"> did not run locking tests </td></tr>
<tr><td class="border"> PostgreSQL 8.3.5 </td><td class="border"> 8.4 JDBC3 (build 701) </td><td class="border"> Sun 1.5.0_11-b03 </td><td class="border"> r885965
(20091201) </td><td class="border"> 31 (x) </td><td class="border"> mtylenda </td><td class="border"> AccessToUnderlyingConnectionAllowed DBCP
property set to true, 12 failures come from locking tests </td></tr>
<tr><td class="border"> H2 1.1.118 </td><td class="border"> Embedded </td><td class="border"> Sun 1.5.0_11-b03 </td><td class="border"> r905001 (20100131) </td><td class="border"> 48 (x) </td><td class="border">
mtylenda </td><td class="border"> in-memory named database, 47 failures come from locking tests;
with MVCC option turned on there are 23 failures from locking tests, <a href="https://issues.apache.org/jira/browse/OPENJPA-1367">OPENJPA-1367</a>
 </td></tr>
<tr><td class="border">  </td><td class="border">  </td><td class="border">  </td><td class="border">  </td><td class="border">  </td><td class="border">  </td><td class="border">  </td></tr>
</table>


  
  
