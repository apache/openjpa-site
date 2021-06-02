Title: Verifying release signatures

On unix platforms the following command can be executed : 

    for file in `find . -type f -iname '*.asc'`
    do
        gpg --verify ${file} 
    done


You'll need to look at the output contains only good signaturesie :

            gpg: Good signature from "Michael Dick (CODE SIGNING KEY) <mikedd@apache.org>"
            gpg: Signature made Tue 12 Jan 2010 05:30:17 PM CST using RSA key ID 7412AD2C
            gpg: Good signature from "Michael Dick (CODE SIGNING KEY) <mikedd@apache.org>"
            gpg: Signature made Tue 12 Jan 2010 05:30:18 PM CST using RSA key ID 7412AD2C
            gpg: Good signature from "Michael Dick (CODE SIGNING KEY) <mikedd@apache.org>"
            gpg: Signature made Tue 12 Jan 2010 05:30:17 PM CST using RSA key ID 7412AD2C
            gpg: Good signature from "Michael Dick (CODE SIGNING KEY) <mikedd@apache.org>"

