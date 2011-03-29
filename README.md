Code for parsing emails and extracint data


This is a repo of sample emails, and the python code parses the headers and body
to extract IPP addresses from the headers, and domains from the body.  In order
to determine the TLD's, we use the Publis Suffix List provided at
http://publicsuffix.org/

This site also makes available a set of C code in the regdom-libs
http://www.dkim-reputation.org/regdom-libs/ which will return a registered
domain name to us if theh TLD is known.  

The version of the code in my repo comments out the cases 1 and 3, so that no
result is returned when we have an unknown domain, or an error.. 


