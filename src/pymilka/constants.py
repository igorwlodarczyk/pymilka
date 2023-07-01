indent = "    "
metadata_params = ("name", "version", "author", "author_email", "description")

options = f"""
[options]
package_dir =
{indent}= src

python_requires = >=3.8
setup_requires =
install_requires =
"""

dev_requirements = ("black", "pytest", "-e .")
