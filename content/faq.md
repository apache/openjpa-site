Title: FAQ


<a name="FAQ-General"></a>

## General
* [What is OpenJPA?](#what)
* [What is the history of OpenJPA?](#history)
* [What is the current relationship between Kodo and OpenJPA?](#kodo)
* [What is the current status of the project?](#status)
* [Where can I download OpenJPA?](#download)
* [Does OpenJPA work with my application server or container?](#server)
* [How can I contribute to OpenJPA?](#contribute)
* [How do I enable connection pooling in OpenJPA?](#pooling)
* [How do I figure out which version of OpenJPA I am running?](#version)
* [How do I see the SQL that OpenJPA is executing?](#sql)
* [Can OpenJPA reorder SQL statements to satisfy database foreign key constraints?](#reorder)
* [Can OpenJPA map a one-sided one-many association without a cross table?](#crosstable)

<a name="what"></a>

## What is OpenJPA?

OpenJPA is a 100% open-source implementation of the Java Persistence API
(JPA), which is the persistence component for EJB in the [Java EE 5 specification](http://java.sun.com/javaee/)
.

<a name="history"></a>

## What is the history of OpenJPA?
OpenJPA has its roots in the popular Kodo product, which was created by SolarMetric, Inc. in 2001. BEA Systems, Inc. 
purchased SolarMetric in November of 2005, and soon thereafter announced that they would be donating the bulk of the code to the Apache Software Foundation. OpenJPA is the result of that donation.

<a name="kodo"></a>

## What is the current relationship between Kodo and OpenJPA?

Version 4.1 of Kodo will be based on the OpenJPA code base.

<a name="status"></a>

## What is the current status of the project?

OpenJPA is a top-level project at the Apache Software Foundation.

<a name="download"></a>

## Where can I download OpenJPA?

Look at the [Downloads](downloads.html) page.

<a name="server"></a>

## Does OpenJPA work with my application server or container?

See [Integration](integration.html)
.

<a name="contribute"></a>

## How can I contribute to OpenJPA?

Check out the [Get Involved](get-involved.html)
 page.

<a name="version"></a>

## How do I figure out which version of OpenJPA I am running?

You can get version number and other details of OpenJPA jar you are using
by:


    
<a name="sql"></a>

## How do I see the SQL that OpenJPA is executing?
    
OpenJPA provides configurable channel-based logging, as described in the
chapter on [Logging](http://openjpa.apache.org/builds/latest/docs/manual/manual.html#ref_guide_logging)
. The simplest example of enabling verbose logging is by using the
following property in your {{persistence.xml}} file:
    
    <persistence xmlns="http://java.sun.com/xml/ns/persistence"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        version="1.0">
        <persistence-unit name="example-logging"
transaction-type="RESOURCE_LOCAL">
    	<properties>
    	    <property name="openjpa.Log" value="SQL=TRACE"/>
    	</properties>
        </persistence-unit>
    </persistence>



<a name="pooling"/>
## How do I enable connection pooling in OpenJPA?

As of the 2.1.0 release, OpenJPA includes the [Apache DBCP](http://jakarta.apache.org/commons/dbcp/)
 connection pool. You can also use any third-party connection pool that is
configurable via the JDBC DataSource API (which most are). The following
*persistence.xml* example shows how to use OpenJPA with a [Apache Derby|http://db.apache.org/derby/]
 database and the [Apache DBCP|http://jakarta.apache.org/commons/dbcp/]
 connection pool:

        <persistence xmlns="http://java.sun.com/xml/ns/persistence"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            version="1.0">
            <persistence-unit name="example-derby"
                transaction-type="RESOURCE_LOCAL">
        	<properties>
        	    <property name="openjpa.ConnectionProperties" 
        		value="DriverClassName=org.apache.derby.jdbc.ClientDriver,
        		  Url=jdbc:derby://localhost:1527/database, 
        		  MaxActive=100, 
        		  MaxWait=10000, 
        		  TestOnBorrow=true, 
        		  Username=user, 
        		  Password=secret"/>
        	    <property name="openjpa.ConnectionDriverName" 
        		value="org.apache.commons.dbcp.BasicDataSource"/>
        	</properties>
            </persistence-unit>
        </persistence>

    
See the documentation on [Using a Third-Party DataSource](http://openjpa.apache.org/builds/latest/docs/manual/manual.html#ref_guide_dbsetup_thirdparty) for further details.
   
<a name="reorder"></a>
                                                          
## Can OpenJPA reorder SQL statements to satisfy database foreign key constraints?
Yes. OpenJPA can reorder and/or batch the SQL statements using different
configurable strategies. The default strategy is capable of reordering the
SQL statements to satisfy foreign key constraints. However ,you must tell
OpenJPA to read the existing foreign key information from the database
schema:
    
      <property name="openjpa.jdbc.SchemaFactory" value="native(ForeignKeys=true)"/>

See the documentation on [Schema Factory](http://openjpa.apache.org/builds/latest/docs/manual/manual.html#ref_guide_schema_info_list) for further details.

<a name="fk"></a>

## Why OpenJPA is not creating foreign key constraints on the database tables?

By default, OpenJPA does not create foreign key constraints on new tables
that gets created according to O-R mapping annotation/descriptors. You can
change this default behavior via following configuration property :

      <property name="openjpa.jdbc.MappingDefaults" \
               value="ForeignKeyDeleteAction=restrict,JoinForeignKeyDeleteAction=restrict"/>

to create foreign key constraints on the database tables generated by OpenJPA. 
    
<a name="crosstable"></a>

## Can OpenJPA map a one-sided one-many association without a cross table?
Yes. Standard JPA specification use a cross table to map one-sided
one-to-many relation without a {{mappedBy}} inverse side. Often, you would
like to create a one-to-many association based on an inverse foreign key
(logical or actual) in the table of the related type. OpenJPA supports this
mapping via {{@ElementJoinColumn}} annotation. The following example will
map the collection of {{LineItem}} of a {{Subscription}} via a foreign key
of {{LINEITEM}} table referring to primary key of {{SUBSCRIPTION}} table.
    {code:JAVA}
    package org.mag.subscribe;
    
    import org.apache.openjpa.persistence.jdbc.*;
    
    @Entity
    public class LineItem {
        // has no inverse relation to Subscription
    }
    
    @Entity
    @Table(name="SUB", schema="CNTRCT")
    public class Subscription {
        @Id 
        private long id;
    
        @OneToMany
        @ElementJoinColumn(name="SUB_ID", referencedColumnName="ID")
        private Collection<LineItem> items;
    
        ...
    }

