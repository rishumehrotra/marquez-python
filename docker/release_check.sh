#!/bin/bash
set -e

does_package_version_match()
{
  expected_version=$CIRCLE_TAG
  current_version=$(python ./setup.py --version)
  echo "current_version is ${current_version}"
  echo "expected_version is ${expected_version}"

  if [[ "${current_version}" != "${expected_version}" ]]; then

    echo "no match"
    return 1
  else

    echo "match"
    return 0
  fi
}

does_package_version_match