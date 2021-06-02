Title: Query Notes

<a name="Query-Notes"></a>


<pre>
name conflict: QueryImpl from JDBC vs. QueryImpl from kernel
openjpa.kernel.jpql.JPQLParser
joins are done by SelectImpl
subselects have some issues especially with non-relationship 
src/main/jjtree/org/apache/openjpa/kernel/jpql/JPQL.jjt has rules
all queries always have a "candidate class" 
openjpa.jdbc.kernel.exps.JDBCExpressionFactory implements
openjpa.kernel.exps.ExpressionFactory
openjpa.kernel.exps.InMemoryExpressionFactory implements
openjpa.kernel.exps.ExpressionFactory
can do in memory filtering by downcasting the JPA Query instance and
passing it a collection to filter
can traverse entity parameters via :param.firstname or
:param.relationship.deptname
DBDictionary contains fields that can be customized per database type
JPQLExpressionBuilder does semantic analysis by walking the syntax tree and
generating the semantic tree
SQLFactoryImpl constructs the SQL for the query
SQLBuffer is the result of applying DBDictionary rules to the semantic tree
Can append SQLBuffer to another SQLBuffer for e.g. subselects
SQLBuffer is almost a StringBuffer
ResultSetResult will call ResultSet.getInt etc.
</pre>