import sys
import os
import getopt
global AdminConfig

#-----------------------------------------------------------------
# WARNING: Jython/Python is extremely sensitive to indentation
# errors. Please ensure that tabs are configured appropriately
# for your editor of choice.
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# daytrader_singleServer.py - DayTrader Single Server Install Script
#-----------------------------------------------------------------
#
# This script is designed to configure the JDBC and JMS resource required by
# the DayTrader application and to install the application.

#---------------------------------------------------------------------
#  Usage info
#---------------------------------------------------------------------

def printUsageAndExit ():
    # start of print block
	print """
	
Usage: wsadmin -f <location of>daytrader_singleServer.py <options> where 
         <options> is zero or more of the following
   --help              Display this usage information.
   --prompt            Whether or not to prompt for input. Valid values are:
                          true (default)
                          false
   -a, --action action Action to perform. Valid values are:
                          all (default) - configures JDBC and JMS resources 
                             and installs the app
                          configure - only configure the JDBC and JMS resource
                          cleanup - remove the JDBC and JMS resources
                          install - install the DayTrader ear
                          uninstall - uninstall the DayTrader ear
   -e, --earfile ear   The location of the earfile to install when the
                       action is 'all' or 'install'. The default
                       is 'daytrader-ear-2.1.3.ear' located in the same
                       directory from which wsadmin is being run.
                       (Note: This is only used for the 'all' or
                       'install' action.)                         
   -s, --security sec  The current status of security. Valid values are:
                          disabled (default)
                          enabled
                       The --userid and --password options are required if 
                       security is enabled.
                       (Note: This is only used for the 'all' or
                       'configure' action.)
   -u, --userid userid The administrative userid to use for JMS. This is
                       required if --security is enabled.
   --password pw       The administrative password to use for JMS. This is
                       required if --security is enabled.
	
	"""
	# end of print block

	sys.exit()
#endDef 

#-----------------------------------------------------------------
# getInput - Obtain generic input from the user. If default value
#            provided, return default value if nothing is entered.
#-----------------------------------------------------------------
def getInput (prompt, defaultValue):
	print ""
	print prompt
	retValue = sys.stdin.readline().strip() 
	if (retValue == ""):
		retValue = defaultValue
	#endIf

	return retValue
#endDef

#-----------------------------------------------------------------
# getValidInput - Obtain valid input from the user based on list of
#            valid options. Continue to query user if the invalid
#            options are entered. Return default value if nothing
#            is entered.
#-----------------------------------------------------------------
def getValidInput (prompt, defaultValue, validOptions):
	validate = 1     

	while (validate):
		print ""
		print prompt
		retValue = sys.stdin.readline().strip()

		if (retValue == ""):
			retValue = defaultValue
			validate = 0
		#endIf
                
		if (validate and validOptions.count(retValue) > 0):
			# Is retValue one of the valid options
			validate = 0
		else:
			print "Response not valid"
		#endIf
	#endWhile

	return retValue
#endDef

#-----------------------------------------------------------------
# getName - Return the base name of the config object.
#-----------------------------------------------------------------
def getName (objectId):
	endIndex = (objectId.find("(c") - 1)
	stIndex = 0
	if (objectId.find("\"") == 0):
		stIndex = 1
	#endIf
	return objectId[stIndex:endIndex+1]
#endDef

#-----------------------------------------------------------------
# getNodeId - Return the node id of the existing node if in a single
#           server environment. If in an ND environment query the
#           user to determine desired node.
#-----------------------------------------------------------------
def getNodeId (prompt):
	nodeList = AdminConfig.list("Node").split("\n")

	if (len(nodeList) == 1):
		node = nodeList[0]
	else:
		print ""
		print "Available Nodes:"
                
		nodeNameList = []

		for item in nodeList:
			item = item.rstrip()
			name = getName(item) 

			nodeNameList.append(name)
			print "   " + name
		#endFor

		DefaultNode = nodeNameList[0]
		if (prompt == ""):
			prompt = "Select the desired node"
		#endIf

		nodeName = getValidInput(prompt+" ["+DefaultNode+"]:", DefaultNode, nodeNameList )

		index = nodeNameList.index(nodeName)
		node = nodeList[index]
	#endElse

	return node
#endDef

#-----------------------------------------------------------------
# getServerId - Return the server id of the existing server if
#           in a single server environment. If in an ND environment
#           query the user to determine desired server.
#-----------------------------------------------------------------
def getServerId (prompt):
	serverList = AdminConfig.list("Server").split("\n")

	if (len(serverList) == 1):
		server = serverList[0]
	else:
		print ""
		print "Available Servers:"
		
		serverNameList = []                

		for item in serverList:
			item = item.rstrip()
			name = getName(item)

			serverNameList.append(name)
			print "   " + name
		#endFor

		DefaultServer = serverNameList[0]
		if (prompt == ""):
			prompt = "Select the desired server"
		#endIf                
		serverName = getValidInput(prompt+" ["+DefaultServer+"]:", DefaultServer, serverNameList )

		index = serverNameList.index(serverName)
		server = serverList[index]
	#endElse

	return server
#endDef

#-----------------------------------------------------------------
# createJAASAuthData - Create a new JAAS Authentication Alias if
#            one with the same name does not exist. Otherwise,
#            return the existing Authentication Alias.
#-----------------------------------------------------------------
def createJAASAuthData ( aliasName, user, passwd ):
	print " "
	print "Creating JAAS AuthData " + aliasName + "..."

	# Check if aliasName already exists
	authDataAlias = ""
	authList = AdminConfig.list("JAASAuthData" )
	if (len(authList) > 0):
		for item in authList.split("\n"):
			item = item.rstrip()
			alias = AdminConfig.showAttribute(item, "alias" )
			if (alias == aliasName):
				authDataAlias = item
				break
			#endIf
		#endFor
	#endIf

	# If authAlias does not exist, create a new one

	if (authDataAlias == ""):
		print "  Alias Name: " + aliasName
		print "  User:       " + user
		print "  Password:   " + passwd

		attrs = AdminConfig.list("Security")
		attrs0 = [["alias", aliasName], ["userId", user], ["password", passwd]]
                
		authDataAlias = AdminConfig.create("JAASAuthData", attrs, attrs0)
                
		print aliasName + " created successfully!"
	else:
		print aliasName + " already exists!"
	#endElse

	return authDataAlias
