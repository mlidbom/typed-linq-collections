@echo off
call "%~dp0venv\Scripts\activate.bat"
npx repomix@latest --output ./repomix/repomix-typed-linq.xml --include "**/*.py,**/*.pyi,**/*.toml,**/*.md,licence.txt" --ignore "_lib,user_files" ..\typed-linq-collections
