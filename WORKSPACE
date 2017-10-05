#http_archive(
#    name = "io_bazel_rules_python",
#    sha256 = "1210df6ec5355ab4eeb5b79cdde7cdb77b0432fd8e9ab1744abe7ac5ef4b2c78",
#    strip_prefix = "rules_python-44fdf5f24a4b634ef7b0f86e7a017f4d8d5aa899",
#    urls = ["https://github.com/bazelbuild/rules_python/archive/44fdf5f24a4b634ef7b0f86e7a017f4d8d5aa899.tar.gz"],
#)

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/kgreenek/rules_python.git",
    commit = "899c2220d368ca4285ca0641810da2f821f61c05",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

pip_import(
   name = "pip_requirements",
   requirements = "//:requirements.txt",
)

load("@pip_requirements//:requirements.bzl", "pip_install")

pip_install()