#endDef

#---------------------------------------------------------------------
# removeJAASAuthData
#---------------------------------------------------------------------
def removeJAASAuthData (name):
	print " "
	print "Removing JAAS AuthData " + name + "..."

	authList = AdminConfig.list("JAASAuthData")
	auth = ""
	if (len(authList) > 0):
		for item in authList.split("\n"):
			item = item.rstrip()
			ident = AdminConfig.showAttribute(item.rstrip(), "alias" )
			if (ident == name):
				auth = item
				break
			#endIf
		#endFor
	#endIf

	if (auth != ""):
		AdminConfig.remove(auth)
		print name + " removed successfully!"
	else:
		print name + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createJDBCProvider - Create a new JDBC Provider if one with the
#            same name does not exist in the specified scope. Otherwise,
#            return the existing JDBCProvider. The 3 types or providers
#            currently supported include DB2 JCC, DB2 CLI, and Oracle.
#-----------------------------------------------------------------
def createJDBCProvider (provider, XA, scopeId, path, nativePath):
	
	XA = XA.lower()
	
	name = "Derby JDBC Provider"
	if (XA == "true"):
		name = "Derby JDBC Provider Only (XA)"
	#endIf

	print " "
	print "Creating JDBC Provider " + name + "..."

	# Check if the JDBC provider already exists	

	scopeName = getName(scopeId)
	stIndex = (scopeId.find("|") + 1)
	endIndex = (scopeId.find(".") - 1)
	scope = scopeId[stIndex:endIndex+1]

	providerId = ""
	if (scope == "cell"):
		providerId = AdminConfig.getid("/Cell:"+scopeName+"/JDBCProvider:\""+name+"\"/" )
	elif (scope == "node"):
		providerId = AdminConfig.getid("/Node:"+scopeName+"/JDBCProvider:\""+name+"\"/" )
	elif (scope == "server"):
		providerId = AdminConfig.getid("/Server:"+scopeName+"/JDBCProvider:\""+name+"\"/" )
	#endIf

	if (providerId == ""):
		print "  Provider Name:        " + name
		print "  Classpath:            " + path
		print "  Native path:          " + nativePath
		print "  XA enabled:           " + XA

		template = AdminConfig.listTemplates("JDBCProvider", name+"(")
		providerId = AdminConfig.createUsingTemplate("JDBCProvider", scopeId, [["name", name], ["classpath", path], ["nativepath", nativePath]], template)

		# Template creates a datasource with the same name as the provider
		# Delete this datasource
		dsId = ""
		dsList = AdminConfig.list("DataSource")
		if (len(dsList) > 0):
			for item in dsList.split("\n"):
				item = item.rstrip()
				provider = AdminConfig.showAttribute(item, "provider" )
				if (providerId == provider):
					dsId = item
					print "Found DS"
				#endIf
			#endFor
		#endIf
		if (dsId != ""):
			AdminConfig.remove(dsId)
		#endIf

		print name + " provider created successfully!"
	else:
		print name + " provider already exists!"
	#endElse

	return providerId
#endDef

#-----------------------------------------------------------------
# removeJDBCProvider
#-----------------------------------------------------------------
def removeJDBCProvider(name):
	print " "
	print "Removing JDBCProvider " + name + "..."

	temp = AdminConfig.getid("/JDBCProvider:" + name + "/")
	if (temp):
		AdminConfig.remove(temp)
		print name + " removed successfully!"
	else:
		print name + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createDatasource
#-----------------------------------------------------------------
def createDatasource (datasourceName, jndiName, stmtCacheSz, authAliasName, providerId):
	# Connection pool properties
	maxConnections =    50
	minConnections =    10

	print " "
	print "Creating DataSource " + datasourceName + "..."
	
	# Check if the DataSource already exists
	dsId = ""
	dsList = AdminConfig.getid("/DataSource:" + datasourceName + "/")
	if (len(dsList) > 0):
		for item in dsList.split("\n"):
			item = item.rstrip()
			provider = AdminConfig.showAttribute(item, "provider" )
			if (providerId == provider):
				dsId = item
			#endIf
		#endFor
	#endIf

	if (dsId == ""):
		print "  Datasource Name:       " + datasourceName
		print "  JNDI Name:             " + jndiName
		print "  Statement Cache Size:  " + str(stmtCacheSz)	
		print "  AuthAliasName:         " + authAliasName
		
		# Map provider to datasource template
		providerName = getName(providerId)
		
		providerToDsDict = {"Derby JDBC Provider Only":"Derby JDBC Driver DataSource",
			"Derby JDBC Provider Only (XA)":"Derby JDBC Driver XA DataSource"}

		dsName = providerToDsDict[providerName]
		
		#template =  AdminConfig.listTemplates("DataSource", dsName)
		template="Derby JDBC Driver XA DataSource(templates/system|jdbc-resource-provider-templates.xml#DataSource_Derby_2)"
		attr = [["name", datasourceName], ["jndiName", jndiName], ["statementCacheSize", stmtCacheSz]]
		if (authAliasName != ""):
			attr.append(["authDataAlias", authAliasName])
		#endIf
		dsId = AdminConfig.createUsingTemplate("DataSource", providerId, attr, template)

		#Update connection pool sizings
		pool = AdminConfig.showAttribute(dsId, "connectionPool")
		AdminConfig.modify(pool, [["maxConnections", maxConnections], ["minConnections", minConnections]])

		#Determine RRA
		tempName = providerId[providerId.rfind("/")+1 : providerId.rfind("|")]
		if (providerId.find("/servers/") > 0):
			radapter = AdminConfig.getid("/Server:" + tempName + "/J2CResourceAdapter:WebSphere Relational Resource Adapter/")
		elif (providerId.find("/nodes/") > 0):
			radapter = AdminConfig.getid("/Node:" + tempName + "/J2CResourceAdapter:WebSphere Relational Resource Adapter/")
		elif (providerId.find("(cells/") > 0):
			radapter = AdminConfig.getid("/Cell:" + tempName + "/J2CResourceAdapter:WebSphere Relational Resource Adapter/")
		#endIf
		
		#Create CMPConnectionFactory
		tempList = AdminConfig.listTemplates('CMPConnectorFactory','default')
		template = ""
		if (len(tempList) > 0):
			for item in tempList.split("\n"):
				item = item.rstrip()
				if (item[0:20] == "CMPConnectorFactory("):
					template = item
					break
				#endIf
			#endFor
		#endIf
		
		attr = [["name", datasourceName + "_CF"], ["cmpDatasource", dsId]]
		cmpFact_id = AdminConfig.createUsingTemplate("CMPConnectorFactory", radapter, attr, template)

		print datasourceName + " created successfully!"
	else:
		print datasourceName + " already exists in this JDBC Provider!"
	#endIf

	return dsId
