# Disposable toolchain smoke harness

Execution evidence for **Install and verify the local Expo, Android Emulator, and Maestro toolchain**, under **Plan the offline verb-reference app and verify its development toolchain**. This is a fixture, not the product or a linguistic correctness test.

## Isolation and versions

Run `source ./env.sh` from this directory. The script selects workspace-local Node, JDK, Android SDK, Gradle cache, npm cache, and AVD directories. It does not change the desktop's shell profile. Large tools and caches live in ignored `tooling/`; keep that directory for subsequent runs. SDK tools may also write conventional host preferences and runtime files.

Scaffold: `create-expo-app@5.0.0`, `expo-template-blank-typescript@58.0.35`. Resolved JavaScript dependencies are in `harness/package-lock.json`. Native source is generated using `npx expo prebuild --platform android --no-install`.

The scaffolder automatically initialized a nested Git repository and created `9ebabd6 Initial commit`. That metadata has been retained at `tooling/scaffold-git`, outside the active harness. No app-repository commit or remote push was performed. For future scaffolds, disable the generator's Git initialization before invoking it when commits are prohibited.

Selected tooling: Node 22.23.2/npm 10.9.8, Temurin JDK 17.0.21+9, Maestro 2.10.0. Downloaded Node and JDK archives were checked against the official SHA-256 values; Android command-line-tools archive was checked against its repository SHA-1. Additional downloaded archives are hashed in `evidence/download-sha256.txt` when recorded; a local hash alone does not authenticate its publisher.

## Reproduce installed setup

From this directory, after sourcing `env.sh`:

```bash
android --no-metrics sdk install platform-tools emulator platforms/android-37.0 \
  build-tools/37.0.0 system-images/android-30/google_apis/x86_64
android --no-metrics sdk install ndk/27.1.12297006
android --no-metrics sdk install build-tools/36.0.0 cmake/3.22.1
echo no | avdmanager create avd --name verb_reference_api30 --device pixel_2 \
  --package 'system-images;android-30;google_apis;x86_64'
emulator -accel-check
emulator -avd verb_reference_api30 -no-window -no-audio -no-snapshot \
  -gpu software -memory 2048
```

The current Android CLI calls the stable platform `platforms/android-37.0`. The legacy `sdkmanager --install 'platforms;android-37'` reported that package missing. Do not interpret that naming mismatch as evidence that no API 37 platform exists. The generated React Native baseline requests compile SDK 37, target SDK 36, minimum SDK 24, Build Tools 37.0.0, NDK 27.1.12297006, and Gradle 9.4.1; actual build results determine compatibility.

In another terminal:

```bash
source ./env.sh
cd harness
npm ci
npx expo install --check
npx expo-doctor
npx tsc --noEmit
cd android
./gradlew :app:assembleDebug -PreactNativeArchitectures=x86_64 --no-daemon --max-workers=2
```

The architecture flag above builds only for the emulator. ARM64/physical-device compatibility requires a separate build and device test.

## Verification procedure

Development: install the debug APK, start `npx expo start --dev-client --localhost --max-workers 2`, reverse TCP 8081 with ADB, open the development-client URL, and run `maestro --device emulator-5554 test open-development.yaml` from this directory. This waits for loading and dismisses the observed development-menu introduction. Test a JS edit and explicit client reload with `reload.yaml`; it expects the temporary header `Toolchain reload confirmed`. Restore the original header afterward.

For offline development, stop Metro, disable emulator internet while retaining ADB, then run `npx expo start --dev-client --offline --port 8081 --max-workers 2`. SDK 58 rejects `--offline` combined with `--localhost`; use the offline flag alone. Require a successful `curl -fsS http://127.0.0.1:8081/status` readiness check before opening the app. The development-client URL is `exp+verbref-toolchain-smoke://expo-development-client/?url=http%3A%2F%2F127.0.0.1%3A8081`.

Packaged offline: build `:app:assembleRelease` with the generated wrapper, inspect APK metadata and signing, install the resulting APK, stop Metro, remove ADB reverse mappings, disable emulator Wi-Fi and cellular data, then run `maestro --device emulator-5554 test smoke.yaml`. Repeat after force-stop and emulator reboot. This clears app state and requires no prior downloaded app content. Local release testing does not establish store signing/readiness.

The executed release build used:

```bash
cd harness/android
NODE_ENV=production ./gradlew :app:assembleRelease \
  -PreactNativeArchitectures=x86_64 --no-daemon --max-workers=2
```

From the harness root after stopping Metro, with this disposable emulator selected:

```bash
adb -s emulator-5554 shell svc wifi disable
adb -s emulator-5554 shell svc data disable
adb -s emulator-5554 shell cmd connectivity airplane-mode enable
adb -s emulator-5554 reverse --remove tcp:8081
adb -s emulator-5554 install -r harness/android/app/build/outputs/apk/release/app-release.apk
adb -s emulator-5554 reverse --list
adb -s emulator-5554 shell dumpsys connectivity
maestro --device emulator-5554 test packaged-offline.yaml
adb -s emulator-5554 reboot
adb -s emulator-5554 wait-for-device
# Wait until sys.boot_completed is 1, then recheck networking and run:
adb -s emulator-5554 shell getprop sys.boot_completed
maestro --device emulator-5554 test smoke.yaml
```

The test requires `Active default network: none`, no reverse mapping, and a refused connection to the stopped host Metro port. `packaged-offline.yaml` includes both a clear-state launch and force-stop/relaunch. Choose the actual emulator serial if it differs from the captured `emulator-5554`.

`lookup.yaml` asserts the app is already open. `smoke.yaml` first launches with cleared app state. Development-client onboarding and connection belong before `lookup.yaml`.

## Evidence

See `evidence/` for installation, diagnostic, build, emulator, and test logs. The final verification report records outcomes and remaining blockers. A running Metro session, a successful bundle export, and a Maestro executable starting are each insufficient evidence of standalone offline operation.

At handoff, Metro and the disposable emulator are stopped. Tools, caches, APKs, and reports remain installed. The AVD retains airplane mode from the offline tests. If needed after restarting it, restore its network using `adb -s emulator-5554 shell cmd connectivity airplane-mode disable`, then enable Wi-Fi/data with `svc wifi enable` / `svc data enable` on that same emulator.
