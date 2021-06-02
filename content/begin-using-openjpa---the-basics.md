Title: Begin using OpenJPA - The Basics

<a name="BeginusingOpenJPA-TheBasics-Introduction"></a>


# Introduction

OpenJPA is an open source implementation of the Java JPA (Java Persistence
API) specification from Apache. JPA provides an agnostic Java-based API for
storing and retrieving information to a backend database. It has a
canonical query language named Java Persistence Query Language, or JPQL,
that blends with the programming methods of Java and eliminates the need to
tailor database queries for a particular database. However, JPA also
supports native SQL which can be used for quick ports with a known backend
database. This tutorial is designed to walk you through the steps of
setting up a simple web application to use OpenJPA
Geronimo and to transact the derby database that comes with Geronimo. The
tutorial code uses a simple Java Server Page (JSP), backed up by some basic
classes. It displays a table of inventory items and categories. In this
tutorial, we will not dive into details regarding the JSP code. Its purpose
is to be a window through which you can examine OpenJPA. &nbsp;The intended
audience for this tutorial is those with some knowledge and understanding
of the Java programming language and who are just beginning with OpenJPA.
To start, you must download the following requirements and install them on
your computer. For the purposes of this tutorial, we are using Eclipse as
the IDE and Microsoft Windows as the operating system of choice.&nbsp;

<a name="BeginusingOpenJPA-TheBasics-Prerequisites"></a>

## Prerequisites

