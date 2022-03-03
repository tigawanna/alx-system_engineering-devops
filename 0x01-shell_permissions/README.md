# Shell permisions
0. su betty
1. whoami
3. groups $whoami
4. sudo chown betty hello
5. touch hello
6. chmod 764 hello
7. chmod 554 hello
8. chmod 555 hello
9. chmod 707 hello
10. chmod 753 hello
11. chmod --reference=hello olleh
12. find . -type d -exec chmod 700 {} +
13.  mkdir -m700 my_dir
14. chgrp school hello
15. sudo chown -R vincent:staff *
16. chown -h vincent:staff _helllo
17.  sudo chown -R --from=guillaume betty *
18.  telnet towel.blinkenlights.nl  
remember test to see if they work first
