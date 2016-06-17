
<!--  <%@ page import="my.*" %>    -->

<html>
<head>
  <title>Connection Testing</title>
</head>
<body>
    <h2>Connection Testing</h2>
<p/>
<hr />
<p/>
<form method="get">
  What URL would you like to connect to?<br>
 <%
      String dest = "http://www.google.com:80";
      String[] args = request.getParameterValues("dest");
      if (args != null) {
         dest = args[0];
      } 
 %>
    <input type="text" name="dest" size="100" value="<%= dest %>">
    <br><br>
    <input type="submit" value="Submit">
</form>

 <%
  if (args != null) 
     {
       out.println(" <hr><h3>Response:</h3> ");
       try{ 
            my.BasicHttpsClient.main(args);
            out.println("Successful Connection to " + dest);
       }catch(Exception exp){
            out.println("Error:  Could not reach: " + dest + "<br><br>" + exp);
       }
    }
 %>

<hr />
<a href="<%= request.getRequestURI() %>">Reset</a>
<hr />
</body>
</html>