#endDef

#-----------------------------------------------------------------
# addDatasourceProperty
#-----------------------------------------------------------------

def addDatasourceProperty (datasourceId, name, value):
    parms = ["-propertyName", name, "-propertyValue", value]
    AdminTask.setResourceProperty(datasourceId, parms)
#endDef 

#-----------------------------------------------------------------
# updateDB2orDerbyDatasource
#-----------------------------------------------------------------
def updateDB2orDerbyDatasource (datasourceId, dbname, hostname, port, driverType):
	resourceProps = AdminConfig.list("J2EEResourceProperty", datasourceId).split("\n")
	for item in resourceProps:
		item = item.rstrip()
		propName = getName(item)
		if (propName == "serverName"):
			AdminConfig.modify(item, [["value", hostname]])
		#endIf
		if (propName == "portNumber"):
			AdminConfig.modify(item, [["value", port]])
		#endIf
		if (propName == "databaseName"):
			AdminConfig.modify(item, [["value", dbname]])
		#endIf
		if (propName == "driverType"):
			AdminConfig.modify(item, [["value", driverType]])
		#endIf
	#endFor
#endDef

#-----------------------------------------------------------------
# removeDatasource
#-----------------------------------------------------------------
def removeDatasource(name):
	print " "
	print "Removing DataSource " + name + "..."

	temp = AdminConfig.getid("/DataSource:" + name + "/")
	if (temp):
		AdminConfig.remove(temp)
		print name + " removed successfully!"
	else:
		print name + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createSIBus - Create a new SIBus if one does not exist. Otherwise,
#            return the existing SIBus.
#-----------------------------------------------------------------
def createSIBus ( busName, authAlias ):
	print " "
	print "Creating SIBus " + busName + "..."

	# Check if the SIBus already exists

	SIBus = AdminConfig.getid("/SIBus:"+busName+"/" )
	if (SIBus == ""):
		parms = ["-bus", busName, "-interEngineAuthAlias", authAlias]
		SIBus = AdminTask.createSIBus(parms )
                
		print busName + " created successfully!"
	else:
		print busName + " already exists!"
	#endElse

	return SIBus
#endDef

#-----------------------------------------------------------------
# deleteSIBus
#-----------------------------------------------------------------
def deleteSIBus(name):
	print " "
	print "Deleting SIBus " + name + "..."

	temp = AdminConfig.getid("/SIBus:" + name + "/")
	if (temp):
		parms = ["-bus", name]
		AdminTask.deleteSIBus(parms)
		print name + " removed successfully!"
	else:
		print name + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createSIBusSecurityRole - Add user role
#-----------------------------------------------------------------
def createSIBusSecurityRole ( busId, userName ):
	print " "
	busName = getName(busId)

	# Check if the SIBAuthUser already exists
	SIBAuthUser = ""
	tmpSIBAuthUserList = AdminConfig.list("SIBAuthUser", busId)
	if (len(tmpSIBAuthUserList) > 0):
		for item in tmpSIBAuthUserList.split("\n"):
			item = item.rstrip()
			tmp = AdminConfig.showAttribute(item, "identifier" )
			if (tmp == userName):
				SIBAuthUser = item
			#endIf
		#endFor
	#endIf

	if (SIBAuthUser == ""):
		print "Creating SIBus security role for " + userName + "..."
                
		parms = ["-bus", busName, "-user", userName]
		SIBAuthUser = AdminTask.addUserToBusConnectorRole(parms )
               
		print userName + " security role created successfully!"
	else:
		print "Role " + userName + " already exists for " + busName + "!"
	#endElse

	return SIBAuthUser
#endDef

#-----------------------------------------------------------------
# addSIBusMember - Add the specified server or cluster to the
#            SIBus if it does not already exist. Assumes that the
#            specified SIBus already exists.
#-----------------------------------------------------------------
def addSIBusMember ( busId, fileStore, targetArgs, dataStoreArgs ):
	#    busName          - SIBus name
	#    fileStore [0]    - create file store, otherwise create data store
 	#    fileStore [1]    - logDirectory - directory where fileStore is located (only used if fileStore[0] = true)
	#    targetArgs[0]    - cluster name or node name
	#    targetArgs[1]    - server name
	#    dataStoreArgs[0] - defaultDS - create default DS (true|false)
	#    dataStoreArgs[1] - dsJndi - jndi name of the datastore (only used if defaultDS = false)

	busName = getName(busId)
	if (len(targetArgs) == 1):
		clusterName = targetArgs[0]
		nodeName = "dummy"
		serverName = "dummy"
	else:
		nodeName = targetArgs[0]
		serverName = targetArgs[1]
		clusterName = "dummy"
	#endElse

	if (len(dataStoreArgs) == 2):
		defaultDS = dataStoreArgs[0]
		dsJndi = dataStoreArgs[1]
		defaultDS = defaultDS.lower()
	#endIf

	# Check if the bus member already exists
	parms = ["-bus", busName]
	busMembers = AdminTask.listSIBusMembers(parms).split("\n")
	member = ""
	if (busMembers[0] != ""):
		for item in busMembers:
			item = item.rstrip()
			cluster = AdminConfig.showAttribute(item, "cluster" )
			node = AdminConfig.showAttribute(item, "node" )
			server = AdminConfig.showAttribute(item, "server" )

			if (cluster == clusterName  or ( server == serverName  and node == nodeName ) ):
				member = item
				break
			#endIf
		#endFor
	#endIf
	
	if (member == ""):
		print ""
		if (len(targetArgs) == 1):
			print "Adding SIBus member " + clusterName + "..."
			parms = ["-bus", busName, "-cluster", clusterName]
		else:
			print "Adding SIBus member " + nodeName + " - " + serverName + "..."
			parms = ["-bus", busName, "-node", nodeName, "-server", serverName]
		#endElse

		print "  File Store:            " + fileStore[0]
		if (fileStore[0] == "true"):
			parms.append("-fileStore")
			if (fileStore[1] != "default" and fileStore[1] != ""):
				print "  File Store Location:   " + fileStore[1]
				parms.append("-logDirectory")
                        	parms.append(fileStore[1])
			#endIf
		else:
			parms.append("-dataStore")
			print "  Default DataSource:    " + defaultDS
			parms.append("-createDefaultDatasource")
			parms.append(defaultDS)
			if (defaultDS == "false"):
				print "  Datasource JNDI Name:  " + dsJndi
				parms.append("-datasourceJndiName")
				parms.append(dsJndi)
			#endIf
		#endElse

		member = AdminTask.addSIBusMember(parms )
		print "SIBus member added successfully!"
	else:
		print "SIBus member already exists!"
	#endElse

	return member
