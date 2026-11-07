Title: Query Notes

<a name="Query-Notes"></a>

Notes on OpenJPA query internals and JPQL processing.

* There is a name conflict between `QueryImpl` in the JDBC store and `QueryImpl` in the kernel.
* The JPQL parser is `openjpa.kernel.jpql.JPQLParser`.
* Joins are performed by `SelectImpl`.
* Subselects have some issues, especially with non-relationship columns.
* `src/main/jjtree/org/apache/openjpa/kernel/jpql/JPQL.jjt` contains the parser rules.
* Every query always has a "candidate class".
* `openjpa.jdbc.kernel.exps.JDBCExpressionFactory` and `openjpa.kernel.exps.InMemoryExpressionFactory` both implement `openjpa.kernel.exps.ExpressionFactory`.
* In-memory filtering is possible by downcasting the JPA `Query` instance and passing it a collection to filter.
* Entity parameters can be traversed via `:param.firstname` or `:param.relationship.deptname`.
* `DBDictionary` contains fields that can be customized per database type.
* `JPQLExpressionBuilder` performs semantic analysis by walking the syntax tree and generating the semantic tree.
* `SQLFactoryImpl` constructs the SQL for the query.
* `SQLBuffer` is the result of applying `DBDictionary` rules to the semantic tree.
* `SQLBuffer` instances can be appended to one another, e.g. for subselects.
* `SQLBuffer` is almost a `StringBuffer`.
* `ResultSetResult` calls `ResultSet.getInt` and similar methods.
