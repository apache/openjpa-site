Title: Detached State Serialization

# Detached State Serialization

## Symptom:

OpenJPA requires persistence entities to be enhanced to support JPA semantics. If the client and server are in
two separate JVMs and entities are serialized/de-serialized in the transport layer, one may encountered
the following problem when:

 * entities are **NOT** enhanced on the client,
 * &lt;property name="openjpa.DetachState" value="fetch-groups(DetachedStateField=true)"/&gt; is specified for the persistence context.

&#20;

    [err] javax.jms.MessageFormatException: CWSIA0122E: An exception occurred deserializing a message, exception: \ 
            java.io.InvalidClassException: com.ibm.wssvt.acme.annuity.common.bean.jpa.AbstractPersistebleObject; \
            Serializable incompatible with Externalizable.
    [err]     at com.ibm.ws.sib.api.jms.impl.JmsObjectMessageImpl.getObject(JmsObjectMessageImpl.java:271)
    [err]     at com.ibm.wssvt.acme.annuity.business.impl.ejb30mdb.AcmeAnnuityMgmtSvcEJB30MDBBean.validateInputMessage \
                  (AcmeAnnuityMgmtSvcEJB30MDBBean.java:173)
    [err]     at com.ibm.wssvt.acme.annuity.business.impl.ejb30mdb.AcmeAnnuityMgmtSvcEJB30MDBBean.onMessage \
                  (AcmeAnnuityMgmtSvcEJB30MDBBean.java:67)
    [err]     at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    [err]     at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:60)
    [err]     at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:37)
    [err]     at java.lang.reflect.Method.invoke(Method.java:611)
    [err]     at [internal classes]
    [err] Caused by: 
    [err] java.io.InvalidClassException: com.ibm.wssvt.acme.annuity.common.bean.jpa.AbstractPersistebleObject; \
            Serializable incompatible with Externalizable
    [err]     at java.io.ObjectStreamClass.initNonProxy(ObjectStreamClass.java:647)
    [err]     at java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:1600)
    [err]     at java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1513)
    [err]     at java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:1600)
    [err]     at java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1513)
    [err]     at java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:1600)
    [err]     at java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1513)
    [err]     at java.io.ObjectInputStream.readOrdinaryObject(ObjectInputStream.java:1749)
    [err]     at java.io.ObjectInputStream.readObject0(ObjectInputStream.java:1346)
    [err]     at java.io.ObjectInputStream.defaultReadFields(ObjectInputStream.java:1964)
    [err]     at java.io.ObjectInputStream.readSerialData(ObjectInputStream.java:1888)
    [err]     at java.io.ObjectInputStream.readOrdinaryObject(ObjectInputStream.java:1770)
    [err]     at java.io.ObjectInputStream.readObject0(ObjectInputStream.java:1346)
    [err]     at java.io.ObjectInputStream.readObject(ObjectInputStream.java:365)
    [err]     at com.ibm.ws.sib.api.jms.impl.JmsObjectMessageImpl.getObjectInternal(JmsObjectMessageImpl.java:344)
    [err]     at [internal classes]
    [err]     ... 22 more

## Solution

When `DetachedStateField=true` option is specified, the client application intends to take advantage of the detached entity 
field update management feature provided by OpenJPA. This requires entities to be enhanced and OpenJPA runtime
be accessible by the application. If application does not have or require the enhanced entity or OpenJPA runtime
on the client side, `DetachedStateField=[false|transient]` option should be used.
 
See [DetachedStateField options](http://ci.apache.org/projects/openjpa/trunk/docbook/manual.html#ref_guide_detach_graph) section for
details of the `DetachedStateField` options as well the enhancement and runtime requirements.  