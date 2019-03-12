#!/bin/bash
set -e

# Usage: $ ./prepare_for_release.py <type>
# type - [major | minor | patch]. Default is patch.

get_current_package_version()
{
  echo $(python ./setup.py --version)
}

set_next_package_version() {
  # The {new_version} is not a bash variable - it's a bumpversion notation for the new version.
  # Please see bumpversion --help for more information.
  bumpversion --current-version $1 --commit --tag --tag-name {new_version} $2 ./setup.py
}

update_package_version()
{
  type=${2}
  if [ -z "${type}" ]
  then
      echo "defaulting to 'patch'"
      type="patch"
  else
      echo "update type is: ${type}"
  fi

  version=$(get_current_package_version)
  echo "Upgrading version from the current version of ${version}"
  set_next_package_version ${version} ${type}
}

update_package_version $1
