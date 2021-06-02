Title: JPA 2.0 Iterations


<a name="JPA2.0Iterations-JPA2.0IterationsandTasks"></a>

# JPA 2.0 Iterations and Tasks

<a name="JPA2.0Iterations-IterationScheduleandContent"></a>

## Iteration Schedule and Content

<!-- table>
<tr><td>* [#Milestone 1](#milestone-1)
</tr -->
* [#Milestone 1](#milestone-1)

    * [#Iteration 1](#iteration-1)
 (Dec. 1, 2008 - Dec. 19, 2008) - [OPENJPA-800](https://issues.apache.org/jira/browse/OPENJPA-800)
    * [#Iteration 1a](#iteration-1a)
 (Dec. 22, 2008 - Jan. 2, 2009) - [OPENJPA-831](https://issues.apache.org/jira/browse/OPENJPA-831)
    * [#Iteration 2](#iteration-2)
 (Jan. 5, 2009 - Jan. 23, 2009) - [OPENJPA-807](https://issues.apache.org/jira/browse/OPENJPA-807)
 
* [#Milestone 2](#milestone-2)

    * [#Iteration 3](#iteration-3)
 (Jan. 26, 2009 - Feb. 13, 2009) - [OPENJPA-808](https://issues.apache.org/jira/browse/OPENJPA-808)
    * [#Iteration 4](#iteration-4)
 (Feb. 16, 2009 - Mar. 6, 2009) - [OPENJPA-875](https://issues.apache.org/jira/browse/OPENJPA-875)
    * [#Iteration 5](#iteration-5)
 (Mar. 9, 2009 - Apr. 3, 2009) - [OPENJPA-956](https://issues.apache.org/jira/browse/OPENJPA-956)
    * [#Iteration 6](#iteration-6)
 (Apr. 6, 2009 - May 1, 2009) - [OPENJPA-1007](https://issues.apache.org/jira/browse/OPENJPA-1007)
    * [#Iteration 7](#iteration-7)
 (May 4, 2009 - May 29, 2009) - [OPENJPA-1052](https://issues.apache.org/jira/browse/OPENJPA-1052)
 
* [#Milestone 3](#milestone-3)

    * [#Iteration 8](#iteration-8)
 (June 1, 2009 - July 3, 2009) - [OPENJPA-1105](https://issues.apache.org/jira/browse/OPENJPA-1105)
    * [#Iteration 9](#iteration-9)
 (July 6, 2009 - July 31, 2009) - [OPENJPA-1152](https://issues.apache.org/jira/browse/OPENJPA-1152)
    * [#Iteration 10](#iteration-10)
 (Aug. 3, 2009 - Aug. 28, 2009) - [OPENJPA-1209](https://issues.apache.org/jira/browse/OPENJPA-1209)
    * [#Iteration 11](#iteration-11)
 (Aug. 31, 2009 - Oct. 2, 2009) - [OPENJPA-1268](https://issues.apache.org/jira/browse/OPENJPA-1268)
 
* [#Milestone 4](#milestone-4)

    * [#Iteration 12](#iteration-12)
 (Oct. 5, 2009 - Oct. 30, 2009) - [OPENJPA-1337](https://issues.apache.org/jira/browse/OPENJPA-1337)
    * [#Iteration 13](#iteration-13)
 (Nov. 2, 2009 - Dec. 4, 2009) - [OPENJPA-1373](https://issues.apache.org/jira/browse/OPENJPA-1373)
    * [#Iteration 14](#iteration-14)
 (Dec. 7, 2009 - Jan. 1, 2010) - [OPENJPA-1426](https://issues.apache.org/jira/browse/OPENJPA-1426)
 
* [#Beta](#beta)
 (Jan. 28, 2010)
 
* [#Release Candidate](#release-candidate)
 - Date TBD
<!--tr></tr>
</table -->

Jump to [#Task List](#task-list)

  
  

----

<a name="milestone-1"></a>

## *Milestone 1*

The Milestone 1 release was never "officially" released, due to the JSR-317
terms of use issues, but the files were tagged in svn and can be checked
out using:

    svn co https://svn.apache.org/repos/asf/openjpa/branches/2.0.0-M1/



<a name="iteration-1"></a>

### *Iteration 1 Summary* \- [OPENJPA-800](https://issues.apache.org/jira/browse/OPENJPA-800)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 1 (Dec. 1, 2008 - Dec. 19, 2008)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-800">OPENJPA-800</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-800">OpenJPA 2.0 iteration 1 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>

With the completion of iteration 1, OpenJPA includes many new JPA 2.0
(based on the 10/31/2008 spec draft) features.	Here is a summary of the
new features provided by OpenJPA:

* The current level of JPA 2.0 API.  You can compile against and use
implemented methods of the new API.  Unimplemented methods will throw an
UnsupportedOperationException.
* Validation using the current JPA 2.0 orm and persistence schemas. 
Version 2.0 persistence and orm files will validate using these new
schemas.  Metadata elements provided in iteration 1 (collection-table and
element-collection) will validate and can be specified in XML.
* Support for nested embeddables.  An embeddable can now be nested within
another embeddable.
* Support for relationships within embeddables.  Embeddables can now
contain relationships.
* Collections of embeddables and basic types through the use of
ElementCollection and CollectionTable.	Element collections and collection
tables can be specified using annotations or in a version 2.0 orm XML.
* Support for the Criteria API based on the current spec level, including
the new constructs; KEY(), VALUE(), and CASE().  OpenJPA also includes the
ability to convert queries constructed with the Criteria API to JPQL.
* Support for JPA 2.0 JPQL.  Compilation of JPA 2.0 JPQL statements and
execution of the new JPQL expressions including simple case expressions,
general case expressions, coalesce, and the nullif expression.	In
addition, the select expression allows mathematical operations and the
result alias can be specified in the select expression and in the ORDER BY
clause.  Execution of additional JPA 2.0 JPQL expressions will be added in
future iterations.
* Native sequence generators allow the database schema name to be specified
on the annotation or in a version 2.0 orm XML.


<a name="iteration-1a"></a>

### *Iteration 1a Summary* \- [OPENJPA-831](https://issues.apache.org/jira/browse/OPENJPA-831)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 1a (Dec. 22, 2008 - Jan. 2, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-837">OPENJPA-837</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-837">OpenJPA 2.0: Update OpenJPA documentation with new persistence schemas</A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>

With the completion of the 1a iteration, the OpenJPA documentation has been
updated to contain the most current JPA 2.0 schemas.


<a name="iteration-2"></a>

### *Iteration 2 Summary* \- [OPENJPA-807](https://issues.apache.org/jira/browse/OPENJPA-807)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 2 (Jan. 5, 2009 - Jan. 23, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-807">OPENJPA-807</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-807">OpenJPA 2.0 iteration 2 primary task</A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 2, OpenJPA includes several additional JPA
2.0 (based on the 10/31/2008 spec draft) features. Here is a summary of the
new features provided by OpenJPA:

* Support for the JPA 2.0 level 2 cache interface.  Operations on the
OpenJPA data cache are now available from the entity manager factory
through a standard JPA interface.
* Support for use of order column through a JPA annotations or orm mapping
file elements.	Existing OpenJPA support for order columns has been
extended to support the JPA standard OrderColumn definition.  This
iteration supports a configurable base value attribue.	Support for the
table and contiguous attributes will be provided in future iterations.
* Enhanced map support.  The use of Map collections has been significantly
enhanced.  This iteration includes use of the new MapKeyClass,
MapKeyColumn, MapKeyJoinColumn, and MapKeyJoinColumns annotations and
corresponding orm mapping file elements.
* Support for JPQL INDEX() function within a query projection or predicate.
 Allows the index of ordered columns to be projected or used as part of a
query predicate.  Projection is currently not supported for element
collection.  This support will be added in a future iteration.
* Support for entity TYPE() expression.  Allows projection of or query
criteria based on entity type.	OpenJPA does not currently allow selection
of an abstract entity type.
* Support for new javax.persistence standard properties.  Standard
properties such as javax.persistence.jdbc.driver can now be specified as
configuration properties.

  
  

----

<a name="milestone-2"></a>

## *Milestone 2*

The Milestone 2 release will not be an official ASF release, but will be
created as a Early Access 2 SNAPSHOT branch due to the JSR-317 terms of use
restrictions.  A distribution of the Early Access 2 SNAPSHOT is available [here](http://cwiki.apache.org/confluence/display/openjpa/OpenJPA+2.0.0+Early+Access+2)
 for download or the code can be checked out from svn.
 
<TABLE class="sectionMacro" border="0" cellpadding="5" cellspacing="0" width="100%"><TBODY><TR>
<TD class="confluenceTd" valign="top" width="5%"></TD>
<TD class="confluenceTd" valign="top" width="20%"><DIV class="table-wrap">
<TABLE class="confluenceTable"><TBODY>
<TR>
<TD class="confluenceTd"><SPAN class="image-wrap" style=""><IMG src="http://openjpa.apache.org/images/fotolia/Fotolia_9174675_Download.png" style="border: 0px solid black"></SPAN></TD>
<TD class="confluenceTd"> <A href="http://openjpa.apache.org/openjpa-200-early-access-2.html" class="external-link" rel="nofollow">Download Milestone 2</A> </TD>
</TR>
</TBODY></TABLE>
</DIV>
</TD>
<TD class="confluenceTd" valign="top" width="5%"></TD>
<TD class="confluenceTd" valign="top" width="20%"><DIV class="table-wrap">
<TABLE class="confluenceTable"><TBODY>

<TR>
<TD class="confluenceTd"><SPAN class="image-wrap" style=""><IMG src="http://openjpa.apache.org/images/fotolia/Fotolia_9174675_Pencil.png" style="border: 0px solid black"></SPAN></TD>
<TD class="confluenceTd"> <A href="http://svn.apache.org/viewvc/openjpa/branches/2.0.0-EA2/" class="external-link" rel="nofollow">View SVN Files</A> </TD>
</TR>
</TBODY></TABLE>
</DIV>
</TD>
<TD class="confluenceTd" valign="top"></TD></TR></TBODY></TABLE>
 
<a name="iteration-3"></a>

### *Iteration 3 Summary* \- [OPENJPA-808](https://issues.apache.org/jira/browse/OPENJPA-808)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 3 (Jan. 26, 2009 - Feb. 13, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-808">OPENJPA-808</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-808">OpenJPA 2.0 iteration 3 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>

With the completion of iteration 3, OpenJPA includes several additional JPA
2.0 (based on the 10/31/2008 spec draft) features. Here is a summary of the
new features provided by OpenJPA:

* Support for collection-valued parameters in JPQL using the IN expression.
 A collection-valued parameter (List, Set, etc.) may now be used in
conjunction with the IN expression within the where clause of a JPQL
statement.
* JPA specification level is available through OpenJPA configuration.  The
JPA specification level of the provider can now be retrieved via the
openjpa.Specification property.
* Support for derived identities including the use of MappedById.  OpenJPA
now supports entities which have an identity that is derived from the id of
another identity for one-to-one and many-to-one relationships with a
parent-dependent type association.
* Support for getSupportedProperties and getProperties methods on the
EntityManager and EntityManagerFactory.  The active properties and their
values, in addition to the full set of supported properties can be
retrieved for the EntityManager and EntityManagerFactory.
* The OrderColumn annotation and equivalent XML now allows the
specification of the table element.  The table element can be used to
specify the join or collection table used to maintain the relationship.
* Support for getHints and getSupportedHints on Query.	The active hints
and their values, in addition to supported hints can be retrieved for a
Query.


<a name="iteration-4"></a>

### *Iteration 4 Summary* \- [OPENJPA-875](https://issues.apache.org/jira/browse/OPENJPA-875)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 4 (Feb. 16, 2009 - Mar. 6, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-875">OPENJPA-875</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-875">OpenJPA 2.0 iteration 4 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>

With the completion of iteration 4, OpenJPA includes several additional JPA
2.0 (based on the 10/31/2008 spec draft) features. Here is a summary of the
new features provided by OpenJPA:

* Support new JPA LockModeType in find, lock and refresh methods in the
EntityManager interface. A new "mixed" lock manager is introduced
implementing the new mixed optimistic and pessimistic entity locking
semantics.
* AttributeOverride enhanced to allow navigation of multiple levels of
embeddables, use with map keys and values, and use with element
collections.
* AssociationOverride enhanced to support specification of of a join table
and override of embeddables within relationships.
* Additional support of derived identities.
* Support for general and qualified identification variables in JQPL
selections.  KEY, ENTRY, and VALUE qualifiers
can now be used within the SELECT clause.


<a name="iteration-5"></a>

### *Iteration 5 Summary* \- [OPENJPA-956](https://issues.apache.org/jira/browse/OPENJPA-956)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 5 (Mar. 9, 2009 - Apr. 3, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-956">OPENJPA-956</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-956">OpenJPA 2.0 iteration 5 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>

With the completion of iteration 5, OpenJPA includes several additional JPA
2.0 (based on the 03/13/2009 spec draft) features. Here is a summary of the
new features provided by OpenJPA:

* Updated spec APIs and schemas based upon most current specification
draft.	New, unimplemented methods will throw an
UnsupportedOperationException.
* A lock timeout hint value can now be specified on applicable entity
manager and query methods.
* Lock mode (including the new pessimistic lock modes) can be specified on
query methods and named queries. This allows for fine-grained locking
configuration at the method level.
* The unwrap method can be used to get access to underlying OpenJPA entity
manager and query interfaces.
* JPQL queries support the selection of KEY, VALUE, and ENTRY map values.
* Single entities or an entity graph may be detached from the entity
manager.  Specifying the new cascade type of DETACH or ALL on relationships
allows selective detachment of an entity graph.
* The third argument of the JPQL SUBSTRING function is now optional.
* JPQL queries have been enhanced to support the projection of element
collections.
* JPQL queries have been enhanced to support nested embeddables and
relationships from embeddables.


<a name="iteration-6"></a>

### *Iteration 6 Summary* \- [OPENJPA-1007](https://issues.apache.org/jira/browse/OPENJPA-1007)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 6 (Apr. 6, 2009 - May 1, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1007">OPENJPA-1007</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1007">OpenJPA 2.0 iteration 6 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 6, OpenJPA includes several additional JPA
2.0 (based on the 03/13/2009 spec draft) features. Here is a summary of the
new features provided by OpenJPA:

* Query timeout detection for additional databases. Query timeouts are more
accurately detected and reported in DB2, Oracle, SQL Server, and Informix.

* Support for scalar expressions in JPQL subqueries. Scalar expressions
such as substring can now be used within a subquery.

* Support for explicit access types on persistent types. The persistence
access method to use can now be specified on a per-type and field/method
level.

* Updates to OrderColumn and EntityManager methods to match new spec draft.

* JPQL queries now support key/value paths as arguments to scalar
functions.  KEY() and VALUE() can now be used to indicate that a map key or
value should be used as an argument to a scalar function.

<a name="iteration-7"></a>

### *Iteration 7 Summary* \- [OPENJPA-1052](https://issues.apache.org/jira/browse/OPENJPA-1052)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 7 (May 4, 2009 - May 29, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1052">OPENJPA-1052</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1052">OpenJPA 2.0 iteration 7 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 7, OpenJPA includes several additional JPA
2.0 (based on the 03/13/2009 spec draft) features. Here is a summary of the
new features provided by OpenJPA:

* New MapKeyEnumerated and MapKeyTemporal annotations and equivalent XML
elements for tagging the key of a map collection as either an enumerated or
temporal type.
* Base support for JSR-303 Bean Validation including basic configuration
and lifecycle-based event validation.
* Support the use of delimited identifiers within annotation attributes for
a subset of mapping annotations when using the Derby and DB2 databases. 
Support for additional databases will be added in future iterations.
* JPQL subqueries now support derived path expressions and the use of KEY()
on map collections.
* OSGI bundle metadata has been added to the OpenJPA jar.  This simplifies
the use of OpenJPA in an OSGi environment such as [Apache Felix](http://felix.apache.org)
.
* OrderBy no longer requires name attribute when applied to a collection of
basic type.

  
  

----

<a name="milestone-3"></a>

## *Milestone 3*

The Milestone 3 release is an official ASF release, but we encourage you to
upgrade to the final 2.0.0 as soon as possible after it is released.  A
distribution of the Milestone 3 is available [here](http://cwiki.apache.org/confluence/display/openjpa/OpenJPA+2.0.0+Milestone+3)
 for download or the code can be checked out from svn.

<TABLE class="sectionMacro" border="0" cellpadding="5" cellspacing="0" width="100%"><TBODY><TR>
<TD class="confluenceTd" valign="top" width="5%"></TD>
<TD class="confluenceTd" valign="top" width="20%"><DIV class="table-wrap">
<TABLE class="confluenceTable"><TBODY>
<TR>
<TD class="confluenceTd"><SPAN class="image-wrap" style=""><IMG src="http://openjpa.apache.org/images/fotolia/Fotolia_9174675_Download.png" style="border: 0px solid black"></SPAN></TD>
<TD class="confluenceTd"> <A href="http://openjpa.apache.org/openjpa-200-milestone-3.html" class="external-link" rel="nofollow">Download Milestone 3</A> </TD>
</TR>
</TBODY></TABLE>
</DIV>
</TD>
<TD class="confluenceTd" valign="top" width="5%"></TD>
<TD class="confluenceTd" valign="top" width="20%"><DIV class="table-wrap">
<TABLE class="confluenceTable"><TBODY>

<TR>
<TD class="confluenceTd"><SPAN class="image-wrap" style=""><IMG src="http://openjpa.apache.org/images/fotolia/Fotolia_9174675_Pencil.png" style="border: 0px solid black"></SPAN></TD>
<TD class="confluenceTd"> <A href="http://svn.apache.org/viewvc/openjpa/tags/2.0.0-M3/" class="external-link" rel="nofollow">View SVN Files</A> </TD>
</TR>
</TBODY></TABLE>
</DIV>
</TD>
<TD class="confluenceTd" valign="top"></TD></TR></TBODY></TABLE>


<a name="iteration-8"></a>

### *Iteration 8 Summary* \- [OPENJPA-1105](https://issues.apache.org/jira/browse/OPENJPA-1105)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 8 (June 1, 2009 - July 3, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1105">OPENJPA-1105</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1105">OpenJPA 2.0 iteration 8 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 8, OpenJPA includes several additional JPA
2.0 features and bug fixes. Here is a summary of the new features provided
by OpenJPA:

* Sub-project for JSR-303 (Bean Validation) testing with configurable bean
validation providers.
* Automatic detection of bean validation providers.
* Support for bean validation groups, configurable through standard
persistence.xml properties.
* Bug fixes for attribute-overrides and embeddable processing.
* Performance enhancements to class reflection utility.  Provides 17%
performance gain in some benchmarks.


<a name="iteration-9"></a>

### *Iteration 9 Summary* \- [OPENJPA-1152](https://issues.apache.org/jira/browse/OPENJPA-1152)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 9 (July 6, 2009 - July 31, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1152">OPENJPA-1152</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1152">OpenJPA 2.0 iteration 9 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 9, OpenJPA includes several additional JPA
2.0 features and bug fixes. Here is a summary of the new features provided
by OpenJPA:

* Bean Validation support for validation groups.  Specific validation
groups can be targeted for lifecycle events.
* A TraversableResolver is now registered with the bean validator.  The
resolver ensures that only loaded attributes are validated.
* A PersistenceProviderResolver and PersistenceProviderResolverHolder are
available from the Geronimo Spec API. PersistenceProviderResolver can be
used to return the list of persistence providers available in the runtime
environment.
* Availablility of ProviderUtil and PersistenceUnitUtil interfaces.  These
interfaces provide methods to determine the load state of a persistent
entity or attribute.  In addition, PersistenceUnitUtil can be used to get
the identifier of an entity.
* Significant improvements to OpenJPA's subquery processing.
* OpenJPA now includes the ability to use a pluggable encryption provider. 
This provider can be used to support encrypted database passwords in the
persistence.xml. See the [Encryption Provider](http://openjpa.apache.org/builds/latest/docs/manual/ref_guide_encryption.html)
 chapter in the documentation for more details.


<a name="iteration-10"></a>

### *Iteration 10 Summary* \- [OPENJPA-1209](https://issues.apache.org/jira/browse/OPENJPA-1209)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 10 (Aug. 3, 2009 - Aug. 28, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1209">OPENJPA-1209</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1209">OpenJPA 2.0 iteration 10 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 10, OpenJPA includes several additional
JPA 2.0 features and bug fixes. Here is a summary of the new features
provided by OpenJPA:

* Support for the Criteria and Metamodel API.  The Criteria and Metamodel
API can be used in conjunction to create and execute strongly-typed
programmatic queries.
* Metamodel source file generation.  OpenJPA provides tooling to generate
metamodel source classes.
* Support for the TypedQuery and Tuple interfaces.  These interfaces are
provided to manipulate typed queries and their results.
* Automatic setting of compatibility options based upon persistence
version.  Compatibility options are configured based on persistence version
to provide backward compatibility for OpenJPA version 1.x applications.
* Support for naming of unique constraints.
* Lob, Temporal, and Enumeration can now be specified on element
collections.
* JPQL now supports multiple constructors in the query projection list.
* Support for the shared-cache-mode element in the persistence.xml. 
Provides configuration/enablement options for L2 cache.
* Support for Cacheable annotation and CacheStoreMode/CacheRetriveMode
properties.  Allows per class configuration of L2 cacheing and
per-operation tuning of cache behavior.
* Database updates including updates for Derby reserved words, usage of a
new version of commons-pool and commons-dbcp, and a new Derby network
server test profile.
* Support for JDBC date, time, and timestamp literals within JPQL and
Criteria queries.

<a name="iteration-11"></a>

### *Iteration 11 Summary* \- [OPENJPA-1268](https://issues.apache.org/jira/browse/OPENJPA-1268)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 11 (Aug. 31, 2009 - Oct. 2, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1268">OPENJPA-1268</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1268">OpenJPA 2.0 iteration 11 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 11, OpenJPA includes several additional
JPA 2.0 features and bug fixes. Here is a summary of the new features
provided by OpenJPA:

* OpenJPA is based upon Proposed Final Draft 2 of [JSR-317](http://jcp.org/en/jsr/detail?id=317)
.
* Support for cascading detach using cascade-detach as specified in the
orm.xml.
* Assertion that relationships in MappedSuperclass are unidirectional.
* OpenJPA was updated to the CR5 level of the bean validation
specification.
* A new code sample which showcases the use of embeddables.
* Corrected an XML encoding issue which occurred when using XML data with
SQL Server.
* Many documentation updates.
* Improved test coverage for many database platforms.  The current test
matrix is available [here](http://cwiki.apache.org/confluence/display/openjpa/JPA+2.0+Test+Coverage)
.

  
  

----

<a name="milestone-4"></a>

## *Milestone 4*

<a name="iteration-12"></a>

### *Iteration 12 Summary* \- [OPENJPA-1337](https://issues.apache.org/jira/browse/OPENJPA-1337)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 12 (Oct. 5, 2009 - Oct. 30, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1337">OPENJPA-1337</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1337">OpenJPA 2.0 iteration 12 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 12, OpenJPA includes several additional
JPA 2.0 features 
and bug fixes. Here is a summary of the new features provided by OpenJPA:

* Support for extended lock scope via the javax.persistence.lock.scope
property.
* Support for the GA version of the [JSR-303](http://jcp.org/en/jsr/detail?id=303)
 Bean Validation API.
* Many documentation updates, notably for Criteria API and Metamodel
tooling.
* More improvements to test coverage for additional database platforms. 
The current test matrix is available [here](http://cwiki.apache.org/confluence/display/openjpa/JPA+2.0+Test+Coverage)
.

  
  

<a name="iteration-13"></a>

### *Iteration 13 Summary* \- [OPENJPA-1373](https://issues.apache.org/jira/browse/OPENJPA-1373)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 13 (Nov. 2, 2009 - Dec. 4, 2009)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1373">OPENJPA-1373</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1373">OpenJPA 2.0 iteration 13 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 13, OpenJPA includes several additional
JPA 2.0 features 
and bug fixes. Here is a summary of the new features provided by OpenJPA:

* Support for CacheRetrieveMode and CacheStoreMode on find and refresh
operations.
* Support for find and refresh entity manager operations that accept
properties.

  
  

<a name="iteration-14"></a>

### *Iteration 14 Summary* - [OPENJPA-1426](https://issues.apache.org/jira/browse/OPENJPA-1426)

 <TABLE cellpadding="2" cellspacing="0" border="0" width="100%" align="center">
 <TR>
 <TD width="1%" nowrap="">
 <B>Iteration 14 (Dec. 7, 2009 - Jan. 1, 2010)</B>&nbsp;
 
 </TD>
 
 <TD width="100%">
 &nbsp;
 </TD>
 
 <TD style="border-width: 1px 1px 0 1px; border-style: solid; border-color: #bbb;" width="1%">
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" nowrap="true" valign="middle" align="right"><FONT size="1">&nbsp;Issue Progress:&nbsp;</FONT></TD>
 
 <TD>
 <TABLE height="6" valign="middle" align="right" cellspacing="0" cellpadding="0" border="0">
 <TR height="6">
 <TD height="6" width="100" bgcolor="009900">
 <IMG src="http://issues.apache.org/jira/images/border/spacer.gif" height="10" width="100" border="0" title="Resolved Issues - 100% (1 issues)">
 </TD>
 </TR>
 </TABLE>
 </TD>
 
 </TR>
 </TABLE>
 </TD>
 </TR>
 </TABLE>
 
 <TABLE width="100%" cellspacing="0" class="grid">
 <TR>
 <TH width="1%" style="text-align: left;">
 &nbsp;
 
 </TH>
 <TH style="text-align: left;">
 Key
 </TH>
 <TH style="text-align: left;">
 Summary
 </TH>
 <TH style="text-align: left;">
 Assignee
 </TH>
 
 <TH style="text-align: left;">
 Pr
 </TH>
 <TH style="text-align: left;">
 Status
 </TH>
 </TR>
 <TR class="rowNormal">
 <TD><DIV style="background-color:ccffcc"><STRIKE>1.</STRIKE></DIV></TD>
 
 <TD nowrap="true">
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1426">OPENJPA-1426</A>
 </TD>
 <TD>
 <A href="http://issues.apache.org/jira/browse/OPENJPA-1426">OpenJPA 2.0 iteration 14 primary task </A>
 </TD>
 <TD nowrap="true">
 Jeremy Bauer
 </TD>
 
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/priority_major.gif" alt="Major" border="0">
 </TD>
 <TD nowrap="true">
 <IMG src="http://issues.apache.org/jira/images/icons/status_closed.gif" alt="Closed" border="0">Closed
 </TD>
 </TR>
 </TABLE>


With the completion of iteration 13, OpenJPA includes several additional
JPA 2.0 features 
and bug fixes. Here is a summary of the new features provided by OpenJPA:

* Support for delimited identifiers.
* Added support for testing with JPA 2.0 TCK

  
  

----

<a name="beta"></a>

## *Beta*

The Beta release is an official ASF release and it passed the JPA 2.0 TCK,
but we encourage you to upgrade to the final 2.0.0 as soon as possible
after it is released.  A distribution of the Beta is available [here](http://cwiki.apache.org/confluence/display/openjpa/OpenJPA+2.0.0+Beta)
 for download or the code can be checked out from svn.

<TABLE class="sectionMacro" border="0" cellpadding="5" cellspacing="0" width="100%"><TBODY><TR>
<TD class="confluenceTd" valign="top" width="5%"></TD>
<TD class="confluenceTd" valign="top" width="20%"><DIV class="table-wrap">
<TABLE class="confluenceTable"><TBODY>
<TR>
<TD class="confluenceTd"><SPAN class="image-wrap" style=""><IMG src="http://openjpa.apache.org/images/fotolia/Fotolia_9174675_Download.png" style="border: 0px solid black"></SPAN></TD>
<TD class="confluenceTd"> <A href="http://openjpa.apache.org/openjpa-200-beta.html" class="external-link" rel="nofollow">Download Beta</A> </TD>
</TR>

</TBODY></TABLE>
</DIV>
</TD>
<TD class="confluenceTd" valign="top" width="5%"></TD>
<TD class="confluenceTd" valign="top" width="20%"><DIV class="table-wrap">
<TABLE class="confluenceTable"><TBODY>
<TR>
<TD class="confluenceTd"><SPAN class="image-wrap" style=""><IMG src="http://openjpa.apache.org/images/fotolia/Fotolia_9174675_Pencil.png" style="border: 0px solid black"></SPAN></TD>
<TD class="confluenceTd"> <A href="http://svn.apache.org/viewvc/openjpa/tags/2.0.0-beta/" class="external-link" rel="nofollow">View SVN Files</A> </TD>
</TR>
</TBODY></TABLE>
</DIV>
</TD>
<TD class="confluenceTd" valign="top"></TD></TR></TBODY></TABLE>
  
  

----

<a name="release-candidate"></a>

## *Release Candidate*

<a name="iteration-15"></a>

### Remaining Work Items - 
* Performance improvements
* L2 Cache provider improvements
* TBD