#endDef

#-----------------------------------------------------------------
# createSIBDestination - Create a new SIB Destination if one with the same
#            name does not exist on the specified SIBus. Otherwise,
#            return the existing Destination.
#-----------------------------------------------------------------
def createSIBDestination ( busId, destName, destType, reliability, optArgs ):
	#    SIBus       - SIBus name
	#    destName    - destination name
	#    destType    - destination type
	#    reliability - reliability
	#    optArgs[0]  - cluster name or node name
	#    optArgs[1]  - server name

	if (len(optArgs) == 1):
		clusterName = optArgs[0]
	elif (len(optArgs) == 2) :
		nodeName = optArgs[0]
		serverName = optArgs[1]
	#endElse

	print " "
	print "Creating SIB Destination " + destName + "..."

	# Check if the SIB Destination already exists
	SIBus = getName(busId)
	parms = ["-bus", SIBus]
	destList = AdminTask.listSIBDestinations(parms )

	dest = ""
	if (len(destList) > 0):
		for item in destList.split("\n"):
			item = item.rstrip()
			ident = AdminConfig.showAttribute(item.rstrip(), "identifier" )
			if (ident == destName):
				dest = item.rstrip()
				break
			#endIf
		#endFor
	#endIf

	if (dest == ""):        
		print "  Destination Name:  " + destName
		print "  Destination Type:  " + destType
		print "  Reliability:       " + reliability
                
		parms = ["-bus", SIBus, "-name", destName, "-type", destType, "-reliability", reliability]

		if (destType == "Queue"):
			if (len(optArgs) == 1):
				print "  Cluster Name:      " + clusterName
				parms.append("-cluster")
				parms.append(clusterName)
			elif (len(optArgs) == 2):
				print "  Node Name:         " + nodeName
				print "  Server Name:       " + serverName
				parms.append("-node")
				parms.append(nodeName)
				parms.append("-server")
				parms.append(serverName)
			#endElse
		#endIf

		dest = AdminTask.createSIBDestination(parms )
                
		print destName + " created successfully!"
	else:
		print destName + " already exists!"
	#endElse

	return dest
#endDef

#-----------------------------------------------------------------
# deleteSIBDestination
#-----------------------------------------------------------------
def deleteSIBDestination(name):
	print " "
	print "Deleting SIB Destination " + name + "..."

	destList = AdminConfig.list("SIBDestination")
	dest = ""
	if (len(destList) > 0):
		for item in destList.split("\n"):
			item = item.rstrip()
			ident = AdminConfig.showAttribute(item.rstrip(), "identifier" )
			if (ident == name):
				dest = item
				break
			#endIf
		#endFor
	#endIf

	if (dest != ""):
		bus = dest[dest.rfind("/")+1 : dest.rfind("|")]
		parms = ["-bus", bus, "-name", name]
		AdminTask.deleteSIBDestination(parms)
		print name + " removed successfully!"
	else:
		print name + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createJMSConnectionFactory - Create a new JMS Connection Factory
#            if one with the same name does not exist on the SIBus.
#            Otherwise, return the existing Connection Factory.
#-----------------------------------------------------------------
def createJMSConnectionFactory ( busId, cfName, cfType, jndiName, authAlias, scope ):
	# Create JMS Connection Factory
	#    SIBus      - SIBus name
	#    cfName     - connection factory name
	#    cfType     - connection factory type
	#    jndiName   - connection factory jndi name
	#    authAlias  - authentication alias name
	#    scope      - scope

	print " "
	print "Creating JMS " + cfType + " Connection Factory " + cfName + "..."

	# Check if the connection factory already exists

	parms = ["-type", cfType]
	cfList = AdminTask.listSIBJMSConnectionFactories(scope, parms )
	connectionFactory = ""
	if (len(cfList) > 0):
		for item in cfList.split("\n"):
			item = item.rstrip()
			if (item.find(cfName) >= 0):
				connectionFactory = item
				break
			#endIf
		#endFor
	#enfIf

	if (connectionFactory == "" ):
		print "  Connection Factory Name:  " + cfName
		print "  Connection Factory Type:  " + cfType
		print "  JNDI Name:                " + jndiName

		params = ["-name", cfName, "-jndiName", jndiName, "-busName", getName(busId), "-type", cfType, "-authDataAlias", authAlias]
		connectionFactory = AdminTask.createSIBJMSConnectionFactory(scope, params )
                
		print cfName + " created successfully!"
	else:
		print cfName + " already exists!"
	#endElse

	return connectionFactory
#endDef

#-----------------------------------------------------------------
# deleteJMSConnectionFactory
#-----------------------------------------------------------------
def deleteJMSConnectionFactory(name):
	print " "
	print "Deleting JMS Connection Factory " + name + "..."

	temp = AdminConfig.getid("/J2CConnectionFactory:" + name + "/")
	if (temp):
		AdminTask.deleteSIBJMSConnectionFactory(temp)
		print name + " removed successfully!"
	else:
		print name + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createJMSQueue - Create a new JMS Queue if one with the same
