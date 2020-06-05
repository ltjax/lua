from conans import ConanFile, CMake, tools


class LuaConan(ConanFile):
    name = "lua"
    version = "5.1"
    license = "MIT"
    author = "Marius Elvert marius.elvert@googlemail.com"
    url = "https://github.com/ltjax/lua"
    description = "https://github.com/ltjax/lua"
    topics = ("lua")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "src/*", "test/*", "etc/*", "cmake/*", "doc/*", "CMakeLists.txt", "dist.info", "README.md", "COPYRIGHT", "HISTORY"

    def source(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".", defs={
            'BUILD_SHARED_LIBS': self.options.shared,
            'BUILD_TESTING': False,
        })
        if self.settings.os == "Windows":
            cmake.definitions['LUA_BUILD_AS_DLL'] = self.options.shared
            cmake.definitions['LUA_BUILD_WLUA'] = False
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["liblua"]

    def configure(self):
        del self.settings.compiler.libcxx
