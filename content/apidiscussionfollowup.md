Title: APIDiscussionFollowUp

<a name="APIDiscussionFollowUp"></a>


After our meeting, Patrick did some analysis of our current API and where
we might want to take it. Here are some initial observations. Please
comment as appropriate.

* OpenJPAEntityManager extends EntityTransaction; should it?

    - clr no, I like your idea below to add an OpenJPAEntityTransaction
      interface, so users could do OpenJPAEntityTransaction tx =
      (OpenJPAEntityTransaction)em.getTransaction();

* StoreCache, QueryResultCache, Extent, FetchPlan, Generator, OpenJPAQuery
all have getDelegate() calls that return an underlying kernel
implementation detail. Maybe these should be pushed down to theh impl
classes only?

    - clr I agree these don't belong in OpenJPAEntityManager

* OpenJPAEntityManager and OpenJPAEntityManagerFactory both have a
getConfiguration() method. Maybe this should be pushed down to the impl
classes only?

    - clr I don't know when I would use the Configuration, so no opinion on this
one.

* OpenJPAEntityManager.getManagedRuntime() should be pushed down to impl
only

    - clr I agree

* The following methods in OpenJPAPersistence return things that are not
currently part of what I consider a user-focused API:

        toBrokerFactory()
        toBroker()
        toEntityManagerFactory()
        toEntityManager()
        getMetaData()
  
    - clr I agree. 

* We have a bunch of methods in OpenJPAEntityManager that seem like they
should belong on a new OpenJPAEntityTransaction interface:

        public void commitAndResume();
        public void rollbackAndResume();
        public void setRollbackOnly(); (already part of EntityTransaction)
        public void setRollbackOnly(Throwable cause);
        public Throwable getRollbackCause();
        public boolean isStoreActive();
        public void setSavepoint(String name);
        public void rollbackToSavepoint();
        public void rollbackToSavepoint(String name);
        public void releaseSavepoint();
        public void preFlush();
  
    - clr All of these seem like transaction-focused methods that belong in
OpenJPAEntityTransaction...
    - pcl: I moved the commit / rollback / rollbackOnly stuff into
OpenJPAEntityTransaction, but things are trickier for the rest of the
methods: you can only call EM.getTransaction() when not in a JTA context,
and these other methods are valuable in a JTA env as well as a non-JTA env.
So, we can either leave them on OpenJPAEM or create some other interface
for them.


* I don't like the OpenJPAEntityManager.setLargeTransaction() method name -
I'd like to rename it to setTrackChangesByType() instead, since it better
reflects what the method does. (We can easily deprecate the old method if
desired.)

    - clr I kinda like setLargeTransaction. It's more "task-oriented". 
pcl: The thing is that if you are using large transactions, you might want
to call either (or both) setLargeTx() and setPopulateDataCache(), depending
on the nature of the tx workload.

* I think that it might make sense to move
OpenJPAEntityManager.setPopulateDataCache() to FetchPlan, and rename
FetchPlan.setQueryResultCache() to setPopulateQueryResultCache(). (We can
easily deprecate the old methods if desired.)

    - clr No opinion here.
