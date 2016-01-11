#!/usr/bin/env sh
# make the script fail for any failed command
set -e
# make the script display the commands it runs to help debugging failures
set -x

# build site
[ ! -e "sculpin.phar" ] && curl -O https://download.sculpin.io/sculpin.phar
php sculpin.phar install
php sculpin.phar generate --env=prod
