#!/bin/bash
set -e

does_package_version_match()
{
  expected_version=$CIRCLE_TAG
  current_version=$(python ./setup.py --version)
  echo "current_version is ${current_version}"
  echo "expected_version is ${expected_version}"

  if [[ "${current_version}" != "${expected_version}" ]]; then
    echo "Packaging code ${current_version} does not equal to tagged version, ${expected_version}"
    return 1
  else
    return 0
  fi
}

does_package_version_match
