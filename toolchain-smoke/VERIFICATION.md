# Toolchain execution evidence

Observed on 17–18 November 2026 for **Install and verify the local Expo, Android Emulator, and Maestro toolchain**. User requested emulator evidence for this session; physical Pixel 2 verification is deferred. Results below concern this disposable fixture only.

## Environment

The restricted execution sandbox could not resolve registry.npmjs.org and did not expose `/dev/kvm` or `/dev/bus/usb`. Approved host execution had working downloads, writable KVM and USB visibility. These are different access contexts on the same development machine; sandbox observations must not be reported as host limitations.

Linux x86_64, 15 GiB RAM, 4 GiB swap. The volume had roughly 29 GiB free before installation. Running the emulator and native compiler together increased swap use to about 3 GiB. Stopping the idle emulator recovered about 3 GiB RAM. Build with two Gradle workers and run Metro with two workers on this shared desktop. These are host observations, not app performance measurements.

Everything intentional is isolated beneath `/home/cormac/Projects/verb-reference/toolchain-smoke`. `env.sh` selects local tools/caches without changing shell startup files. The Android and Maestro CLIs also use conventional host runtime/preferences/report locations. No production app implementation was added.

## Installed versions

| Component | Observed version |
| --- | --- |
| Node / npm | 22.23.2 / 10.9.8 |
| JDK | Eclipse Temurin 17.0.21+9 |
| create-expo-app / TypeScript template | 5.0.0 / 58.0.35 |
| Expo / React Native / React | 58.0.26 / 0.88.1 / 19.3.0 |
| expo-dev-client / TypeScript | 58.0.21 / 6.0.3 |
| Android command-line tools / Android CLI | 23.0 / 1.1.16919734; archive commandlinetools-linux-16111833_latest.zip |
| platform-tools / emulator | 37.0.1-15733141 / 37.2.13.0 (16740729) |
| Android build platform | API 37.0, revision 2 |
| Build Tools | 37.0.0; Gradle additionally installed 36.0.0 |
| Android test image | API 30 Google APIs x86_64, revision 16 |
| NDK / CMake | 27.1.12297006 / 3.22.1 |
| Gradle / Android Gradle Plugin | generated wrapper 9.4.1 / React Native catalog 9.2.1 |
| Kotlin / KSP | Expo resolved 2.2.10 / 2.2.10-2.0.2 |
| Maestro | 2.10.0 |

Exact npm resolution is captured in `harness/package-lock.json` and `evidence/javascript-versions.txt`. Source archives, official catalogs, JDK metadata, and Node checksums are retained under `tooling/downloads`; local SHA-256 hashes are in `evidence/download-sha256.txt`.

## Setup findings

The installed SDK CLI replaces `sdkmanager` with `android sdk`. `sdkmanager --licenses` says the option is no longer necessary. The legacy package name `platforms;android-37` was unavailable. The current repository schema exposes stable `platforms;android-37.0`; `android --no-metrics sdk install platforms/android-37.0` installed it successfully. Gradle accepts the generated compile SDK 37 configuration against this installation. Do not change the compile SDK to 30 to test an API 30 device.

The generated native baseline declares minimum SDK 24 and target SDK 36. Expo selects Kotlin 2.2.10 over React Native's catalog value 2.2.0. The generated project uses legacy Android variant APIs and reports deprecation warnings; no dependency patch was applied to suppress these warnings.

The first Gradle attempt was deliberately canceled when Gradle and the SDK CLI both attempted NDK installation. Once the CLI completed, the build was restarted and reused compiled plugins. Initial and resumed logs are retained separately. SDK installation and native builds should run sequentially.

The scaffolder automatically created a nested initial Git commit, `9ebabd6`. Its metadata was moved to `tooling/scaffold-git`; the active harness is no longer a nested repository. No app-repository commit, push, publication, or Dolt remote sync was performed.

## Completed checks

| Check | Result / evidence |
| --- | --- |
| Expo compatible dependency check | Passed, `evidence/expo-check.log` |
| Expo Doctor | 20/20 passed, `evidence/expo-doctor.log` |
| TypeScript | Passed, `evidence/typecheck.log` |
| Android prebuild | Passed, `evidence/prebuild.log` |
| KVM acceleration | Passed, `evidence/android-host.txt` |
| Pixel 2 AVD boot | Android 11/API 30, 1080×1920, 420 dpi; `evidence/emulator-target.txt` and `evidence/avd-config.txt` |
| Maestro driver connection | Passed Settings launch and visible Search settings assertion; `evidence/maestro-driver.log` and `evidence/maestro-driver/` |
| Development APK build | Passed in 11m 34s for resumed attempt; `evidence/build-debug.log` |
| Standalone release APK build | Passed in 12m 10s, including R8 optimization and app lint-vital tasks; `evidence/build-release.log` |

The debug APK is `harness/android/app/build/outputs/apk/debug/app-debug.apk` (about 61 MiB), SHA-256 `2be296afd4155cc966bebeef356e1845522e642ab11d69f962b247b762f8e9fb`. APK inspection reports package `com.verbref.toolchainsmoke`, minimum SDK 24, target SDK 36, compile SDK 37, and native ABI x86_64. Signature verification passed with the generated Android Debug certificate. See `evidence/debug-apk-metadata.txt` and `evidence/debug-apk-signing.txt`.

