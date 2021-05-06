from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'MQTT-TLS'
    version = '1e4cb27'
    url = 'https://github.com/hicktech/conan-MQTT-TLS'
    repo_url = 'https://github.com/jw3/MQTT-TLS.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src', src='src')
        self.copy('*.h*', dst='include', src='src')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
