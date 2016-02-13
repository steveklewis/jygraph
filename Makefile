
.PHONY: war
war:
	jar cf jygraph-war.war -C warpack .
	jar tvf jygraph-war.war

.PHONY: run
run:
	java -cp jetty-runner-8.1.16.v20140903.jar org.mortbay.jetty.runner.Runner jygraph-war.war

.PHONY: install
install:
	~/2jython2.7.0/bin/jython setup.py install
