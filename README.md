# fedora-docker-gccgo
Fedora docker(and BR) specfiles modified to use gcc-go

docker.spec and docker-gccgo.patch are for docker package 
based on:
http://pkgs.fedoraproject.org/cgit/docker.git/commit/?id=08156ff8df61b2325b3a07cc81cc8706f76931db

remaining spec files are for their respective packages.

golang-github-cpuguy83-go-md2man.spec
based on:
http://pkgs.fedoraproject.org/cgit/golang-github-cpuguy83-go-md2man.git/commit/?id=b2bac60c5fb19012d0a49b57f5bb0894efc3591d

golang-github-russross-blackfriday.spec
based on:
http://pkgs.fedoraproject.org/cgit/golang-github-russross-blackfriday.git/commit/?id=6b58d861f832c5bf3b6675c494d669b24affa5c0

golang-github-shurcooL-sanitized_anchor_name.spec
based on:
http://pkgs.fedoraproject.org/cgit/golang-github-shurcooL-sanitized_anchor_name.git/commit/?id=dd60acb3f89c65b2764a865c2168d4c38a8f6f27


(All are based on master branch, and you need to rebuild packages in reverse order than they are listed here.)

COPR repo for Fedora 22(23):
https://copr.fedoraproject.org/coprs/jcajka/docker-gccgo/