#            name does not exist at the specified scope. Otherwise,
#            return the existing JMS Queue.
#-----------------------------------------------------------------
def createJMSQueue ( qName, jndiName, SIBDest, delMode, scope ):
	#    qName    - queue name
	#    jndiName - queue jndi name
	#    SIBDest  - SIB destination
	#    delMode  - delivery mode
	#    scope    - scope

	print " "
	print "Creating JMS Queue " + qName + "..."

	# Check if the queue already exists

	qList = AdminTask.listSIBJMSQueues(scope )
	queue = ""
	if (len(qList) > 0):
		for item in qList.split("\n"):
			item = item.rstrip()
			if (item.find(qName) >= 0):
				queue = item
				break
			#endIf
		#endFor
	#endIf

	if (queue == ""):
		print "  Queue Name:       " + qName
		print "  JNDI Name:        " + jndiName
		print "  SIB Destination:  " + SIBDest
		print "  Delivery Mode:    " + delMode

		params = ["-name", qName, "-jndiName", jndiName, "-queueName", SIBDest, "-deliveryMode", delMode]
		queue = AdminTask.createSIBJMSQueue(scope, params )
                
		print qName + " created successfully!"
	else:
		print qName + " already exists!"
	#endElse

	return queue
#endDef

#-----------------------------------------------------------------
# deleteJMSQueue
#-----------------------------------------------------------------
def deleteJMSQueue(queueName):
	print " "
	print "Deleting JMS Queue " + queueName + "..."

	temp = AdminConfig.getid("/J2CAdminObject:" + queueName + "/")
	if (temp):
		AdminTask.deleteSIBJMSQueue(temp)
		print queueName + " removed successfully!"
	else:
		print queueName + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createJMSTopic - Create a new JMS Topic if one with the same
#            name does not exist at the specified scope. Otherwise,
#            return the existing JMS Topic.
#-----------------------------------------------------------------
def createJMSTopic ( tName, jndiName, tSpace, delMode, scope ):
	#    tName    - topic name
	#    jndiName - topic jndi name
	#    tSpace   - topic space
	#    delMode  - delivery mode
	#    scope    - scope

	print " "
	print "Creating JMS Topic " + tName + "..."

	# Check if the topic already exists

	tList = AdminTask.listSIBJMSTopics(scope )
	topic = ""
	if (len(tList) > 0):
		for item in tList.split("\n"):
			item = item.rstrip()
			if (item.find(tName) >= 0):
				topic = item
				break
			#endIf
		#endFor
	#endIf

	if (topic == ""):
		print "  Topic Name:     " + tName
		print "  JNDI Name:      " + jndiName
		print "  Topic Space:    " + tSpace
		print "  Delivery Mode:  " + delMode

		params = ["-name", tName, "-jndiName", jndiName, "-topicName", tName, "-topicSpace", tSpace, "-deliveryMode", delMode]
		topic = AdminTask.createSIBJMSTopic(scope, params )
                
		print tName + " created successfully!"
	else:
		print tName + " already exists!"
	#endElse

	return topic
#endDef

#-----------------------------------------------------------------
# deleteJMSTopic
#-----------------------------------------------------------------
def deleteJMSTopic(topicName):
	print " "
	print "Deleting JMS Topic " + topicName + "..."

	temp = AdminConfig.getid("/J2CAdminObject:" + topicName + "/")
	if (temp):
		AdminTask.deleteSIBJMSTopic(temp)
		print topicName + " removed successfully!"
	else:
		print topicName + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# createMDBActivationSpec - Create a new MDB Activation Spec if one
#            with the same name does not exist at the specified
#            scope. Otherwise, return the existing Activation Spec.
#-----------------------------------------------------------------
def createMDBActivationSpec ( mdbName, jndiName, busId, JMSDestJndi, destType, authAlias, scope, durability ):
	#    mdbName     - MDB name
	#    jndiName    - activation spec jndi name
	#    SIBus       - SIBus name
	#    JMSDestJndi - JMS destination JNDI name
	#    destType    - destination type
	#    authAlias   - authentication alias name
	#    scope       - scope
	#    durability  - subscriptionDurability

	print " "
	print "Creating MDB Activation Spec " + mdbName + "..."

	# Check if the activation spec already exists

	asList = AdminTask.listSIBJMSActivationSpecs(scope )
	mdb = ""
	if (len(asList) > 0):
		for item in asList.split("\n"):
			item = item.rstrip()
			if (item.find(mdbName) >= 0):
				mdb = item
				break
			#endIf
		#endFor
	#endIf

	if (mdb == ""):
		print "  MDB Activation Spec Name:   " + mdbName
		print "  JNDI Name:                  " + jndiName
		print "  JMS Destination JNDI Name:  " + JMSDestJndi
		print "  Destination Type:           " + destType

		SIBus = getName(busId)
		params = ["-name", mdbName, "-jndiName", jndiName, "-busName", SIBus, "-destinationJndiName", JMSDestJndi, "-destinationType", destType, "-authenticationAlias", authAlias, "-subscriptionDurability", durability, "-clientId", mdbName, "-subscriptionName", mdbName]
		mdb = AdminTask.createSIBJMSActivationSpec(scope, params )
                
		print mdbName + " created successfully!"
	else:
		print mdbName + " already exists!"
	#endElse

	return mdb
#endDef

#-----------------------------------------------------------------
# deleteMDBActivationSpec
#-----------------------------------------------------------------
def deleteMDBActicationSpec (mdbName):
	print " "
	print "Deleting MDB Activation Spec " + mdbName + "..."

	temp = AdminConfig.getid("/J2CActivationSpec:" + mdbName + "/")
	if (temp):
		AdminTask.deleteSIBJMSActivationSpec(temp)
		print mdbName + " removed successfully!"
	else:
		print mdbName + " not found!"
	#endElse
#endDef

