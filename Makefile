code:
	# code format
	autoflake api config core models services tests utils -r --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --in-place --recursive
	pyupgrade --py311-plus `find api config core models services tests utils -path -prune -o -path "*/tests/*" -prune -o -name "*.py" -print`
	black api config core models services tests utils
	isort api config core models services tests utils

	# lint check
	pylint --extension-pkg-whitelist='pydantic' api config core models services tests utils
