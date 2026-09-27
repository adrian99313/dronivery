# 🚁 Dronivery — Autonomous Drone Restaurant Delivery

[![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)](https://flutter.dev)
[![Dart](https://img.shields.io/badge/Dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)](https://dart.dev)
[![Material 3](https://img.shields.io/badge/Material--3-Enabled-00C853?style=for-the-badge)](https://m3.material.io)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

**Dronivery** is a modern cross-platform Flutter application for an **Autonomous Drone Restaurant Delivery** service. It showcases ultra-fast skyway logistics connecting certified local kitchens directly to doorstep landing pads.

Built with Flutter & Material 3, Dronivery features a fluid responsive UI optimized for Desktop, Web, Tablet, and Mobile devices.

---

## ✨ Features

- 🛰️ **Live Drone Air Radar**: Interactive flight tracking status showing active altitude (200ft), ETA countdown, and progress telemetry.
- 🍣 **Multi-Cuisine Catalog**: Detailed restaurant cards covering Asian, Mexican, Indian, Middle Eastern, Italian, and Burger kitchens with ratings, flight time, and menu preview dialogs.
- 🔍 **Instant Search & Category Filtering**: Filter kitchens by cuisine or quickly search for items like sushi, tacos, ramen, pizza, and burgers.
- 🛒 **Payload Bay Cart & Checkout**: Slide-out drawer cart with item count management, subtotal calculations, aerial delivery fee logic, and promo code support.
- 🎟️ **Promo & Discount System**: Integrated coupon codes (`FIRSTFLY`, `DRONEFREE`, `GOLDFLASH`, `NIGHTOWL`) with copy-to-clipboard and dynamic discount application.
- ⚡ **Dronivery Gold Membership**: Premium tier toggle granting priority air routing, waived delivery fees, 20-mile extended radius, and member-only flash sales.
- 📱 **Responsive Design Shell**: Desktop view featuring a permanent sidebar & top header, automatically converting to an adaptive Drawer & AppBar on mobile form factors.

---

## 🛠️ Architecture & Tech Stack

- **Framework**: [Flutter](https://flutter.dev) (Dart SDK `>=3.0.0`)
- **Design System**: Material Design 3 (Custom palette: `emeraldTeal`, `electricOrange`, `warmSunset`, `darkSlate`)
- **State Management**: Reactive `StatefulWidget` state flow
- **Layout System**: `LayoutBuilder` & `MediaQuery` responsive breakpoints (`desktop >= 900px`)
- **Image Handling**: Custom `SafeNetworkImage` fallback system with network progress & gradient loading states

---

## 📁 Repository Structure

```text
dronivery/
├── lib/
│   └── main.dart            # Complete Dronivery UI, Models, Views & Navigation Shell
├── test/
│   ├── widget_test.dart     # Navigation shell widget test
│   └── dronivery_test.dart   # App rendering smoke test
├── android/                 # Android project configuration
├── ios/                     # iOS project configuration
├── web/                     # Web deployment entrypoint
├── pubspec.yaml             # Flutter project dependencies and metadata
├── .gitignore               # Flutter/Dart git ignore rules
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the Flutter SDK installed on your system:
- [Flutter SDK](https://docs.flutter.dev/get-started/install) (`>= 3.0.0`)
- Dart SDK (`>= 3.0.0`)

### Installation & Run

1. **Clone the repository** (replace `<your-username>` with your GitHub username):
   ```bash
   git clone https://github.com/<your-username>/dronivery.git
   cd dronivery
   ```

2. **Install dependencies**:
   ```bash
   flutter pub get
   ```

3. **Run the application**:
   ```bash
   # Run on default connected device / browser
   flutter run

   # Run specifically on Chrome (Web)
   flutter run -d chrome

   # Run on Desktop (macOS/Windows/Linux)
   flutter run -d macos
   ```

### Running Tests

Execute the widget test suite to verify UI compilation:
```bash
flutter test
```

---

## 📤 How to Push to GitHub

Follow these simple commands to initialize Git and push this repository to GitHub:

```bash
# 1. Initialize Git in the project directory
git init

# 2. Add all project files
git add .

# 3. Create initial commit
git commit -m "feat: initial commit of Dronivery Flutter application"

# 4. Set main branch
git branch -M main

# 5. Add remote GitHub repository (Create a new empty repo on github.com first)
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/dronivery.git

# 6. Push code to GitHub
git push -u origin main
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
