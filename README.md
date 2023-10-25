## Random Password
Password generator for those of you who want to locally keep a piece of software 
which can generate a password for you. To run, simply execute the programme as 
per usual and type '1' or '2' followed by ENTER to tell the programme which 
option you would like to run. 

To run, first we cd to the directory where the file is kept and we run it like so:

```
python pasword_gen.py

```

Then, the programme will prompt:

```

has_uppercase =
        1. True
        2. False
        
> 
```

To proceed, type '1' or '2' followed by ENTER, depending on whether you want the 
password to include uppercase letters. Then the programme will prompt:

```
has_symbols =
        1. True
        2. False
>
```

Next, we do the same as above, but this time it'll be if you want to include special
characters such as '!', '@' and '#'. 

```
password_length =
```

This part will take an integer length greater than 0 to be your chosen length of 
password. Since I asked for a password of length 10 with capital letters and 
no special symbols, the programme returned

```
CbgifbZHou
```

which we can copy straight from the terminal. Enjoy!

# Security notice
Please remember this is repo is for the purpose of education only and
is not for the purpose of maintaining security. The passwords that you are making 
here are displayed on the screen in your terminal, so if you do not reset your terminal
window, the password you have generated is vulnerable to onlookers. 

Future improvements to this programme to improve security may be considered.

# Future ideas and notes
A goal for the future of this project is related to the above comments, which 
is to improve the security by saving the output of the password in a secure
form which is then accessed by the user and only the user.

This could involve entering the password for the laptop to access the file, or
by exporting it directly to a known password tool. 
