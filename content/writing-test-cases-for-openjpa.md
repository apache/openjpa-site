Title: Writing Test Cases For OpenJPA


<a name="WritingTestCasesForOpenJPA-TipsonwritingTestCaseforOpenJPA"></a>

# Tips on writing TestCase for OpenJPA

You are welcome to contribute new test cases. Following are few suggestions
and guidelines on how to contribute new test case to OpenJPA repository of
2000 test cases spread across 400 classes.

## Inherit from OpenJPA TestCases
Unit Tests are **JUnit** Tests. The base JUnit test case implementation
*org.junit.TestCase* has been extended to facilitate common
initialization steps or configuration settings for unit testing OpenJPA. 
The inheritance hierarchy is:
<pre>
        <code>
            junit.framework.TestCase
               +-- org.apache.openjpa.persistence.test.PersistenceTestCase
                   +-- org.apache.openjpa.persistence.test.SingleEMFTestCase
            	  +-- org.apache.openjpa.persistence.test.SQLListenerTestCase
        </code>
</pre>
As a test developer, you should inherit your test class from one of the
extended TestCases. In general, *SingleEMFTestCase* is a good candidate
to inherit from. If your test needs to analyze or count number of SQL
statements, *SQLListenerTestCase* should be your choice.


## Use correct name and package for test case and entity classes
* Test case should be in a separate sub-package of
*org.apache.openjpa.persistence.* **or** *org.apache.openjpa.persistence.jdbc.**
* Test case class names must start with "Test" e.g. **TestEagerFetch**
* There are hundreds of testable entity classes. But if your test requires
new entity classes, place them in the same package as that of the new Test
cases. 


## setUp() and tearDown()}
* OpenJPA TestCases augment the **setUp()** method to accept a list of
arguments. In this list, you should specify:
 * the entity classes used by your test
 * the critical configuration properties
 * **CLEAR_TABLES** or **DROP_TABLES** : these are constants declared in
the superclass which clears the existing rows or drops the tables
altogether.

* The following is an example *setUp()* method 
<pre class="code codeContent">
        <code>
            public void setUp() throws Exception {
                super.setUp(CLEAR_TABLES,               // clears records for domain classes
            	  Candidate.class, Election.class,      // registers Candidate and Election as persistence-capable entity
            	  "openjpa.Multithreaded", "true",      // sets configuration property as name-value pairs
            	  "openjpa.Log", "SQL=TRACE");	     
            }
        </code>
</pre>


* Notice that some configuration parameters can be set in the *setUp()*
method of test program itself. This is recommended for properties that are
important for your test. The non-critical parameters such as database
connection properties (unless your test is about some specific aspect of a
particular database) are better be specified in
*META-INF/persistence.xml*. The persistence name can be specified by
overwriting the following method:
<pre>
        <code>
        protected String getPersistenceUnitName() {
                return "test-eager-fetch";
        }
        </code>
</pre>

* *SingleEMFTestCase* ensures that *tearDown()* method deletes all rows
for the domain classes involved in your test. You may want the database
records to remain for analysis especially when tests are failing. In that
case, you may consider suppressing the superclass behavior of
*tearDown()* by simply nullifying the method as
<pre>
        <code>
            public void tearDown() throws Exception {
                 // avoids super class to delete all records
            }
        </code>
</pre>

## Annotate O-R Mapping

Prefer annotation over XML Descriptors for O-R Mapping because that helps
to collocate relevant information. Unless, of course, the test is specific
about variations in behavior across annotation and XML Descriptors.


## Use JUnit assert*() methods
For verification, use many assertion methods provided by *JUnit* e.g.
**assertEquals()** or **assertTrue()** rather than depending on printing
trace with **System.out.println()**. If you want to trace generated SQL or
other runtime information, use appropriate **openjpa.Log** property
settings.


## Create JIRA Issue
Create a JIRA issue. Refer to the JIRA issue in the comments section of the
new test case.


## ASF License
Remember to include ASF License header in the comment section of all the
new source or resource files.


## Attach the test to JIRA Issue
Package all the *.java files related to your test case in a JAR file and
attach it to JIRA issue you have created.
You must check in the radio button **Grant license to ASF for inclusion in
ASF works** that appears near the bottom of **Attach File** JIRA page.