#-----------------------------------------------------------------
# installApp - Install the specified application ear file if an
#            application with the same name does not exist.
#-----------------------------------------------------------------
def installApp ( appName, ear, deployejb, deployws, defaultBindings, earMetaData, dbType, target ):
	#    appName         - application name
	#    ear             - ear file
	#    deployejb       - deploy ejb (true|false)
	#    deployws        - deploy webservices (true|false)
	#    defaultBindings - use default binding (true|false)
	#    earMetaData     - use MetaData from ear (true|false)
	#    dbType          - ejb deploy db type
	#    target[0]       - node name or cluster name
	#    target[1]       - server name

	print ""
	print "Installing application " + appName + "..."
	
	deployejb = deployejb.lower()
	deployws = deployws.lower()
	defaultBindings = defaultBindings.lower()
	earMetaData = earMetaData.lower()

	# Check if the application already exists
	app = ""
	appList = AdminApp.list( )
	if (len(appList) > 0):
		for item in appList.split("\n"):
			item = item.rstrip()
			if (item.find(appName) == 0):
				app = item
				break
			#endIf
		#endFor
	#endIf

	if (app == ""):
		print "  Application Name:      " + appName
		print "  Ear file:              " + ear
		if (len(target) == 1):
			cluster = target[0]
			print "  Target Cluster:        " + cluster
		else:
			node = target[0]
			server = target[1]
			print "  Target Node:           " + node
			print "  Target Server:         " + server
		#endElse
		print "  Deploy EJB:            " + deployejb
		print "  Deploy WebServices:    " + deployws
		print "  Use default bindings:  " + defaultBindings
		print "  Use Ear MetaData:      " + earMetaData
		print "  Deployed DB Type:      " + dbType

		parms = "-appname " + appName
		if (deployejb == "true"):
			parms += " -deployejb"
			parms += " -deployejb.dbtype " + dbType
		else:
			parms += " -nodeployejb"
		#endElse
		if (deployws == "true"):
			parms += " -deployws"
		else:
			parms += " -nodeployws"
		#endElse
		if (defaultBindings == "true"):
			parms += " -usedefaultbindings"
		#endIf
		if (earMetaData == "true"):
			parms += " -useMetaDataFromBinary"
		else:
			parms += " -nouseMetaDataFromBinary"
		#endElse

		if (len(target) == 1):
			parms += " -cluster " + cluster
		else:
			parms += " -node " + node + " -server " + server
		#endElse

		parms1 = [parms]

		print "Starting application install..."

		app = AdminApp.install(ear, parms1 )

		print "Install completed successfully!"
	else:
		print appName + " already exists!"
	#endElse

	return app
#endDef

#-----------------------------------------------------------------
# uninstallApp - Uninstall the specified application if it exists.
#-----------------------------------------------------------------
def uninstallApp ( appName ):
	#    appName - application name

	print ""
	print "Uninstalling application..."

	# Check if the application does not exist
	app = ""
	appList = AdminApp.list( )
	if (len(appList) > 0):
		for item in appList.split("\n"):
			item = item.rstrip()
			if (item.find(appName) >= 0):
				app = item
				break
			#endIf
		#endFor
	#endIf

	if (app != ""):
		AdminApp.uninstall(appName )

		print "Application uninstalled successfully!"
	else:
		print "Application does not exist!"
	#endElse
#endDef

#-----------------------------------------------------------------
# start processing
#-----------------------------------------------------------------
print ""
print "daytrader_singleServer.py"

# Edit this parameter to switch between Interactive and Silent installs
SilentInstall = "false"

#---------------------------------------------------------------------
# Default Properties for Silent Install
#
# Edit the variables in this section to perform a silent install. 
#---------------------------------------------------------------------

# Silent install properties for Managed Node
# - Modify these properties to specify the target node and server
TargetNodeName =   "nodeName"
TargetServerName = "serverName"
# - Or uncomment the following lines to detect the server and node names
#TargetNodeName =   getName(getNodeId(""))
#TargetServerName = getName(getServerId(""))


# Security options
# Note: If global security is enabled or will be enabled at some point and
#   time, the AdminAuthAlias should be updated with a valid administrative
#   userid and password. In single-server configurations, this can be provided
#   by role-based auth (default), local OS auth, LDAP, etc. For cluster 
#   configurations, LDAP, Windows Active Directory or some other form of 
#   centralized authentication mechanism must be used to validate the userid.
SecurityEnabled = "false"
DefaultAdminUser =   "AdminUserID"
DefaultAdminPasswd = "password"

# JDBC provider options
DefaultProviderType =   "Derby"
DefaultPathName =       "${DERBY_JDBC_DRIVER_PATH}/derby.jar"
DefaultNativePathName = ""

# Datasource options
DefaultDatabaseName = "tradedb"
DefaultHostname =     "localhost"
DefaultPort =         "50000"
DefaultUser =         "userid"
DefaultPasswd =       "password"

# Additional defaults for vendor specific Datasources
#DefaultIfxLockMode =   "60"
#DefaultIfxServerName = "ifxServerName"
#DefaultOraclePort =    "1521"
DefaultDB2DriverType = "4"

# Deploy options
# Deploy types include:
#   "DB2UDB_V82","DB2UDBOS390_V8","DB2UDBISERIES_V54","DERBY_V10","MSSQLSERVER_2005","ORACLE_V10G","INFORMIX_V100"
DefaultEJBDeployType = "DERBY_V10"

# JMS Messaging Engine Datastore options
# Note: true - file store will be used
#       false - database data store will be used
DefaultMEFileStore = "true"
DefaultMEFileStoreLocation = "default" 


#---------------------------------------------------------------------
#  Misc options
#---------------------------------------------------------------------

CmdOptions =      ["all", "configure", "cleanup", "install", "uninstall"]
DefaultOptions =  ["yes", "no"]
BooleanOptions =  ["true", "false"]
ProviderOptions = ["DB2 Universal","DB2 iSeries (Toolbox)","DB2 iSeries (Native)","Derby","Oracle","Embedded MS SQL Server","Informix"]
DeployOptions =   ["DB2UDB_V82","DB2UDBOS390_V8","DB2UDBISERIES_V54","DERBY_V10","MSSQLSERVER_2005","ORACLE_V10G","INFORMIX_V100"]


#---------------------------------------------------------------------
# Application specific config information
#
# NOTE: This should NOT be modified!!!
#---------------------------------------------------------------------

DefaultTradeAppName = "DayTrader"
DefaultEarFile = "daytrader-ear-2.1.3.ear"

# Deployment options
DefaultRunEJBDeploy = "false"
DefaultRunWSDeploy =  "false"
DefaultBindings =     "true"
DefaultUseMetadata =  "true"

# JDBC Driver and DataSource Config Parameters
# Datasource properties
DefaultDatasourceName = "TradeDataSource"
DefaultDatasourceAuthAliasName =  "TradeDataSourceAuthData"
DefaultNoTxDatasourceName = "NoTxTradeDataSource"

DefaultStmtCacheSize =  60
DefaultXA = "true"