**Geronimo V2.2:** You can get it [here](http://www.apache.org/dyn/closer.cgi/geronimo/2.2/geronimo-tomcat6-javaee5-2.2-bin.zip)
. Download this file and unzip it to a permanent location. There is no
installer. The server will run from the command line.

**Java (J2SE) V1.6:** This tutorial was developed and tested with Java V1.6.
If you don't already have Java V1.6 you can get the IBM JDK [here](http://www.ibm.com/developerworks/java/jdk/)
 or the Sun JDK [here](https://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_Developer-Site/en_US/-/USD/ViewProductDetail-Start?ProductRef=jdk-6u16-oth-JPR@CDS-CDS_Developer)
.

**Eclipse V3.2 or later:** This version has annotation support included.
Annotations play a large role in OpenJPA.&nbsp; [Download](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/galileo/SR1/eclipse-jee-galileo-SR1-win32.zip)
Eclipse 3.2 or later.

**Apache OpenJPA library:** For the purpose of implementing this tutorial you
can select
OpenJPA v1.2 or greater. You can download [Apache OpenJPA](http://openjpa.apache.org/downloads.html)
 from the Apache site. Note that the Milestone (openjpa-all-2.0.0-M3.jar as
of this writing) is an early release of OpenJPA 2.0 and may have some
instabilities. No issues have been noted for the usage in this tutorial.

*The tutorial code files*: [These files](artifacts/OpenJPAWebAppTutorial.zip)
 are provided with this tutorial. You will add them to your Eclipse
project.

<a name="BeginusingOpenJPA-TheBasics-SetupandRunningtheSample"></a>

# Setup and Running the Sample

Now, that you have all the prerequisites for this tutorial downloaded and
installed, the following sections will walk you through the Eclipse project
setup and the OpenJPA configuration. Make sure you read through and follow
each part carefully. &nbsp;

<a name="BeginusingOpenJPA-TheBasics-SettingupEclipse"></a>

## Setting up Eclipse

After installing Eclipse, create a new project in a dedicated workspace for
the tutorial. Complete the following setup instructions: First, make sure
your Eclipse environment is updated and has the Geronimo plugin. If you do
not know how to do that, follow the instructions found at the [Geronimo website](http://geronimo.apache.org/geronimo-eclipse-plugin-installation-instructions.html)
.

1. Create a new Java project in Eclipse called, **"OpenJPATutorial"**.

   * From the menu, select: **File->New->Enterprise Application Project**. (If
     **Enterprise Application Project** is not available as an option, select
     **Project** and then choose **Enterprise Application Project** from the
     list. Then click on the **Next** button).
     When the New Project settings dialog appears, use the following settings:

     ![images/image001.jpg](/images/image001.jpg)
  
1. Under the **Target Runtime** section, select **Apache Geronimo v2.2**.

    * If you do not already have Geronimo setup in Eclipse then you will have
      to do so now. Click on the **New...** button.
    * If Apache Geronimo v2.2 does not appear in the list under **Apache**,
      click the **Download additional server adapters** link at the top right of
      the dialog. If the adapter does not appear in that list then follow the [directions from the Geronimo site](http://geronimo.apache.org/geronimo-eclipse-plugin-installation-instructions.html).

      ![images/image002.jpg](/images/image002.jpg)
  
    * Select **Apache->Apache Geronimo v2.2**
    * Click **Next**.

      ![images/image003.jpg](/images/image003.jpg)
  
    * Set the JRE to **jre6** if it is not already set.
    * Browse for the install directory of Geronimo v2.2 on your system.
    * Click **Finish**. You should see the following:

      ![images/image001.jpg](/images/image001.jpg)
  
1. Now, click the **Next** button. You should see this:

   ![images/image004.jpg](/images/image004.jpg)
   
   * Check the **Generate application.xml deployment descriptor** option.
   * Click the **New Module...** button:

     ![images/image005.jpg](/images/image005.jpg)
  
   * De-select **Create default modules**.
   * Select	the **Web** option.
   * Click **Next**.

     ![images/image006.jpg](/images/image006.jpg)
  
   * Click **Finish**. You will see the following:

     ![images/image007.jpg](/images/image007.jpg)
 
   * Click **Finish**.
  
  
1. Now, your Project Explorer should look like this (partially expanded):

   ![images/image008.jpg](/images/image008.jpg)

  
   * If you double-click on the **Deployment Descriptor: OpenJPATutorial**, you
     should see the application.xml open:
  
     ![images/image009.jpg](/images/image009.jpg)
  
1. Now we will bring in the sample code. The easiest way to add the sample code is
   to find the source provided with this tutorial and copy it to the src folder
   under the **OpenJPATutorialWeb** folder in your project directory in Windows Explorer:

   ![images/image010.jpg](/images/image010.jpg)

   * Now go back to Eclipse. Right-click on the **OpenJPATutorialWeb** folder in the Project Explorer view
     and select **Refresh,** or press the **F5** key on your keyboard. Now you will see this:

     ![images/image011.jpg](/images/image011.jpg)
  
     Notice that all the source files compile without error. That is because Geronimo comes with OpenJPA v1.1 built in.
  
1. Now copy the index.jsp file from the tutorial into the Web Content directory under the Project directory in Windows Explorer:  

   ![images/image012.jpg](/images/image012.jpg)
  
   * Got to the Project Explorer and refresh the project. You should see this:  

   ![images/image013.jpg](/images/image013.jpg)

<a name="BeginusingOpenJPA-TheBasics-RunningandConfiguringGeronimoandDerby"></a>

## Running and Configuring Geronimo and Derby

Geronimo has no installer and runs from the command line. Here are some
quick instructions to get you started.

1. In Windows, open a command prompt and navigate to the Geronimo **bin** directory.
1. Type the command:

        start-server
  
   ![images/image014.jpg](/images/image014.jpg)
        
   Press the *Enter* key.

   ![images/image015.jpg](/images/image015.jpg)
  
1. Open a web browser and go to the address:

   http://localhost:8080/console

   ![images/image016.jpg](/images/image016.jpg)
  
   The default password is _manager_.
  
1. You will come to the Welcome page. On the left menu, at the bottom, find the section
   for the Embedded DB. This is the Derby database control page.

   ![images/image017.jpg](/images/image017.jpg)
  
1. Click on the link for the **DB Manager**
1. You will see two sections: **DB Viewer** and **Run SQL**.
1. In the Run SQL section, in the text field labeled Create DB, type in **StoreSystem**.
   This is the name of the database that the OpenJPA sample is configured to transact.

   ![images/image018.jpg](/images/image018.jpg)
  
1. Click on the **Create** button. You should now see the **StoreSystem** database appear in
   the **DB Viewer** section.

   ![images/image019.jpg](/images/image019.jpg)
  
1. We are now ready to deploy and run the sample code.

<a name="BeginusingOpenJPA-TheBasics-RunningandDeployingtheSampleCodeinGeronimo"></a>

## Running and Deploying the Sample Code in Geronimo

The sample code provided with this tutorial is working code. It is a simple
inventory database program that shows items and categories. But even this
simple example requires the ability to add, edit and delete entries. It
requires the ability to sort and filter database queries and it requires
the identification of the relationship of the items to the categories. In
this example, the relationship is **one to many**. Knowing that relationship
is important to how the code is written. Before we analyze the code and
OpenJPA, we will first deploy the sample and see it work. To deploy the
sample code follow these instructions:

1. In Eclipse, in the Project Explorer, right click on the OpenJPATutorial
   project and select: **Export->EAR file**.

   ![images/image020.jpg](/images/image020.jpg)
  
1. In the Ear Export dialog, find a convenient place to put the exported EAR file.
1. Check the **Overwrite existing file** check box.

   ![images/image021.jpg](/images/image021.jpg)
  
1. Click **Finish**.
1. Go out to Windows Explorer and copy the file **TutorialDeploymentPlan.xml**
   to the location of the exported ear. This is the deployment plan that
   Geronimo requires to deploy the application.

   ![images/image022.jpg](/images/image022.jpg)
  
1. Open the Geronimo console in a web browser and log in.
1. In the Console Navigation menu on the left, under the **Applications**
   section, click on the **Deploy New** item.
1. Browse to the location of the exported EAR file and the deployment plan
   XML file.

   ![images/image023.jpg](/images/image023.jpg)
  
1. Click on the **Install** button. You should see this.

   ![images/image024.jpg](/images/image024.jpg)
  
1. In the Console Navigation menu on the left, under the **Applications**
   section, click on the **Web App WARs** item.
   * Notice that the OpenJPATutorial application is now listed and that there
     is a clickable link under the URL heading:

     ![images/image025.jpg](/images/image025.jpg)
  
1. Click on the link **OpenJPATutorial** and now you should see this:

   ![images/image026.jpg](/images/image026.jpg)

   Each of the buttons will execute OpenJPA code. The lists are filled by
   running queries on the Derby database.

   * Add a some categories and items
   * Make sure you test each of the buttons and see the results.
  
<a name="BeginusingOpenJPA-TheBasics-ExaminingtheSampleCode"></a>

# Examining the Sample Code

Now that everything is set up and you have seen it work, let's look more
closely at the parts of the code that use OpenJPA. The JSP code is just a
prop to explore OpenJPA and we will not examine it.The sample application
source code is provided for this tutorial and you may run as-is with no
customizations. However, you have the option of reproducing the code
manually using the following explanations. Whichever method you choose,
locate the code that corresponds to explanations as you follow along.

* Java code: This tutorial comes with the following java source files:
    * index.jsp: This is the interface code only. It does call into other
      classes but it does not use any OpenJPA code directly.
    * InventoryEntityBroker.java:&nbsp;This class contains methods that
      encapsulate the OpenJPA handling code. It is provided as a way to separate
      OpenJPA functionality from the web interface.
    * InventoryItem.java: This is an OpenJPA Entity class file. This file is
      an example of a simple OpenJPA Entity with a relationship.
    * InventoryCategory.java: This is an OpenJPA Entity class file. This file
      is an example of a simple OpenJPA Entity with a relationship.
* Persistence code: Each entity concept that would be a database table will
  be its own class. In this case, the tables are called "InventoryItem" and
  "InventoryCategory". Annotations in the Java file will associate the
  properties with the database columns. The annotation,
  <font color="#646464">@Column</font>, maps the property name to the column name
  for synchronization with the database. If the table corresponding tables do
  not exist, OpenJPA can use these annotations to create the tables' schema
  dynamically based on the property type and length.

<DIV style="border-style: solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>InventoryCategory.java</B></DIV>

        package tutorial;
        import java.util.List;

        import javax.persistence.CascadeType;
        import javax.persistence.Column;
        import javax.persistence.Entity;
        import javax.persistence.GeneratedValue;
        import javax.persistence.GenerationType;
        import javax.persistence.Id;
        import javax.persistence.OneToMany;
        import javax.persistence.Version;
    
        @Entity
        public class InventoryCategory
        {
           private int version;
           private int id;
    
           private String categoryName;
           private String categoryDescription;
    
           List<InventoryItem> items;
    
           public InventoryCategory(){}
    
           @Column(name = "categoryName")
           public String getCategoryName()
           {
              return categoryName;
           }
    
           public void setCategoryName(String name)
           {
              this.categoryName = name;
           }
    
           @Column(name = "itemDescription")
           public String getCategoryDescription()
           {
              return categoryDescription;
           }
    
           public void setCategoryDescription(String description)
           {
              this.categoryDescription = description;
           }
    
           @Version
           @Column(name = "version_field")
           // not required
           public int getVersion()
           {
               return version;
           }
    
           public void setVersion(int version)
           {
              this.version = version;
           }
    
           @Id
           @GeneratedValue(strategy = GenerationType.AUTO)
           public int getId()
           {
              return id;
           }
    
           public void setId(int id)
           {
              this.id = id;
           }
    
           @OneToMany(targetEntity=tutorial.InventoryItem.class,
              cascade=CascadeType.ALL,
              mappedBy="category")
           public List<InventoryItem> getItems()
           {
              return items;
           }
    
           public void setItems(List<InventoryItem> items)
           {
              this.items = items;
           }
    
           public void addItem(InventoryItem item)
           {
              this.items.add(item);
           }
        }
    </div>
  
<table class="info"><tr>
  <td valign="top"> <IMG src="images/information.gif" width="16" height="16" border="0">
  <td> <B>Note</B><BR>  
In this example, the property annotations (
<font color="#646464">@Column, @Version</font>, and
<font color="#646464">@Id</font>) are placed on the getter methods. They can
alternatively be placed on the property declarations. For more information
on these annotations and to see what other annotations are in OpenJPA, see
the <a href="http://openjpa.apache.org/builds/latest/docs/manual/jpa_overview_meta.html">Apache OpenJPA 2.0 User's Guide: Chapter 5</a>
<ul>
<li> The annotated class and property declarations are all that are required.
<li> The <font color="#646464">@Id</font> annotation is needed as the unique
identifier (primary key) for each record.
<li> The <font color="#646464">@Version</font> annotation is common practice. It
ensures data integrity during merges and acts as an optimistic concurrency
control.
<li> Every property must have both a getter and a setter and the standard case
convention must be observed.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<ul>
<li>Correct: <font color="#7f0055">public void</font> setCategoryName(String name)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li>Incorrect: <font color="#7f0055">public void setcategoryname(String name)
</ul>
</ul>
</tr></table>


* Persistence.xml: JPA requires the use of a XML file called the
  "persistence.xml" that describes how to access the data. The XML file must
  be created in the META-INF directory. The META-INF directory containing the
  persistence.xml must be located with the source files.

  ![images/image027.jpg](/images/image027.jpg)
  
  In the following example, the file only requires a few fields.
  
  <DIV style="border-style:solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>META-INF/persistence.xml</B></DIV>
    
        <persistence xmlns=http://java.sun.com/xml/ns/persistence
            xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance
            version="1.0">
        <persistence-unit name="InventorySystem" transaction-type="RESOURCE_LOCAL">
	        <class>tutorial.InventoryItem</class>
	        <class>tutorial.InventoryCategory</class>
	        <properties>
	            <property name="openjpa.jdbc.SynchronizeMappings" 
	                     value="buildSchema"/>
	            <property name="openjpa.ConnectionURL" 
	                     value="jdbc:derby://localhost:1527/StoreSystem"/>
	            <property name="openjpa.ConnectionDriverName" 
	                     value="org.apache.derby.jdbc.ClientDriver"/>
	        </properties>
         </persistence-unit>
    </persistence>

  </div>
    
* The following elements are specific to this tutorial:
  * **persistence-unit**: the **name** is the table name to bind. In this case it is 'person'.
  * **class**: the java class that is bound to the table 'person'.
  * **property:** openjpa.jdbc.SynchronizeMappings: This tells OpenJPA to automatically create
    the table with the class definition if a table does not already exist.
  * **property:** openjpa.ConnectionURL: The URL of the database connection.
  * **property:** openjpa.ConnectionDriverName: the class name of the JDBC
    driver for Derby. This must be available via the classpath. In this
    tutorial, the driver is built into Geronimo so no extra actions are needed.

* A complete explanation of the persistence.xml is in the [Apache OpenJPAV2.0 user's Guide: Chapter 6](http://openjpa.apache.org/builds/latest/docs/manual/jpa_overview_persistence.html)

* Create the Entity Manager. In the provided code, the EntityManager is a
  property of the InventoryEntityBroker class. The Entity Manager controls
  the interaction with the database. You must use the Entity Manager to start
  or access transactions or to send queries.
  * The following code must be added before using any of the persistence
    APIs (If you are using the provided sample code, this is already included):

            EntityManagerFactory factory = Persistence.
                createEntityManagerFactory("InventorySystem", System.getProperties());
                  
            EntityManager em = factory.createEntityManager();

  * Note that the name, **"InventorySystem"**, is the same one identified in the persistence.xml.
  * This code can be placed just before a query or transaction or they can be class properties.
  * Regardless of the scope, the EntityManager and the EntityManagerFactory should be closed when they are no longer needed:
  
              ...
              em.close();
              factory.close();
              ...

  * The EntityManagerFactory and EntityManager full descriptions are in the following OpenJPA documentation:
    * EntityManagerFactory: http://openjpa.apache.org/builds/latest/docs/manual/jpa_overview_emfactory.html
    * EntityManager: http://openjpa.apache.org/builds/latest/docs/manual/jpa_overview_em.html
    
* DB interface class. In this example, the InventoryEntityBroker class contains all the OpenJPA database interaction code.
  This is not required but it is a good idea for keeping the functionality componentized. For example, if you want
  to pull all of the records from the InventoryItem table, the code would look like this:

  <DIV style="border-style:solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>InventoryEntityBroker.java</B></DIV>
    
        ...
        List<Person> getAllItems()
        {
             Query q = em.createQuery("SELECT item FROM InventoryItem item");
        
             return (List<InventoryItem>)q.getResultList();
        }
        ...

  </div>

  <DIV style="border-style:solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>index.jsp</B></DIV>
    
        ...
		List<InventoryItem> itemList = getAllItems();
		...

  </div>
	
  * All of the specific APIs are described in the OpenJPA [javadoc](http:/openjpa.apache.org/builds/latest/docs/javadoc/index.html)
  * Notice that the Query is not standard SQL. It is actually JPQL, which is a specialized form of query language specifically designed for JPA.
    * In the JPQL statement, "<font color="#2a00ff">SELECT item FROM InventoryItem item</font>", notice that InventoryItem has the same case as the class
      InventoryItem.
    * JPQL uses java objects in the query and not the database table names. The statement identifies the variable for InventoryItem as
      "<font color="#2a00ff">item</font>".
    * JPQL provides an object oriented query language that is independent of the database being queried.&nbsp; So, regardless of which database being
      used, the JPQL does not change.&nbsp; The JPA runtime takes care of doing the translation from the object world to the desired relational database.
    * For more information on JPQL, check out this [Java Persistence Query Language reference](http://java.sun.com/javaee/5/docs/tutorial/backup/update3/doc/QueryLanguage.html)
        
* Also in the InventoryEntityBroker is code to add entries the database tables. Since you did not create a table for InventoryItem in the
  StoreSystem database in Derby, OpenJPA 2.0 will create the table the first time an _"add"_ is attempted.
  * Consider the following code:
    
  <DIV style="border-style:solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>InventoryEntityBroker</B></DIV>
        
            ...
            void addItem(String name, String description, float price, int categoryID)
            {
                InventoryItem item = new InventoryItem();
                item.setName(name);
                item.setDescription(description);
                ...
            
                em.persist(item);
            }
            ...

  </div>

    You can then call the addItem() method in another part of the code. The
    EntityManager.persist() method will throw an exception if a transaction has
    not been started. The transaction must be committed by calling the
    Transaction.commit() method after all updates have been applied or else the
    changes will not be saved to the database:

            ...
            em.getTransaction().begin();
            
            addItem(...);
            
            em.getTransaction().commit();
            ...

    * When this is executed the first time it will use the annotations to create the Person table, then OpenJPA 2.0 will populate it with the
      provided data.
    * Note the use of the getTransaction() method to start an update and then to commit it. The concept is the same as in any database transaction
      processing.
    * Also note that while the getAllItems() function requires a JPQL SELECT query, the update type actions have APIs.
    * Take a look in the InventoryEntityBroker code at the addItem(), updateItem() and deleteItem() functions and note the simplicity of these
      operations.

* An important aspect of relational databases is, of course, the
  relationships. The basic relationship types are: one to many, many to one,
  and many to many. OpenJPA provides annotations to identify the related fields.
  Open the source file, InventoryCategory.java in Eclipse and find the
  following code:

  <DIV style="border-style:solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>InventoryCategory.java</B></DIV>
        
            ...
            @OneToMany(targetEntity=tutorial.InventoryItem.class,
                cascade=CascadeType.ALL,
                mappedBy="category")
            public List<InventoryItem> getItems()
            {
                return items;
            }
            ...

  * The annotation <font color="#646464">@OneToMany</font> identifies that:
  * This object has a one-to-many relationship with targetEntity=tutorial.InventoryItem.class. Meaning that one
    InventoryCategory can have many InventoryItems associated with it.
  * The property of InventoryItem that specifies the InventoryCategory it is associated with is mappedBy="category". In other
    words, InventoryItem has a class property of type InventoryCategory named "category".  Now open the source file,
    InventoryItem.java and find the following code:

  <DIV style="border-style:solid;border-width: 0px;"><DIV style="border-bottom-width: 1px;border-bottom-style: solid;"><B>InventoryItem.java</B></DIV>
    
            ...
            @ManyToOne
            @JoinColumn(name="CAT_ID", nullable=false)
            public InventoryCategory getCategory()
            {
                return category;
            }
            ...

    * The annotation @ManyToOne identifies that:
    * This object has a many-to-one relationship with the InventoryCategory object. Meaning that there many InventoryItems can reference the same
      InventoryCategory
  * The annotation <font color="#646464">@JoinColumn</font> identifies that:
    * The column in the database table that holds the InventoryCategory
      reference by the attribute: name=<font color="##2a00ff">"CAT_ID"</font>.
  
<table class="info"><tr>
  <td valign="top"> <IMG src="images/information.gif" width="16" height="16" border="0">
  <td> <B>Remember</B><BR>
These annotations contribute to the creation of the tables and the
relationships. It is important to put as much thought into how these
objects relate to each other as you would if you were designing the
database tables because you are designing the database tables.
You can see more about the relationship annotations at the Apache OpenJPA
site. The&nbsp; <a href="http://openjpa.apache.org/builds/latest/docs/manual/jpa_overview_meta_field.html">documentation is here</a>
.
</tr></table>


<a name="BeginusingOpenJPA-TheBasics-Summary"></a>

# Summary

This was a very basic example of how to use OpenJPA with Geronimo and
Derby. However, many applications that require database persistence do not
use much more than the basic functionality demonstrated in this tutorial.
The purpose of this was to be a primer. Aside from the setup of the server
and database, we went through the creation of a persistence.xml file, the
basics of the OpenJPA Entity, and EntityManager and some of the
functionality.

**Exercises**

Using this sample code as a base, try to do some of the following:

* Add additional fields to the InventoryItem Entity.
* Create a Customer Entity and establish a one-to-many relationship with
the InventoryItems as one customer having purchased many items.
* Since several customers could have purchased the same items and an item
could have been purchased by many customers, use the documentation to
create a many-to-many relationship using @ManyToMany*.

\*To make these changes you may have to delete the existing database
tables so that they can recreated with the new relationship fields.

  
  

<a name="BeginusingOpenJPA-TheBasics-References"></a>

# References

* **Java J2SE 1.6**
    * [Download](https://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_Developer-Site/en_US/-/USD/ViewProductDetail-Start?ProductRef=jdk-6u16-oth-JPR@CDS-CDS_Developer)
*&nbsp;*
* **Apache Sources**
    * **Geronimo**
        * [Geronimo Homepage](http://geronimo.apache.org/)
        * [Gernimo V2.2 Server Documentation](http://cwiki.apache.org/GMOxDOC22/documentation.html)
        * [Geronimo V2.2 Server download](http://www.apache.org/dyn/closer.cgi/geronimo/2.2/geronimo-tomcat6-javaee5-2.2-bin.zip)
    * **JPA**
        * [Apache OpenJPA home page](http://openjpa.apache.org/)
        * [Apache OpenJPA download](http://openjpa.apache.org/downloads.html)
        * [Apache OpenJPA documentation](http://openjpa.apache.org/documentation.html)
&nbsp;&nbsp;

* **Annotations**
    * [Documentation       for Java Annotations](http://java.sun.com/j2se/1.5.0/docs/guide/language/annotations.html)
* **JPQL**
    * [A reference for JPQL](http://java.sun.com/javaee/5/docs/tutorial/backup/update3/doc/QueryLanguage.html)
* **Blogs**
    * [Discussion       on The Server Side](http://www.theserverside.com/news/thread.tss?thread_id=58343)
    * [Websphere & OpenJPA blog on       blogspot](http://bit.ly/WASJPAblog)
    * [JPA Blog on developerWorks](http://bit.ly/JPATutApachedwBlog)
* **Implementation Sites**
    * [IBM WebSphere Application Server V7 Java Persistence API (JPA) 2.0 Open Beta](http://bit.ly/BetaSiteApache)
