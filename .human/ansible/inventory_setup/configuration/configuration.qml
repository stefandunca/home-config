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
            dev_host,
            dev_cpp,
            dev_extra,
            dev_android,
            dev_status
        ]
    }

    Target {
        id: workstation_manjaro

        host: "workstation-manjaro"
        package_list: workstation.package_list
        allow_labels: workstation.allow_labels.concat([ "manjaro" ])
    }

    Target {
        id: mobilerig_manjaro

        host: "mobilerig-manjaro"
        package_list: workstation_manjaro.package_list.concat([ mobilerig_arch ])
        allow_labels: workstation_manjaro.allow_labels
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

        LinuxPackage { name: "zsh" }
        LinuxPackage { name: "git" }
        LinuxPackage { name: "curl" }
        LinuxPackage { name: "wget" }
        LinuxPackage { name: "p7zip" }
        LinuxPackage { name: "vim" }
        LinuxPackage { name: "htop" }
        LinuxPackage { name: "mc" }
        LinuxPackage { name: "tree" }
        LinuxPackage { name: "xclip" }
        LinuxPackage { name: "nano" }
        LinuxPackage { name: "net-tools" }
        LinuxPackage { name: "util-linux" }
        LinuxPackage { name: "rmlint" }
        LinuxPackage { name: "gparted" }

        PipPackage { name: "thefuck" }

        PacmanPackage { name: "nano-syntax-highlighting" }

        Package {
            name: "borg"
            pacman: "borg"
            apt: "borgbackup"
        }

        Package {
            name: "git-extras"
            aur: "git-extras"
            apt: "git-extras"
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
        }

        Package {
            name: "pip"
            pacman: "python-pip"
            apt: "python3-pip"
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

        Package {
            name: "vscode"
            aur: "visual-studio-code-bin"
            deb: "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
        }
        Package {
            name: "jre8"
            pacman: "jre8-openjdk-headless"
            apt: "openjdk-8-jre-headless"
        }
        Package {
            name: "jdk8"
            pacman: "jdk8-openjdk"
            apt: "openjdk-8-jdk"
        }
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
    }

    PackageList {
        id: gui_base

        Package {
            name: "firefox"
            pacman: "firefox"
            apt: "firefox"
            choco: "firefox"
        }
        Package {
            name: "chrome"
            aur: "google-chrome"
            deb: "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
            choco: "googlechrome"
        }
        AllPackage { name: "meld" }     // Diff
        AllPackage { name: "vlc" }      // Media files
        AllPackage { name: "gimp" }     // Raster editing
        AllPackage { name: "imagemagick" }  // image manipulation helpers
        AllPackage { name: "inkscape" } // Vector graphics
        LinuxPackage { name: "peek" }   // GIF screen recorder
        Package {
            name: "nomachine"   //  Remote desktop connection
            aur: "nomachine"
            deb: "https://download.nomachine.com/download/7.8/Linux/nomachine_7.8.2_1_amd64.deb"
            choco: "nomachine"
        }
        Package {
            name: "discord"
            pacman: "discord"
            deb: "https://discord.com/api/download?platform=linux&format=deb"
            choco: "discord"
        }
    }

    PackageList {
        id: hobby

        // 3D printing slicer
        Package {
            pacman: "cura"
            snap: "cura-slicer"
        }
        AllPackage { name: "blender" }  // 3D editing
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
            }
        }
        AllPackage { name: "nodejs" }
        AllPackage { name: "npm" }      // Node package manager
        AllPackage { name: "maven" }    

        LinuxPackage { name: "docker" }
        LinuxPackage { name: "docker-compose" }

        AllPackage {
            exclude: true
            name: "hub"
        }
    }

    PackageList {
        id: dev_host

        AllPackage { name: "virtualbox" }   // VMs
        AllPackage { name: "vagrant" }      // Cmd line VM management
        // Diagrams
        Package {
            name: "drawio"
            aur: "drawio-desktop"
            snap: "drawio"
        }
    }

    PackageList {
        id: dev_cpp

        AllPackage { name: "cmake" }
        AllPackage { name: "gdb" }
        AllPackage { name: "clang" }
        AllPackage { name: "lldb" }
        AllPackage { name: "valgrind" }
        PipPackage { name: "jupyterlab" }
        PipPackage { name: "conan" }
        
        Package {
            name: "ninja"
            pacman: "ninja"
            apt: "ninja-build"
        }

        Package {
            name: "emsdk"
            pacman: "emscripten"
        }
    }

    PackageList {
        id: dev_extra

        Package {
            name: "go"
            pacman: "go"
            choco: "golang"
        }
        Package {
            name: "go-tools"
            pacman: "go-tools"
            choco: "golang"
        }

        AllPackage { name: "nim" }

        Package {
           name: "mqtt-cli"
           aur: "mqtt-cli-bin"
        }
    }

    PackageList {
        id: dev_android

        AurPackage { name: "android-studio" }
        AurPackage { name: "android-sdk" }
        AurPackage { name: "android-sdk-build-tools" }
        AurPackage { name: "android-sdk-platform-tools" }
        AurPackage { name: "android-sdk-cmdline-tools-latest" }
        AurPackage { name: "android-platform" }
        AurPackage { name: "android-emulator" }
    }


    PackageList {
        id: dev_status

        LinuxPackage { name: "jq" } // command-line JSON processor
    }

    PackageList {
        id: handy_when_needed

        AllPackage { name: "audacity" }     // Audio editor
        AllPackage { name: "darktable" }    // photography
    }

    PackageList {
        id: srv

        LinuxPackage { name: "mdadm" }      // Raid management
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

    //
    // Helper components
    //

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
    }
}