# JMS (Messaging) Config Parameters
# Global Security properties for JMS
DefaultAdminAuthAliasName = "TradeAdminAuthData"

#reliability = "ASSURED_PERSISTENT"
reliability = "EXPRESS_NONPERSISTENT"

#deliveryMode = "Persistent"
deliveryMode = "NonPersistent"

#durability = "Durable"
durability = "NonDurable"

# Queue/Topic Names
brokerSIBDest =  "TradeBrokerJSD"
topicSpace =     "Trade.Topic.Space"
brokerJMSQCF =   "TradeBrokerQCF"
streamerJMSTCF = "TradeStreamerTCF"
brokerQueue =    "TradeBrokerQueue"
streamerTopic =  "TradeStreamerTopic"
brokerMDB =      "TradeBrokerMDB"
streamerMDB =    "TradeStreamerMDB"


#---------------------------------------------------------------------
# Common JDBC Driver Paths 
#---------------------------------------------------------------------
# Note: wsadmin parses the command line based on ";" regardless of platform type
#DB2WinJccPath =         "c:/sqllib/java/db2jcc.jar;c:/sqllib/java/db2jcc_license_cu.jar;"
#DB2zSeriesNativePath =  "/usr/lpp/db2/db2810/jcc/lib"
#DB2CliPath =            "c:/sqllib/java/db2java.zip"
#OraclePath =            "c:/oracle/product/10.1.0/db_1/jdbc/lib/ojdbc14.jar"
#DerbyPath =             "$\{WAS_INSTALL_ROOT\}/derby/lib/derby.jar"
#DB2iSeriesNativePath =  "/QIBM/ProdData/Java400/ext/db2_classes.jar"
#DB2iSeriesToolboxPath = "/QIBM/ProdData/HTTP/Public/jt400/lib/jt400.jar"

validActions = ["all", "configure", "cleanup", "install", "uninstall"]
validSecurity = ["enabled", "disabled"]
validPrompt = ["true", "false"]



#---------------------------------------------------------------------
# Parse command line options
#---------------------------------------------------------------------
try:
	opts, args = getopt.getopt(sys.argv[0:], "a:s:u:e:", ["action=", "security=", "userid=", 
		"password=", "earfile", "prompt=", "help"])
	#opts, args = getopt.getopt(sys.argv[1:], "a:", ["action="])
except getopt.GetoptError, err:
	print str(err)
	# usage()
	sys.exit()
#endTry	

action = "all"
#SecurityEnabled = "false"
#DefaultAdminUser =   "AdminUserID"
#DefaultAdminPasswd = "password"
#DefaultPort = "5000"
#SilentInstall = "false"
prompt = "true"
operation = "all"
useridProvided = "false"
passwordProvided = "false"

for opt, arg in opts:
	if opt == "--help":
		printUsageAndExit()
	elif opt in ("-a", "--action"):
		print "action - " + arg
		if arg in validActions:
			operation = arg
		else:
			print "invalid action: '" + arg + "'"
			printUsageAndExit()
	elif opt in ("-e", "--earfile"):
		DefaultEarFile = arg
	elif opt in ("-s", "--security"):
		print "security - " + arg
		if arg in validSecurity:
			if arg == "enabled":
				SecurityEnabled = "true"
			else:
				SecurityEnabled = "false"
		else:
			print "invalid security value: '" + arg + "'"
			printUsageAndExit()
	elif opt in ("-u", "--userid"):
		print "userid - " + arg
		useridProvided = "true"
		DefaultAdminUser = arg
	elif opt in ("-p", "--password"):
		print "password - " + arg
		passwordProvided = "true"
		DefaultAdminPasswd = arg			
	elif opt == "--prompt":
		print "prompt - " + arg
		if arg in validPrompt:
			prompt = arg
		else:
			print "invalid prompt value: '" + arg + "'"
			printUsageAndExit()
	else:
		print "invalid option: '" + opt + "'"
		sys.exit()
	#endIfElse
#endFor

if SecurityEnabled == "true":
	if useridProvided == "false":
		print ""
		print "Error: --userid must be specified when security is enabled"
		printUsageAndExit()
	#endIf
	if passwordProvided == "false":
		print ""
		print "Error: --password must be specified when security is enabled"
		printUsageAndExit()
	#endIf
#endIf

if prompt == "true":
	operation = getValidInput("Action: (all | configure | cleanup | install | uninstall) ["+operation+"]:", operation, validActions)
#endIf

if (prompt == "true" and (operation == "all" or operation == "install")):
	DefaultEarFile = getInput("Please enter the ear file location [" + DefaultEarFile + "]:", DefaultEarFile)
#endIf

print ""
print "------------------------------------------------"
print " Daytrader Install/Configuration Script"
print ""
print " Action:  " + operation
print "------------------------------------------------"

#---------------------------------------------------------------------
# Daytrader configuration procedures
#---------------------------------------------------------------------

scope = ""

if (SilentInstall == "false" and ( operation == "configure" or operation == "all") ):
	if prompt == "true":
		SecurityEnabled = getValidInput("Global security is (or will be) enabled (true|false) ["+SecurityEnabled+"]:", SecurityEnabled, BooleanOptions )

	# Obtain node name and id for scope
	print "------------------------------------------------"
	print " Collecting Single Server or Managed Server Info"
	print "" 
        
	node = getNodeId("")
	TargetNodeName = getName(node )
	scope = node

	server = getServerId("")
	TargetServerName = getName(server )

	print " Node:   " + TargetNodeName
	print " Server: " + TargetServerName
	print "------------------------------------------------"

	if (SecurityEnabled == "true" and prompt == "true"):
		print "-------------------------------------------------"
		print " Collecting Security Information for JMS"
		print " "
		print " Note: The supplied authentication data must"
		print "  correspond to a valid administrative username"
		print "  and password."
		print "-------------------------------------------------"

		DefaultAdminUser = getInput("Please enter a valid administrative username ["+DefaultAdminUser+"]:", DefaultAdminUser )
		DefaultAdminPasswd = getInput("Please enter a valid administrative password ["+DefaultAdminPasswd+"]:", DefaultAdminPasswd )
	#endIf
#endIf 

