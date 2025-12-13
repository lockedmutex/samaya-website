> [!NOTE]
> **This is not the source code for samaya!**
>
> The official source code and active development for samaya application is hosted at **[https://codeberg.org/lockedmutex/samaya](https://codeberg.org/lockedmutex/samaya)**.
>

---

<p align="center">
  <img src="src/io.github.redddfoxxyy.samaya.svg" alt="Samaya app icon" width="200"/>
</p>

<h1 align="center">Samaya</h1>

<p align="center">
  <img src="src/screenshot1.avif"  alt="Samaya Screenshot 1"/>
  <img src="src/screenshot3.avif"  alt="Samaya Screenshot 2"/>
</p>

#### A simple, elegant, minimalist Pomodoro timer for your desktop. Designed to help you stay focused and productive, it offers a clean, distraction-free interface to manage work and break intervals with ease.

#### Samaya means time in Hindi, written as `समय`.

## Features

* **Light Weight:** The size of the app is only around 55KB and around 111KB including all the data and assets!
* **Routine Management:** Switch between **Pomodoro (25 min)**, **Short Break (5 min)**, and **Long Break (20 min)** routines.
* **Custom Work/Break Durations:** Change the working or break durations in the settings menu.
* **Skip Sessions:** Skip the current session and start the next one.
* **Timer Notifications:** Get notified (using sound) when the timer ends.

## Download & Installation

- Get the app from FlatHub:

  [![Get it on Flathub](https://flathub.org/api/badge?locale=en)](https://flathub.org/apps/io.github.redddfoxxyy.samaya)

- Flatpak builds for linux are available in [latest release](https://codeberg.org/lockedmutex/samaya/releases/latest).

- To install the application from source:

    ```bash
    git clone -b release --single-branch https://codeberg.org/lockedmutex/samaya.git
    cd samaya
    meson setup build_release --buildtype=release -Dprefix=$HOME/.local
    meson compile -C build_release
    meson install -C build_release
    cd ..
    rm -rf samaya
    ```

- For other operating systems, the app can only be compiled and installed manually from source 
	(and might fail because samaya depends heavily on glib, libcanberra and gsound which are linux only libs).
	
## License

This project is licensed under the **GNU Affero General Public License v3.0**. See
the [LICENSE](LICENSE) file for details.

Contributions made by all contributors are licensed strictly under **GNU AGPL v3.0 only**.

```
    Copyright (C) 2025  lockedmutex(Suyog Tandel)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## Maintainers

[@lockedmutex](https://github.com/lockedmutex)
