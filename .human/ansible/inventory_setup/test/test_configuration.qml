import dev.dunca.home

AnsibleVarsExporter {
    Target {
        host: "sdmobile"
        package_list: [
            base
        ]
    }

    Target {
        host: "mediasrv"
        package_list: [
            base,
            srv
        ]
    }
    
    PackageList {
        id: base

        LinuxPackage { name: "binutils" }
        LinuxPackage { name: "gcc" }
        LinuxPackage { name: "htop" }

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
        id: srv
    }

    component LinuxPackage: Package {
        pacman: name
        apt: name
    }
}
