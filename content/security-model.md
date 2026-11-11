Title: Security Model

# Apache OpenJPA Security Model

This page describes the security model of Apache OpenJPA: what OpenJPA trusts, what it does not, which parts of a secure deployment are the responsibility of the application and its operators, and which reports we treat as security vulnerabilities. It is meant to help developers and operators use OpenJPA safely, and to help security researchers decide whether a finding is a vulnerability in OpenJPA or expected behaviour.

The page describes the OpenJPA 4.x release line. Where behaviour differs between releases, it says so.

## Reporting Security Vulnerabilities

The Apache Software Foundation takes security problems in its projects seriously. Please report security problems in OpenJPA privately, before disclosing them in any public forum, by e-mail to [security@apache.org](mailto:security@apache.org). The ASF security team will forward the report to the OpenJPA PMC. Send one plain-text e-mail per vulnerability; the process and the accepted report format are described at [https://www.apache.org/security/](https://www.apache.org/security/).

Please use this address only for undisclosed security vulnerabilities in OpenJPA's own code. Regular bugs, questions and feature requests belong in [JIRA](https://issues.apache.org/jira/browse/OPENJPA) or on the users and dev mailing lists.

Before reporting, please read this page. Some behaviour that would be a vulnerability in a network service is expected in a library that runs inside an application with the application's privileges. A good report states the OpenJPA version, the configuration used, which input the attacker controls, and why that input is untrusted under this model.

## What OpenJPA Is, From a Security Point of View

OpenJPA is a library. It implements Jakarta Persistence and runs inside an application's JVM, with that application's privileges and class path. It does not run as a standalone server and, with the default configuration, it opens no network listener.

The application that embeds OpenJPA, together with the people who build, configure and deploy it, is trusted. OpenJPA's job is to map Java objects to a relational database correctly, and to keep data that the application hands it as data: values must not change the structure of the SQL that OpenJPA generates. OpenJPA does not authenticate users, does not authorize access to entities or rows, and does not decide which end user may run which query. Those are the application's responsibilities.

The data cache and the query cache, when enabled, are shared by all `EntityManager`s of an `EntityManagerFactory`, whichever database user each of them connects as. If the application relies on per-user database credentials, database grants or row-level security, do not enable these caches, or use a separate `EntityManagerFactory` per security context.

## Trusted Inputs

The following inputs are trusted. Anyone who controls them can already run code in the application or read and change its data, so abusing them is not a vulnerability in OpenJPA.

- **Configuration from every source.** This includes `persistence.xml`, `openjpa.xml` and other global configuration resources, the property map passed to `Persistence.createEntityManagerFactory`, `EntityManager` properties, query hints, and all `openjpa.*` JVM system properties (these override global configuration resources). Many OpenJPA properties are *plugin strings* of the form `ClassName(property=value, ...)`: OpenJPA loads the named class, instantiates it and calls its setters. Configuration can also name log files to write, SQL scripts to read and execute, JNDI names to look up, network ports to open and JDBC URLs to connect to. Treat OpenJPA configuration as code. Never build property names or values from end-user input.
- **Mapping metadata.** Annotations, `orm.xml` and other mapping files, and the entity classes themselves. Table names, column names and `columnDefinition` values are written into SQL and DDL as they appear in the metadata.
- **XML configuration and mapping files.** OpenJPA parses them with the JDK's default XML parser settings. Because these files are trusted, issues such as external entity resolution in them are not vulnerabilities. Do not feed OpenJPA's XML parsing with files from untrusted sources.
- **Query text.** JPQL strings, native SQL strings, named query definitions, the function name passed to `CriteriaBuilder.function`, and database-specific SQL hints such as `openjpa.hint.OracleSelectHint`. OpenJPA passes this text to its parser or to the database as written. The `openjpa.MethodQL` query language calls a static Java method named in the query string.
- **The JDBC driver, URL and connection properties.** Some JDBC drivers can run code, read files or deserialize data based on URL options. The URL is configuration. Encryption and authentication of the database connection are configured through the driver, the URL or the `DataSource`; OpenJPA has no setting of its own for them. Use TLS when the database is reached over a network that is not trusted.
- **The database and its schema.** OpenJPA trusts the database it connects to and the data the database returns. In particular, fields mapped as serialized Java objects are deserialized when they are read (see [Serialization](#serialization)), and fields mapped as XML are parsed with JAXB when they are read.
- **The class path and the build.** The bytecode enhancer (build-time tool, Ant task, Maven plugin and javaagent) loads and rewrites the application's classes, and runs any auxiliary enhancers registered on the class path through `META-INF/services`. The OpenJPA Maven plugin runs with the privileges of the build like any other Maven plugin.
- **Files and URLs named in configuration**, such as log files, a `CacheMarshaller` input URL, SQL script sources, or the directory used by the sample XML store. Files at paths named in configuration are created with the process's default permissions.
- **Serialized OpenJPA objects created by the application itself**, such as a serialized `EntityManagerFactory`, `EntityManager` or detached entity. Their serialized form contains the full configuration (see [Serialization](#serialization)).

## Untrusted Inputs

OpenJPA is designed to handle the following as untrusted data:

- **Query parameter values** set with `Query.setParameter` (named and positional), for JPQL, Criteria and native queries.
- **Value arguments of the Criteria API**: any value the application passes to a `CriteriaBuilder` method as a value, for example as an operand of a comparison, `coalesce`, `nullif` or a `selectCase` branch, whether or not it is wrapped in `CriteriaBuilder.literal`. Query text, function names and hints are not values.
- **String literals in JPQL text that the application has escaped correctly** (a single quote written as two single quotes). OpenJPA must keep such a literal a single string value.
- **Entity field values** that the application persists, merges or uses for lookups.

A value from one of these sources that changes the structure of the SQL statement OpenJPA generates is a vulnerability in OpenJPA.

## Query Safety

Pass every untrusted value as a parameter:

```java
// Safe: the value is bound as a JDBC parameter
em.createQuery("SELECT c FROM Customer c WHERE c.name = :name", Customer.class)
  .setParameter("name", userInput)
  .getResultList();

// Unsafe: the value becomes part of the JPQL text
em.createQuery("SELECT c FROM Customer c WHERE c.name = '" + userInput + "'", Customer.class);
```

The same applies to the Criteria API (use `CriteriaBuilder.parameter` and bind the value) and to native queries (use `?1`, `?2` markers and `setParameter`).

If an application concatenates untrusted input into JPQL without escaping it, it has a JPQL injection problem. Through JPQL an attacker can read any mapped entity, and can make OpenJPA instantiate classes named in a `SELECT NEW` clause. Concatenating untrusted input into native SQL is SQL injection. Neither is a vulnerability in OpenJPA. When a query needs a dynamic sort order or a dynamic attribute, map the user's choice to a fixed set of attribute names in application code, or use `Path.get` in the Criteria API, which only accepts attributes known to the metamodel.

A bound value used with `LIKE` is still a pattern. Escape `%`, `_` and the escape character in untrusted input and use an `ESCAPE` clause, or the user can widen the match.

With the `openjpa.hint.UseLiteralInSQL` hint, literal values in a query, including values passed to the Criteria API other than through `CriteriaBuilder.parameter`, are written into the SQL text instead of being bound. Do not use this hint on queries that contain untrusted values other than bound parameters.

## Serialization

OpenJPA uses Java serialization in these places:

- Reading persistent fields that are mapped as serialized Java objects (for example a `Serializable` field stored in a BLOB column). The bytes come from the database.
- Receiving remote commit events in the TCP remote commit provider (see [Remote Commit Providers](#remote-commit-providers)).
- Reading the inner broker state of an `EntityManager` that the application deserializes. The outer stream belongs to the application.

On these paths OpenJPA checks class descriptors, and from 4.2.0 also the interface names of dynamic proxies, against a configurable list before the class is loaded. Accepted classes are initialized when they are resolved. The list is controlled by two JVM system properties, read once when the class is initialized:

- `openjpa.serialization.class.blacklist`: comma-separated class name prefixes to reject, or `*` to reject everything that is not whitelisted. The default contains three prefixes: `org.codehaus.groovy.runtime.`, `org.apache.commons.collections4.functors.` and `org.apache.xalan`. Most published gadget chains are not covered by it.
- `openjpa.serialization.class.whitelist`: comma-separated class name prefixes that are always accepted. It is empty by default.

From OpenJPA 4.0.1, a whitelisted name is always accepted, and any other name is rejected only if it matches the blacklist. A whitelist on its own does not restrict anything; to accept only listed classes, set the blacklist to `*` and list the needed prefixes in the whitelist. With `blacklist=*` the whitelist must cover every class descriptor that legitimately appears in the stream, including array descriptors such as `[B` (`byte[]`), JDK collection and wrapper types, OpenJPA's event and object id classes (`org.apache.openjpa.event.`, `org.apache.openjpa.util.`), the application's id classes, and every type stored in serialized fields.

**Upgrade note:** in 3.x and 4.0.0 a whitelist on its own acted as an allow list, and `blacklist=*` had no special meaning. If you upgrade from those releases and rely on a whitelist, also set `openjpa.serialization.class.blacklist=*`, or the whitelist has no effect.

This check is defence in depth, not a security boundary. A default deny list cannot list every gadget class on every class path, and OpenJPA does not install a JDK serialization filter (JEP 290). Deserializing data that an attacker controls is not safe, with or without the list. We recommend that deployers:

- Do not let untrusted parties write to columns that hold serialized Java objects or XML-mapped fields. Prefer explicit mappings (embeddables, converters, JSON text) over serialized fields.
- Configure an allow list with `blacklist=*` and a whitelist, or a JVM-wide filter with the `jdk.serialFilter` system property, or both.
- Never deserialize OpenJPA objects (`EntityManagerFactory`, `EntityManager`, detached entities with detached state, configuration) from an untrusted source. These objects carry their configuration, and OpenJPA configuration is code. Streams the application deserializes itself, for example for HTTP session replication or RMI, are outside OpenJPA's control and do not pass through OpenJPA's class list.
- Do not point a `CacheMarshaller` at a location that untrusted parties can write to. Its input is read with plain Java deserialization.

## Remote Commit Providers

OpenJPA can notify other JVMs about committed changes so that they evict stale entries from their L2 data and query caches. This is off by default: `openjpa.RemoteCommitProvider` has no default value. Any party that can send events to a node can affect the cache contents of that node, and the events are delivered to any `RemoteCommitListener` the application has registered. Received events are not written to the database. From 4.2.0, the type names in a received event are only resolved to persistent types of the persistence unit, and other names are ignored. A named class that is not yet known may be loaded through the persistence unit's class loader to find out whether it is persistent, but it is only initialized if it is. Every party that can send events must still be trusted.

### TCP provider

The TCP provider (`openjpa.RemoteCommitProvider=tcp(...)`) and every provider that extends it, including subclasses of `DynamicTCPRemoteCommitProvider` such as the Kubernetes provider, open a listening socket (port 5636 by default) and exchange events as Java serialized objects. The protocol has **no authentication and no encryption**, and the sender information in a message is not verified. In releases before 4.2.0, any host that can open a connection to the port is treated as a cluster member.

From 4.2.0, the listener only accepts connections from the hosts configured in `Addresses` and from the local host, unless `RestrictToPeers` is set to `false`. The Kubernetes provider sets it to `false` by default, because pods that are not ready yet already send events but are not listed as peers. This check compares IP addresses only. It is not authentication: hosts behind the same NAT gateway or on the same machine as a peer share its address, and peer host names are resolved when the addresses are set.

The TCP provider is meant only for a network that can be reached by the members of the cluster and nothing else. Deployers must:

- Restrict access to the port with a firewall, security group or Kubernetes NetworkPolicy so that only cluster members can connect. `RestrictToPeers` does not replace this.
- Bind the listener to the cluster-facing interface with the `BindAddress` property (available from 4.2.0). Earlier releases listen on all interfaces, so the firewall is the only control there.
- Configure the deserialization allow list described in [Serialization](#serialization), or a `jdk.serialFilter`.
- Not route this traffic over networks where it can be read or modified. Events contain entity class names and object ids.
- With the Kubernetes provider, control who can create pods with the configured label in the namespace, because every such pod becomes a peer and receives all events. Give the service account only the permission to list pods.

From 4.2.0, the number of receiving connections is limited by `MaxReceiveConnections` (100 by default), and accepted connections use TCP keep-alive so that connections from crashed peers are closed eventually. Earlier releases do not limit the number of connections. The provider does not limit message size or read time in any release, and a host that may connect can hold receiving connections open and use up the limit. Anyone who can reach the port can therefore consume threads and memory and evict cache entries. This is another reason the port must only be reachable by cluster members.

Applications that enable the TCP provider are responsible for these restrictions. [CVE-2024-54676](https://www.cve.org/CVERecord?id=CVE-2024-54676) (Apache OpenMeetings) is an example: the application's clustering setup enabled the TCP provider without configuring the class lists.

### JMS provider

The JMS provider (`openjpa.RemoteCommitProvider=jms(...)`) publishes events as JMS `ObjectMessage`s to a topic it looks up through JNDI. It opens no socket of its own. Received messages are deserialized by the JMS client library, not by OpenJPA, so OpenJPA's class list does not apply. Every principal that can publish to the topic is trusted. Use JMS rather than TCP when events must cross a network that is not limited to cluster members, and:

- enable authentication, authorization and TLS on the broker, and allow only the application nodes to publish to the topic;
- configure the JMS client's allow list for `ObjectMessage` payloads (for example the trusted packages setting of the broker client), or a `jdk.serialFilter`.

## Other Components

- **JMX instrumentation** (`openjpa.Instrumentation=jmx`) is off by default. When enabled, OpenJPA registers MBeans that expose cache statistics and query cache content and allow clearing caches. OpenJPA does not open a JMX connector. Whether these MBeans are reachable remotely, and with which credentials, depends on the JVM's JMX configuration, which is the deployer's responsibility.
- **JEST** (`openjpa-jest`) is a servlet that exposes a persistence unit over HTTP, including running JPQL queries supplied in the request and showing configuration properties. It has no authentication or authorization of its own. It is a development and diagnostic tool. Do not expose it to untrusted users; if it is deployed at all, the container or a reverse proxy must restrict access to it.
- **Slice** (`openjpa-slice`) opens no listener. It connects to each configured database over JDBC, and every slice is a trusted data store.
- **The XML store** (`openjpa-xmlstore`) and **fetch statistics** (`openjpa-fetch-statistics`) are samples and diagnostic tools, not production components.
- **Dynamic enhancement.** By default OpenJPA may try to attach an enhancement agent to the running JVM. We recommend enhancing classes at build time and setting `openjpa.DynamicEnhancementAgent=false` in production.

## Logging and Secrets

OpenJPA logs can contain SQL statements, JPQL text (including any user input an application has concatenated into a query), database error messages and, at TRACE level, the full configuration. Parameter values are shown as `?` in SQL logs unless `PrintParameters=true` is set on the connection factory.

Only `openjpa.ConnectionPassword` and `openjpa.Connection2Password` are masked when configuration is logged or returned. Credentials placed in `ConnectionURL`, `ConnectionProperties` or `ConnectionFactoryProperties` are not masked. They can appear in logs, in `EntityManagerFactory.getProperties()` and in the serialized form of OpenJPA objects. The serialized form of OpenJPA objects also contains the password in clear text; protect it like the configuration itself.

Deployers should:

- supply connections through a container-managed `DataSource`, or put the password only in `ConnectionPassword`;
- keep TRACE logging and `PrintParameters` off in production, and protect log files like any other sensitive data.

## Database Privileges and Schema Tools

The mapping tool, schema tool and schema generation build DDL from mapping metadata and can execute SQL scripts named in configuration (the `jakarta.persistence.schema-generation.*` script sources and `jakarta.persistence.sql-load-script-source`). With `openjpa.jdbc.SynchronizeMappings` or `jakarta.persistence.schema-generation.database.action` set, or with a load script configured, OpenJPA runs DDL or SQL when the `EntityManagerFactory` is created, using the runtime connection. We recommend using a separate account for schema changes, a runtime account limited to the data access the application needs, and leaving these properties unset (or `none`) in production.

## What Is and Is Not a Security Vulnerability

The following are **not** considered vulnerabilities in OpenJPA:

- Issues that require control over trusted inputs: any OpenJPA configuration source (including JVM system properties and property maps), plugin class names, mapping metadata, entity classes, the JDBC URL or driver properties, JNDI names, files and URLs named in configuration, or the build and class path. This includes loading arbitrary classes, writing files, executing SQL scripts, JNDI lookups and XML external entity resolution driven by such inputs.
- JPQL or SQL injection where the application concatenates untrusted input into query text without escaping it, or builds hints or function names from untrusted input.
- Attacks on the TCP remote commit provider port from hosts that are not cluster members, when the deployment exposes the port contrary to the guidance above. This includes denial of service through connections, threads, memory or cache eviction.
- Deserialization of data that the deployment lets untrusted parties write: serialized columns writable by untrusted parties, JMS topics they can publish to, `CacheMarshaller` files, or OpenJPA objects the application deserializes from untrusted streams. A weakness in the *default* deny list on its own (a gadget class that is not listed) is a hardening request, not a vulnerability.
- Access through JEST, when it is reachable by untrusted users, to the data, queries and configuration properties that its documented commands expose; and remote JMX access to OpenJPA MBeans.
- Information in logs, credentials placed in unmasked properties, and credentials in the serialized form of OpenJPA objects, as described in [Logging and Secrets](#logging-and-secrets).
- Resource consumption that is proportional to the data or the requests an attacker sends, or to the size of the result of a query the application chose to run.
- Vulnerabilities in the JDK, JDBC drivers, JMS brokers or other third-party dependencies themselves. Report those to the respective project. A request to upgrade a dependency with a public CVE can go to JIRA. If you have found that vulnerable code is reachable through OpenJPA in a way that is not public, report it privately to security@apache.org.

The following **are** considered vulnerabilities and should be reported privately:

- A value listed under [Untrusted Inputs](#untrusted-inputs) that changes the structure of the SQL OpenJPA generates.
- A class descriptor in a serialization stream that is resolved although a configured `blacklist=*` and whitelist reject it, on a deserialization path that uses OpenJPA's class list.
- For the remote commit providers deployed according to this page: the TCP listener opening when no provider is configured, or binding beyond `BindAddress` when it is set; or a received event causing database writes, code execution, or loading of classes rejected by a configured `blacklist=*` and whitelist.
- OpenJPA opening a network listener in its default configuration, or exposing masked credentials in log output, exception messages or `getProperties()`.
- Temporary files that OpenJPA creates on its own initiative (for example the dynamic enhancement agent jar) with permissions that let other local users read or replace them.
- Any other issue that compromises an application that uses OpenJPA as described on this page.

We also welcome hardening suggestions outside this scope, for example safer defaults, stricter parsing, or better masking of secrets. They are handled as regular improvements in JIRA.

## Questions About Known Security Problems

Questions about whether a published vulnerability affects your deployment, about published advisories, or about the availability of fixed releases should go to the OpenJPA [users or dev mailing list](https://openjpa.apache.org/mailing-lists.html).
