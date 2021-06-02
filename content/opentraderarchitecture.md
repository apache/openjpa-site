Title: OpenTraderArchitecture

<a name="OpenTraderArchitecture"></a>


State the design goals<br/>
Describe the architecture

One of the good practices of software development is to start with a set of
basic requirements and then express these requirements more formally
through a set the interfaces. So let us begin by listing the requirements
for OpenTrader sample.	

* a trader can offer to buy or sell stocks at a certain price 
* an offer to sell(buy) a stock can be matched with matching offer(s) to
buy(sell)
* a pair of matching buy/sell offer can be committed as a trade

Besides the functional requirements, let us define some non-functional
goals

* the trader will access the service from a browser
* the service will use a relational database to record the committed trades 

and then some purely technical goals

* the browser-based client will be implemented using Google Web Toolkit
* the service will be implemented using Java Persistence API





GWT takes a position that is a significantly unique among the multitude of
frameworks available to build a browser based client. GWT framework is
based on several key concepts:

* an asynchronous RPC protocol for communication between web client and
server. Such asynchronous RPC is popularized by AJAX (Asynchronous
JavaScript and XML) since last several years.
* a cross-compiler that converts Java to JavaScript. This is the most
critical component in the framework as it allows the client be written
completely in Java. Besides adding a comfort layer for Java developers, the
cross-compiler solves one of the most complex issue of browser based
clients namely cross-browser compatibility. The cross-compiler generates
separate JavaScript targeted to prominent browsers and the framework knows
to activate the appropriate JavaScript based on the particular browser a
client is using.
* a library of interactive visual widgets such as dialog boxes,
combo-boxes, tables etc. This Java based library realizes the widget as the
elements of a Document Object Model (DOM) for a browser to render them in
HTML. For example, an instance of com.google.gwt.user.client.ui.FlexTable
urns into a &lt;table&gt; in the displayed HTML page by the framework. The widget
library not only provides rendering support, it also comes with a event
dispatching model for the client application to handle the user
interaction.


OpenTrader - the sample example described in these pages - demonstrates how
to develop a GWT client for a transactional, server application based on
Java Persistence API (JPA). This example is somewhat more involved than a
typical AddressBook example in terms of the complexity of the domain model,
the transactional functions of the server as well as the interaction
between multiple widgets in the client. Also the sample application covers
a realistic use case where the core server application is defined
independent of both GWT and JPA – and then demonstrates how these two
technologies are used to implement an end-to-end service running inside a
Tomcat Servlet Container. 
