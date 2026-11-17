# Expo, Android 11, and Maestro toolchain research

Resolves **Research a compatible Expo, Android 11, and Maestro toolchain** (Beads `app-vs7.1`), under **Plan the offline verb-reference app and verify its development toolchain**. Researched 17 November 2026. This is a proposed installation and validation plan; no SDK, JDK, emulator, Maestro, or app dependencies were installed and no build was tested.

## Answer and proposed baseline

Use a local TypeScript Expo development build, with a separate release APK for offline validation. Android 11 is compatible with the documented Expo minimum and Maestro's documented API 30 target support. This establishes a supported route, not evidence that this particular host or Pixel 2 has passed it.

| Component | Baseline for the installation ticket | Evidence and qualification |
| --- | --- | --- |
| Expo / React Native / React | Expo SDK 58 / RN 0.88 / React 19.3.0 | The [versioned Expo compatibility table](https://docs.expo.dev/versions/v58.0.0/) pairs these versions, requires Node 22.13.x or newer, and lists Android 7+, compile SDK 37, target SDK 36. Android 11/API 30 is above that runtime minimum. Use Expo's compatible package resolution rather than choosing RN independently. |
| Node | Node 22.23.2, exact baseline pin | [Expo's SDK 58 build image](https://docs.expo.dev/build-reference/infrastructure/) uses this Node version, Java 17, NDK 27.1.12297006, and Maestro 2.10.0. This is useful evidence of a coherent build environment, not an obligation to use EAS or a claim that all its packages are mandatory locally. [Node's release policy](https://nodejs.org/en/about/previous-releases) recommends Active or Maintenance LTS for production. |
| Java | JDK 17; record distribution and patch during installation | Both [Expo local setup](https://docs.expo.dev/get-started/set-up-your-environment/) and [Maestro CLI installation](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli) support JDK 17; Maestro requires 17+. Set `JAVA_HOME` and confirm Gradle actually uses it. |
| Android build tools | SDK Platform 37; Build Tools 37.0.0; platform-tools; command-line tools; NDK 27.1.12297006 if requested by the generated project | [Expo's documentation registry](https://github.com/expo/expo/blob/main/docs/README.md) lists SDK 58 compile SDK 37 and Build Tools 37.0.0. Keep generated Gradle/AGP/wrapper/NDK versions together. Inspect the generated project before installing additional CMake/NDK packages; don't guess independent versions. |
| Android test target | Pixel 2 hardware profile, Android 11/API 30, Google APIs x86_64 image on this x86_64 host | Proposed AVD configuration, to be checked against the actual SDK catalog. A physical Pixel 2 needs an APK containing its ARM64 native libraries. A Pixel 2-shaped x86_64 emulator does not establish ARM64 or real-device performance compatibility. |
| Maestro | CLI 2.10.0, exact baseline pin | A published [official release](https://github.com/mobile-dev-inc/Maestro/releases/tag/cli-2.10.0), also listed in Expo's SDK 58 image. This is a reproducible candidate, not an assertion that it is the newest release. [Maestro QuickStart](https://docs.maestro.dev/get-started/quickstart) explicitly lists API 30. Its statement about future API 35/36 support is dated; don't infer current high-API support from that promise. |

The generic Expo setup page still directs readers to platform 36, whereas the SDK 58 versioned table says compile SDK 37. Follow the versioned SDK 58 requirements and generated native configuration. If they disagree during installation, record the discrepancy and resolve it before calling the baseline verified. Do not downgrade compile/target SDK to 30 to test an API 30 device: the build platform and minimum runtime OS have different roles.

Use `blank-typescript` for the disposable harness; it avoids unrelated routing decisions and is an [official TypeScript template](https://docs.expo.dev/more/create-expo/). Select an exact published SDK 58 template version at execution time and retain its resolved version plus `package-lock.json`. Exact Expo/RN/React/TypeScript patches must come from that compatible template and lockfile; this research does not invent unverified patch pins. Reproduction begins from that captured scaffold and `npm ci`, not from a moving `latest` tag.

## What is actually visible locally

Read-only commands ran in `/home/cormac/Projects/verb-reference/app`:

```text
uname -sm                         Linux x86_64
/etc/os-release                   Ubuntu 24.04.5 LTS
node --version                    v26.12.1
npm --version                     11.6.2
command -v java adb emulator
  maestro sdkmanager              no matching executable on PATH
~/Android/Sdk, ~/.maestro          absent at these conventional paths
/dev/kvm, /dev/bus/usb             absent
DISPLAY / WAYLAND_DISPLAY         :0 / wayland-0
ANDROID_HOME / ANDROID_SDK_ROOT
  JAVA_HOME                       unset
/tmp/.X11-unix                     X0, X1, X1024, X1025 sockets visible
/proc/cpuinfo                     vmx flag visible
```

These are sandbox observations, not an inventory of the interactive host. Missing PATH tools or default directories do not prove that no installation exists elsewhere. A visible CPU virtualization flag does not establish accessible KVM. Display variables and sockets do not establish that this session can authenticate to a desktop or render an emulator. No GUI connection, USB connection, ADB server, RAM/disk capacity, BIOS setting, host group membership, or device OS was verified.

Before installation, inspect the real host's existing SDK/JDK paths, free storage/RAM, network/package-download access, KVM device permissions, and desktop access. Use `emulator -accel-check` when available. [Android's acceleration documentation](https://developer.android.com/studio/run/emulator-acceleration) requires suitable virtualization and KVM permissions on Linux; GPU software rendering does not supply missing CPU virtualization. If this sandbox cannot access KVM, run the emulator on the desktop host and use an intentionally configured ADB connection, or run the harness on a physical device. Record each target separately; neither fallback silently satisfies missing emulator coverage.

## Installation plan for the existing follow-up ticket

Everything below is a proposal for **Install and verify the local Expo, Android Emulator, and Maestro toolchain**, not commands already executed.

1. Establish the execution host and inspect existing tools before modifying them. Select Node 22.23.2 in a project-scoped version manager rather than replacing the user's global Node. Install/select JDK 17 and capture its patch version. Choose one SDK root; set `ANDROID_HOME` and put its platform-tools, emulator, and command-line tools on PATH for the harness session. Install Android Studio from the official distribution if interactive AVD management is useful; command-line setup is sufficient for automated tests.
2. Inspect the package catalog, accept required Android SDK licenses, then install the SDK 58 build components and the separate API 30 system image. Record command-line-tools, platform-tools, emulator, build-tools, image revision, and downloaded installer versions/checksums. Android Studio's SDK/Device Manager is the preferred interactive route. Android now documents `android sdk` and `android emulator` as replacements for older [sdkmanager](https://developer.android.com/tools/sdkmanager) and [avdmanager](https://developer.android.com/tools/avdmanager); their pages still document the legacy commands below. Check installed tool help before using them.

   ```bash
   sdkmanager --list
   sdkmanager --licenses
   sdkmanager --install 'platform-tools' 'emulator' 'platforms;android-37' \
     'build-tools;37.0.0' 'system-images;android-30;google_apis;x86_64'
   avdmanager list device
   avdmanager create avd --name verb_reference_api30 --device pixel_2 \
     --package 'system-images;android-30;google_apis;x86_64'
   emulator -accel-check
   emulator -avd verb_reference_api30 -no-snapshot
   ```

   Confirm the `pixel_2` identifier and image availability from the installed catalogs. On other host architectures select an available architecture-compatible image and record the change. [Android's emulator command reference](https://developer.android.com/studio/run/emulator-commandline) documents startup options including headless operation; `-no-window` can remove a GUI requirement for automation but cannot solve missing KVM. Keep a visible run for human inspection when possible.
3. Install Maestro CLI 2.10.0. Download and inspect the official installer, then invoke it with `MAESTRO_VERSION=2.10.0`; capture the installer and artifact checksum. [Maestro documents version selection](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli/update-the-maestro-cli). Check `maestro --version` and `java -version`. Local CLI tests need neither Maestro Cloud nor cloud credentials.
4. Create a disposable harness outside the production app, using the exact resolved TypeScript template. Preserve the template/tool versions and lockfile. Use package `com.verbref.toolchainsmoke`, install `expo-dev-client` through Expo, and inspect generated Android properties. Leave Expo's supported minimum alone unless deliberately raising it to the product's API 30 floor; never lower it to accommodate an incompatible dependency. Example sequence after substituting the recorded template and generator versions:

   ```bash
   npx create-expo-app@<recorded-version> toolchain-smoke \
     --template expo-template-blank-typescript@<recorded-sdk58-version> --yes
   cd toolchain-smoke
   npx expo install expo-dev-client
   npx expo install --check
   npx expo-doctor
   npx tsc --noEmit
   npx expo prebuild --platform android
   npx expo run:android --device
   npx expo start --dev-client
   ```

   The angle-bracket values are explicit execution-time substitutions, not runnable literals. [Expo's development-build guide](https://docs.expo.dev/develop/development-builds/introduction/) supports installing `expo-dev-client` and compiling locally with `expo run:android`. This route does not require creating an Expo account. Use the generated Gradle wrapper, not a separately selected global Gradle. Inspect requested SDK/NDK/CMake dependencies and generated APK ABI contents before declaring installation complete.
5. For a physical Pixel 2, enable developer options/USB debugging and authorize the host on the phone. Check `adb devices -l`, OS release/API level, model, and `ro.product.cpu.abilist`; require API 30 for the minimum-environment test. [Android hardware setup](https://developer.android.com/studio/run/device) documents Linux udev/group setup and USB/Wi-Fi alternatives. USB is preferable for the offline test so disabling Wi-Fi does not remove the test connection. Build/install an ARM64-capable APK. For the emulator, record the image, boot completion, API level, resolution/density and selected serial.

## Validation plan and acceptance evidence

The following is a proposed smoke harness, not production UI: a bundled fixture, one text field, and a button that updates a visible result. For example, enter `hablar`, tap `Look up`, and assert `hablo — I speak`. This exercises JS execution, input, events, bundled data, visible output, and Maestro selectors; it proves no linguistic completeness. Use accessible labels and stable test IDs where needed.

Maestro [connects through ADB to emulators or physical Android devices](https://docs.maestro.dev/get-started/supported-platform/android), expects the application to be installed, and identifies it by package name. Its automation is external to the app. A proposed flow after the harness exists:

```yaml
appId: com.verbref.toolchainsmoke
---
- launchApp:
    clearState: true
- tapOn: "Verb"
- inputText: "hablar"
- tapOn: "Look up"
- assertVisible: "hablo — I speak"
```

Run against an explicitly selected serial: `maestro --device <serial> test smoke.yaml`; [the CLI reference](https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options) documents device selection. Development-client onboarding or its launcher may need a separate opening step; establish a repeatable connection to Metro before running the app-level assertions. Keep such setup out of the release flow.

Record three distinct outcomes:

- **Development loop:** install the development client, reach Metro through USB `adb reverse tcp:8081 tcp:8081` or configured LAN/emulator networking, open the harness, and pass the flow. Reload once and confirm a JS change appears. This verifies the iteration path.
- **Development without internet:** start Metro with `npx expo start --dev-client --offline`, disable the device's internet routes while retaining the explicit USB/local Metro route, and repeat the flow. This tests offline developer operation after dependencies are cached. It does not establish a standalone app: `--offline` does not package Metro's JS into an ordinary development build. See [Expo CLI's server and release commands](https://docs.expo.dev/more/expo-cli/).
- **Packaged offline:** build `npx expo run:android --variant release --device`; establish a clean installed state, stop Metro, remove any ADB reverse mapping, disable cellular/Wi-Fi and cold-launch after clearing app data. Repeat the flow, force-stop/relaunch, and reboot/retest. Bundled assets must work without prior downloads. This release variant is a local production-mode test, not a store-signed submission. Record the APK SHA-256 and whether the artifact is installed/testable; resolve signing explicitly if the generated release variant is not installable. Never report an unsigned artifact as a successful device test.

Use the API 30 emulator and actual Android 11 Pixel 2 as separate evidence rows. Record commands, exit codes, tool versions, APK ABI/min/target metadata, Maestro reports/screenshots, launch logs, device state and network conditions, and all failures. Package-download/build network requirements are separate from app runtime network requirements. This research authorizes no runtime update service or dependency on online assets.

## Remaining uncertainty and handoff

No toolchain compatibility was executed locally. Remaining work is already captured by **Install and verify the local Expo, Android Emulator, and Maestro toolchain**: host access, exact resolved dependency/tool patches, SDK catalog/image availability, successful compilation, Maestro startup and assertions, ARM64 physical-device behavior, and standalone offline launches. Lack of KVM/USB access in this sandbox is concrete missing evidence, not proof that the user's desktop lacks them. If those routes remain inaccessible, the installation ticket must record the precise blocked checks instead of claiming verification.

The research dispatch required by the map was attempted; its subagent reported no callable tools. The parent completed the primary-source research instead. Artifact lives uncommitted in the isolated `research/toolchain` worktree at `/home/cormac/Projects/verb-reference/toolchain-research/research/toolchain.md`; the main checkout remains on its original branch. Retain this worktree until the artifact is deliberately incorporated; no commit, push, remote sync, installation, or production implementation was performed.
