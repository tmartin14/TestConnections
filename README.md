# TestOutboundConnections
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
