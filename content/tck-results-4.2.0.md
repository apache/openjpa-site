Title: OpenJPA 4.2.0 TCK Results

# Jakarta Persistence 3.2 TCK Results for OpenJPA 4.2.0

Apache OpenJPA 4.2.0 passes the Jakarta Persistence 3.2 TCK on PostgreSQL, MySQL, MariaDB, Microsoft SQL Server,
Oracle and Apache Derby.

## Summary

- Product: Apache OpenJPA 4.2.0, [downloads](downloads.html)
- Specification: [Jakarta Persistence 3.2](https://jakarta.ee/specifications/persistence/3.2/)
- TCK: Jakarta Persistence TCK 3.2.0,
  [jakarta-persistence-tck-3.2.0.zip](https://download.eclipse.org/jakartaee/persistence/3.2/jakarta-persistence-tck-3.2.0.zip),
  SHA-256 `db74101c3f52f737f57804271ea9c845cb1941f2a0685284c54c4ad4fa1f05c7`
- TCK challenges: none
- Runner: `openjpa-integration/tck/run-tck32.sh` of the
  [4.2.0 tag](https://github.com/apache/openjpa/tree/4.2.0/openjpa-integration/tck), GlassFish 8.0.0
- Java: Eclipse Temurin 21.0.13+9 (OpenJDK 64-Bit Server VM), test JVM `-Xmx4g`
- Build: Apache Maven 3.9.16
- OS: Ubuntu 26.04.1 LTS, Linux 7.0.0, x86_64, locale `C`
- Hardware: Intel Core i7-6700 (4 cores, 8 threads), 32 GB RAM
- Run: 2026-11-17 to 2026-11-18, three full TCK runs per database

## Results

Each run has 2135 tests. The 4 skipped tests are disabled in the TCK itself.

| Database | Version | Run | Passed | Failed | Errors | Skipped |
|---|---|---|---|---|---|---|
| PostgreSQL | 15.19 | 1 / 2 / 3 | 2131 / 2131 / 2131 | 0 / 0 / 0 | 0 / 0 / 0 | 4 / 4 / 4 |
| MySQL | 8.4.8 | 1 / 2 / 3 | 2131 / 2131 / 2131 | 0 / 0 / 0 | 0 / 0 / 0 | 4 / 4 / 4 |
| MariaDB | 12.3.3 | 1 / 2 / 3 | 2131 / 2131 / 2131 | 0 / 0 / 0 | 0 / 0 / 0 | 4 / 4 / 4 |
| Apache Derby | 10.17.1.0 (network server) | 1 / 2 / 3 | 2131 / 2131 / 2131 | 0 / 0 / 0 | 0 / 0 / 0 | 4 / 4 / 4 |
| Microsoft SQL Server | 2017 CU12 (14.0.3045.24) | 1 / 2 / 3 | 2131 / 2130 / 2131 | 0 / 0 / 0 | 0 / 1 / 0 | 4 / 4 / 4 |
| Oracle Database Free | 23.26.3.0.0 | 1 / 2 / 3 | 2131 / 2130 / 2131 | 0 / 0 / 0 | 0 / 1 / 0 | 4 / 4 / 4 |

On SQL Server and Oracle one of the three runs had an error in `core.types.datetime.Client#dateTimeTest`; the test
passed in the two other runs on these databases and in all runs on the other databases.

## Notes

- The databases ran in Docker on the same host (images `postgres:15`, `mysql:8.4.8`, `mariadb:12.3`,
  `mcr.microsoft.com/mssql/server:2017-CU12-ubuntu`, `gvenzl/oracle-free:23-slim`); Derby is the network server
  bundled with GlassFish.
- The OpenJPA jar was built from the 4.2.0 tag (SHA-256
  `2feeadde49cc7a6fc2a976482d5896dcfe0a0a7f271bd2385229a66a6cdba541`).
- The runs had a JDBC listener attached that counts the SQL statements per test; it does not change the result of
  any test.
