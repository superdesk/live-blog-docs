.. _Authentication:

Authentication
===================

#. Make a POST request to `Security/Authentication <http://doc.sd-demo.sourcefabric.org/resources/Security/Authentication>`_ with the following parameters:
   
   userName:
      <USERNAME>
   
   Example response:

   .. literalinclude:: examples/token.xml
      :language: xml  
 
#. Calculate an SHA-512 encrypted string using a combination of the token received in the previous step, the user name and the password. This example uses the `jsSHA library <https://github.com/Caligatio/jsSHA/>`_::

    shaPassword = new jsSHA(password, "ASCII");
    shaStep1 = new jsSHA(shaPassword.getHash("SHA-512", "HEX"), "ASCII");
    shaStep2 = new jsSHA(loginToken, "ASCII");
    HashedToken = shaStep1.getHMAC(username, "ASCII", "SHA-512", "HEX");            
    HashedToken = shaStep2.getHMAC(HashedToken, "ASCII", "SHA-512", "HEX");

   For example code in Python see :ref:`python-example`.

#. Make a POST request to `Security/Authentication/Login <http://doc.sd-demo.sourcefabric.org/resources/Security/Authentication/Login>`_ with the following parameters:

   Token: 
      <TOKEN>
   HashedToken: 
      <HASHED-TOKEN>

#. Use the session token from the response as a header for POST requests or as a parameter for GET requests that need authorization.

    param: 
       Authorization: <SESSION>

