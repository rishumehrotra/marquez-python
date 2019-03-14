#!/bin/bash
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
set -e -x

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
  type=${1}
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
  git push --tags origin master
}

update_package_version $1
