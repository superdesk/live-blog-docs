Authentication
===================

   1. Make a POST request to :base_url:/Security/Authentication with the following parameters:
   
   userName:
      <USERNAME>
   
   The response is a token.
 
   2. Calculate the HashedToken as an SHA-512 encrypted token using the Token received in the previous step:

   .. code:: javascript	

            shaPassword = new jsSHA(password, "ASCII"),         
            shaStep1 = new jsSHA(shaPassword.getHash("SHA-512", "HEX"), "ASCII"),
            shaStep2 = new jsSHA(loginToken, "ASCII"),          
            HashedToken = shaStep1.getHMAC(username, "ASCII", "SHA-512", "HEX");            
            HashedToken = shaStep2.getHMAC(HashedToken, "ASCII", "SHA-512", "HEX");

   2. Make POST request to :base_url:/Security/Authentication/Login with the following parameters:

   Token: 
      <TOKEN>
   HashedToken: 
      <HASHED-TOKEN>

   The response is a session.

in js:

All authenificated requested must have on HEADER or on GET
        param: Authorization: <SESSION>

