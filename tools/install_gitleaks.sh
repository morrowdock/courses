#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Verified Linux x64 release only. Never resolve a moving tag or download "latest".
set -euo pipefail
destination=${1:?Usage: install_gitleaks.sh DESTINATION}
version=8.24.3
checksum=9991e0b2903da4c8f6122b5c3186448b927a5da4deef1fe45271c3793f4ee29c
archive=$(mktemp)
trap 'rm -f "$archive"' EXIT
curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 \
  "https://github.com/gitleaks/gitleaks/releases/download/v${version}/gitleaks_${version}_linux_x64.tar.gz" \
  --output "$archive"
printf '%s  %s\n' "$checksum" "$archive" | sha256sum --check --status
mkdir -p "$destination"
tar -xzf "$archive" -C "$destination" gitleaks
"$destination/gitleaks" version
