# TestConnections
A simple Java application to test connectivity from your application server to the outside world on http and https.

Simply enter your proxy parameters and you should be all set

```
JAVA_OPTS="-Dhttp.proxyHost=proxy.youcompany.com -Dhttp.proxyPort=80 -Dhttps.proxyHost=proxy.yourcompany.com -Dhttps.proxyPort=443"
```  

That's it.  

If you see Exceptions, something's not quite right.

## Basic test case

```
$ ./test.sh http://www.google.com
```

(to create the WAR file try "jar cvf TestConnections.war *")

---
## Additional Fun
This repo contains one additional file, [Connection-Testing.txt](./Connection-Testing.txt), that includes several shell script files inside of a single file.  These scripts can be used to test Splunk connectivity to New Relic and AppDynamics APIs. You will see separate files for Python 2.7 and Python 3.x, support for specifying a proxy and setting your authenticaton parameters.  This file should make troubleshooting Splunk connections to these data sources a lot easier.