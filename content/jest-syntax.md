Title: JEST Syntax


<a name="JESTSyntax-JESTURISyntax"></a>


## JEST URI Syntax

JEST defines URI syntax to access persistent resources over HTTP. 

As an example, to find a persistent Person instance with primary key 1234 and
receive the result in *JSON* format, an example URI would look like this (non functional URI):
	  
<http://www.example.com:8080/jest/find/format=json?type=Person&1234>

The formal notation of a JEST URI is

      URI := http://{host}[:port]/{context}/{action}[/qualifier]* [?argument] [&argument]*

The URI syntax rules, in the light of the above example, are as follows:

  * _protocol_ is always `http`
  
  * _host_ (`www.example.com`) and optional _port_ number locates the
JEST servlet
  
  * _context_ (`jest`) identifies the context path of the JEST servlet.
The context path is the servlet name
    as specified in the web deployment descriptor for JEST servlet
    
  * _action_ (`find`) is the first segment of the servlet path. 
    Allowed actions are `find`, `query`, `domain`, `properties`
etc.
  
  * zero or more `qualifier` may constitute the servlet path. Each
qualifier is separated by `/` character.
  * A qualifier must have a key and an optional value. 
  * The qualifier key and value, if present, are separated by `=` sign.
  * A qualifier key is a valid Java identifier. The exact key is
conditional on the action. For example, `find` action
    accepts *format* qualifier, `query` action accepts `single`,
`named`, `maxResult`, `firstResult`, 
    `format` as qualifiers.
    In the example above, `format=json` qualifies that the response of
`find` action be formatted as JSON. 
  * A qualifier may or may not have a value. For example, `maxResult`
qualifier for `query` action must have 
    an integer value while `single` qualifier does not.
    
  * zero or more _argument_ may follow after the path by `?` character.
  * each _argument_ is separated by `&` character
  * An _argument_ has an optional key and must have a value.
  * The _argument_ key, if present, and value are separated by `=` sign.
   
  * some actions may enforce mandatory argument(s). For example, a `find`
action must have `type` argument 
    and at least one more argument for the primary key. A `query` action
must have `q` argument etc.
           

<a name="JESTSyntax-Listofsupportedactions,qualifiersandarguments"></a>

## List of supported actions, qualifiers and arguments

The following sections tabulates the currently supported actions and
corresponding qualifiers and arguments.
A **bold font** denotes qualifier or argument as mandatory.
 
<a name="JESTSyntax-Action:find"></a>

### Action: find

Returns the result of a *find()* operation.  

<table>
<tr><th>qualifier-key </th><th> qualifier-value</th><th>	      Comment</th></tr>
<tr><td class="border">format 	 </td><td class="border"> <tt>xml</tt> or <tt>json</tt>	 </td><td class="border"> default is <tt>xml</tt></td></tr>
<tr><td class="border">plan		 </td><td class="border">			 </td><td class="border"> name of one or more fetch
plan(s). Each name separated by comma character.</td></tr>
<tr><td class="border">		 </td><td class="border">			 </td><td class="border"> e.g.
<tt>find/plan=onlyBasicFields?type=Person&1234</tt></td></tr>
<tr><td class="border">		 </td><td class="border">			 </td><td class="border"> where <tt>onlyBasicFields</tt> is
name of a pre-defined Fetch Group</td></tr>
</table>

<table>
<tr><th>argument-key	</th><th>argument-value       </th><th>     Comment </th></tr>
<tr><td class="border"><tt>type</tt> 	</td><td class="border">entity name	       </td><td class="border"> Fully-qualified Java class name or
alias of the entity </td></tr>
<tr><td class="border">		</td><td class="border">primary key value     </td><td class="border"> can be used for simple identity
without the id property name</td></tr>
<tr><td class="border">		</td><td class="border">		       </td><td class="border"> e.g. <tt>/find?type=Person&1234</tt></td></tr>
<tr><td class="border">id property	</td><td class="border">primary key value     </td><td class="border"> Used for compound primary keys</td></tr>
<tr><td class="border">		</td><td class="border">		       </td><td class="border"> e.g.
<tt>/find?type=Person&firstName=John&lastName=Doe</tt></td></tr>
</table>
               
<a name="JESTSyntax-Action:query"></a>

### Action : query

Returns the result of a `Query.getResultList()` or
`Query.getSingleResult()` operation.	

<table>
<tr><th>qualifier-key </th><th> qualifier-value</th><th>	      Comment</th></tr>
<tr><td class="border">format 	</td><td class="border"> <tt>xml</tt> or <tt>json</tt>	 </td><td class="border"> default is <tt>xml</tt></td></tr>
<tr><td class="border">plan		</td><td class="border">		</td><td class="border"> name of one or more fetch plan(s). Each
name separated by comma character.</td></tr>
<tr><td class="border">single 	</td><td class="border">		</td><td class="border"> enforces single instance as query result
</td></tr>
<tr><td class="border">		</td><td class="border">		</td><td class="border"> e.g. {{/query/single?q=select p from
Person p where p.name=:x&x=John}} </td></tr>
<tr><td class="border">named		</td><td class="border">		</td><td class="border"> interprets the q argument value as a
named query</td></tr>
<tr><td class="border">		</td><td class="border">		</td><td class="border"> e.g.
<tt>/query/named?q=PersonByName&x=John</tt> </td></tr>
<tr><td class="border">		 </td><td class="border">		</td><td class="border"> where <tt>PersonByName</tt> is named query
with <tt>x</tt> its named parameter</td></tr>
</table>

<table>
<tr><th>argument-key	</th><th>argument-value       </th><th>     Comment </th></tr>
<tr><td class="border"><tt>q</tt>		</td><td class="border">JPQL or Named Query   </td><td class="border"> e.g. <tt>/query/named?q=AllPerson</tt></td></tr>
<tr><td class="border">		</td><td class="border">		       </td><td class="border"> or {{/query?q=select p from Person
p}}</td></tr>
<tr><td class="border">		</td><td class="border">		       </td><td class="border"> e.g. {{/query?q=select p from
Person p where p.firstName=:x&x=John}}</td></tr>
<tr><td class="border">bind parameter </td><td class="border">parameter value       </td><td class="border"> the values are converted to match
the target type</td></tr>
<tr><td class="border">		</td><td class="border">		       </td><td class="border"> e.g. {{/query?q=select p from
Person p where p.gender=:g&g=MALE}}</td></tr>
</table>

<a name="JESTSyntax-Action:domain"></a>

### Action : domain

Returns the domain model in XML format.

Accepts no qualifier.
Accepts no argument. 

<a name="JESTSyntax-Action:properties"></a>

### Action : properties

Returns the configuration properties in HTML format.

Accepts no qualifier.
Accepts no argument. 


<a name="JESTSyntax-Formalsyntax:"></a>

### Formal syntax:

    URI := http://{host}[:port]/{context}/{action}[/qualifier]* [?argument][&argument]*

    context         := JEST servlet context root
    action	        := find|query|domain|properties
    qualifier       := qualifier-key[=qualifier-value]
    argument        := [argument-key=] argument-value
    qualifier-key   := any valid Java identifier 
    qualifier-value := string
    argument-key    := string 
    argument-value  := string
