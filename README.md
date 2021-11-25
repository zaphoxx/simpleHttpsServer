# simpleHttpsServer
Simple Python Based Https Server As Sink For Pentests

In order to make this work you will need to create your own CA and signed server certificate. There is plenty of instructions to google for. e.g. https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/  or  https://www.akadia.com/services/ssh_test_certificate.html.

---------------------------------------------------------------------------------------------------------------------------------------------------
From https://stackoverflow.com/questions/21297139/how-do-you-sign-a-certificate-signing-request-with-your-certification-authority/21340898#21340898

Sometimes, such as for testing, you just want a simplistic means of generating a signed certificate, without setting up a full-blown CA configuration. This is possible using just the openssl req and openssl x509 commands. You would never use this method for production certificates, but since it is useful for some non-production situations, here are the commands.

Generate a self-signed signing certificate
First, create a self-signed certificate that will be used as the root of trust:
```
openssl req -x509 -days 365 -key ca_private_key.pem -out ca_cert.pem
```
Or equivalently, if you want to generate a private key and a self-signed certificate in a single command:
```
openssl req -x509 -days 365 -newkey rsa:4096 -keyout ca_private_key.pem -out ca_cert.pem
```
Generate a certificate request
Next, create a certificate request for the certificate to be signed:
```
openssl req -new -key my_private_key.pem -out my_cert_req.pem
```
Again, you may generate the private key and the request simultaneously, if needed:
```
openssl req -new -newkey rsa:4096 -keyout my_private_key.pem -out my_cert_req.pem
```
Generate a signed certificate
Finally, use the self-signed signing certificate to generate a signed certificate from the certificate request:
```
openssl x509 -req -in my_cert_req.pem -days 365 -CA ca_cert.pem -CAkey ca_private_key.pem -CAcreateserial -out my_signed_cert.pem
```
