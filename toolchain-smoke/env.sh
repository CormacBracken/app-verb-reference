#!/usr/bin/env bash
# Source this file; all tooling and caches stay beside the disposable harness.
SMOKE_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
export JAVA_HOME="$SMOKE_ROOT/tooling/jdk-17.0.21+9"
export ANDROID_HOME="$SMOKE_ROOT/tooling/android-sdk"
export ANDROID_USER_HOME="$SMOKE_ROOT/tooling/android-user"
export ANDROID_AVD_HOME="$ANDROID_USER_HOME/avd"
export GRADLE_USER_HOME="$SMOKE_ROOT/tooling/gradle"
export npm_config_cache="$SMOKE_ROOT/tooling/npm-cache"
export EXPO_NO_TELEMETRY=1
export MAESTRO_CLI_NO_ANALYTICS=1
export MAESTRO_CLI_ANALYSIS_NOTIFICATION_DISABLED=true
export PATH="$SMOKE_ROOT/tooling/node-v22.23.2-linux-x64/bin:$JAVA_HOME/bin:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$SMOKE_ROOT/tooling/maestro/bin:$PATH"
