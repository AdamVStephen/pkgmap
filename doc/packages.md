# Package Manager Tips

## Package Management Overview.

Linux distributions comprise the aggregation of a very large number of open source projects.  Some are managed directly with
a particular distribution and package manager.  Some support several package managers.  In some cases, distribution packages
supply curation services to upstream projects.

## Yum.

For full fat yum capability install yum-utils.  

show-installed
find-repos-of-install "package"

yum search "package"

Description of package including license and package URL

yum info "package"

Package to install file

yum provides "/path/to/file"

Files installed by package

repoquery -l "package"

Cheat sheet links

https://access.redhat.com/sites/default/files/attachments/rh_yum_cheatsheet_1214_jcs_print-1.pdf

# Distributions

The two main families are the RedHat/Centos/Fedora group which use rpm/yum, and the Debian/Ubuntu stable which use apt.
Honorable mentions go to Arch and the like which generally pull projects from source and build on demand.

# Packages and Projects
## libxml


