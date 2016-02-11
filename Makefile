
.PHONY: war
war:
	jar cf jygraph.war -C war .
	jar tvf jygraph.war

.PHONY: run
run:
	java -cp jetty-runner-8.1.16.v20140903.jar org.mortbay.jetty.runner.Runner jygraph.war