if (operation == "all" or operation == "configure"):
	# Create the JDBC/Datasource config objects
	
	if (scope == ""):
		#scope = AdminConfig.getid("/Node:"+TargetNodeName+"/Server:"+TargetServerName+"/")
		# By default, we normally use Node scope
		scope = AdminConfig.getid("/Node:"+TargetNodeName+"/")
	#endIf

	print ""
	print "------------------------------------------------"
	print " Configuring JDBC/Datasource Resources"
	print " Scope: "+scope
	print "------------------------------------------------"

	createJAASAuthData(DefaultDatasourceAuthAliasName, DefaultUser, DefaultPasswd )

	provider = createJDBCProvider(DefaultProviderType, DefaultXA, scope, DefaultPathName, DefaultNativePathName )

	datasource = createDatasource(DefaultDatasourceName, "jdbc/"+DefaultDatasourceName, DefaultStmtCacheSize, DefaultDatasourceAuthAliasName, provider)
	noTxDatasource = createDatasource(DefaultNoTxDatasourceName, "jdbc/"+DefaultNoTxDatasourceName, 10, DefaultDatasourceAuthAliasName, provider)
	addDatasourceProperty(noTxDatasource, "nonTransactionalDataSource", "true")

	#if (DefaultProviderType.find("DB2") >= 0 or DefaultProviderType == "Derby"):
	updateDB2orDerbyDatasource(datasource, DefaultDatabaseName, DefaultHostname, DefaultPort, DefaultDB2DriverType)
	updateDB2orDerbyDatasource(noTxDatasource, DefaultDatabaseName, DefaultHostname, DefaultPort, DefaultDB2DriverType)

	print ""
	print "------------------------------------------------"
	print " JDBC Resource Configuration Completed!!!"
	print "------------------------------------------------"

	# Create the JMS config objects

	print ""
	print "------------------------------------------------"
	print " Configuring JMS Resources"
	print " Scope: "+scope
	print "------------------------------------------------"

	createJAASAuthData(DefaultAdminAuthAliasName, DefaultAdminUser, DefaultAdminPasswd )

	sibus = createSIBus(getName(scope ), DefaultAdminAuthAliasName )
	fileStore = [DefaultMEFileStore, DefaultMEFileStoreLocation]
	target = [TargetNodeName, TargetServerName]
	dsParms = ["true", "dummy"]
	addSIBusMember(sibus, fileStore, target, dsParms)

	if (SecurityEnabled == "true"):
		createSIBusSecurityRole(sibus, DefaultAdminUser )
	#endIf 

	# Create the Trade Broker Queue and Trade TopicSpace Destinations

	createSIBDestination(sibus, brokerSIBDest, "Queue", reliability, target )
	createSIBDestination(sibus, topicSpace, "TopicSpace", reliability, [] )

	createJMSConnectionFactory(sibus, brokerJMSQCF, "Queue", "jms/"+brokerJMSQCF, DefaultAdminAuthAliasName, scope )
	createJMSConnectionFactory(sibus, streamerJMSTCF, "Topic", "jms/"+streamerJMSTCF, DefaultAdminAuthAliasName, scope )

	createJMSQueue(brokerQueue, "jms/"+brokerQueue, brokerSIBDest, deliveryMode, scope )
	createJMSTopic(streamerTopic, "jms/"+streamerTopic, topicSpace, deliveryMode, scope )

	createMDBActivationSpec(brokerMDB, "eis/"+brokerMDB, sibus, "jms/"+brokerQueue, "javax.jms.Queue", DefaultAdminAuthAliasName, scope, durability )
	createMDBActivationSpec(streamerMDB, "eis/"+streamerMDB, sibus, "jms/"+streamerTopic, "javax.jms.Topic", DefaultAdminAuthAliasName, scope, durability )

	print ""
	print "------------------------------------------------"
	print " JMS Resource Configuration Completed!!!"
	print "------------------------------------------------"
	
	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf 


#---------------------------------------------------------------------
# Daytrader install procedures
#---------------------------------------------------------------------

if (operation == "all" or operation == "install"):
	print " "
	print "------------------------------------------------"
	print " Installing DayTrader"
	print "------------------------------------------------"

	if (SilentInstall == "false" and operation == "install"):
		TargetNodeName = getName(getNodeId(""))
		TargetServerName = getName(getServerId(""))
        
		#print "Deploy options include the following:"
		#for deploy in DeployOptions:
		#	print " " + deploy
		##endFor
		#DefaultEJBDeployType = getValidInput("Select the EJB deployment target ["+DefaultEJBDeployType+"]:", DefaultEJBDeployType, DeployOptions)
	#endIf 

	target = [TargetNodeName, TargetServerName]

	installApp(DefaultTradeAppName, DefaultEarFile, DefaultRunEJBDeploy, DefaultRunWSDeploy, DefaultBindings, DefaultUseMetadata, DefaultEJBDeployType, target )

	print ""
	print "------------------------------------------------"
	print " DayTrader Installation Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf

if (operation == "uninstall"):
	print " "
	print "------------------------------------------------"
	print " Uninstalling DayTrader"
	print "------------------------------------------------"

	uninstallApp(DefaultTradeAppName)

	print ""
	print "------------------------------------------------"
	print " DayTrader Uninstall Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf

if (operation == "cleanup"):
	print " "
	print "------------------------------------------------"
	print " Uninstalling JMS Resources"
	print "------------------------------------------------"

	deleteMDBActicationSpec(brokerMDB)
	deleteMDBActicationSpec(streamerMDB)

	deleteJMSQueue(brokerQueue)
	deleteJMSTopic(streamerTopic)

	deleteJMSConnectionFactory(brokerJMSQCF)
	deleteJMSConnectionFactory(streamerJMSTCF)

	deleteSIBDestination(brokerSIBDest)
	deleteSIBDestination(topicSpace)

	deleteSIBus(getName(getNodeId("")))

	removeJAASAuthData(DefaultAdminAuthAliasName)

	print " "
	print "------------------------------------------------"
	print " Uninstalling JDBC Resources"
	print "------------------------------------------------"

	removeDatasource(DefaultDatasourceName)
	removeDatasource(DefaultNoTxDatasourceName)
	removeJAASAuthData(DefaultDatasourceAuthAliasName)

	print ""
	print "------------------------------------------------"
	print " DayTrader Resource Cleanup Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf

print ""
print "Saving config..."
AdminConfig.save( )


