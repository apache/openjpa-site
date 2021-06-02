Title: Architecture Notes

OpenJPA Architecture notes:

Design point: object persistence; ORM but other stores also supported by
the architecture

domain model: user's responsibility; other areas are OpenJPA

persistence kernel is central part

delegates to other stores via data cache store

front ends, kernel, back ends

query parse tree is general purpose, with several query generators

openjpa.kernel: 

dirty tracking, state management, lazy loading

only keeps track of the fact that a field has changed, not the previous value unless retainValues flag is set

supports managed relationships (rectifying domain model at commit or flush)

two types of managed relationships (inverse vs. dependent)

query parser written in JJTree (extension of javacc but generates AST Nodes)

openjpa.datacache:

query cache might not be optimal depending on the query: if there is a rich fetch plan but data is already cached from a previous query

openjpa.enhance:

now optional but performance costs

enhancer allows lazy loading of all fields; and dirty tracking

lifecycle management, instance factory should be separated from dirty tracking and field management

openjpa.meta:

used at enhancement time, runtime, schema generation

distinguishes between persistence metadata and mapping metadata

openjpa.persistence:

binding to JPA specification

openjpa.lib.jdbc:

wrappers to work around driver-specific bugs

BrokerFactory:

abstract class extended by store-specific factory

Broker:
Hibernate Session, JDO PersistenceManager analog

OpenJPAStateManager:

internal transient object identity is used for newly-persistent instances

OpenJPA also supports JDO datastore identity

if user asks for the id, the instance is flushed to get the id if needed (unless not using agent)

StoreManager:

tight relationship with Broker, e.g. for relationship loading

the link between Broker and StoreManager has a cache decorator to involve the data cache and query cache