The release APK is `harness/android/app/build/outputs/apk/release/app-release.apk` (about 21 MiB), SHA-256 `b1ed97bf757f182bfa39cd46387d6e4791eaacb874d8aad54e26af989438da26`. It declares the same package and SDK levels, contains x86_64 native libraries and a 1,204,616-byte `assets/index.android.bundle`, and passes signature verification with the Android Debug certificate. See `evidence/release-apk-metadata.txt`, `evidence/release-apk-signing.txt`, and `evidence/release-apk-contents.txt`. This establishes packaging, not an offline runtime result.

## Runtime results

All completed app flows enter `hablar`, tap Look up, and assert `hablo — I speak`.

| Scenario | Observed result / evidence |
| --- | --- |
| Development with Metro | Passed; `evidence/maestro-development.log` and `evidence/maestro-development/` |
| JS edit and explicit client reload | Passed without recompiling/reinstalling the APK; `evidence/maestro-reload.log` and `evidence/maestro-explicit-reload/` |
| Fresh development client, offline Metro, device internet disabled | Passed after clearing app data; `evidence/maestro-development-offline.log` and `evidence/maestro-development-offline-retry/` |
| Fresh packaged release, no Metro, no device network | Passed with cleared app data; `evidence/maestro-packaged-offline.log` and `evidence/maestro-packaged-offline/` |
| Packaged release after force-stop/relaunch | Passed in the same packaged-offline flow |
| Packaged release after emulator reboot | Passed with app data cleared again and offline state rechecked; `evidence/maestro-packaged-offline-reboot.log` and `evidence/maestro-packaged-offline-reboot/` |

Offline-development network evidence: airplane mode `1`, Wi-Fi `0`, mobile data `0`, `Active default network: none`, with only the explicit ADB reverse mapping for TCP 8081 retained. Expo printed `Networking has been disabled` and served the bundle locally. See `evidence/development-offline-network.txt`, `evidence/development-offline-connectivity.txt`, and `evidence/metro-offline.log`.

Packaged-release evidence: the same disabled-network state, no ADB reverse mappings, and a failed HTTP request to the stopped Metro server (`connection refused`). The installed APK hash matches the recorded release artifact. See `evidence/release-offline-network.txt`, `evidence/release-offline-connectivity.txt`, `evidence/release-metro-absent.txt`, and `evidence/installed-release-sha256.txt`. Screenshots are retained alongside the logs.

Execution findings and failed attempts are retained rather than counted as passes:

- The development client initially showed a blank loading view, then its developer-menu introduction. A UI probe failed on the missing actual `verb-input` field while the introduction was visible. After Continue/Close, the same probe passed. `open-development.yaml` now waits for loading and handles that observed onboarding. See `evidence/debug/` for the clearly marked diagnostic artifacts.
- One Maestro driver startup timed out while external UIAutomator dumps were running. Subsequent sequential runs passed. Exact causality was not isolated; avoid running competing UI automation sessions. No extended driver-startup timeout was required.
- An automatic-refresh assertion failed after a JS-only header edit. Explicitly reopening the development-client URL loaded the changed header and passed. Automatic Fast Refresh is **not verified**. The temporary header was restored, and the restored fixture passed the later offline-development flow.
- Expo SDK 58 rejected `--offline` together with `--localhost`. The first offline test consequently failed because no server was available. Retrying with `--offline` alone and an enforced HTTP readiness check passed. Failed flow logs are `evidence/maestro-development-offline-server-unavailable.log` and `evidence/maestro-development-offline/`.

After reboot, Android reported `sys.boot_completed=1`, airplane mode `1`, Wi-Fi `0`, mobile data `0`, no ADB reverse mapping, and `Active default network: none`. The fresh-state app flow passed again. See `evidence/reboot-offline-network.txt` and `evidence/reboot-offline-connectivity.txt`.

## Limits for the specification decision

- This x86_64 emulator is a Pixel 2 hardware profile; it is not a physical ARM64 Pixel 2. The image advertises translated ARM ABIs, which does not establish hardware compatibility. The generated debug APK deliberately contains x86_64 only.
- No physical-device launch, ARM64 runtime, real-device performance, accessibility acceptance, store signing, store submission, or production corpus correctness was verified.
- `npm audit` reports 28 dependency vulnerabilities (26 high, 2 moderate, 0 critical) in the installed template/development dependency graph. The raw report is `evidence/npm-audit.json`; counts alone do not establish runtime exploitability. No broad or breaking audit fix was applied during compatibility verification. Dependency review belongs in implementation/release acceptance.
- A local release variant uses the generated debug key for installability. That is not store-signing evidence.

See `README.md` for commands. Retain this directory until the evidence and harness are deliberately incorporated or discarded.

## Handoff state

The toolchain task is closed, its resolution links this report, and the parent map index was updated while preserving other sessions' decisions. No additional decision ticket was needed. Metro and the disposable emulator are stopped. Installed tools, caches, APKs, and evidence occupy approximately 18 GiB; the volume has approximately 11 GiB free. The AVD retains airplane mode from the offline tests. The app checkout's pre-existing working changes were left as found.
