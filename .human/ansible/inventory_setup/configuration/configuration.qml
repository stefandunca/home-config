import dev.dunca.home

AnsibleVarsExporter {
    Target {
        host: "workstation-manjaro"
        package_list: [
            base,
            gui_base
        ]
        allow_labels: ["manjaro"]
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
        LinuxPackage { name: "borg" }
        LinuxPackage { name: "rmlint" }
        LinuxPackage { name: "gparted" }

        PacmanPackage { name: "nano-syntax-highlighting" }

        Package {
            name: "git-extras"
            aur: "git-extras"
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
            name: "vscode"
            aur: "visual-studio-code-bin"
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
    }

    PackageList {
        id: srv

        LinuxPackage { name: "mdadm" }
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
}
