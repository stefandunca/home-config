import dev.dunca.home

AnsibleVarsExporter {
    Target {
        id: workstation

        host: "workstation"
        package_list: [
            base,
            gui_base,
            hobby,
            dev_base,
            dev_gui,
            dev_host,
            dev_cpp,
            dev_extra,
            //dev_android,
            dev_status,

            blockchain,
        ]
    }

    Target {
        id: workstation_manjaro

        host: "workstation-manjaro"
        package_list: workstation.package_list
        allow_labels: workstation.allow_labels.concat([ "manjaro" ])
    }

    Target {
        id: workstation_mac

        host: "workstation-mac"
        package_list: workstation.package_list
        allow_labels: workstation.allow_labels.concat([ "mac" ])
    }

    Target {
        id: mobilerig_manjaro

        host: "mobilerig-manjaro"
        package_list: workstation_manjaro.package_list.concat([ mobilerig_arch ])
        allow_labels: workstation_manjaro.allow_labels.concat([ "mobilerig" ])
    }

    Target {
        host: "workstation-wsl"
        package_list: [
            base,
            dev_base,
            dev_cpp,
            dev_extra
        ]
        allow_labels: ["wsl"]
    }

    PackageList {
        id: base

        UnixPackage { name: "zsh" }
        UnixPackage { name: "git" }
        UnixPackage { name: "curl" }
        UnixPackage { name: "wget" }
        UnixPackage { name: "p7zip" }
        UnixPackage { name: "vim" }
        UnixPackage { name: "htop" }
        UnixPackage { name: "mc" }
        UnixPackage { name: "tree" }
        UnixPackage { name: "xclip" }
        UnixPackage { name: "nano" }
        UnixPackage { name: "util-linux" }
        UnixPackage { name: "rmlint" }
        UnixPackage { name: "ranger" }
        UnixPackage { name: "bench" }

    	LinuxPackage { name: "gparted" }
        LinuxPackage { name: "net-tools" }


        PipPackage { name: "thefuck" }
        PipPackage { name: "shell-gpt" }
        PipPackage { name: "watchdog" }

        PacmanPackage { name: "nano-syntax-highlighting" }

        Package {
            name: "borg"
            pacman: "borg"
            apt: "borgbackup"
            brew: "borgbackup"
        }

        Package {
            name: "dict"
            pacman: name
            apt: name
            brew: name
        }

        Package {
            name: "git-extras"
            aur: name
            apt: name
            brew: name
        }
        Package {
            name: "yay"
            pacman: "yay"
            allowlist: ["manjaro"]
        }
        Package {
            name: "base-devel"
            pacman: "base-devel"
            apt: "build-essential"
        }

        Package {
            name: "pip"
            pacman: "python-pip"
            apt: "python3-pip"
            brew: "python"
        }

        Package {
            name: "python3-dev"
            //aur: "python-devtools"
            apt: "python3-dev"
        }

        Package {
            name: "python-setuptools"
            pacman: "python-setuptools"
            apt: "python3-setuptools"
        }

        PipPackage {
            name: "python-setuptools-mac"
            pip: "setuptools"
        }

        Package {
            name: "vscode"
            aur: "visual-studio-code-bin"
            deb: "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
            brew_cask: "visual-studio-code"
            denylist: ["wsl"]
        }

        Package {
            name: "java"
            apt: "default-jre"
            pacman: "jre-openjdk"
            choco: "javaruntime"
            brew_cask: "temurin"
        }
        // Not available natively yet
        // Package {
        //     name: "jdk"
        // }
        // TODO: still needed?
        // Package {
        //     name: "jre8"
        //     pacman: "jre8-openjdk-headless"
        //     apt: "openjdk-8-jre-headless"
        // }
        // Package {
        //     name: "jdk8"
        //     pacman: "jdk8-openjdk"
        //     apt: "openjdk-8-jdk"
        // }
        Package {
            name: "jre11"
            pacman: "jre11-openjdk-headless"
            apt: "openjdk-11-jre-headless"
        }
        Package {
            name: "jdk11"
            pacman: "jdk11-openjdk"
            apt: "openjdk-11-jdk"
        }
        Package {
            name: "cheat"
            brew: "cheat"
        }
    } // PackageList { id: base }

    PackageList {
        id: gui_base

        Package {
            name: "firefox"
            pacman: name
            apt: name
            choco: name
            brew_cask: name
        }
        // Package {
        //     name: "google-chrome"
        //     aur: name
        //     deb: "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
        //     choco: name
        //     brew_cask: name
        // }
        Package {
            name: "brave"
            aur: "brave"
            custom_apt: CustomApt {
                name: "brave"
                key: "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"
                repo: "deb https://brave-browser-apt-release.s3.brave.com/ stable main"
            }
            choco: name
            brew_cask: "brave-browser"
        }
        AllUiPackage { name: "meld" }     // Diff
        AllUiPackage { name: "vlc" }      // Media files
        AllUiPackage { name: "gimp" }     // Raster editing
        AllPackage { name: "imagemagick" }  // image manipulation helpers
        AllUiPackage { name: "inkscape" } // Vector graphics
        LinuxPackage { name: "peek" }   // GIF screen recorder
        Package {
            name: "nomachine"   //  Remote desktop connection
            aur: name
            deb: "https://download.nomachine.com/download/7.8/Linux/nomachine_7.8.2_1_amd64.deb"
            choco: name
            brew_cask: "nomachine"
        }
        Package {
            name: "discord"
            pacman: name
            deb: "https://discord.com/api/download?platform=linux&format=deb"
            choco: name
            brew_cask: name
        }
        Package {
            name: "whatsapp"
            aur: name
            choco: name
            brew_cask: name
        }
        Package {
            name: "openvpn-connect"
            // On linux use the one integrated in gnome
            choco: name
            brew_cask: name
        }
        Package {
            name: "Flameshot"
            brew_cask: name
        }
        Package {
            name: "Slate"
            brew_cask: name
        }
    }

    PackageList {
        id: hobby

        // 3D printing slicer
        // Package {
        //     pacman: "cura"
        //     snap: "cura-slicer"
        //     brew_cask: "ultimaker-cura"
        //     exclude: true
        // }
        AllUiPackage { name: "blender" }  // 3D editing
    }

    PackageList {
        id: dev_base

        // Github cmd line
        Package {
            name: "github-cli"
            pacman: "github-cli"
            custom_apt: CustomApt {
                name: "gh"
                key: "https://cli.github.com/packages/githubcli-archive-keyring.gpg"
                repo: "deb https://cli.github.com/packages stable main"
            }
            brew: "gh"
        }
        AllPackage { name: "nodejs" }
        AllPackage { name: "npm" }      // Node package manager
        AllPackage { name: "maven" }

        UnixPackage { name: "docker" }
        UnixPackage { name: "docker-compose" }

        AllPackage {
            exclude: true
            name: "hub"
        }

        PipPackage { name: "PySide6" }
    }

    PackageList {
        id: dev_gui

        Package {
            name: "db-browser-for-sqlite"
            brew_cask: "db-browser-for-sqlite"
        }
    }

    PackageList {
        id: dev_host

        // VMs
        Package {
            name: "virtualbox"
            pacman: name
            apt: name
            choco: name
            //brew_cask: name   // Not available yet
        }
        // Control VMs
        Package {
            name: "vagrant"
            pacman: name
            apt: name
            choco: name
            //brew_cask: name   // Not available yet
        }
        // Diagrams
        Package {
            name: "drawio"
            aur: "drawio-desktop"
            snap: "drawio"
            brew_cask: "drawio"   // Not available yet
        }
    }

    PackageList {
        id: dev_cpp

        AllPackage { name: "cmake" }
        // Control VMs
        Package {
            name: "gdb"
            pacman: name
            apt: name
            choco: name
            //brew_cask: name   // Not available yet
        }
        Package {
            name: "clang"
            pacman: name
            apt: name
            choco: name
        }
        Package {
            name: "lldb"
            pacman: name
            apt: name
            choco: name
        }
        // Control VMs
        Package {
            name: "valgrind"
            pacman: name
            apt: name
            choco: name
            // brew_tap:  CustomBrewTap {
            //     tap: "LouisBrunner/valgrind"
            //     brew: "valgrind"
            // }
        }
        PipPackage { name: "jupyterlab" }
        PipPackage { name: "conan" }
        PipPackage { name: "aqtinstall" }

        Package {
            name: "ninja"
            pacman: "ninja"
            apt: "ninja-build"
            brew: "ninja"
        }

        Package {
            name: "emsdk"
            pacman: "emscripten"
            brew: "emscripten"
        }
    }

    PackageList {
        id: dev_extra

        Package {
            name: "go"
            pacman: "go"
            choco: "golang"
            brew: "go"
        }
        Package {
            name: "go-tools"
            pacman: "go-tools"
            choco: "golang"
            brew: "golang"
        }

        AllPackage { name: "nim" }

        Package {
           name: "mqtt-cli"
           aur: "mqtt-cli-bin"
           brew_tap: CustomBrewTap {
                tap: "hivemq/mqtt-cli"
                cask: "mqtt-cli"
            }
        }
    }

    PackageList {
        id: dev_android

        Package {
            name: "android-studio"
            brew_cask: name
            aur: name
        }
        AurPackage { name: "android-sdk" }
        AurPackage { name: "android-sdk-build-tools" }
        AurPackage { name: "android-sdk-platform-tools" }
        AurPackage { name: "android-sdk-cmdline-tools-latest" }
        AurPackage { name: "android-platform" }
        AurPackage { name: "android-emulator" }
    }


    PackageList {
        id: dev_status

        UnixPackage { name: "jq" } // command-line JSON processor
        Package {
            name: "sqlcipher"
            pacman: name
            apt: name
            brew: name
        }
    }

    PackageList {
        id: handy_when_needed

        AllUiPackage { name: "audacity" }     // Audio editor
        AllUiPackage { name: "darktable" }    // photography
    }

    PackageList {
        id: srv

        UnixPackage { name: "mdadm" }      // Raid management
    }

    PackageList {
        id: mobilerig_arch

        Package {
            name: "fprintd"
            pacman: "fprintd"
        }
        Package {
            name: "libfprint"
            aur: "libfprint-2-tod1-xps9300-bin"
        }
    }

    PackageList {
        id: blockchain

        Package {
            name: "ganache"
            brew_cask: name
        }
        Package {
            name: "ledger-live"
            brew_cask: name
        }
    }

    //
    // Helper components
    //

    component UnixPackage: Package {
        pacman: name
        apt: name
        brew: name
    }

    component LinuxPackage: Package {
        pacman: name
        apt: name
    }

    component PacmanPackage: Package {
        pacman: name
    }
    component AurPackage: Package {
        aur: name
    }
    component PipPackage: Package {
        pip: name
    }
    component AllPackage: Package {
        pacman: name
        apt: name
        choco: name
        brew: name
    }
    component AllUiPackage: Package {
        pacman: name
        apt: name
        choco: name
        brew_cask: name
    }
}
